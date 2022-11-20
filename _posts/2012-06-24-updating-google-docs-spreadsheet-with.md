---
layout: post
title: Updating google docs spreadsheet with POST request
date: 2012-06-24 10:20
tags: apps, script, google, spreadsheet
slug: updating-google-docs-spreadsheet-with
---

Google spreadsheets has a nice [ImportHtml](https://support.google.com/docs/bin/answer.py?hl=en&answer=155182) function that can import data from a list or table within an html page retrieved using a standard GET request.

This is great for simple cases, but if the source data needs massaging or cannot be retrieved using a GET request then you'll need to use a Google Apps Script.

I had this problem with a Hockey Club website I maintain. I was using ImportHtml to import the competition points tables to the website but after a (much needed) upgrade the official system required a POST to get the data.
New Script

## New Script

Open the script editor by going to Tools -> Script editor in a Google spreadsheet.
Retrieve Data

## Retrieve Data

Use the default app service function [UrlFetchApp.fetch](https://developers.google.com/apps-script/class_urlfetchapp#fetch) to retrieve the data.

fetch takes 2 arguments, 'url' the url string of the data and 'optAdvancedArgs' a javascript object to provide advanced arguments.

The useful advanced arguments in this case are 'method', used to set the HTTP method used and 'payload' which is a javascript object of key values pairs that will form the POST body.

```javascript
function retrieveData(output, grade) {
  var url = 'http://drawsresults.sportsrunner.net/data.php';
  var payload = {
    orgcode:'AKH',
    sportcode:'SY',
    sporttype:'other',
    gradenumber:grade,
    output:output
  };
  var options = {
    method: 'POST',
    payload: payload
  }
  var response = UrlFetchApp.fetch(url, options);
  return response;
}
```

## Parsing Data

Once the data has been downloaded the html snippet can be parsed as xml using Xml.parse.

parse takes 2 arguments. The XML string to parse and a boolean indicating whether the parser should be lenient. 

```javascript
function getXML(response) {
  var docString = '<?xml version="1.0" standalone="no"?><data>' + response.getContentText()+'</data>';
  var xml = Xml.parse(docString, true);
  return xml;
}
```

The response content is wrapped in an xml header and a root element so that it can be parsed as a proper document.

## Processing

Unfortunately the XML API in Google Apps Script is quite limited. There is no support for XPath only methods to get child elements by name. Using these methods a 2D array can be constructed and returned to the client. Each first level element represents a row and each second level element a cell value for that row.

```javascript
function getData(xml) {
  var rows = xml.getElement().getElement('div').getElement('table').getElements('tr');
  var data = [];
  for (var i in rows) {
    var cells = rows[i].getElements('td');
    var values = [];
    for (var j in cells) {
      values.push(cells[j].getText());
    }
    data.push(values);
  }
  return data;
}
```

## Spreadsheet

Once the function to retrieve data has been created it can be called from the spreadsheet like any other function. e.g. set the cell A1 to  '=myFunction(arg1, arg2)' to call a function named myFunction passing in the arguments arg1 and arg2. The spreadsheet can then be styled and published on the internet using the File -> Publish to the Web option.

## Finished

The published spreadsheet can be added to a Google Sites page using the Google Spreadsheet widget

![AUHC Points](|filename|/images/auhc-points.png)