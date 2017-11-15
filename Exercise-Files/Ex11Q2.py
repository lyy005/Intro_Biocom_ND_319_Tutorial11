import numpy
import pandas
import re

infile="motifsort.fasta"
out1="motif1.fasta"
out2="motif2.fasta"
null="null.fasta"

#define the patterns
Pat1="AKKPRVZE"
Pat2="AAQWWRNYGG"

for line in infile:
    line=line.strip()
    if line[0] == ">":
        seqid=line
    else:
        if Pat1 in in line:
        #(re.search(Pat1, line))
            out1.write(seqid + "\n")
            out1.write(line + "\n")
        elif if Pat2 in line: 
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
              
        
