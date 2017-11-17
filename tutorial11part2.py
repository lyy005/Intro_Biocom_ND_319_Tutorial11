import numpy
import pandas

sequences=open("motifsort.fasta","r")
motif1file=open(motif1.txt,"w")
motif2file=open(motif2.txt,"w")
others=open(nonMotif.txt,"w")

for line in sequences:
    motif1= re.match(AKKPRVZE,str(sequences))
    motif2- re.match(AAQWWRNYGG,str(sequences))
    
    if motif1:
        motif1file.write(line + '\n')
    if motif2:
        motif2file.write(line + '\n')
    else:
        others.write(line + '\n')

print motif1file
print motif2file
print others