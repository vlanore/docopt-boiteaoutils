#!/usr/bin/python3

"""Counts the number of occurences of a given letter in a file.

Usage:
  myapp-argparse.py [options...] <input> <letter>

Positional arguments:
  input                 the input file
  letter                the letter to count

Options:
  -h, --help            show this help message and exit
  -c, --color           set this flag to turn on colored output
  -i, --ignore-first-line
                        set this flag to ignore the first line
"""

from docopt import docopt

args = docopt(__doc__)

filename = args["<input>"]
letter = args["<letter>"]
color = args["--color"]
ignore = args["--ignore-first-line"]


# == SCRIPT ========================================================================================================================
myfile = open(filename, 'r')
lines = myfile.readlines()
if ignore:
    lines = lines[1:]
occurences = "".join(lines).count(letter)
if color:
    form = "Number of occurences of letter \033[31m{}\033[0m in file \033[34m{}\033[0m : \033[33m{}\033[0m"
else:
    form = "Number of occurences of letter {} in file {}: {}"
print(form.format(letter, filename, occurences))
