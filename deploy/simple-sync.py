#!/usr/bin/python

'''
Check for differences between the hashes in HASH_FILE and SITE_URL/HASH_FILE
and delete the unmodified files from the output directory.

requires wget, find and md5sum to be installed
'''
import os

HASH_FILE = "site.md5"
SITE_URL = "http://jessek.co.nz"

# read in the hash file as a set of tuples (hash, filename)
def read_hash(filename):
    with open(filename) as f:
        return { tuple(line.split()) for line in f }

#########  main program ###########
os.system("wget -q -O old_%s %s/%s" % (HASH_FILE, SITE_URL, HASH_FILE))
os.system("find output -type f -exec md5sum {} \; > output/%s" % HASH_FILE)

new_hashes = read_hash("output/%s" % HASH_FILE)
old_hashes = read_hash("old_%s" % HASH_FILE)

for key in new_hashes & old_hashes:
    print 'removing unchanged file [md5 %s] %s' % key
    os.remove(key[1])
