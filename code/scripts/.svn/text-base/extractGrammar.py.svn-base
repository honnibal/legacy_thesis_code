#!/usr/bin/python
"""
Extract a grammar from CCGbank AUTO files
"""
import sys
import os.path
from os.path import join as pjoin
from general import log

import Treebank

def extractGrammars(corpusLoc, grammarsDir, ranges):
    for fRange, desc in ranges:
        grammarLoc = pjoin(grammarsDir, 'wsj%s.grammar' % desc)
        extractGrammar(corpusLoc, grammarLoc, fRange)

def extractGrammar(corpusLoc, outputLoc, fRange):
    grammar = {}
    filePaths = Treebank.fileList(corpusLoc)
    for i in fRange:
        if i >= len(filePaths):
            print i
        fLoc = filePaths[i]
        lines = open(fLoc).read().strip().split('\n')
        sentences = []
        ids = []
        while lines:
            ids.append(lines.pop(0).split()[0].replace('ID=', ''))
            sentences.append(lines.pop(0))
        for sentence, idLine in zip(sentences, ids):
            productions = getProductions(sentence)
            for production in productions:
                pStr = '%s --> %s %s' % (production)
                log.msg('%s\t%s' % (idLine, pStr))
                grammar.setdefault(production, 0)
                grammar[production] += 1
    output = open(outputLoc, 'w')
    sortable = [(f, k) for k, f in grammar.items()]
    sortable.sort()
    sortable.reverse()
    for freq, key in sortable:
        parent, left, right = key
        if right:
            children = left + ' ' + right
        else:
            children = left
        formatted = '%d # %s --> %s\n' % (freq, parent, children)
        output.write(formatted)
    output.close()


def getProductions(sentenceStr):
    depth = 0
    stack = []
    top = []
    stack.append(top)
    current = top
    cat = []
    insideCat = False
    for char in sentenceStr:
        if char == '<':
            insideCat = True
        elif char == '>':
            insideCat = False
            current.append(''.join(cat).split(' ')[1])
            cat = []
        elif char == '(' and not insideCat:
            depth += 1
            newCat = []
            current.append(newCat)
            current = newCat
            stack.append(current)
        elif char == ')' and not insideCat:
            depth -= 1
            stack.pop(-1)
            current = stack[-1]
        elif insideCat:
            cat.append(char)
    productions = _extractFromParsed(top, 'TOP', [])
    return productions

def _extractFromParsed(parsed, parent, productions):
    if len(parsed) == 1:
        child = parsed[0]
        label = child.pop(0)
        productions.append((parent, label, None))
        _extractFromParsed(child, label, productions)
    elif len(parsed) == 2:
        left = parsed[0]
        right = parsed[1]
        leftLabel = left.pop(0)
        rightLabel = right.pop(0)
        productions.append((parent, leftLabel, rightLabel))
        _extractFromParsed(left, leftLabel, productions)
        _extractFromParsed(right, rightLabel, productions)
    return productions
        

offcuts = range(100, 200) + range(2074, 2157) + range(2257, 2312)
fRanges = [(xrange(0, 100), '00'), (xrange(200, 2074), '02-21'), (xrange(0, 2312), 'full'), (xrange(2157, 2257), '23'), (offcuts, 'offcuts')]        
if __name__ == '__main__':
   # path = '/home/mhonn/Data/NPBank0.1/'
    if len(sys.argv) != 2:
        print "Usage: extractGrammar.py <corpus path>"
        sys.exit(1)
    corpusLoc = sys.argv[1]
    log.openLog('/tmp/productions.txt')
    autoPath = pjoin(corpusLoc, 'data', 'AUTO')
    grammarsDir = pjoin(corpusLoc, 'grammars')
    if not os.path.exists(grammarsDir):
        os.makedirs(grammarsDir) 
    extractGrammars(autoPath, grammarsDir, fRanges)
    log.close()


