"""
Print a treebank with propbank annotation
"""
import sys
import pb
import Treebank
from Treebank import CCGbank
import data
from Treebank.Nodes import PropbankPrinter

def getLoc(loc):
    if loc.startswith('data.'):
        return eval(loc)
    else:
        return loc

if len(sys.argv) != 4:
    print "USAGE: <ptb|ccgbank> <corpus loc> <propbank>"
    sys.exit(1)
else:
    corpusType = sys.argv[1]
    corpusLoc = getLoc(sys.argv[2])
    pbLoc = getLoc(sys.argv[3])
    if corpusType == 'ptb':
        corpus = Treebank.makeCorpus(corpusLoc)
    elif corpusType == 'ccgbank':
        corpus = CCGbank.CCGbank(path=corpusLoc)
pb = pb.Propbank(pbLoc)
printer = PropbankPrinter()
for f in corpus.children():
    for s, entries in pb.fileEntries(f):
#        for entry in entries:
#            print entry
	printer.setEntries(entries)
	print printer(s)
