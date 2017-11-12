import re
import os

current = os.getcwd()
os.chdir("./Exercise11_files/Problem2/")
inputFile = open("motifsort.fasta","r")
os.chdir(current)
motif1Output = open("motif1.txt","w")
motif2Output = open("motif2.txt","w")
noMotifOutput = open("noMotif.txt","w")

motif1 = re.compile(r"AKKPRVZE")
motif2 = re.compile(r"AAQWWRNYGG")

for ln in inputFile:
    if ln.startswith(">"):
        continue
    ln.strip()
    if re.search(motif1, ln) is not None:
        motif1Output.write(ln)
        continue
    if re.search(motif2, ln) is not None:
        motif2Output.write(ln)
        continue
    noMotifOutput.write(ln)
        

inputFile.close()
motif1Output.close()
motif2Output.close()
noMotifOutput.close()