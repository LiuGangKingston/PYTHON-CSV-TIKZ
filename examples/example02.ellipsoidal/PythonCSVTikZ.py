#   This is the supporting source file for
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
#
import sys
import math
from   collections import deque


PI             = 3.14159265358979323846e0             #;
Rad2Deg        = 57.29577951308232e0                  #;  // 180/pi;
Deg2Rad        = 0.017453292519943296e0               #;  // pi/180;
NapierConstant = 2.71828182845904523536e0             #;
EulerNumber    = 2.71828182845904523536e0             #;

AccelerationDueToEarthGravity  = 9.80e0               #;// "m/s$^2$"
AtomicMassConstant             = 1.66053906660e-27    #;// kg
AvogadroNumber                 = 6.02214076e23        #;// "mol$^{-1}$"
BohrMagneton                   = 9.2740100783e-24     #;// "J/T"
BohrRadius                     = 5.29177210903e-11    #;// m
BoltzmannConstant              = 1.380649e-23         #;// "J/K"
ClassicalElectronRadius        = 2.8179403262e-15     #;// m
CoulombConstant                = 8.9875517923e9       #;// "N$\cdot $m$^2$/C$^2$"
ElementaryCharge               = 1.602176634e-19      #;// "C"
FaradayConstant                = 9.648533212e4        #;// C/mol
FineStructureConstant          = 7.2973525693e-3      #;//
FirstRadiationConstant         = 3.741771852e-16      #;// W$\dot m^2$
MassOfElectron                 = 9.1093837015e-31     #;// "kg"
MassOfNeutron                  = 1.67492749804e-27    #;// "kg"
MassOfProton                   = 1.67262192369e-27    #;// "kg"
NuclearMagneton                =  5.0507837461e-27    #;// "J/T"
PlanckConstant                 = 6.62607015e-34       #;// "J$\cdot $s"
RydbergConstant                = 1.0973731568160e7    #;// 1/m
SecondRadiationConstant        = 1.438776877e-2       #;// m$\dot K$
SpeedoFlightInVacuum           = 2.99792458e+8        #;// "m/s"
ThomsonCrossSection            = 6.6524587321e-29     #;//  $m^2$
UniversalGasConstant           = 8.314462618e0        #;// "J/(mol$\cdot $K)"
UniversalGravitationalConstant = 6.67430e-11          #;// "N$\cdot $m$^2$/kg$^2$"
VacuumElectricPermittivity     = 8.8541878128e-12     #;// "F/m"
VacuumMagneticPermeability     = 1.25663706212e-6     #;// "N/$A^2$"

TypicalColors=['red','orange','yellow','green','blue']

TikZColors=['red','purple','magenta','pink',
            'violet','white','orange','yellow',
            'green','lime','brown','olive',
            'blue','cyan','teal','lightgray',
            'gray','darkgray','black'           ]

Colors=['Apricot','Aquamarine','Bittersweet','Black',
        'Blue','BlueGreen','BlueViolet','BrickRed',
        'Brown','BurntOrange','CadetBlue','CarnationPink',
        'Cerulean','CornflowerBlue','Cyan','Dandelion',
        'DarkOrchid','Emerald','ForestGreen','Fuchsia',
        'Goldenrod','Gray','Green','GreenYellow',
        'JungleGreen','Lavender','LimeGreen','Magenta',
        'Mahogany','Maroon','Melon','MidnightBlue',
        'Mulberry','NavyBlue','OliveGreen','Orange',
        'OrangeRed','Orchid','Peach','Periwinkle',
        'PineGreen','Plum','ProcessBlue','Purple',
        'RawSienna','Red','RedOrange','RedViolet',
        'Rhodamine','RoyalBlue','RoyalPurple','RubineRed',
        'Salmon','SeaGreen','Sepia','SkyBlue',
        'SpringGreen','Tan','TealBlue','Thistle',
        'Turquoise','Violet','VioletRed','White',
        'WildStrawberry','Yellow','YellowGreen','YellowOrange']

def PickTypicalColor(i):
    return TypicalColors[abs(i)%len(TypicalColors)]

def PickTikZColor(i):
    return TikZColors[abs(i)%len(TikZColors)]

def PickColor(i):
    return Colors[abs(i)%len(Colors)]

