#!/usr/bin/env python
"""
Get a lexicon from a corpus
"""
import re, Treebank
import sys, os, CCG, re
def genWords(corpusLoc, fRange):
    filePaths = Treebank.fileList(corpusLoc)
    for i in fRange:
        filePath = filePaths[i]
        for cat, pos, word in getWords(open(filePath).read()):
            assert word
            assert pos
            assert cat
            yield (word, pos, cat)

# Super annoying AUTO file format for leaves (lexical entries):
# <L supertag ccgbank_pos ptb_pos word>
tokenRE = re.compile(r'<L (\S+) \S+ (\S+) (\S+) \S+>')
def getWords(ccgFile):
    return tokenRE.findall(ccgFile)

def makeLine(word, pos, freqs):
    """
    word pos stag=f
    """
    sortable = [(f, s) for s, f in freqs.items()]
    sortable.sort()
    sortable.reverse()
    writeable = '\t'.join(["%s=%d" % (s, f) for f, s in sortable])
    return '%s\t%s\t%s\n' % (word, pos, writeable)
    
def getFreqs(fRange, ccgBank):
    lexFreqs = {}
    for word, pos, cat in genWords(ccgBank, fRange):

        cat = re.sub(r':A[1-9]*', ':A', cat)
        cat = re.sub(r':AM-[A-Z]*', ':AM', cat)
        key = (word, pos)
        key2 = cat
        lexFreqs.setdefault(key, {}).setdefault(key2, 0)
        lexFreqs[key][key2] += 1
    return lexFreqs

def writeLex(lexiconDir, lexFreqs, desc):
    outputLoc = os.path.join(lexiconDir, '%s.lex' % desc)
    output = open(outputLoc, 'w')
    keys = lexFreqs.keys()
    keys.sort()
    for word, pos in keys:
        freqs = lexFreqs[(word, pos)]
        line = makeLine(word, pos, freqs)
        output.write(line)
    output.close()        

def main():
    corpusPath = sys.argv[1]
    lexiconDir = os.path.join(corpusPath, 'lexicons')
    if not os.path.isdir(lexiconDir):
        os.mkdir(lexiconDir)
    offcuts = range(100, 200) + range(2074, 2157) + range(2257, 2312)
    fRanges = [
        (xrange(0, 100), '00'),
        (xrange(200, 2074), '02-21'),
        (xrange(0, 2312), 'full'),
        (xrange(2157, 2257), '23'),
        (offcuts, 'offcuts')
        ]
    for fRange, desc in fRanges:
        print desc
        lexFreqs = getFreqs(fRange, corpusPath)
        writeLex(lexiconDir, lexFreqs, desc)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "USAGE: getLexicon.py <corpus path>"
        sys.exit(0)
    try:
        import psyco
        psyco.full()
    except:
        pass
    main()
    
        

