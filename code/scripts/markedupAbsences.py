#!/usr/bin/python2.4
"""
Find a frequency sorted list of categories in a corpus absent
from a markedup file
"""
import Treebank, CCG
import re, sys
from os.path import join as pjoin
def getCatFreqs(corpusLoc, muLoc):
    muCats = getMUCats(muLoc)
    catFreqs = {}
    examples = {}
    for filePath in Treebank.fileList(corpusLoc):
        # Only want sections 2 to 21
        fileNum = int(filePath.split('_')[-1][:2])
        if 2 > fileNum or fileNum > 21:
            continue
        for i, sentence in enumerate(open(filePath)):
            sentence = getCats(sentence)
            for category, token  in sentence:
                category = category.replace(r'/.', '/').replace(r'\.', '\\')
                if category not in muCats:
                    catFreqs.setdefault(category, 0)
                    catFreqs[category] += 1
                    examples.setdefault(category, []).append((len(sentence), sentence))
        
    sortable = [[f, c, examples[c]] for c, f in catFreqs.items()]
    sortable.sort()
    sortable.reverse()
    catData = []
    for f, c, examples in sortable:
        examples.sort()
        catData.append((f, c, examples[:3]))
    return catData

tokenRE = re.compile(r'<L (\S+) \S+ \S+ (\S+) \S+>')
def getCats(ccgFile):
    return tokenRE.findall(ccgFile)


def getMUCats(muLoc):
    catRE = re.compile(r'(?<=\n)[^=\s#]+')
    cats = {}
    for cat in catRE.findall(open(muLoc).read()):
        cats[cat] = True
    return cats

def formatCat(cat):
    addHeadRE = re.compile(r'(?=[\)/\\])')
    headIndexed = addHeadRE.sub('{}', '(%s)' % cat)
    return '%s\n  n %s{_}\n  n\n' % (cat, headIndexed)
    
def formatExamples(examples):
    formatted = []
    for length, sentence in examples:
        tokens = []
        for stag, text in sentence:
            tokens.append('%s|%s' % (text, stag))
        formatted.append('# %s' % ' '.join(tokens))
    return '\n'.join(formatted)

try:
    import psyco
    psyco.full()
except:
    pass
corpusLoc = sys.argv[1]
muLoc = pjoin(corpusLoc, 'markedup')
catFreqs = getCatFreqs(corpusLoc, muLoc)
total = 0
overThresh = 0
missingCats = 0
output = open(pjoin(corpusLoc, 'missingCats.txt'), 'w')
for f, c, examples in catFreqs:
    total += f
    #if f < 10: continue
    output.write('# %d\n' % f)
    output.write(formatExamples(examples) + '\n')
    output.write(c + '\n')
    output.write('\n')
    overThresh += f
    missingCats += 1
output.close()
print total
print overThresh
print missingCats
