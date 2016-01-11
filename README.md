jessek-blog
===========

Blog built with Pelican and deployed with Travis CI

Install
-------

```
sudo easy_install pip
sudo pip install virtualenvwrapper
mkvirtualenv blog
pip install -r requirements.txt
git submodule init
git submodule update
```

Build
-----

```
make publish
```

Travis
------

Push to master to build blog and deploy to Amazon S3
