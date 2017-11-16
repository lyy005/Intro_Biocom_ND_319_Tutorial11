#Problem1
#File already unzipped

#muscle steps for each .ref file

../muscle3.8.31_i86win32.exe -in sigma.ref -out sigma.ref.muscle
../muscle3.8.31_i86win32.exe -in sporecoat.ref -out sporecoat.ref.muscle
../muscle3.8.31_i86win32.exe -in transporter.ref -out transporter.ref.muscle

#hmmbuild steps for each .ref file

../hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe sigma.ref.hmm sigma.ref.muscle
../hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe sporecoat.ref.hmm sporecoat.ref.muscle
../hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transporter.ref.hmm transporter.ref.muscle


for i in *fasta
do
	../hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.sigma.hits sigma.ref.hmm $i
	../hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.sporecoat.hits sporecoat.ref.hmm $i
	../hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transporter.hits transporter.ref.hmm $i
done

cat *.hits | grep "tr|" | sed -E 's/[tr|A-Z0-9]+\_9//' | awk '{print $1 " " $3 " " $5}' > finalhmmout.txt

