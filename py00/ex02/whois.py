#!/usr/bin/python
from sys import argv
import sys

if len(argv) != 2:
    sys.exit('AssertionError: more than one argument are provided')
try:
    i = int (argv[1])
except ValueError:
    sys.exit('AssertionError: argument is not an integer')
if (i == 0):
    sys.exit("I'm Zero.")
if (i % 2):
    sys.exit("I'm Odd.")
sys.exit("I'm Even.")
