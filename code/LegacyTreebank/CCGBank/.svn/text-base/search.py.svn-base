#!/usr/bin/python2.4
from general.Singleton import singleton
from CCGConstructors import CCGBankNodeConstructor
from CCGNodes import CCGRoot
import Treebank
from Treebank.NodeVisitors import NodePrinter
import os, re

def doGrep(query, tbLoc):
    filePaths = Treebank.fileList(tbLoc)
   # query = re.compile(r'.+%s.+' % grepEscape(query))
   # print query.pattern
    for filePath in filePaths:
        print filePath
        text = open(filePath).read()
        if query in text:
            sentences = text.split('\n')
            for i, sentence in enumerate(sentences):
                print sentence
                if query in sentence:
                    print i
                    yield sentence
#        matches = query.findall(text)
#        for sentence in matches:
#            yield sentence
#    grepStr = r'grep %s %s' % (grepEscape(query), tbLoc)
#    print grepStr
#    for sentence in os.popen(grepStr):
#        yield sentence
    
def makeSentence(sentStr):
    global constructor
    return constructor.make(sentStr, CCGRoot)

def grepEscape(pattern):
    pattern = pattern.replace('\\', r'\\\\')
    pattern = pattern.replace('[', '\\[')
    pattern = pattern.replace(']', '\\]')
    pattern = pattern.replace('(', '\(')
    pattern = pattern.replace(')', '\)')
    pattern = pattern.replace('^', '\^')
    return pattern


constructor = singleton(CCGBankNodeConstructor)
printer = singleton(NodePrinter)
TB_LOC = '/home/mhonn/Data/CCGBank/Morph/v0.8/allchanged/data/AUTO'
counter = 0
count = False
for sentence in doGrep(r'N^NP^(S\S)', TB_LOC):
    if count:
        counter += 1
    else:
        sent = makeSentence(sentence)
        print printer.actOn(sent)
        raw_input("Enter to continue.")
if count:
    print counter


