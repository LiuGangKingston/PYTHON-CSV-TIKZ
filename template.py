#   This is template source file for
#       https://github.com/LiuGangKingston/PYTHON-CSV-TIKZ.git
#            Version 1.0
#   free for non-commercial use.
#   Please send us emails for any problems/suggestions/comments.
#   Please be advised that none of us accept any responsibility
#   for any consequences arising out of the usage of this
#   software, especially for damage.
#   For usage, please refer to the README file.
#   This code was written by
#        Gang Liu (gl.cell@outlook)
#                 (http://orcid.org/0000-0003-1575-9290)
#          and
#        Shiwei Huang (huang937@gmail.com)
#   Copyright (c) 2021
#
#   You can code your specific computations in the area of 
#   "Specific calculation to generate CSV files" at the
#   end of this file.
#

import os
import sys

# The next statement should make the directory where the file
# PythonCSVTikZ.py is copied be visible to this code. Like:
sys.path.append(os.path.abspath("/c/python.codes"))
from PythonCSVTikZ import *

# Specific calculation to generate CSV files
# Specific calculation to generate CSV files
# like the following lines:

totallines=500
startingline=1
datalinesineachfile=50
...

# The next object creation will also open files "iterated.alldata.1.csv", 
#                                               "iterated.alldata.2.csv", 
#                                               "iterated.alldata.3.csv", 
#                                               ..., 
#                                               till the last needed one:
bigfile = PythonCSVTikZFileGroup("iterated.alldata.",startingline,totallines,datalinesineachfile)

# The next routine call will output the long string into all the above files as the top line:
bigfile.FirstListToAllFiles(["variablenames","seperate","bycommaswithoutanythingelse"])

for i in range(startingline, totallines + 1):
    ...

    # The next statement will output data into the specific file based on "i" value. 
    bigfile.WriteAListRow( i,       [f"{onevariable}, {anothervariable}, {anothervariable}",
              f"{anothervariable}, {anothervariable}, {anothervariable}, {anothervariable}",
              f"{anothervariable}, {anothervariable}, {anothervariable}, {anothervariable}",
              f"{anothervariable}, {anothervariable}, {anothervariable}, {anothervariable}",
              f"{anothervariable}, {anothervariable}, {anothervariable}, {anothervariable}",
              f"{anothervariable}, {anothervariable}, {anothervariable}, {anothervariable}",
              f"{anothervariable}, {PickTikZColor(i)}"])
              #  where the function "PickTikZColor(i)" returns a TikZ color for any input integer "i", 
              #  which can be used to add various colors to iteratively calculated drawings.

# The next routine call will close all files in the group.
bigfile.FileGroupClose()



