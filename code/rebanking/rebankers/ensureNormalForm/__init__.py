import sys

from rebanking import rebankers
from _EnsureNormalForm import EnsureNormalForm
from _EnsureHeadIndex import HeadCorrecter
_processes = [
    EnsureNormalForm(),
    HeadCorrecter()
    ]
_applications = {}

# Use closures to supply a persistent argument
doSentence = rebankers.processWrapper(_processes, _applications)
debug = rebankers.debugWrapper(doSentence)
reportApplications = rebankers.reportWrapper(_applications)
testMaker = rebankers.testMakerWrapper(doSentence)

if __name__ == '__main__':
    testMaker(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]) 
