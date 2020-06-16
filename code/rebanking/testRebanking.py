from rebankers import *
from pb import Propbank, Nombank
from Treebank import CCGbank
from Treebank.Nodes import PropbankPrinter
import nAttach
import data

printer = PropbankPrinter()
nombank = Nombank(data.nombankCCG)
propbank = Propbank(data.propbankCCG)
ccgbank = CCGbank.CCGbank(path=data.ccgbankNP)
argToAdj = ArgumentToAdjunct()
adjToArg = AdjunctToArgument()
for f in ccgbank.children():
    for sentence, entries in propbank.fileEntries(f):
        printer.setEntries(entries)
        print printer(sentence)
        argToAdj.rebank(entries)
        adjToArg.rebank(entries)
    for sentence, entries in nombank.fileEntries(f):
        if sentence.globalID != 'wsj_0003.17': continue
        nAttach.doSentence(sentence)
        argToAdj.rebank(entries)
        adjToArg.rebank(entries)
        print sentence
        raw_input("Any key to continue")
