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
from _Preprocess import FixVPVPfPP
from _PartitiveGenitive import PartitiveGenitive
from _PartitiveGenitive import UnaryPartitiveGenitive
from _NAttach import NAttach
from _NCoord import NCoord
from _NoisyTR import NoisyTR
from _Cleanup import PiedPiping
from _Cleanup import BinariseNonRestrictive
from _Cleanup import NAttachNP
from rebanking import rebankers

_processes = [
    FixPunctHeads(),
    FixVPVPfPP(),
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

# Use closures to supply a persistent argument
doSentence = rebankers.processWrapper(_processes, _applications)
debug = rebankers.debugWrapper(doSentence)
reportApplications = rebankers.reportWrapper(_applications)
testMaker = rebankers.testMakerWrapper(doSentence)
if __name__ == '__main__':
    main = rebankers.mainWrapper(doSentence)
    main()
    print NAttach.applied
    #testMaker(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]) 
