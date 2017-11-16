import numpy
import pandas
import re

# open files to read and write
infile=open("motifsort.fasta","r")
out1=open("motif1.fasta","w")
out2=open("motif2.fasta","w")
null=open("null.fasta","w")

#define the REGEX patterns
Pat1=r"AKKPRVZE"
Pat2=r"AAQWWRNYGG"

for line in infile:
    line=line.strip()
    if line[0] == ">":
        seqid=line
    else:
        if Pat1 in line:
        #(re.search(Pat1, line))
            out1.write(seqid + "\n")
            out1.write(line + "\n")
        elif Pat2 in line: 
        #(re.search(Pat2, line))
            out2.write(seqid + "\n")
            out2.write(line + "\n")
        else:
            null.write(seqid + "\n")
            null.write(line + "\n")
              
#Close files
infile.close()
out1.close()
out2.close()
null.close()
              
        
