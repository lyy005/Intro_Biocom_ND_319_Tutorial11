###Question 1###

for i in *ref
do
    ../../../../muscle.exe -in $i -out $i.aln
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmbuild $i.hmm $i.align
done

for i in *fasta
do
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout sigma.hits sigma.hmm $i
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout sporecoat.hits sporecoat.hmm $i
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout transporter.hits transporter.hmm $i
done
