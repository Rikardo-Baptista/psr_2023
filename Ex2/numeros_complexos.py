#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style
from time import time
import math

# define functions here ...
def addComplex(x, y):
# add code here ...

    pass
def multiplyComplex(x, y):
# add code here ...

def printComplex(x):
    # add code here ...

def main():
    # ex2 a)

# define two complex numbers as tuples of size two
c1 = (5, 3)
c2 = (-2, 7)

# Test add
c3 = addComplex(c1, c2)
printComplex(c3)

# test multiply
printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()