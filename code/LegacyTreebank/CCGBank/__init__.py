from CCGConstructors import *
from CCGNodes import *
from Treebank import TreeConstructors, Nodes
   
    
def makeCCGBank(location):
    sentenceConstructor = CCGBankNodeConstructor()
    fileConstructor = AutoFileConstructor()
    fileConstructor.addChildConstructors({'ccg': sentenceConstructor})
    corpusConstructor = CCGConstructors.CCGCorpusConstructor()
    corpusConstructor.addChildConstructors({'ccg': fileConstructor})
    return corpusConstructor.make('ccg', location, CCGCorpus) 

def makeCorpus(location):
    return makeCCGBank(location)


def ccgBankFromFlat(location):
    sentenceConstructor = CCGFlatSentenceConstructor()
    fileConstructor = CCGFlatFileConstructor()
    fileConstructor.addChildConstructors({'ccg': sentenceConstructor})
    corpusConstructor = CCGConstructors.CCGCorpusConstructor()
    corpusConstructor.addChildConstructors({'ccg': fileConstructor})
    return corpusConstructor.make('ccg', location, CCGCorpus)
