"""
Find sentences with a particular word|stag sequence
"""
import re
import doctest
import sys

import Treebank
from Treebank.CCGbank import CCGSentence

def genSentences(corpusLoc):
    filePaths = Treebank.fileList(corpusLoc)
    for filePath in filePaths:
        lines = open(filePath).read().strip().split('\n')
        while lines:
            idLine = lines.pop(0)
            sentence = lines.pop(0)
            yield sentence, idLine

# Super annoying AUTO file format for leaves (lexical entries):
# <L supertag ccgbank_pos ptb_pos word>
tokenRE = re.compile(r'<L (\S+) \S+ (\S+) (\S+) \S+>')
def getStags(sentence):
    tokens = ['|'.join(reversed(token)) for token in tokenRE.findall(sentence)]
    return ' '.join(tokens)


def makeQuery(stags):
    """
    Format the stags into a regular expression, to allow optional POS
    tags and words
    """
    tokens = []
    for token in stags.split():
        regex = []
        for field in token.split('|'):
            if field == '*':
                value = r'[^|\s]+'
            else:
                value = re.escape(field)
            regex.append(value)
        tokens.append(r'\|'.join(regex))
    return ' '.join(tokens) + r'(?=\s)'

def parseArgs():
    return sys.argv[1:]

def main():
    stagStr, corpusLoc = parseArgs()
    query = re.compile(makeQuery(stagStr))
    print query.pattern
    for autoSent, idLine in genSentences(corpusLoc):
        stagSent = getStags(autoSent)
        if query.search(stagSent):
            print idLine
            sentence = CCGSentence(string=autoSent, localID=-1, globalID=-1)
#            print autoSent
            print sentence
#            print >> sys.stderr, idLine
#            print >> sys.stderr, stagSent
            
        

def testQuery():
    r"""
    >>> query = makeQuery(r'all|*|NP of|*|(NP\NP)/NP')
    >>> print query
    all\|[^|\s]+\|NP of\|[^|\s]+\|\(NP\\NP\)\/NP
    >>> re.match(query, r'all|DT|NP of|IN|(NP\NP)/NP us|PRP|NP').group()
    'all|DT|NP of|IN|(NP\\NP)/NP'
    >>> query = makeQuery('all|IN|NP of|*|(NP\NP)/NP')
    >>> print query
    all\|IN\|NP of\|[^|\s]+\|\(NP\\NP\)\/NP
    >>> print re.match(query, r'all|DT|NP of|IN|(NP\NP)/NP us|PRP|NP')
    None
    >>> re.match(query, r'all|IN|NP of|IN|(NP\NP)/NP us|PRP|NP').group()
    'all|IN|NP of|IN|(NP\\NP)/NP'
    """
    pass
    
    
if __name__ == '__main__':
#doctest.testmod()
    main()
