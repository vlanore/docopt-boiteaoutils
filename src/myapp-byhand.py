#!/usr/bin/python3

import sys

if len(sys.argv) < 3:
    print("Usage:\n  myapp-byhand.py [-c] [-i] [-h] <input> <letter>")
    exit(1)

pos = 0
color = False
ignore = False
for arg in sys.argv[1:]:
    if arg == "-c":
        color = True
    elif arg == "-i":
        ignore = True
    elif arg == "-h":
        print("Usage:\n  myapp-byhand.py [-c] [-i] [-h] <input> <letter>")
        exit(1)
    elif pos == 0:
        filename = arg
        pos += 1
    else :
        letter = arg

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
