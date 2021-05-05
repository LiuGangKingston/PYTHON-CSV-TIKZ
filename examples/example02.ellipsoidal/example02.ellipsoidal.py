#   This is example02.ellipsoidal source file for
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
#   This file is formed by adding new lines at the
#   "Specific calculation to generate CSV files" area at the
#   end of the template file.
#

import os
import sys
sys.path.append(os.path.abspath("/c/python.codes"))
from PythonCSVTikZ import *

# Specific calculation to generate CSV files
# Specific calculation to generate CSV files

totallines=10
startingline=1
datalinesineachfile=50

a=7.0e0
b=3.0e0
startingangleofsoidal = 35.0e0
endinggangleofsoidal = 325.0e0
startinxofsoidal = a * math.cos(startingangleofsoidal*Deg2Rad)
startinyofsoidal = b * math.sin(startingangleofsoidal*Deg2Rad)
c=-math.sqrt(a*a-b*b)

afile = open("setup.scalars.csv",'w')
if afile.closed:
    print("The file setup.scalars.csv open is failed, then stopped.")
    sys.exit()

afile.write("a,b,c,startingangleofsoidal,endinggangleofsoidal,startinxofsoidal,startinyofsoidal\n")
afile.write(f"{a},{b},{c},{startingangleofsoidal},{endinggangleofsoidal},{startinxofsoidal},{startinyofsoidal}\n")
afile.close()

bigfile = PythonCSVTikZFileGroup("iterated.alldata.",startingline,totallines,datalinesineachfile)
bigfile.FirstListToAllFiles(["c,d,startingangle,dk,bigf,t,x,y,yprime",
                             "tangentangle,normalangle,incidentangle,reflectangle,mycolor"])

d=math.fabs(c)
for j in [1, -1]:
    for i in range(startingline, totallines + 1):
        startingangle= j*(5.0e0 + 5.0e0*i*i)
        dk=d*math.cos(startingangle*Deg2Rad)
        bigf=a*a - dk*dk
        t=b*b*(dk+math.sqrt(bigf+dk*dk))/bigf
        x=t*math.cos(startingangle*Deg2Rad)-d
        y=t*math.sin(startingangle*Deg2Rad)
        yprime=-b*b*x/(a*a*y)
        z = math.sqrt((b*b*x)**2 + (a*a*y)**2)
        if x < 0.0e0: 
            if y < 0.0e0 :
                tangentangle = math.asin(b*b*x /z) * Rad2Deg 
            else :
                tangentangle = 180.0e0 + math.acos(a*a*y /z) * Rad2Deg 
        else :
            if y  < 0.0e0 :
                tangentangle = math.acos(-a*a*y /z) * Rad2Deg
            else :
                tangentangle = math.acos(-a*a*y /z) * Rad2Deg
       
        normalangle = tangentangle - 90.0e0
        incidentangle = normalangle - startingangle
        reflectangle = tangentangle + 90.0e0 + incidentangle

        bigfile.WriteAListRow(i,[f" {c}, {d}, {startingangle}, {dk}, {bigf}, {t}", 
                  f"{x}, {y}, {yprime}, {tangentangle}, {normalangle} ",
                  f"{incidentangle}, {reflectangle}, {PickTypicalColor(i)}"])

bigfile.FileGroupClose()




