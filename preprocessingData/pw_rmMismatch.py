import sys
import os
sys.path.append(os.path.abspath("/home/kuangyu/Dropbox/research/MultinomProject/code/pyScripts"))
from codon2AA_mapping import *

def pw_rmMismatch(inputFile, outFile, mismatchFile):
	mapper = Codon2AAconvertor()
	fInput = open(inputFile, "r")
	allLines = fInput.readlines()
	fInput.close()
	fOut = open(outFile, "w")
	fMismatch = open(mismatchFile, "w")
	for line in allLines:
		tmpLine = line.split()
		if not (mapper.isCodonAAmatch(tmpLine[1], tmpLine[4]) and mapper.isCodonAAmatch(tmpLine[2], tmpLine[5]) and tmpLine[1] == tmpLine[8] and tmpLine[2] == tmpLine[12] and tmpLine[4] == tmpLine[11] and tmpLine[5] == tmpLine[15]):
			fMismatch.write(line)
		else:
			fOut.write(line)
	fOut.close()
	fMismatch.close()

if __name__ == '__main__':
	inputFile = sys.argv[1]
	outFile = sys.argv[2]
	mismatchFile = sys.argv[3]
	pw_rmMismatch(inputFile, outFile, mismatchFile)
