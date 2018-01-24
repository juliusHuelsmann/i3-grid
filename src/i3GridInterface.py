#!/usr/bin/python

from time import time
st = time()
import sys
import os

currPath = os.path.dirname(os.path.abspath(__file__)) # /a/b/c/d/e
sys.path.append(currPath)

from grid import GridInterface 
import os


if len(sys.argv) > 1:
    k = GridInterface();

    for i in range(1, len(sys.argv)):
        try:
            command = "k." + sys.argv[i] + "()"
            i = exec(command)
            print("x command", i , command)
        except:
            print("Command " + sys.argv[i] + " not recognized.")
            help(k)

   
    # 5 milisekunden.  
    # 0.05189943313598633
    print(time() - st)
else:
    print("Please provide some of the functions below as arguments!")
    help(GridInterface)

