import re
# open fastafile
thefile=open('./Exercise11_files/Problem2/motifsort.fasta',"r")

# search strings
Motif1= r'AKKPRVZE'
Motif2 = r'AAQWWRNYGG'

# lists!
m1_id = []
m1_seq = []

m2_id = []
m2_seq = []

other_id = []
other_seq = []

# loop over the file
for line in thefile:
    line = line.strip()
    if ">" in line:
        seqid = line
    elif re.search(Motif1, line):
        m1 = line
        m1_id.append(seqid)
        m1_seq.append(m1)
    elif re.search(Motif2, line):
        m2 = line
        m2_id.append(seqid)
        m2_seq.append(m2)
    else:
        other_id.append(seqid)
        other_seq.append(line)

# write fasta files from lists :)
ofile = open("m1_motif.txt", "w")
for i in range(len(m1_id)):
    ofile.write(m1_id[i] + "\n" +m1_seq[i] + "\n")
ofile.close()

ofile = open("m2_motif.txt", "w")
for i in range(len(m2_id)):
    ofile.write(m2_id[i] + "\n" +m2_seq[i] + "\n")
ofile.close()

ofile = open("other.txt", "w")
for i in range(len(m1_id)):
    ofile.write(other_id[i] + "\n" +other_seq[i] + "\n")
ofile.close()