from rebanking.rebankers import flipArgumentStatus
from rebanking.rebankers import mainWrapper, debugWrapper
from pb import Propbank, Nombank
from _ArgumentToAdjunct import ArgumentToAdjunct
from _AdjunctToArgument import AdjunctToArgument
from _PhrasalVerb import PhrasalVerbChanger
from _Cleanup import FixNfPPToNPfPP, TrimUnary

from rebanking.rebankers import normalisePunct
from rebanking.rebankers import ensureNormalForm

import sys

def doSentence(sentence):
    """
    Do flipArgumentStatus
    """
    global argToAdj, adjToArg, particleToArg, cleanup
    propEntries = propbank.sentenceEntries(sentence)
    argToAdj.rebank(propEntries, 'propbank')
    adjToArg.rebank(propEntries, 'propbank')
    for rebanker in cleanup:
        rebanker.rebank(sentence)
    normalisePunct.doSentence(sentence)
    ensureNormalForm.doSentence(sentence)


propbank = Propbank('/home/mhonn/code/repos/data/daniel_punct_np/propbank.txt')
argToAdj = ArgumentToAdjunct()
adjToArg = AdjunctToArgument()

cleanup = [FixNfPPToNPfPP(), TrimUnary()]

debug = debugWrapper(doSentence)
if __name__ == '__main__':
    if sys.argv[1] == '-d':
        debug(sys.argv[2], sys.argv[3])
    else:
        main = mainWrapper(doSentence)
        main()
