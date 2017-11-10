#!/usr/bin/ bash
for i in Problem1/*.ref
	do 
	../../.././muscle3.8.31_i86win32 -in $i -out $i.aln
	../../../hmmer-3.1b2-cygwin64/binaries/./hmmbuild $i.hmm $i.aln
	done
for i in Problem1/*.fasta
	do 
	../../../hmmer-3.1b2-cygwin64/binaries/./hmmsearch sigma.hmm i 
> sigma.hmms
	../../../hmmer-3.1b2-cygwin64/binaries/./hmmsearch sporecoat.hmm i 
> sporecoat.hmms
	../../../hmmer-3.1b2-cygwin64/binaries/./hmmsearch transporter.hmm 
i > transporter.hmms
	done
	
 
