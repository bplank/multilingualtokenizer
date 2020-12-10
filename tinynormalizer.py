#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A tiny tokenizer
for multi-lingual data

author: Barbara Plank

# Note: needs the regex package, as the package "re" does not capture indic vowel markers in \w
# this is a bug is cf. http://stackoverflow.com/questions/12746458/
"""
import re
import regex 
import sys
import argparse

parser = argparse.ArgumentParser(description="""simple tokenizer, inspired by Christopher Pott's twitter tokenizer; expects one sentence per line""")
parser.add_argument("infile", help="file with one sentence per line")

class TinyNormalizer(object):
    """
    TinyNormalizer

    replace @usernames and http (urls) with <USER> and <URL>
    """

    def normalize(self, word):
        if word.lower().startswith("http"):
            return "<URL>"
        
        elif word.startswith("@") or word.startswith(".@"):
            return "<USER>"
        else:
            return word
        
    def tokenize(self,line):
        """
        return list of tokens
        """
        line = regex.sub(r"\s+"," ",line) # remove extra spaces
        return [self.normalize(w) for w in line.split()]


def main():

    args = parser.parse_args()

    tt = TinyNormalizer()

    for line in open(args.infile):
        line=line.strip()

        out = tt.tokenize(line)
        outline = " ".join(out)
        try:
            #assert(str(regex.sub(r"\s","",line))==str(regex.sub("\s","",outline)))
            print(outline)
            
        except:
            print("==== CHECK FILE! ====",  args.infile, file=sys.stderr)
            print("+"*20, file=sys.stderr)
            print("in:  >>{}<<".format(line), file=sys.stderr)
            print("out: >>{}<<".format(outline), file=sys.stderr)     
            

if __name__=="__main__":
    if (sys.version_info < (3, 0)):
        print("needs python 3")
        exit()
    main()
