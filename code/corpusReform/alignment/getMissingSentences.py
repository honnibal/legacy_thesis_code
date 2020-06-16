"""
Get the location of sentences missing from CCGBank and store them in a pickle,
so that other processes can easily skip sentences from the PTB
"""
import pickles
import Treebank
from Treebank import CCGBank
from ccgPropBank import alignFile
import psyco
psyco.full()
ptb = Treebank.makeCorpus('/home/mhonn/Data/Treebank3_wsj/')
ccg = CCGBank.ccgBankFromFlat('/home/mhonn/Data/CCGBank/Flat/')
missing = {}
for i in xrange(ptb.length()):
    ptbFile = ptb.child(i)
    ccgFile = ccg.child(i)
    alignment = alignFile(ccgFile, ptbFile)
    for sentence in ptbFile.children():
        if sentence not in alignment:
            missing[(ptbFile.ID, sentence.globalID)] = True
pickles.store(missing, 'ccgbankMissing')
        
