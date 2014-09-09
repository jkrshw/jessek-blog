#!/usr/bin/python

'''
Check for differences between the hashes in images.md5 and old_images.md5
and delete the unmodified files so they are not uploaded to S3.

uses md5sum to generate hashes
'''
import os

# read in the hash file. Keyed by hash
def read_hash(filename):
    with open(filename) as f:
        return dict([line.split() for line in f])

#########  main program ###########
os.system("wget -q -O old_images.md5 http://jessek.co.nz/images.md5")
os.system("md5sum output/images/* > output/images.md5")

new_hashes = read_hash("output/images.md5")
old_hashes = read_hash("old_images.md5")

for key in new_hashes.viewkeys() & old_hashes.viewkeys():
    print 'removing unchanged file %s' % new_hashes[key]
    os.remove(new_hashes[key])
