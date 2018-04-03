#!/usr/bin/python3

from argparse import ArgumentParser, FileType

parser = ArgumentParser(description='Counts the number of occurences of a given letter in a file.')
parser.add_argument('inputFile', metavar="input", type=FileType('r'), nargs=1, help='the input file')
parser.add_argument('letter', metavar="letter", nargs=1, help='the letter to count')
parser.add_argument('-c', '--color', dest="color", action='store_true', help="set this flag to turn on colored output")
parser.add_argument('-i', '--ignore-first-line', dest="ignore", action='store_true', help="set this flag to ignore the first line")

args = parser.parse_args()

filename = args.inputFile[0].name
letter = args.letter[0]
color = args.color
ignore = args.ignore

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
