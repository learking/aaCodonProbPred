import sys
from aaProbSolver import *
import re
import glob
import math

#'L' is the reference codon
aaList = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

#coef file and folders
firstOrderCoefFile = '/home/kwang2/scripts/aaCodonProbPred/coefs/aa_sa_coef.txt'
firstCondSecondFiles = glob.glob("/home/kwang2/scripts/aaCodonProbPred/coefs/aa_firstCondSecond_coefs/*.txt")
secondCondFirstFiles = glob.glob("/home/kwang2/scripts/aaCodonProbPred/coefs/aa_secondCondFirst_coefs/*.txt")

class AApairwise:
    
    __catPattern = re.compile(r"\_(\w+)\_coef\.txt")

    def __init__(self, pwFile):
        #init solvers
        ## first order solver
        fFirstOrder = open(firstOrderCoefFile, "r")
        firstOrderCoefs = fFirstOrder.readlines()
        fFirstOrder.close()
        self.firstOrderSolver = aaProbSolver(firstOrderCoefs)

	## second order solvers
	### first conditioned on second
	self.firstCondSecondSolvers = self.__constructSolvers__(firstCondSecondFiles)
	### second conditioned on first
	self.secondCondFirstSolvers = self.__constructSolvers__(secondCondFirstFiles)

        self.aaDict = dict()
        self.saDict = dict()
        self.firstPosDict = dict()
        self.secondPosDict = dict()
        self.pairDict = dict()
        self.posList = []

        fInput = open(pwFile, "r")
        allLines = fInput.readlines()
        fInput.close()
        for line in allLines:
            tmpLine = line.split()
            firstAA = tmpLine[4]
            secondAA = tmpLine[5]
            firstPos = tmpLine[6]
            secondPos = tmpLine[7]
            firstSA = tmpLine[9]
            secondSA = tmpLine[13]
            #float
            invSD = 1.0/(float(secondPos) - float(firstPos))
            invTD = 1.0/float(tmpLine[3])

            # fill aaDict and saDict
            if firstPos not in self.aaDict.keys():
                self.aaDict[firstPos] = firstAA
                self.saDict[firstPos] = firstSA
            if secondPos not in self.aaDict.keys():
                self.aaDict[secondPos] = secondAA
                self.saDict[secondPos] = secondSA
            
            # fill pos Dicts
            if firstPos not in self.firstPosDict.keys():
                self.firstPosDict[firstPos] = []
                self.firstPosDict[firstPos].append(secondPos)
            else:
                if secondPos not in self.firstPosDict[firstPos]:
                    self.firstPosDict[firstPos].append(secondPos)

            if secondPos not in self.secondPosDict.keys():
                self.secondPosDict[secondPos] = []
                self.secondPosDict[secondPos].append(firstPos)
            else:
                if firstPos not in self.secondPosDict[secondPos]:
                    self.secondPosDict[secondPos].append(firstPos)

            #fill in pairDict
            currPair = (firstPos, secondPos)
            self.pairDict[currPair] = map(float, ["1", firstSA, secondSA, invSD, invTD])

        self.posList = sorted(map(int, self.aaDict.keys()))

    
    def __constructSolvers__(self, coefFiles):
	solvers = {}

	for f in coefFiles:
		currCatName = AApairwise.__catPattern.search(f).group(1)
		currFile = open(f, "r")
            	currDat = currFile.readlines()
            	currFile.close()
		solvers[currCatName] = aaProbSolver(currDat)

	return solvers

    def getAAprob_onePos(self, pos):
        aaProbs = []
        for aa in aaList:
	    currAAprob = 0
	    currLogP = 0
            #calculate prob for this aa
            #first order
	    firstOrderX = [1, float(self.saDict[pos])]
            firstOrderProb = self.firstOrderSolver.getCatProb(aa, firstOrderX)

	    currLogP += math.log(firstOrderProb)

            #second order
	    beforeAAs = []
	    afterAAs = []
	    if pos in self.secondPosDict.keys():
		beforeAAs = self.secondPosDict[pos]
		#deal with P(pos=second|first) prob calculation
		for firstAA_pos in beforeAAs:
			tmpX = self.pairDict[(firstAA_pos, pos)]
			currLogP += math.log(self.firstCondSecondSolvers[aa].getCatProb(self.aaDict[firstAA_pos], tmpX)) - math.log(self.firstOrderSolver.getCatProb(self.aaDict[firstAA_pos], [1, float(self.saDict[firstAA_pos])]))

	    if pos in self.firstPosDict.keys():    
		afterAAs = self.firstPosDict[pos]
		#deal with P(pos=first|second) prob calculation
		for secondAA_pos in afterAAs:
			tmpX = self.pairDict[(pos, secondAA_pos)]
			currLogP += math.log(self.secondCondFirstSolvers[aa].getCatProb(self.aaDict[secondAA_pos], tmpX)) - math.log(self.firstOrderSolver.getCatProb(self.aaDict[secondAA_pos], [1, float(self.saDict[secondAA_pos])]))

	    currAAprob = math.exp(currLogP)
	    aaProbs.append(currAAprob)
	sumProb = sum(aaProbs)
	aaProbs = [x/sumProb for x in aaProbs]

	maxProb = max(aaProbs)
	maxAA = aaList[aaProbs.index(maxProb)]
	trueAA = self.aaDict[pos]
	trueProb = aaProbs[aaList.index(trueAA)]
	return pos + "," + maxAA + "," + str(maxProb) + "," + trueAA + "," + str(trueProb) + "," + ",".join(map(str, aaProbs)) + "\n"

    def getAAprob_allPos(self, outputFile):
	f = open(outputFile, "w")
	for i in self.posList:
		resultLine = self.getAAprob_onePos(str(i))
		f.write(resultLine)
	f.close()

if  __name__ =='__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    AApw = AApairwise(inputFile)
    AApw.getAAprob_allPos(outputFile)
