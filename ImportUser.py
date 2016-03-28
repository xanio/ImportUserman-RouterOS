#!/usr/bin/env python

__author__ = "Xanio"
__license__ = "CC0"
__version__ = "1.1"
__maintainer__ = "Xanio"
__email__ = "xanio@nemesilabs.org"

import csv     # imports the csv module
import argparse  # imports the argparse module


def set_easy_logger(name, verbosity, logfile=False):
    '''
    Easy setup for a logger
    '''
    import logging
    level = getattr(logging, verbosity, None)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # create file handler
    if logfile:
        try:
            fh = logging.FileHandler(logfile)
            fh.setLevel(level)
            fh.setFormatter(formatter)
            # add the handler to logger
            logger.addHandler(fh)
        except IOError as e:
            print e
    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    # add the handler to logger
    logger.addHandler(ch)
    # finally, return the logger
    return logger


def options():
    parser = argparse.ArgumentParser(
        prog='ImportUser',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
       Given a CSV file, it returns a script that can be imported into RouterOS

       Ex. CSV File:
           "Login","Passord"
           "user1","pass1"
           "user2","pass2"
           ...
        ''')
    parser.add_argument('FileCsv', help='First Argument is infile.csv')
    parser.add_argument('OutputFile', help='Second Argument is outfile.rsc')
    parser.add_argument('ProfileName', help='Third Argument is Profile Name')
    parser.add_argument(
        '-v',
        '--verbosity',
        help='set verbosity',
        choices=[
            'debug',
            'info',
            'warning',
            'error',
            'critical'],
        default='warning')
    parser.add_argument('-l', '--logfile', help='log output to a file',
                        default=False)
    return parser.parse_args()


def main():
    with open(args.FileCsv, 'rb') as a, open(args.OutputFile, 'w') as b:
        reader = csv.DictReader(a)
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
            logger.info(statement1)
            logger.info(statement2)
            b.write(statement1)
            b.write(statement2)


if __name__ == "__main__":
    # parsing command line options
    args = options()
    logger = set_easy_logger(
        'ImportUser',
        args.verbosity.upper(),
        args.logfile)
    # Ex:
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warn('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
    try:
        main()
    except Exception as e:
        logger.critical("BIG TROUBLE!")
        logger.critical(e)
        logger.critical("quitting with error..")
        exit(-1)
