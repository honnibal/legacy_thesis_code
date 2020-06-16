"""
Write a prop.txt file referring to CCG constituents instead of PTB constituents
"""
import Treebank, sys
import pb as Propbank
from Treebank import CCGbank, PTB
from os.path import join as pjoin

class CCGRefChain(Propbank.ReferenceChain):
    def __init__(self, ptbRefChain, ccgTokenMap):
        ccgWords = {}
        for nodeSet in ptbRefChain.contentNodes():
            for word in nodeSet.words():
                if isPunc(word):
                    continue
                ccgWord = ccgTokenMap[word]
                if ccgWord:
                    ccgWords[ccgWord] = ccgWord
        ccgNodes = self._reduce(ccgWords)
        self.append(CCGNodeSet(ccgNodes))    

    def _reduce(self, coveredWords):
        """
        Find the smallest set of constituents that cover all and only the word
        set, by moving up the tree
        """
        return coveredWords
        constituents = {}
        for constituent in coveredWords:
            while self._moveUpTree(constituent, coveredWords):
                constituent = constituent.parent()
            constituents[constituent] = constituent
        nodes = constituents.values()
        nodes.sort()
        return nodes

    def _moveUpTree(self, constituent, coveredWords):
        """
        Decide whether to move up to the constituent's parent,
        by a) checking whether we're at the root
        b) checking whether the parent includes words it shouldnt
        """
        # Return False if root, to break the loop
        if constituent.isRoot():
            return False
        for word in constituent.parent().listWords():
            if isPunc(word):
                continue
            if word not in coveredWords:
                return False
        return True

class CCGNodeSet(Propbank.NodeSet):
    def __init__(self, ccgNodes):
        self.extend(ccgNodes)
    


def alignFile(ccgFile, ptbFile):
    """
    Make an alignment map that takes a sentence ID and produces a dictionary
    mapping directly to the ccg token
    """
    fileMap = {}
    i = 0
    for ptbSent in ptbFile.children():
        try:
            ccgSent = ccgFile.child(i)
        except IndexError:
            print "Skipping at end of file"
            continue
        # Get the alignment map for this sentence
        alignment = alignSentence(ptbSent, ccgSent)
        if alignment:
            # Update the fileMap with it
            fileMap[ptbSent] = (alignment, i)
            i += 1
        else:
            print "Alignment failed"
    return fileMap

def alignSentence(ptbSent, ccgSent):
    alignment = {}
    i = 0
    ccgWords = [w for w in ccgSent.listWords() if not isPunc(w)]
    ptbWords = [w for w in ptbSent.listWords() if not isPunc(w)]
    if len(ccgWords) != len(ptbWords):
        print [(w.label, w.text) for w in ccgWords]
        print [(w.label, w.text) for w in ptbWords]
        
        return False
    alignment = {}
    for ptbWord, ccgWord in zip(ptbWords, ccgWords):
        if ptbWord.text != ccgWord.text:
            return False
        else:
            alignment[ptbWord] = ccgWord
    return alignment


def isPunc(word):
    q = ['RQU', 'LQU']
    return bool(not word.label[0].isalnum() or word.label in q)

def writeNewPropbank(outputLoc, ccgBank, ptb, propBank):
    outputFile = open(outputLoc, 'w')
    for i in xrange(0, ptb.length()):
        ccgFile = ccgBank.child(i)
        # Get ptb file
        section = ccgFile.ID[4:6]
        ptbFile = ptb.file(pjoin(PTB_PATH, section, ccgFile.ID[:-5] + '.mrg'))
        # Get propbank entries
        propEntries = propbank.fileEntries(ptbFile)
        convertedEntries = convertFile(ccgFile, ptbFile, propEntries)
        for entry in convertedEntries:
            outputFile.write(str(entry) + '\n')
    outputFile.close()
        
def convertFile(ccgFile, ptbFile, propEntries):
    # Make token map
    sentenceMap = alignFile(ccgFile, ptbFile)
    convertedEntries = []
    for sentence, entries in propEntries:
        tokenMap, i = sentenceMap.get(sentence, [None, 0])
        if tokenMap and entries:
            convertedEntries.extend(convertSentence(entries, tokenMap, i, ccgBank))
    return convertedEntries

def convertSentence(entries, tokenMap, sentIdx, ccgBank):
    convertedEntries = []
    for entry in entries:
        for parg in entry.pargs:
            parg.refChain = CCGRefChain(parg.refChain, tokenMap)
        entry.rel = tokenMap[entry.rel]
        entry.corpus = ccgBank
        entry.sentIdx = sentIdx
        convertedEntries.append(entry)
    return convertedEntries




if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    # Make propbank
   # propbank = Propbank.Propbank('/home/mhonn/Data/propbank_1/data/prop.txt')
    if 'nombank' in sys.argv[1]:
        propbank = Propbank.Nombank(sys.argv[1])
    else:
        propbank = Propbank.Propbank(sys.argv[1])
    # Make CCGBank
    ccgBank = CCGbank.CCGbank(path=sys.argv[2])
    PTB_PATH = sys.argv[3]
    ptb = PTB.PennTreebank(path=PTB_PATH)
    if 1:
        writeNewPropbank(sys.argv[4], ccgBank, ptb, propbank)
    else:
        ccgFile = ccgBank.file('/home/mhonn/Data/CCGBank/AUTO/22/wsj_2210.auto')
        ptbFile = ptb.file('/home/mhonn/Data/Treebank3_wsj/22/wsj_2210.mrg')
        propEntries = propbank.fileEntries(ptbFile)
        convertedEntries = convertFile(ccgFile, ptbFile, propEntries)
        for entry in convertedEntries:
            print str(entry)
            for parg in entry.pargs:
                print str(parg)
                for nodeSet in parg.refChain:
                    for node in nodeSet:
                        print node
