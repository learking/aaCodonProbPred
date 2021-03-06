import sys
from aaProbSolver import *
import re
import glob
import math

#'L' is the reference codon                                                                           
aaList = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

#coef file and folders                                                                                
#on desktop
#firstOrderCoefFile = '/home/kuangyu/workspace/aaCodonProbPred/coefs/aa_sa_coef.txt'
#on mac
firstOrderCoefFile = '/Users/kwang2/Documents/workspace/aaCodonProbPred/coefs/aa_sa_coef.txt'

fFirstOrder = open(firstOrderCoefFile, "r")
firstOrderCoefs = fFirstOrder.readlines()
fFirstOrder.close()
firstOrderSolver = aaProbSolver(firstOrderCoefs)

#sanac range:
#min: 0
#max: 172.4

#generate test data points between min and max
allPoints = range(1,172,2)

fOutput=open("/Users/kwang2/Documents/workspace/aaCodonProbPred/studyHydroResult/aaProb_sa_0_172.csv","w")
for x in allPoints:
    aaProbs = []
    for aa in aaList:
        tmpX = [1, x]
        tmpProb = firstOrderSolver.getCatProb(aa, tmpX)
        aaProbs.append(tmpProb)
    resultLine = ",".join(map(str,aaProbs)) + "\n"
    #print resultLine
    #print sum(aaProbs)
    fOutput.write(resultLine)
fOutput.close()
