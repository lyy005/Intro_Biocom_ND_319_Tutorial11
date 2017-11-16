import pandas
import numpy
import re

infile=open("motifsort.fasta","r") #Open input fasta file as read-only
outfile1=open("motif1.fasta","w") #Create 3 new files - one each to store sequences that match a motif
outfile2=open("motif2.fasta","w") 
outfile3=open("null.fasta","w") #And one for sequences that do not match either

for line in infile: #Loop through each line in the fasta file
    line=line.strip() #Strip newline characters
    if '>' in line: #If the line has a >, it's a sequence ID - store it for later reference
        seqID=line
    elif re.search("AKKPRVZE",line): #Check for matches for motif 1
        outfile1.write(seqID+"\n") #If motif 1 is a match, store the sequence ID, followed by the actual
        outfile1.write(line+"\n") #sequence read in the file for motif 1
    elif re.search("AAQWWRNYGG",line): #Chaeck for matches for motif 2 if there are no matches for motif 1
        outfile2.write(seqID+"\n") #If motif 2 is a match, store the sequence ID, followed by the
        outfile2.write(line+"\n") #sequence read in the file for motif 2
    else: #If neither motif matches, store the sequence ID and the sequence read in the file for no motifs
        outfile3.write(seqID+"\n") 
        outfile3.write(line+"\n")

infile.close() #Close all files
outfile1.close()
outfile2.close()
outfile3.close()
    

