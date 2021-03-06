import sys

def getRank(inputFile, outputFile):
    fInput = open(inputFile, "r")
    allInput = fInput.readlines()
    fInput.close()

    fOutput = open(outputFile, "w")
    for line in allInput:
        tmpLine = line.rstrip().split(",")
        trueProb = tmpLine[4]
        sortedProbs = sorted(map(float, tmpLine[5:len(tmpLine)]), reverse=True)
        rank = map(str,sortedProbs).index(trueProb) + 1
	if(rank<3):
        	fOutput.write(line)
    fOutput.close()

if  __name__ =='__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    getRank(inputFile, outputFile)
