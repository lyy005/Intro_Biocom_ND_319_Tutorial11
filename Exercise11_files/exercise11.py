###Question 1###

for i in *ref
do
    muscle -in 4i -out $i.aln
    hmmbuild ________
done

for i in *fasta
do
    hmmsearch #model1
    hmmsearch #model2
    hmmsearch #model3
done

####Question 2####
for line in infile:
    if ">"
        seqid=line
    elif "/tkk"
        print seqid
        print line