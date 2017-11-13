###Question 1###

for i in *ref
do
    ../../../../muscle.exe -in $i -out $i.aln
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmbuild $i.hmm $i.aln
done

for i in *fasta
do
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout $i.sigma.hits sigma.ref.hmm $i
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout $i.sporecoat.hits sporecoat.ref.hmm $i
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout $i.transporter.hits transporter.ref.hmm $i
done
