import sys
from os.path import join as pjoin

from rebanking import rebankers
from Treebank.CCGbank import Writers
from Treebank import CCGbank
from _Preprocess import RemoveNB
from _Preprocess import FixNPtoAdverbAttach
from _Preprocess import FixPredeterminer
from _Preprocess import FixNominalNounAdjuncts
from _Preprocess import FixQuantifiedNP
from _Preprocess import FixConjConj
from _Preprocess import FixWhoseApposition
from _Preprocess import FixPunctHeads
from _PartitiveGenitive import PartitiveGenitive
from _PartitiveGenitive import UnaryPartitiveGenitive
from _NAttach import NAttach
from _NCoord import NCoord
from _NoisyTR import NoisyTR
from _Cleanup import PiedPiping
from _Cleanup import BinariseNonRestrictive
from _Cleanup import NAttachNP
from rebanking.rebankers import flipArgumentStatus
from rebanking.rebankers import normalisePunct
from rebanking.rebankers import ensureNormalForm
from general import log
_processes = [
    FixPunctHeads(),
    FixQuantifiedNP(),
    RemoveNB(),
    FixWhoseApposition(),
    FixConjConj(),
    FixNPtoAdverbAttach(),
    FixPredeterminer(),
    FixNominalNounAdjuncts(),
    NCoord(),
    NAttach(),
    NoisyTR(),
    PiedPiping(),
    BinariseNonRestrictive(),
    NAttachNP()
    ]
_applications = {}

def doSentence(sentence):
    flipArgumentStatus.doPropbank(sentence)
    doNAttach(sentence)
    #normalisePunct.doSentence(sentence)
    #ensureNormalForm.doSentence(sentence)

def main():
    inLoc, outLoc = sys.argv[1:]
    log.openLog('/tmp/invalid.log', 'invalid')
    corpus, autoWriter = setup(inLoc, outLoc)
    for i in xrange(0, corpus.length()):
        file_ = corpus.child(i)
        changed = []
        for sentence in file_.children():
            try:
                doSentence(sentence)
            except:
                print sentence.globalID
                raise
           # if not sentence.validate():
           #     print "Invalid: %s" % sentence.globalID
            changed.append(autoWriter.getSentenceStr(sentence))
       # if i == 10: break
        autoWriter.writeFile(file_.ID, changed)
    print 'Non-restrictive: %d' % NAttach.nonRestrictive
    print 'Non-restrictive relative: %d' % NAttach.nonRestrictiveRelative
    print 'Restrictive relative: %d' % NAttach.restrictiveRelative
    t = float(NAttach.restrictiveRelative + NAttach.nonRestrictiveRelative)
    print 'Restrictive relative p.c.: %.4f' % (NAttach.nonRestrictiveRelative/t)
    return main

def setup(inLoc, outLoc):
    outDir = pjoin(outLoc, 'data/AUTO')
    muLoc = pjoin(outLoc, 'markedup')
    autoWriter = Writers.AutoFileWriter(directory=outDir, markedup=muLoc)
    ccgbank = CCGbank.CCGbank(path=inLoc)
    return ccgbank, autoWriter


# Use closures to supply a persistent argument
doNAttach = rebankers.processWrapper(_processes, _applications)
debug = rebankers.debugWrapper(doSentence)
if __name__ == '__main__':
    if sys.argv[1] == '-d':
        debug(sys.argv[2], sys.argv[3])
    else:
        main()
