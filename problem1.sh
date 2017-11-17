#!/usr/bin/env bash
#################################################

for reffile in Exercise11_files/Problem1/*.ref

do

  #../muscle3.8.31_i86darwin64 -in $reffile -out $reffile.aln

  #../hmmer-3.1b2-macosx-intel/binaries/hmmbuild $reffile.hmm $reffile.aln

  for fastafile in Exercise11_files/Problem1/*.fasta

  do

    ../hmmer-3.1b2-macosx-intel/binaries/hmmsearch --tblout $reffile.hits $reffile.hmm $fastafile 


  done

done

cat *.hits | grep -v "#" | awk '{print $1, $2}' >> results.txt
