Title: FuguPass
Date: 2013-02-12 10:20
Tags: apps, script, encryption, fugupass, passwords
Slug: fugupass

[FuguPass](https://script.google.com/d/1l23aUzJBCfy5QZAxtZGiXyy3XOv0JtDoSrjFhzlEh7R4qaz-XoDuLoKk/edit) is a Google app script that uses the Blowfish encryption algorithm (implementation from the [Barnses Storming](http://barnes-storming.blogspot.co.nz/2011/08/encrypting-data-in-google-documents.html) blog) to store encrypted passwords in a Google Drive Spreadsheet.

The script requires a Google account and all information is stored within your account's properties and a spreadsheet called 'EncryptedPasswords'.

This is the first in a few posts on how I've achieved this so far. Starting with how to use the script.

## Usage

Before using FuguPass you need to grant the script privileges. Unfortunately there is no nice way to do this from the app itself, instead you need to open the script in [edit mode](https://script.google.com/d/1l23aUzJBCfy5QZAxtZGiXyy3XOv0JtDoSrjFhzlEh7R4qaz-XoDuLoKk/edit) and run it by selecting a function (e.g. doGet) and clicking the run icon. You'll be prompted to grant the required privileges to the script and then you can access the [web app](https://script.google.com/macros/s/AKfycbwNHyA_BuHR9JcOUCAz8hgnFZ75x57r5zp9Bo_mVS2Rf6uAIOaO/exec) (link fixed).

![Edit Mode](|filename|/images/fp-editmode.png)

On first run enter a master key that will be used for encryption. This input field is not masked so you can check that the value you entered is correct. Clicking 'Save' will generate the derived key used for encryption and create the spreadsheet used to store the encrypted passwords.

On subsequent runs you will be prompted to enter the master key. This time the input field is masked and the value entered is checked to make sure it is the same as the initial master key. If you lose your master key there is zero chance of recovering it. So don't do that.

After unlocking FuguPass there are two input boxes and two buttons. To save a new password type in the name you want to associate with the password and the password plaintext and click save. You will be prevented from overwriting any existing passwords with the same name.

![Unlocking](|filename|/images/fp-unlocking.png)

To retrieve a password type in the name and click get. If the password exists it will be displayed in the password text field unmasked.

![Password](|filename|/images/fp-password.png)

The EncryptedPasswords spreadsheet contains the name, the encrypted password and the salt used for that password. If you want to change a stored password, delete the row from the spreadsheet and save it again in the app.

I will cover the encryption algorithm in the next post. For now I'll say the level of security provided by this script is somewhere in between [ROT13](http://en.wikipedia.org/wiki/ROT13) and secret algorithms used by the [NSA](http://en.wikipedia.org/wiki/Nsa). So more than that post it note on your desk but who knows how much more. Also this is absolutely in alpha release, use it as such! I wont support upgrades until the next post.
