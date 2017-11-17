./Muscle -in ./Problem1/sigma.ref -out sigma.align
./Hammer/binaries/hmmbuild sigma.hmm sigma.align 

./Muscle -in ./Problem1/sporecoat.ref -out sporecoat.align
./Hammer/binaries/hmmbuild sporecoat.hmm sporecoat.align

./Muscle -in ./Problem1/transporter.ref -out transporter.align
./Hammer/binaries/hmmbuild transporter.hmm transporter.align 

for file in Problem1/*.fasta
do
    ./Hammer/binaries/hmmsearch --tblout $file.sigma.hits sigma.hmm $file
    ./Hammer/binaries/hmmsearch --tblout $file.sporecoat.hits sporecoat.hmm $file
    ./Hammer/binaries/hmmsearch --tblout $file.transporter.hits transporter.hmm $file
done

cat Problem1/*.hits | grep -v "#" | awk '{print $1,$3,$5}' | sed -E 's/tr\|[A-Z0-9]+\|[A-Z0-9]+_9//' > results.txt
