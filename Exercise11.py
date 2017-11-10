#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:44:24 2017

@author: chenyingying
"""

import re as re
import pandas as pd

reg1='AKKPRVZE'
reg2='AAQWWRNYGG'

vcffile = open("motifsort.fasta","r")
outfile1= open("Motif1.fasta","w")
outfile2= open("Motif2.fasta","w")
outfile3= open("Motifno.fasta","w")
for line in vcffile:
    line=line.strip()
    if line.startswith('>'):
        seqid=line
    elif re.search(reg1,line):
        motif1=line
        outfile1.write(seqid+'\n')
        outfile1.write(line+'\n')
    elif re.search(reg2,line):
        motif2=line
        outfile2.write(seqid+'\n')
        outfile2.write(line+'\n')
    else:
         outfile3.write(seqid+'\n')
         outfile3.write(line+'\n')

outfile1.close()
outfile2.close()
outfile3.close()
vcffile.close()