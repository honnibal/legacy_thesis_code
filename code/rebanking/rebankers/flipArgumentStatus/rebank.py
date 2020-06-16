from rebanking.rebankers import flipArgumentStatus
from rebanking.rebankers import mainWrapper
from pb import Propbank, Nombank
from _ArgumentToAdjunct import ArgumentToAdjunct
from _AdjunctToArgument import AdjunctToArgument
from _PhrasalVerb import PhrasalVerbChanger
from _Cleanup import FixNfPPToNPfPP, TrimUnary

def doSentence(sentence):
    """
    Do flipArgumentStatus
    """
    global argToAdj, adjToArg, particleToArg, cleanup
    propEntries = propbank.sentenceEntries(sentence)
    #nomEntries = nombank.sentenceEntries(sentence)
    # Do propbank
    particleToArg.rebank(propEntries)
    argToAdj.rebank(propEntries, 'propbank')
    adjToArg.rebank(propEntries, 'propbank')
    # Do nombank
    genitiveArguments.rebank(nomEntries)
    argToAdj.rebank(nomEntries, 'nombank')
    adjToArg.rebank(nomEntries, 'nombank')
    for rebanker in cleanup:
        rebanker.rebank(sentence)
   # for e in nomEntries:
   #     print e

main = mainWrapper(doSentence)
propbank = Propbank('/home/mhonn/code/repos/data/daniel_punct_np/propbank.txt')
argToAdj = ArgumentToAdjunct()
adjToArg = AdjunctToArgument()
particleToArg = PhrasalVerbChanger()

cleanup = [FixNfPPToNPfPP(), TrimUnary()]
if __name__ == '__main__':
    main()
