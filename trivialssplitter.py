#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A trivial punctuation-based sentence splitter
for multi-lingual data

author: Barbara Plank

"""
import re
import regex 
import sys
import argparse

parser = argparse.ArgumentParser(description="""a trivial sentence splitter - works on a line-by-line basis""")
parser.add_argument("infile", help="file with one sentence per line")

class TinySentenceSplitter(object):
    """
    split by punctuation, i.e. fullstop, question mark and exclamation mark
    """
    def __init__(self):
        ## see punct_unicode.txt 
        self.punct_re = regex.compile(r'([.?!\u06D4\u061F\u1362\u1367\u0589\u055E\u166E\u3002\u0964\uFF0E\uFF1F])', regex.UNICODE)
        pass

    def split(self,line):
        """
        split line by punctuation
        """
        return [line.strip() for line in self.punct_re.sub(r"\1\n",line).split("\n") if line]


def main():

    args = parser.parse_args()

    tt = TinySentenceSplitter()

    for line in open(args.infile):
        line=line.strip()

        for line in tt.split(line):
            print(line)


if __name__=="__main__":
    if (sys.version_info < (3, 0)):
        print("needs python3 or above")
        exit()
    main()
