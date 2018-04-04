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
 
 
