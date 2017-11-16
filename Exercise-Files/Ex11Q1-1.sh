#!/usr/bin/ bash

for i in Problem1/*.ref
	do 
	../../.././muscle3.8.31_i86win32 -in $i -out $i.aln
	../../../hmmer-3.1b2-cygwin64/binaries/./hmmbuild $i.hmm $i.aln
	done 
cat Problem1/*.fasta >> all-files.fasta
../../../hmmer-3.1b2-cygwin64/binaries/./hmmsearch Problem1/sigma.ref.hmm all-files.fasta > sigma.hmms
../../../hmmer-3.1b2-cygwin64/binaries/./hmmsearch Problem1/sporecoat.ref.hmm all-files.fasta > sporecoat.hmms
../../../hmmer-3.1b2-cygwin64/binaries/./hmmsearch Problem1/transporter.ref.hmm all-files.fasta > transporter.hmms
	
 
