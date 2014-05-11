Title: Continuous Blogging
Date: 2014-05-10 09:03
Tags: blogging, travis-ci, github, pelican, python
Slug: continuous-blog

In my last [post](http://jessek.co.nz/2014/05/pelican-static-blog.html), I talked about moving from Blogger to the blog aware static site generator Pelican.

Using make to compile markdown files in to html with a python tool started giving me ideas. The blog's source was already in github and it made sense to move the compilation to an automated tool. Automate everything.

<!-- PELICAN_END_SUMMARY -->

Travis
------

[Travis](https://travis-ci.org/) is a free, hosted CI tool integrated with [github](https://github.com/) that can build projects in a bunch of languages, including python.

Getting started is really easy. You sign in with your github account and then choose the repositories you want to build.

The [getting started](http://docs.travis-ci.com/user/getting-started/) guide covers all of this and provides a basic example of a ```.travis.yml``` file. For Pelican that would look something like this

```yaml
language: python
python:
- '2.7'
install:
- pip install -r requirements.txt
script: make publish
```

This script will set up a python 2.7 environment and install the dependencies specified in the requirements.txt file. You may need to generate the ```requirements.txt``` file if you don't already have one

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
Could not find a version that satisfies the requirement argparse==1.2.1 
(from -r requirements.txt (line 6)) 
(from versions: 0.1.0, 0.2.0, 0.3.0, 0.4.0, 0.5.0, 0.6.0, 0.7.0, 0.8.0, 0.9.0, 0.9.1, 1.0.1, 1.0, 1.1)
```

I was able to pick the latest available version of argparse, update the requirements.txt and try again. Such an approach may not work for a more essential library.

Themes
------

Once Travis is able to install the correct dev environment and run the make script you should run in to your first build failure.

```
...
Exception: Could not find the theme pure
make: *** [publish] Error 1

The command "make publish" exited with 2.

Done. Your build exited with 1.
```

Themes are installed from source into the development environment using the command ```pelican-themes```. Travis automatically initialises and updates git submodules. Add the theme as a git submodule and an additional install command.

```bash
git add submodule https://github.com/jkrshw/pure.git pure
```

In ```.travis.yml``` add a second install command to run ```pelican-themes```

```yaml
language: python
python:
  - '2.7'
install:
  - pip install -r requirements.txt
  - pelican-themes -i pure
script: make publish
```

Push the changes and now you should have your first successful build!

```bash
git add .travis.yml
git commit -m"Add pelican theme"
git push origin master
```

Plugins
-------

After including the theme, pelican will happily generate html but will not be able to find any plugins. Surprisingly this doesn't result in a build failure.

```
ERROR: Can't find plugin `sitemap`: No module named sitemap
ERROR: Can't find plugin `summary`: No module named summary
Done: Processed 29 articles and 0 pages in 1.84 seconds.

The command "make publish" exited with 0.

Done. Your build exited with 0.
```

Instead of being installed into the development environment, plugins are included via source and a variable in ```pelicanconf.py```. The approach is still pretty much the same as for themes. Add a submodule for the pelican-plugins repo and configure the ```PLUGIN_PATH``` variable.

```bash
git add submodule https://github.com/getpelican/pelican-plugins pelican-plugins
```

In ```pelicanconf.py``` set the ```PLUGIN_PATH``` variable

```python
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['sitemap', 'summary']
```

Then push the changes

```bash
git add pelicanconf.py
git commit -m"Add pelican plugins"
git push origin master
```

You'll now have a successful build that has generated your blog exactly the way you want it! Only one thing.. you can't download the output of build from Travis.

Deploy
------

Travis has a [multitude](http://docs.travis-ci.com/user/deployment/) of options for deployment, including to [Amazon S3](http://docs.travis-ci.com/user/deployment/s3/). 

Before getting started with the ```.travis.yml``` configuration, install the Travis [Command Line Client](https://github.com/travis-ci/travis.rb#readme). The Travis client is used to encrypt the AWS secret access key which you'll absolutely want to do if you're using a public github repo.

The Travis Client requires Ruby 1.9.3 or greater. I'm running Ubuntu 14.04 and although the system default Ruby it says it's Ruby 1.9.3, it doesn't act like it. Even installing Ruby 2.0 from apt-get wont help as 1.9 is still set as the default version.

Fortunately there's a tool for that. Install [RVM](http://rvm.io/rvm/install) and all your ruby version worries will be over.

```bash
curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
rvm use 2.1
```

Now the Travis Client gem can be installed

```bash
gem install travis -v 1.6.10 --no-rdoc --no-ri
```

To configure Travis to deploy to S3 you need to know the S3 bucket, endpoint and region as well as an access key from the AWS console. I use the Asia Pacific (Sydney) Region, you can use this table of [Amazon S3 regions](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) to find the values for your region.

```yaml
deploy:
  provider: s3
  access_key_id: <your-access-key-id>
  skip_cleanup: true
  local-dir: output
  bucket: jessek.co.nz
  region: ap-southeast-2
  endpoint: jessek.co.nz.s3-website-ap-southeast-2.amazonaws.com
```

After adding the S3 configuration and access key id, use the Travis Client to add the encrypted secret access key. Run the command below and paste the secret key in when prompted for std-in.

```bash
travis encrypt --add deploy.secret_access_key
```

Your ```.travis.yml``` configuration should now contain a language, environment installation commands, a script and deploy configuration

```yaml
language: python
python:
- '2.7'
install:
- pip install -r requirements.txt
- pelican-themes -i pure
script: make publish
deploy:
  provider: s3
  access_key_id: AKIAICC7Z3GSB5QRCTKA
  secret_access_key:
    secure: d9VJXcSahW+OjUxKyHEM/TE4BGjfq2NAAY2XP8e6MbfwEVOjquJDk5hHu8y8Mjh2UHP2AWMPhUmaSEluWoTc3Vc85FcKegLwj5VB3iF0UH8ykM3pBLdptpc63oFFuKo3BeyU1tWdGj0iHK557MMvhUWc6og27pcrLQo340qsgD0=
  skip_cleanup: true
  local-dir: output
  bucket: jessek.co.nz
  region: ap-southeast-2
  endpoint: jessek.co.nz.s3-website-ap-southeast-2.amazonaws.com
```

Push the changes to master. After 5 mins your site should be updated.

Why?
----

Mostly I did this for fun and to brush up on some Continuous Delivery tools. I can't tell if I've made blogging more fun or more like work. The workflow is not as seamless as an online editor such as Blogger. This approach makes it a little easier, and a lot better than building and uploading manually.

It's pretty slow too. The environment setup and build takes around 30 seconds and deploying to S3 adds another 4 minutes. I suspect this is because all articles, images and rollups are being re-deployed. Hopefully there is room for optimisation by not deploying artifacts that haven't been changed.

For a blog with a lot of collaborates I think this could be a really cool workflow. Posts, corrections and edits can be submitted by anyone as a pull request and approved by a contributors with write access to the repo. Using git as a source repo also provides traceability of edits. History rewrites can be picked up by anyone with a clone, keeping the writers honest.