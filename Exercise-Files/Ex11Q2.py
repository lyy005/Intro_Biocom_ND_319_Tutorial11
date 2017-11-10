import numpy
import pandas
import re
infile="motifsort.fasta"
out1="motif1.fasta"
out2="motif2.fasta"
null="null.fasta"

for line in infile:
    line=line.strip()
    if ">":
        seqid=line
    elif "AKKPRVZE":
        print seqid
        print line
    elif "AAQWWRNYGG":
        print seqid
        print line
    else:
        print seqid
        print line