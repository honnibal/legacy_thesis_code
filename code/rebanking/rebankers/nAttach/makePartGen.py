import sys

from rebanking import rebankers

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
    PartitiveGenitive(),
    UnaryPartitiveGenitive(),
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
    normalisePunct.doSentence(sentence)
    ensureNormalForm.doSentence(sentence)

# Use closures to supply a persistent argument
doNAttach = rebankers.processWrapper(_processes, _applications)
debug = rebankers.debugWrapper(doSentence)
if __name__ == '__main__':
    if sys.argv[1] == '-d':
        debug(sys.argv[2], sys.argv[3])
    else:
        main = rebankers.mainWrapper(doSentence)
        main()
