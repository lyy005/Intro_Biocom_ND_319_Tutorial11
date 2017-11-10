import pandas
import numpy
import re

infile=open("motifsort.fasta","r")
outfile1=open("motif1.fasta","w")
outfile2=open("motif2.fasta","w")
outfile3=open("null.fasta","w")

for line in infile:
    line=line.strip()
    if '>' in line:
        seqID=line
    elif re.search("AKKPRVZE",line):
        outfile1.write(seqID+"\n")
        outfile1.write(line+"\n")
    

