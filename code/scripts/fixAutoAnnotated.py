"""
Correct the annotated categories in AUTO files a CCGbank, using the
pred-arg annotated categories in the default CCGbank, and converted versions
from a markedup file. Note that the conversion from the markedup file is lossy,
because the markedup file does not include a distinction between bounded and
unbounded dependencies. However, we do not evaluate on those labels.
"""
import sys
import re
import os
from os.path import join as pjoin

import CCG
from CCG import Markedup
import Treebank
import data

def files(loc):
    for f in Treebank.fileList(loc):
        yield f

lexRE = re.compile(r'<L [^ >]+ [^ >]+ [^ >]+ [^ >]+ [^ >]+(?=>)')
def doFile(inLoc, outLoc, dict1, dict2):
    auto = open(inLoc).read()
    mapping = {}
    for lexString in lexRE.findall(auto):
        start, bare, pos1, pos2, text, annot = lexString.split(' ')
        bare = lexString.split(' ')[1]
        if bare in dict1:
            newAnnot = dict1[bare]
        elif bare in dict2:
            newAnnot = dict2[bare]
        else:
            cat = CCG.Category(bare)
            newAnnot = cat.fullPrint()
        newLex = ' '.join((start, bare, pos1, pos2, text, newAnnot))
        mapping[lexString] = newLex
    for oldLex, newLex in mapping.items():
        if oldLex != newLex:
            auto = auto.replace(oldLex, newLex)
            print '%s --> %s' % (oldLex, newLex)
    open(outLoc, 'w').write(auto)

def main(corpusLoc, outLoc, muLoc, muFirst):
    entries, null = Markedup.getEntries(muLoc)
    markedup = {}
    for cat in entries:
        markedup[cat.cat] = cat.toJulia()
    if muFirst:
        dict1 = markedup
        dict2 = CCG.catDict
    else:
        dict1 = markedup
        dict2 = CCG.catDict
    for path in files(corpusLoc):
        outPath = path.replace(corpusLoc, outLoc)
        outDir, outFile = outPath.rsplit('/', 1)
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        doFile(path, outPath, dict1, dict2)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print "USAGE: fixAutoAnnotated.py <corpus> <out dir> <markedup> <muFirst?>"
        sys.exit(1)
    inPath = data.getLoc(sys.argv[1])
    outPath = data.getLoc(sys.argv[2])
    muLoc = data.getLoc(sys.argv[3])
    muFirst = bool(sys.argv[4] == 'true')
    main(inPath, outPath, muLoc, muFirst)
    
    
