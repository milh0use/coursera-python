import sys

filename = sys.argv[1]
ifh = open(filename)
ofh = open('humptylength.txt','w')

for line in ifh:
    ofh.write(str(len(line.strip('\n'))))
    ofh.write('\n')

ofh.close()
