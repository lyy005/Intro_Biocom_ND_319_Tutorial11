for i in *ref
do
    ../../../../muscle.exe -in $i -out $i.aln
    ../../../../hmmer-3.1b2-cygwin64/binaries/hmmbuild $i.hmm $i.aln
done


for i in *fasta
do
/home/Mati/hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout $i.sigma.hits sigma.ref.hmm $i
/home/Mati/hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout $i.sporecoat.hits sporecoat.ref.hmm $i                   
/home/Mati/hmmer-3.1b2-cygwin64/binaries/hmmsearch --tblout $i.transporter.hits transporter.ref.hmm $i
done

cat *.hits | grep "tr|" | sed -E 's/[tr|A-Z0-9]+\_9//' | awk '{print $1 " " $3 " " $5}' > bacteriahmmout.txt

