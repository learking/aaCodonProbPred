import sys
import math

class AllPW:
    def __init__(self, inputCodon, inputAA, inputSA):
        self.aa_SD_dict = self.__initAAdict()
        self.aa_TD_dict = self.__initAAdict()

        self.codon_SD_dict = self.__initCodonDict()
        self.codon_TD_dict = self.__initCodonDict()

        self.codon = inputCodon
        self.AA = inputAA
        self.sa = inputSA

    def __initAAdict(self):
        aaDict = {'A': [],'C': [],'D': [],'E': [],'F': [],'G': [],'I': [],'H': [],'K': [],'L': [],'M': [],'N': [],'P': [],'Q': [],'R': [],'S': [],'T': [],'V': [],'W': [],'Y': []}
        return aaDict

    def __initCodonDict(self):
        codonDict = {
              'TTT': [], 'TCT': [], 'TAT': [], 'TGT': [],
              'TTC': [], 'TCC': [], 'TAC': [], 'TGC': [],
              'TTA': [], 'TCA': [], 
              'TTG': [], 'TCG': [], 'TGG': [],
              'CTT': [], 'CCT': [], 'CAT': [], 'CGT': [],
              'CTC': [], 'CCC': [], 'CAC': [], 'CGC': [],
              'CTA': [], 'CCA': [], 'CAA': [], 'CGA': [],
              'CTG': [], 'CCG': [], 'CAG': [], 'CGG': [],
              'ATT': [], 'ACT': [], 'AAT': [], 'AGT': [],
              'ATC': [], 'ACC': [], 'AAC': [], 'AGC': [],
              'ATA': [], 'ACA': [], 'AAA': [], 'AGA': [],
              'ATG': [], 'ACG': [], 'AAG': [], 'AGG': [],
              'GTT': [], 'GCT': [], 'GAT': [], 'GGT': [],
              'GTC': [], 'GCC': [], 'GAC': [], 'GGC': [],
              'GTA': [], 'GCA': [], 'GAA': [], 'GGA': [],
              'GTG': [], 'GCG': [], 'GAG': [], 'GGG': []
        }
        return codonDict

    def addSDTD(self, inputCodon, inputAA, inputSD, inputTD):

        self.codon_SD_dict[inputCodon].append(float(inputSD))
        self.codon_TD_dict[inputCodon].append(float(inputTD)) 

        self.aa_SD_dict[inputAA].append(float(inputSD))
        self.aa_TD_dict[inputAA].append(float(inputTD))

    def aa_TD2str(self):
        aaList = ['A','C','D','E','F','G','I','H','K','L','M','N','P','Q','R','S','T','V','W','Y']
        TDlist = []
        for aa in aaList:
            
            #TDlist.append()

    def sumList_invsq(self, inputList):
        sumValue = 0
        for val in inputList:
            sumValue += math.pow(1.0/val, 2)
        return sumValue

def getSumInput(inputFile, outFile):
    posDict = {}

    # read all lines of input file
    fInput = open(inputFile, "r")
    allLines = fInput.readlines()
    fInput.close()

    #go through one pass and get all positions, add AllPW to posDict and get their SA first
    for line in allLines:
        tmpLine = line.split()

        firstPos = tmpLine[6]
        firstCodon = tmpLine[1]
        firstAA = tmpLine[4]
        firstSA = tmpLine[9]

        secondPos = tmpLine[7]
        secondCodon = tmpLine[2]
        secondAA = tmpLine[5]
        secondSA = tmpLine[13]

        SD = str(int(secondPos) - int(firstPos))
        TD = tmpLine[3]

        if firstPos not in posDict.keys():
            posDict[firstPos] = AllPW(firstCodon, firstAA, firstSA)
            #add this interaction to posDict
            posDict[firstPos].addSDTD(secondCodon, secondAA, SD, TD)
        else:
            #add this interaction to posDict
            posDict[firstPos].addSDTD(secondCodon, secondAA, SD, TD)

        if secondPos not in posDict.keys():
            posDict[secondPos] = AllPW(secondCodon, secondAA, secondSA)
            #add this interaction to posDict
            posDict[secondPos].addSDTD(firstCodon, firstAA, SD, TD)            
        else:
            #add this interaction to posDict
            posDict[secondPos].addSDTD(firstCodon, firstAA, SD, TD)

    #simple check
    #print str(max(map(int, posDict.keys())))

    # for each pos in posDict.keys() produce output in the following format:
    # codon AA sa 20 summaried values for either TD (rightnow) or SD
    posIntList = sorted(map(int, posDict.keys()))
    for currPos in posIntList:
        currResult = posDict[str(currPos)].aa_TD2str()
        print currResult

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outFile = sys.argv[2]
    getSumInput(inputFile, outFile)
