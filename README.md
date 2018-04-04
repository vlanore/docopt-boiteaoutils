## Boite à outils informatique #2
# Command line arguments in python

Having reliable and well-documented command line interfaces is important.
Other people are more likely to use your script if it has a good interface.

There are different ways to specify and parse command line arguments:

## By hand
Example code: [argument parsing by hand](src/myapp-byhand.py)

This approach is bad:
 - usage message is not guaranteed to be correct;
 - syntax is not really checked;
 - very fragile;
 - difficult to write;
 - etc...
 
## argparse
Example code: [argument parsing with argparse](src/myapp-argparse.py)

Documentation: [argparse](https://docs.python.org/3/library/argparse.html)

Principle: specify your desired command line parameters using an object-oriented interface.

It's better:
 - usage message automatically generated (thus guaranteed to be correct);
 - support for combined options (e.g., -ci);
 - elaborate syntax checking (number of parameters, types, order...).
  
But it's not easy to write, especially for small scripts.
 
## docopt
Example code: [argument parsing with docopt]

Documentation: [docopt](https://github.com/docopt/docopt)

Principle: write your usage message directly, docopt does the rest.

Pros:
 - easy to write, especially for small scripts;
 - documentation directly in code;
 - "commands" are easy to use
 
Cons:
 - parameter checking is more basic than argparse.
