import numpy as np
import math

class aaProbSolver:
    'given file that contains coefficients, can calc prob for each category when input data X is known'
    __possibleAAs = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

    def __init__(self, coefDat):
        #open coefFile and read in coefs
        self.refCat = ""
        self.catCoef = {}
        self.__parseCoefs__(coefDat)

    def __parseCoefs__(self, coefDat):
        #store coefs for non-ref codon in a dictionary
        for line in coefDat:
            lineSplit = line.split()
            if len(lineSplit) > 0:
                currentCat = lineSplit[0]
                self.catCoef[currentCat] = []
                for i in range(1, len(lineSplit)):
                    self.catCoef[currentCat].append(float(lineSplit[i]))

        #print str(self.catCoef)
        #print str(sorted(self.catCoef.keys()))

        #find out reference codon
        self.refCat = list(set(CatProbSolver.__possibleCodons) - set(self.catCoef.keys()))[0]
        #print self.refCat

    def getCatProb(self, queryCat, X):
        catExp = {}
        expSum = 0
        for cat in self.catCoef.keys():
            tmpExp = math.exp(np.dot(self.catCoef[cat], X))
            catExp[cat] = tmpExp
            expSum += tmpExp
        #treat refCodon seperately
        catExp[self.refCat] = 1

        queryCatProb = catExp[queryCat] / (1 + expSum)
        return queryCatProb
