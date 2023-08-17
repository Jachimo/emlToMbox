# .eml to .mbox converter

Forked from Gist [kadin2048/emlToMbox.py](https://gist.github.com/kadin2048/c332a572a388acc22d56).

## Info
Converts a directory full of .eml files to a single Unix "mbox" file.

Accepts as input either an individual .eml file or a directory containing one
or more .eml files.

The output mbox will be created if it doesn't already exist.  If it exists,
it will be appended to.

There is no checking for duplicates, so use caution.
If duplicate filtering is desired, it could be added to `add_file_to_mbox()`.

Inspired by http://www.cosmicsoft.net/emlxconvert.html

Usage:  
Directory mode: `$ ./emlToMbox.py inputdir/ output.mbox`  
Single-file mode: `$ ./emlToMbox.py input.eml output.mbox`  
