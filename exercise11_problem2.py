import os
import pandas
import re

cwd = os.getcwd()
print cwd

Motif1= r'AKKPRVZE'
Motif2 = r'AAQWWRNYGG'

thefile=open('./Exercise11_files/Problem2/motifsort.fasta',"r")

for line in thefile:
    line = line.strip()
    if ">" in line:
        seqid = line
    elif re.search(Motif1, line):
        m1 = line
        print seqid
        print m1
    elif re.search(Motif2, line):
        m2 = line
        print seqid
        print m2







