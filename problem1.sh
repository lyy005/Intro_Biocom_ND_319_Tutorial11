#!/usr/bin/env bash

for reffile in Exercise11_files/Problem1/*.ref
do
  #../muscle3.8.31_i86darwin64 -in $reffile -out $reffile.aln
  #../hmmer-3.1b2-macosx-intel/binaries/hmmbuild $reffile.hmm $reffile.aln
  for fastafile in Exercise11_files/Problem1/*.fasta
  do
    #echo $fastafile
    #echo $reffile
    ../hmmer-3.1b2-macosx-intel/binaries/hmmsearch $reffile.hmm $fastafile | head -n 15 | tail -n 1
    #| awk  '{printf("%s\n", $1)}' >> resultsProblem1.txt
    #| awk '{print $1, $2}' >> results.txt
  done
done
