#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, signal, argparse
import re
import unidecode

parser = argparse.ArgumentParser("main.py")
parser.add_argument("file", metavar='file', help="input file (e.g. 'input.txt')", type=str)
parser.add_argument("inc", metavar='inc', help="include letters (e.g. 'us')", type=str)
parser.add_argument("exc", metavar='exc', help="exclude letters (e.g. 'abc')", type=str)
parser.add_argument("--starts", metavar='starts', help="starts with (e.g. 's')", type=str)
parser.add_argument("--ends", metavar='ends', help="ends with (e.g. 'u')", type=str)
args = parser.parse_args()

def main():
    lines = 0
    with open(args.file) as f:
        lines = f.readlines()
    sel = []
    for line in lines:
        if (len(line) == 6):
            sel.append(unidecode.unidecode(line).strip())
    
    contains = str(args.inc)
    notcontains = str(args.exc)

    include = ''
    for i in contains:
        include = include + "(?=.*[" + i + "])"
    exclude = ''
    for i in notcontains:
        exclude = exclude + "(?![" + i + "])"
    regex = '^' + include + '(?:' + exclude + '.)*$'
    print("[debug] Regex filter 1: " + regex)

    pat = re.compile(regex)

    res = []
    for x in sel:
        if (pat.search(x)):
            res.append(x)
    
    ret = res
    if (args.starts or args.ends):

        starts = str(args.starts)
        ends = str(args.ends)
        if (starts == 'None'):
            regex = "^.*(" + ends + ")$"
        elif (ends == 'None'):
            regex = "^(?=" + starts + ").*$"
        else:
            regex = "^(?=" + starts + ")(.*" + ends + ")$"
        print("[debug] Regex filter 2: " + regex)

        pat = re.compile(regex)
        ret = []

        for x in res:
            if (pat.search(x)):
                ret.append(x)
    
    temp = ''; i = 1
    for x in ret:
        if (i == 1):
            temp = '(' + str(i) + ') ' + x + '\t'
            i += 1
            continue
        temp = temp + '(' + str(i) + ') ' + x + '\t'
        if ((i % 5) == 0):
            temp = temp + '\r\n'
        i += 1
    print("[info ] Results from file:")    
    print(temp)

if __name__=="__main__":
    try:
        main()
    except (KeyboardInterrupt):
        print("\r\n[ info] Exiting")