class PythonCSVTikZFileGroup:
    FileNamePrefixes = []
    PythonCSVTikZFileExtension=".csv"

    def __init__(self, FileNamePrefix, StartingRow, EndingRow, RowsInEachFile):
        self.PrefixLength = len(FileNamePrefix)
        for self.inpf in FileNamePrefix:
            if self.inpf == ' ':
                self.PrefixLength = self.PrefixLength - 1
            if self.inpf == '\t':
                self.PrefixLength = self.PrefixLength - 1

        if self.PrefixLength < 1:
            print("Since the FileNamePrefix is empty,")
            print("stopped, when creating a PythonCSVTikZFileGroup object.")
            sys.exit()

        for self.ipre in self.FileNamePrefixes:
            if FileNamePrefix == self.ipre:
                print("The FileNamePrefix was used in other PythonCSVTikZFileGroup object creation earlier.")
                print("Although just a WARNING, maybe you are trying to overwrite exsisting file(s). ")
                print("Although just a WARNING, maybe you are trying to overwrite exsisting file(s). ")
                print("Although just a WARNING, maybe you are trying to overwrite exsisting file(s). ")

        if RowsInEachFile < 0:
            print("Since RowsInEachFile is "+ str(RowsInEachFile) + " negative, ")
            print("stopped, when creating a PythonCSVTikZFileGroup object.")
            sys.exit()

        self.TotalRowsInEachFile = RowsInEachFile
        self.StartingRowNumber = StartingRow
        self.EndingRowNumber = EndingRow
        self.AbsoluteRowRange = abs(EndingRow - StartingRow)
        self.RowNumberDirection = 1
        if StartingRow > RowsInEachFile:
            self.RowNumberDirection = -1
        self.TotalFiles = abs(StartingRow - EndingRow) // RowsInEachFile + 1

        self.GroupFiles = deque()
        for self.i in range(self.TotalFiles):
            self.thefilename = FileNamePrefix+str((self.i) + 1)+self.PythonCSVTikZFileExtension
            (self.GroupFiles).append(open(self.thefilename,'w'))
            if  (self.GroupFiles)[self.i].closed:
                print('The file ' + self.thefilename + ' open is failed ')
                print("stopped, when creating a PythonCSVTikZFileGroup object.")
                sys.exit()
            else:
                print('The file ' + self.thefilename + ' is opened as number: ' + str(self.i))
        self.FileNamePrefixes.append(FileNamePrefix)

    def FileGroupClose(self):
        for self.ifile in self.GroupFiles:
            self.ifile.close()

    def GetFileForRow(self,RowNumber):
        self.dis = RowNumber-self.StartingRowNumber
        if (self.dis*self.RowNumberDirection) < 0:
            print("The RowNumber should be from "+ str(self.StartingRowNumber) + " to "+ str(self.EndingRowNumber))
            print("Stopped for bad RowNumber " + str(RowNumber) + " in GetFileForRow.")
            sys.exit()
        if abs(self.dis) > self.AbsoluteRowRange:
            print("The RowNumber should be from "+ str(self.StartingRowNumber) + " to "+ str(self.EndingRowNumber))
            print("Stopped for bad RowNumber " + str(RowNumber) + " in GetFileForRow.")
            sys.exit()
        self.iii = abs(self.StartingRowNumber - RowNumber) // self.TotalRowsInEachFile
        return (self.GroupFiles)[self.iii]

    def FirstListToAllFiles(self,TheList):
        for self.ifile in self.GroupFiles:
            self.WriteARowToTheFile(self.ifile,TheList)

    def WriteAListRow(self,RowNumber,TheList):
        self.thefile = self.GetFileForRow(RowNumber)
        self.WriteARowToTheFile(self.thefile,TheList)

    def WriteARowToTheFile(self,thefile,TheList):
        self.totalelement = len(TheList)
        self.tlessone = self.totalelement - 1
        if self.tlessone > 0:
            for self.element in range(self.tlessone):
                thefile.write(TheList[self.element])
                thefile.write(',')
        thefile.write(TheList[self.tlessone])
        thefile.write('\n')


# The end of class PythonCSVTikZFileGroup and file.
# The end of class PythonCSVTikZFileGroup and file.
# The end of class PythonCSVTikZFileGroup and file.



