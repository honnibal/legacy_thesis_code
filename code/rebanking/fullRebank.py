import sys

import CCG
import rebankers
from rebankers import nAttach
from rebankers import flipArgumentStatus
from rebankers import normalisePunct
from rebankers import nodeMover
from rebankers import ensureNormalForm

try:
    import psyco
    psyco.full()
except:
    pass

def doSentence(sentence):
    #nodeMover.doSentence(sentence)
    nAttach.doSentence(sentence)
    flipArgumentStatus.doSentence(sentence)
    normalisePunct.doSentence(sentence)
    ensureNormalForm.doSentence(sentence)
    

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
