#!/usr/bin/env python3

""" Converts a directory full of .eml files to a single Unix "mbox" file.
This is similar to http://www.cosmicsoft.net/emlxconvert.html

Accepts as input either an individual .eml file or a directory containing one
or more .eml files.

Usage:
$ ./emlToMbox.py inputdir/ output.mbox
$ ./emlToMbox.py input.eml output.mbox

STATUS:  Lightly tested using Python 3.9.1 
"""

import os
import sys
import mailbox
from pathlib import Path

global debug
debug = True


def main(arguments):
  infile_name = arguments[1]
  dest_name = arguments[2]

  if debug:
    print("Input is:  " + infile_name)
    print("Output is: " + dest_name)

  # if dest doesn't exist create it
  dest_mbox = mailbox.mbox(dest_name, create=True)
  dest_mbox.lock()  # lock the mbox file

  if os.path.isdir(infile_name):
    if debug:
      print("Detected directory as input, using directory mode")
    count = 0
    for filename in Path(infile_name).rglob('*.eml'):
      try:
        fi = open(os.path.join(filename), 'r')
      except:
        sys.stderr.write("Error while opening " + filename + "\n")
        dest_mbox.close()
        raise
      addFileToMbox(fi, dest_mbox)
      count += 1
      fi.close()
    if debug:
      print("Processed " + str(count) + " total files.")

  if infile_name.split('.')[-1] == "eml":
    if debug:
      print("Detected .eml file as input, using single file mode")
    try:
      fi = open(infile_name, 'r')
    except:
      sys.stderr.write("Error while opening " + infile_name + "\n")
      dest_mbox.close()
      raise
    addFileToMbox(fi, dest_mbox)
    fi.close()

  dest_mbox.close()  # close/unlock the mbox file
  return 0


def addFileToMbox(fi, dest_mbox):
  # Any additional preprocessing logic goes here...
  try:
    dest_mbox.add(fi)
  except:
    dest_mbox.close()
    raise


if __name__ == "__main__":
  if len(sys.argv) != 3:
    sys.stderr.write("Usage: ./emlToMbox.py input outbox.mbox\n")
    sys.exit(1)
  sys.exit(main(sys.argv))
