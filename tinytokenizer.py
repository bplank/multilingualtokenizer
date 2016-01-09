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
parser.add_argument("--conll", help="conll format rather than one sentence per line", required=False,default=False,action="store_true")

class TinyTokenizer(object):
    """
    TinyTokenizer
    """
    def __init__(self):
        pattern =  '''
                        (?:[+\-]?\d+[,/.:-]\d+)  # Numbers, including fractions, decimals.
                        |
                        (?:[\w]+[-]+[\w]+)       # don't split words with dashes
                        |
                        (?:[\w_]+)               # Words without dashes
                        |
                        (?:\S)                   # Everything else that isn't whitespace.
                        '''
        self.word_re = regex.compile(pattern, regex.VERBOSE | regex.UNICODE | regex.I)         # use regex for save unicode handling

    def tokenize(self,line):
        """
        return list of tokens
        """
        line = regex.sub(r"\s+"," ",line) # remove extra spaces
        return [w.group() for w in self.word_re.finditer(line)]


def main():

    args = parser.parse_args()

    tt = TinyTokenizer()

    for line in open(args.infile):
        line=line.strip()

        out = tt.tokenize(line)
        outline = " ".join(out)
        try:
            assert(str(regex.sub(r"\s","",line))==str(regex.sub("\s","",outline)))
            if args.conll:
                for w in out:
                    print(w)
                print()
            else:
                print(outline)
            
        except:
            print("==== CHECK FILE! ====",  args.infile, file=sys.stderr)
            print("+"*20, file=sys.stderr)
            print("in:  >>{}<<".format(line), file=sys.stderr)
            print("out: >>{}<<".format(outline), file=sys.stderr)     
            print(str(regex.sub(r"\s","",line)), file=sys.stderr)
            print(str(regex.sub(r"\s","",outline)), file=sys.stderr)





if __name__=="__main__":
    main()
