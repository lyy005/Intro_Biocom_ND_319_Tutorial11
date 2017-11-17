
import re

motifsortin=open("motifsort.fasta","r")
motif1out=open("motif1.fasta","w")
motif2out=open("motif2.fasta","w")
nomotifout=open("nomotif.fasta","w")

motif1= r'AKKPRVZE'
motif2= r'AAQWWRNYGG'

tempid_m1=[]
tempid_m2=[]
tempid_no=[]
tempseq_m1=[]
tempseq_m2=[]
tempseq_no=[]


for line in motifsortin:
    line = line.strip()
    if ">" in line:
        seqid = line
    elif re.search(motif1, line):
        motif1out.write(seqid + "\n" +line + "\n")
    elif re.search(motif2, line):
        motif2out.write(seqid + "\n" +line + "\n")
    else:
        nomotifout.write(seqid + "\n" +line + "\n")
        

