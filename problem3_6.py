import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]
ifh = open(infilename)
ofh = open(outfilename,'w')

for line in ifh:
    ofh.write(str(len(line.strip('\n'))))
    ofh.write('\n')

ofh.close()
