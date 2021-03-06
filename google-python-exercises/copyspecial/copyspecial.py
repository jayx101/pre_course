#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
# +++your code here+++
# Write functions and modify main() to call them
def get_special_path(dir):
  filenames = os.listdir(dir)
  abspaths = []
  for file in filenames:
    match = re.search(r'__(\w+)__', file)
    if match:
      abspaths.append(os.path.abspath(os.path.join(dir, file)))
  print abspaths
  return abspaths

def copy_to(paths, dir):
  if not os.path.exists(dir): os.mkdir(dir)
  for srcpath in paths:
    fname = os.path.basename(srcpath)
    shutil.copy(srcpath, os.path.join(dir, fname))

def zip_to(paths, zipfile):
  zips = ' ' + ' '.join(paths)
  (status, output) = commands.getstatusoutput('zip -j ' + zipfile + zips)

  # If there is an error status is non-zero. Then write output to std error ,
  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if args[0]: paths = get_special_path(args[0])
  if todir:
    copy_to(paths, todir)
  if tozip:
    zip_to(paths, tozip)

if __name__ == "__main__":
  main()
