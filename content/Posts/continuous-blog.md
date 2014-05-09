Title: Continuous Blogging
Date: 2014-05-10 09:03
Tags: blogging, travis-ci, github
Slug: continuous-blog

Continuous Blogging
===================

In my last [post](http://jessek.co.nz/2014/05/pelican-static-blog.html), I talked about moving from Blogger to the blog aware static site generator Pelican.

Using make to compile markdown files in to html with a python tool started giving me ideas. The blog's source was already in github and it made sense to move the compilation to an automated tool. Automate everything.

Travis
------

[Travis](https://travis-ci.org/) is a free hosted CI tool integrated with [github](https://github.com/) that understands a bunch of languages, including python.

Getting started is really easy. You sign in with your github account and then choose the repositories you want to build.

The [getting-started](http://docs.travis-ci.com/user/getting-started/) guide covers all of this and provides a basic example of a ```.travis.yml``` file. For Pelican that would look something like this:

```yaml
language: python
python:
- '2.7'
install:
- pip install -r requirements.txt
script: make publish
```

This script will set up a python 2.7 environment and install the dependencies specified in the requirements.txt file. You may need to generate the requirements.txt file if you don't alreay have one: 

```bash
pip freeze > requirements.txt
```

You're now ready to push the changes to origin and watch Travis get to work

```bash
git add .travis.yml requirements.txt
git commit -m"Add basic travis config"
git push origin master
```

If Travis can't find all of your dependencies the build will Error out and you'll see something like this in the logs

```
Downloading/unpacking argparse==1.2.1 (from -r requirements.txt (line 6))
Could not find a version that satisfies the requirement argparse==1.2.1 (from -r requirements.txt (line 6)) (from versions: 0.1.0, 0.2.0, 0.3.0, 0.4.0, 0.5.0, 0.6.0, 0.7.0, 0.8.0, 0.9.0, 0.9.1, 1.0.1, 1.0, 1.1)
```

Luckily I was able to pick the latest available version, update the requirements.txt and try again. Such an approach may not work for a more essential library.

Themes
------

Once Travis is able to set up the correct dev environment and start running the make script you should run in to your first build failure!

```
...
Exception: Could not find the theme pure
make: *** [publish] Error 1

The command "make publish" exited with 2.

Done. Your build exited with 1.
```

Themes are installed from source into the development environment using the command ```pelica-themes```.

Add the theme as a git submodule

```
git add submodule https://github.com/jkrshw/pure.git pure
```

And add the install command to the ```.travis.yml```

```yaml
language: python
python:
  - '2.7'
install:
  - pip install -r requirements.txt
  - pelican-themes -i pure
script: make publish
```

Push the changes and now you should have your first sucessful build!


Plugins
-------

Deploy
------