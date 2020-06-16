import sys

import rebankers
from rebankers import nAttach
from rebankers import flipArgumentStatus
from rebankers import normalisePunct
from rebankers import ensureNormalForm
from rebanking.rebankers import verbInflection

try:
    import psyco
    psyco.full()
except:
    pass

def doSentence(sentence):
    nAttach.doSentence(sentence)
    flipArgumentStatus.doSentence(sentence)
    normalisePunct.doSentence(sentence)
    ensureNormalForm.doSentence(sentence)
    verbInflection.doSentence(sentence)
    
debug = rebankers.debugWrapper(doSentence)
testMaker = rebankers.testMakerWrapper(doSentence)


if __name__ == '__main__':
    if sys.argv[1] == '-d':
        debug(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == '-t':
        # start, stop, inLoc, testLoc
        testMaker(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5])
    else:
        main = rebankers.mainWrapper(doSentence)
        main()
