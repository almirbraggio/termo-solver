#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, signal, argparse
import re
import unidecode

parser = argparse.ArgumentParser("main.py")
parser.add_argument("inc", metavar='inc', help="include letter", type=str)
parser.add_argument("exc", metavar='exc', help="exclude letter", type=str)
args = parser.parse_args()

def main():
    lines = 0
    with open('dicio') as f:
        lines = f.readlines()
    sel = []
    for line in lines:
        if (len(line) == 6):
            sel.append(unidecode.unidecode(line).strip())
    
    alphabet = "abcdefghijklmnopqrstuvxwyz"
    contains = str(args.inc) #alphabet.translate({ord(i): None for i in str(args.inc)})
    notcontains = str(args.exc)
    #regex = "^(?=.*[" + contains + "])(?:(?![" + notcontains + "]).)*$"
    regex = "^(?=.*[o])(?=.*[i])(?=.*[s])(?=.*[a])(?:(?![c]).)*$"
    pat = re.compile(regex)

    res = []
    for x in sel:
        if (pat.search(x)):
            if ((x[1] != 'o') and (x[2] != 'i') and (x[3] != 's') and (x[4] != 'a')):
                res.append(x)
    
    for x in res:
        print(x)

if __name__=="__main__":
    try:
        main()
    except (KeyboardInterrupt):
        print("\r\n[ info] Exiting")
