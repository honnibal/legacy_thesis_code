import sys
from os.path import join as pjoin

import data
import CCG
from Treebank import CCGbank
from pb import ccgPB
from general import log
from rebanking import rebankers
from _ArgumentToAdjunct import ArgumentToAdjunct
from _AdjunctToArgument import AdjunctToArgument
from _GenitiveArguments import GenitiveArguments
from _PhrasalVerb import PhrasalVerbChanger
from _RoleLabeller import PPLabeller
from _Cleanup import FixNfPPToNPfPP, TrimUnary

def getEntries(file_):
    global propbank, nombank
    fromProp = propbank.fileEntries(file_)
    fromNom = nombank.fileEntries(file_)
    bySentence = {}
    for (sentence, propEntries), (null, nomEntries) in zip(fromProp, fromNom):
        bySentence[sentence] = (propEntries, nomEntries)
    return bySentence

def doSentence(sentence):
    """
    Do flipArgumentStatus
    """
    global argToAdj, adjToArg, particleToArg, cleanup
    propEntries = propbank.sentenceEntries(sentence)
    nomEntries = nombank.sentenceEntries(sentence)
    particleToArg.rebank(propEntries)
    argToAdj.rebank(propEntries, 'propbank')
    adjToArg.rebank(propEntries, 'propbank')
    # Do nombank
    genitiveArguments.rebank(nomEntries)
    argToAdj.rebank(nomEntries, 'nombank')
    adjToArg.rebank(nomEntries, 'nombank')
    ppLabeller.rebank(sentence)
    #roleLabeller.rebank(propEntries, 'propbank')
    #roleLabeller.rebank(nomEntries, 'nombank')
    for rebanker in cleanup:
        rebanker.rebank(sentence)
   # for e in nomEntries:
   #     print e

def doPropbank(sentence, doParticle=True):
    global argToAdj, adjToArg, particleToArg, cleanup
    propEntries = propbank.sentenceEntries(sentence)
    nomEntries = nombank.sentenceEntries(sentence)
    # Do propbank
    if doParticle:
        particleToArg.rebank(propEntries)
    argToAdj.rebank(propEntries, 'propbank')
    adjToArg.rebank(propEntries, 'propbank')

##def deprdebug(inLoc, key):
##    log.openLog('/dev/null', 'invalid')
##    ccgbank = CCGbank.CCGbank(path=inLoc)
##    fileKey = pjoin(inLoc, 'data', 'AUTO', key[4:6], key.replace('.', '.auto~'))
##    fileID, sentID = fileKey.split('~')
##    file_ = ccgbank.file(fileID)
##    s = file_.sentence(key)
##    print s
##    print s.validate()
##    entriesBySentence = getEntries(file_)
##    propEntries, nomEntries = entriesBySentence[s]
##    nAttach.doSentence(s)
##    doSentence(s, propEntries)
##    doSentence(s, nomEntries)
##    print s
##    print s.validate()

# Initialise stuff
_entries = {}
_applications = {}
nombank = ccgPB.Nombank('/home/matt/code/repos/data/np_punct/nombank')
propbank = ccgPB.Propbank('/home/matt/code/repos/data/np_punct/propbank')
#propbank = Propbank(data.propbankHatCCG)
#nombank = Propbank(data.nombankCCGNP)
#propbank = Propbank(data.propbankCCGNP)
argToAdj = ArgumentToAdjunct()
adjToArg = AdjunctToArgument()
particleToArg = PhrasalVerbChanger()
genitiveArguments = GenitiveArguments()
ppLabeller = PPLabeller()
cleanup = [FixNfPPToNPfPP(), TrimUnary()]
debug = rebankers.debugWrapper(doSentence)
reportApplications = rebankers.reportWrapper(_applications)
testMaker = rebankers.testMakerWrapper(doSentence)

if __name__ == '__main__':
   debug(sys.argv[2], sys.argv[3])
