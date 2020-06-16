"""
Get a list of word leafs from CCGbank .auto files
"""
import re
import os
import PTB
from os.path import join as pjoin
class CCGBank:
    def __init__(self, rootDir):
        sections = os.listdir(rootDir)
        sections.sort()
        files = []
        for section in sections:
            path = pjoin(rootDir, section)
            fileNames = os.listdir(path)
            fileNames.sort()
            for fn in fileNames:
                if fn.endswith('.swp'): continue
                files.append(CCGBankFile(pjoin(path, fn)))
        self.files = files

    def __getitem__(self, index):
        return self.files[index]
                             

class CCGBankFile:
    def __init__(self, fileLoc):
        sentences = []
        for line in open(fileLoc):
            if line.startswith('ID'):
                continue
            sentences.append(Sentence(line.strip()))
        self.sentences = sentences
        self.name = fileLoc.split('/')[-1]

    def __getitem__(self, index):
        return self.sentences[index]
                             

class Sentence:
    ID = 0
    _textRE = re.compile(r'(?<=<L )[^>]+(?=>)')
    def __init__(self, text):
        leaves = Sentence._textRE.findall(text)
        tokens = []
        for leaf in leaves:
            form = leaf.split()[3]
            tokens.append(form)
        self.tokens = tokens

    def __getitem__(self, index):
        return self.tokens[index]

def alignSentence(ptbSent, ccgSent):
    ccgIdx = 0
    alignment = []
    for i, token in ptbSent.listWords():
        if isValidToken(token):
            if token.text != ccgSent[ccgIdx]:
                return False
            alignment.append( (i, ccgIdx) )
            ccgIdx += 1
        else:
            alignment.append( (i, -1) )
    return alignment

def isValidToken(token):
    if word.label == '-NONE-':
        return False
    elif word.text == '``' or word.text == '`' or word.label == "''":
        return False
    return True

def makeAlignmentMap(ptb, ccgBank):
    fullMap = {}
    for i, ccgFile in enumerate(ccgBank.files):
        ptbFile = ptb.child(i)
        if ptbFile.filename[:-4] != ccgFile.name[:-5]:
            print ptbFile.filename
            print ccgFile.name
            raise StandardError
        fileMap = {}
        i = 0
        for ptbSent in ptbFile.children():
            try:
                ccgSent = ccgFile[i]
            except IndexError:
                for idx in xrange(i, ptbFile.length()):
                    print "Skipping end sentence: %s, %d" % (ptbFile.filename, idx)
                continue
            # Get the alignment map for this sentence
            alignment = sentenceAlign(ptbSent, ccgSent, i)
            if alignment:
                # Update the fileMap with it
                fileMap.update(alignment)
                i += 1
            else:
                if len([c for c in ptbFile.children()]) == len(ccgFile.sentences):
                    print ' '.join(ptbLex(ptbSent))
                    print ' '.join(ccgSent.tokens)
                    raise StandardError, "Alignment failed! %s, %d" % (ptbFile.filename, i)
                else:
                    print "Skipping sentence: %s, %d" % (ptbFile.filename, i)


def rewritePropBank(propbankLoc, alignmentMap):
    newLines = []
    for line in open(propbankLoc):
        pieces = line.strip().split()
        path = pieces[0]
        sentIdx = pieces[1]
        relIdx = pieces[2]
        gold = pieces[3]
        frame = pieces[4]
        morph = pieces[5]
        pargs = pieces[6:]
        fileName = pieces[0].split('/')[-1][:-4]
        fileMap = alignmentMap[fileName]
        newSent, newRel = fileMap(sentIdx, relIdx)
        newPargs = []
        for parg in pargs:
            newPargs.append(translateParg(parg, sentIdx, fileMap))
        newPieces = [path, newSent, newRel, gold, frame, morph] + newPargs
        newLines.append(' '.join(newPieces))
    return newLines

def translateParg(parg, sentIdx, fileMap):
    
        

ccgBank = CCGBank('/home/mhonn/Data/CCGBank/AUTO')
os.environ['DATAPATH'] = '/home/mhonn/Data'
ptb = PTB.makeCorpus('/home/mhonn/Data/Treebank3_wsj/')
for i, ccgFile in enumerate(ccgBank.files):
    ptbFile = ptb.child(i)
    if ptbFile.filename[:-4] != ccgFile.name[:-5]:
        print ptbFile.filename
        print ccgFile.name
        raise StandardError
    i = 0
    for ptbSent in ptbFile.children():
        try:
            ccgSent = ccgFile[i]
        except IndexError:
            for idx in xrange(i, ptbFile.length()):
                print "Skipping end sentence: %s, %d" % (ptbFile.filename, idx)
            continue
        aligns = sentenceAlign(ptbSent, ccgSent)
        if aligns:
            i += 1
        else:
            if len([c for c in ptbFile.children()]) == len(ccgFile.sentences):
                print ' '.join(ptbLex(ptbSent))
                print ' '.join(ccgSent.tokens)
                raise StandardError, "Alignment failed! %s, %d" % (ptbFile.filename, i)
            else:
                print "Skipping sentence: %s, %d" % (ptbFile.filename, i)
                
