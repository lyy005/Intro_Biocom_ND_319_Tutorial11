import os
import pandas

cwd = os.getcwd()
print cwd

thefile=open('./Exercise11_files/Problem2/motifsort.fasta',"r")

for line in thefile:
    line = line.strip()
    if ">" in line:
        print line
    else:
        print "harold"