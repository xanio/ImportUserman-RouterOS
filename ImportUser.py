#!/usr/bin/env python

__author__ = "Xanio"
__license__ = "CC0"
__version__ = "1.0"
__maintainer__ = "Xanio"
__email__ = "xanio@nemesilabs.org"

import csv     # imports the csv module
import sys      # imports the sys module
import argparse # imports the argparse module

parser = argparse.ArgumentParser(
        prog='ImportUser',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=''''Application for import user into user-manager
            from a CSV File. The Application create a output script RouterOS

            Ex. CSV File:
            "Login","Passowd"
            "user1","pass1"
            "user2","pass2"
            ...
            ''')
parser.add_argument('FileCsv', help='First Argument is infile.csv')
parser.add_argument('OutFile', help='Second Argument is outfile.rsc')
parser.add_argument('ProfileName', help='Third Argument is Profile Name')
args = parser.parse_args()

filename = open(sys.argv[1], 'rb') # opens the csv file
out_file = open(sys.argv[2],"w") # opens the rsc file
profilename = sys.argv[3] # write ProfileName
with filename as f:
    reader = csv.DictReader(f)
    try:
        for row in reader:
            out_file.write("tool user-manager user add disabled=no username="+row['Login']+" password="+row['Password']+" customer=admin\n")
            out_file.write("tool user-manager user create-and-activate-profile \""+row['Login']+"\" profile="+profilename+" customer=admin\n")
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
filename.close()
out_file.close()
