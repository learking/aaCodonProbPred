import sys
from aaProbSolver import *

#coef file and folders
firstOrderCoefFile = '/home/kuangyu/workspace/aaCodonProbPred/coefs/aa_sa_coef.txt'

#'L' is the reference codon
aaList = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

class AApairwise:
    def __init__(self, pwFile):
        #init solvers
        ## first order solver
        self.firstOrderSolver = aaProbSolver(firstOrderCoefFile)

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
            self.pairDict[currPair] = [firstSA, secondSA, invSD, invTD]

        self.posList = sorted(map(int, self.aaDict.keys()))

'''
    def getAAprob_onePos(self, pos):
        aaProbs = []
        for aa in aaList:
            #calculate prob for this aa
            #first order
            firstOrderProb = 0

            #simple check: first order probs should sum up to 1

            #second order

            #total prob
            
            ##add total prob to aaProbs
'''

if  __name__ =='__main__':
    inputFile = sys.argv[1]
    #outputFile = sys.argv[2]
    AApw = AApairwise(inputFile)
    AApw.getAAprob_onePos(1)
