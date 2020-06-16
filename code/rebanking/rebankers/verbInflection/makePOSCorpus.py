import sys

from rebanking import rebankers
from _VerbInflection import POSRelabeller

_processes = [
    POSRelabeller(),
    ]
_applications = {}

# Use closures to supply a persistent argument
doSentence = rebankers.processWrapper(_processes, _applications)
debug = rebankers.debugWrapper(doSentence)
reportApplications = rebankers.reportWrapper(_applications)
testMaker = rebankers.testMakerWrapper(doSentence)

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except:
        pass
    if '-d' in sys.argv:
        debug(sys.argv[2], sys.argv[3])
    else:
        main = rebankers.mainWrapper(doSentence)
        main()
