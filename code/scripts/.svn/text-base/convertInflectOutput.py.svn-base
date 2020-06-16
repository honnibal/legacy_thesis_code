"""
Convert the dependencies from an inflectional morphology parser so that it can be evaluated against
ordinary CCGbank. This means removing dependencies involving the morphological tokens, removing the tokens
themselves, and updating the verb's category.
"""
import sys
import re

import CCG
import CCG.Markedup


class Document(object):
    def __init__(self, text):
        sentences = []
        sentences = re.split(r'\n(?=\n)', text.strip())
        self.header = sentences.pop(0)
        
        assert self.header.startswith('#')
        self.sentences = [Sentence(s.strip()) for s in sentences]

class Sentence(object):
    def __init__(self, data):
        if not data.strip():
            self.deps = []
            self.tokens = []
        else:
            deps = data.split('\n')
            stags = deps.pop(-1).split()
            stags.pop(0)
            self.tokens = [Token(i, *t.split('|')) for i, t in enumerate(stags)]
            self.deps = [Dependency(self.tokens, *dep.split()) for dep in deps]

    def __str__(self):
        if not self.tokens:
            return ''
        deps = '\n'.join([str(dep) for dep in self.deps])
        tokens = ' '.join([str(token) for token in self.tokens])
        if deps:
            return '%s\n<c> %s' % (deps, tokens)
        else:
            return '<c> %s' % (tokens)

    def convert(self, rawSent, markedup):
        self.fixTokens(rawSent)
        self.fixDeps(markedup)

    def fixTokens(self, forms):
        tokenMap = {}
        for token in self.tokens:
            if token.isInflect:
                lastToken.fixStag(token.stag)
            lastToken = token
        self.tokens = [t for t in self.tokens if not t.isInflect]
        for i, (token, form) in enumerate(zip(self.tokens, forms)):
            token.form = form
            token.idx = i

    def fixDeps(self, markedup):
        byAgents = set()
        for dep in self.deps:
            # Fix passives
            if CCG.isIdentical(dep.head.stag.innerResult(), 'S[pss]'):
                
                if dep.arg.form == 'by' and dep.arg.stag == 'PP/NP':
                    dep.head, dep.arg = dep.arg, dep.head
                    dep.argNum = 2
                    dep.head.stag = CCG.Category(r'((S\NP)\(S\NP))/NP')
                    byAgents.add(dep.head)
                if dep.argNum > 2:
                    dep.argNum -= 1
        for dep in self.deps:
            if dep.head in byAgents and dep.argNum == 1:
                dep.argNum = 3
            dep.updateCat(markedup)
        self.deps = [dep for dep in self.deps if not dep.head.isInflect]
        
        

class Token(object):
    def __init__(self, idx, form, pos, stag, *args):
        self.idx = idx
        self.form = form
        self.pos = pos
        self.stag = CCG.Category(stag)
        self.isInflect = self.pos.startswith('VI')

    def __str__(self):
        return '%s|%s|%s' % (self.form, self.pos, self.stag)

    def fixStag(self, inflectCat):
        cats = CCG.combine(self.stag, inflectCat)
        if cats:
            self.stag = cats.keys()[0]
        if inflectCat == CCG.Category(r'(((S[pss]\NP)/PP)\((S[b]\NP)/NP)'):
            self.stag = self.stag.result
        

class Dependency(object):
    def __init__(self, tokens, head, muCat, argNum, arg, ruleID, *args):
        headForm, headIdx = head.split('_')
        argForm, argIdx = arg.split('_')
        headIdx = int(headIdx)-1
        argIdx = int(argIdx)-1
        self.cat = muCat
        self.argNum = int(argNum)
        self.head = tokens[headIdx]
        self.arg = tokens[argIdx]
        self.ruleID = ruleID
        self.extra = args
        assert self.head.form == headForm
        assert self.arg.form == argForm

    def __str__(self):
        fields = (self.head.form, self.head.idx+1, self.cat, self.argNum, self.arg.form, self.arg.idx+1, self.ruleID)
        template = '%s_%d %s %d %s_%d %s'
        return template % fields

    def updateCat(self, markedup):
        if self.cat != 'conj':
            self.cat = markedup.get(self.head.stag, self.cat)

    
def deprremoveInflections(sentence, forms, markedup):
    sentence.tokens = [t for t in sentence.tokens if not t.pos.startswith('VI')]
    fixedDeps = []
    for dep in sentence.deps:
        head = dep.head
        arg = dep.arg
        if head.pos.startswith('VI'):
            cats = CCG.combine(arg.stag, head.stag)
            if not cats:
                cat = arg.stag
            else:
                cat = cats.keys()[0]
            arg.stag = cat
        assert not arg.pos.startswith('VI')
    sentence.deps = [d for d in sentence.deps
                     if d.head in sentence.tokens and d.arg in sentence.tokens]
    for i, (token, form) in enumerate(zip(sentence.tokens, forms)):
        token.form = form
        token.idx = i
    byAgents = set()
    for dep in sentence.deps:
        # Fix passives
        if CCG.isIdentical(dep.head.stag.innerResult(), 'S[pss]'):
            if dep.arg.form == 'by' and dep.arg.stag == 'PP':
                byAgents.add(dep.arg)
                dep.head, dep.arg = dep.arg, dep.head
                dep.argNum = 2
                dep.arg.stag = CCG.Category(r'((S\NP)\(S\NP))/NP')
            if dep.argNum > 2:
                dep.argNum -= 1
        if dep.cat != 'conj':
            dep.cat = markedup.get(dep.head.stag, dep.cat)
    for dep in sentence.deps:
        if dep.head in byAgents:
            assert dep.argNum == 1
            dep.argNum = 3
        
            
        

    
def readRaw(rawLoc):
    header, data = open(rawLoc).read().strip().split('\n\n')
    sentences = [s.split() for s in data.split('\n')]
    return sentences


def main():
    validateArgs()
    doc = Document(open(sys.argv[1]).read())
    rawSents = readRaw(sys.argv[2])
    cats, markedup = CCG.Markedup.getEntries(sys.argv[3])
    assert len(rawSents) == len(doc.sentences)
    print doc.header
    print '# Converted with convertInflectOutput.py'
    print
    #doc.sentences = [doc.sentences[20]]
    #rawSents = [rawSents[20]]
    for sentence, rawSent in zip(doc.sentences, rawSents):
        sentence.convert(rawSent, markedup)
        #removeInflections(sentence, rawSent, markedup)
        sentStr = str(sentence)
        print sentStr
        if sentStr:
            print

def validateArgs():
    if len(sys.argv) != 4:
        print "Usage: convertInflectOutput.py <test> <raw> <markedup>"
        sys.exit(1)

if __name__ == '__main__':
    main()
