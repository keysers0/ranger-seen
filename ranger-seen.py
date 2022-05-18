#!/usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(description="Mark files as watched or unwatched,")
parser.add_argument("-f", help="pass file name", default=None)
parser.add_argument("-d", help="pass file directory", default=None)
args = parser.parse_args()

def do_magic(file, directory):
    name = directory + "/" + file
    seen = directory + "/+++" + file
    unseen = name.replace('+++', '', -3)

    if "+++" in file:
        os.rename(name, unseen)
    else:
        os.rename(name, seen)

try:
    do_magic(file=args.f, directory=args.d)
except:
    print("You must provide a directory and a file using -d and -f flags respectivley.")
    exit()
