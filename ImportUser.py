#!/usr/bin/env python

__author__ = "Xanio"
__license__ = "CC0"
__version__ = "1.1"
__maintainer__ = "Xanio"
__email__ = "xanio@nemesilabs.org"

import csv     # imports the csv module
import argparse  # imports the argparse module


def options():
    parser = argparse.ArgumentParser(
        prog='ImportUser',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=''''An application to import user into user-manager
                from a CSV File. The Application creates an output script
                RouterOS

                Ex. CSV File:
                "Login","Passord"
                "user1","pass1"
                "user2","pass2"
                ...
                ''')
    parser.add_argument('FileCsv', help='First Argument is infile.csv')
    parser.add_argument('OutputFile', help='Second Argument is outfile.rsc')
    parser.add_argument('ProfileName', help='Third Argument is Profile Name')
    return parser.parse_args()


def main():
    # parsing opzioni linea di comando
    args = options()
    try:
        with open(args.FileCsv, 'rb') as a, open(args.OutputFile, 'w') as b:
            reader = csv.DictReader(a)
            try:
                for row in reader:
                    statement1 = (  # spezzo riga lunga
                        "tool user-manager user add disabled=no "
                        "username=%s "
                        "password=%s "
                        "customer=admin"
                        "\n"
                        % (row['Login'], row['Password'])
                    )
                    statement2 = (
                        'tool user-manager user '
                        'create-and-activate-profile "%s" '
                        'profile=%s '
                        'customer=admin'
                        '\n'
                        % (row['Login'], args.ProfileName)
                    )
                    b.write(statement1)
                    b.write(statement2)
            except csv.Error as e:
                exit(
                    'file %s, line %d: %s' %
                    (args.FileCsv, reader.line_num, e)
                )
    except IOError as e:
        print e
        exit(-1)


if __name__ == "__main__":
    main()
