#   This is example01 source file for
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


refractiveindex=1.5e0
bigradius=8.0e0
a=3.0e0
b=3.0e0
z=math.sqrt(bigradius * bigradius- b * b)
anglez=math.asin(b/bigradius)*Rad2Deg
c=-math.sqrt(bigradius * bigradius - (a+b) **2)
anglea=math.acos(c/bigradius)*Rad2Deg

afile = open("setup.scalars.csv",'w')
if afile.closed:
    print("The file setup.scalars.csv open is failed, thne stopped.")
    sys.exit()

afile.write("totallines,refractiveindex,bigradius,a,b,z,anglez,c,anglea\n")
afile.write(f"{totallines},{refractiveindex},{bigradius},{a},{b},{z},{anglez},{c},{anglea}\n")
afile.close()


bigfile = open("iterated.alldata.csv",'w')
if bigfile.closed:
    print("The file iterated.alldata.csv open is failed, thne stopped.")
    sys.exit()

bigfile.write("totallines,i,refractiveindex,bigradius,a,b,z,anglez,c,"+
                             "anglea,incidentangle,refractiveangle,anglede,dx,ee,et,ex,ey,"+
                             "anglece,angleced,outangle,mycolor\n")

for i in range(startingline, totallines + 1):
    incidentangle=3.0e0 + 05.0e0* i
    refractiveangle=math.asin(math.sin(incidentangle*Deg2Rad)/refractiveindex)*Rad2Deg
    anglede=180-refractiveangle-anglea
    # x component of D position
    dx=a/math.tan(anglede*Deg2Rad) + c

    # To find E position by solving equations, with t and et as DE length:
    #  (t sin(anglede) + \b)^2 + (t cos(anglede) + \dx )^2 = 64
    #  t^2 + 2 (\b sin + \dx cos ) + (\b sin + \dx cos )^2
    #  = 64 - \b^2 - \dx^2 + (\b sin +  \dx cos  )^2
    #  t = sqrt ((\b sin + \dx cos )^2 +  64 - \b^2 - \dx^2 )  - (\b sin + \dx cos )
    ee=b*math.sin(anglede*Deg2Rad) + dx*math.cos(anglede*Deg2Rad)
    et=math.sqrt(ee * ee + bigradius * bigradius -b * b - dx * dx) - ee

    # x and y components of E position
    ex=et*math.cos(anglede*Deg2Rad) + dx
    ey=et*math.sin(anglede*Deg2Rad) + b
    anglece=math.acos(ex/math.sqrt(ex * ex+ey * ey))*Rad2Deg
    angleced=anglece-anglede
    outangle=math.asin(math.sin(angleced*Deg2Rad) * refractiveindex)*Rad2Deg

    bigfile.write(f" {totallines}, {i}, {refractiveindex}, {bigradius}," +
                  f"{a}, {b}, {z}, {anglez}, {c}, {anglea}," +
                  f"{incidentangle}, {refractiveangle}, {anglede}, {dx}," +
                  f"{ee}, {et}, {ex}, {ey}, {anglece}, {angleced}," +
                  f"{outangle}, {PickTypicalColor(i)} \n")

bigfile.close()



