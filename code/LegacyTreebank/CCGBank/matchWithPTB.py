import Treebank
import Treebank.CCGBank
import Treebank.NodeVisitors
import pickles

def align(ptbSent, ccgSent, alignment):
    ptbNodes = {}
    for node in ccgSent.depthList():
        if node.isLeaf():
            continue
        firstWord = None
        i = 0
        nodeLen = len([w for w in node.listWords()])
        while firstWord == None:
            word = node.getWord(i)
            
            if not isSpeech(word) and word.sentIdx in alignment:
                firstWord = alignment[word.sentIdx]
            i += 1
            if i == nodeLen - 1:
                break
        if firstWord == None:
            print "skipping on first"
            print node
            continue
        i = nodeLen - 1
        lastWord = None
        while lastWord == None:
            word = node.getWord(i)
            if not isSpeech(word) and word.sentIdx in alignment:
                lastWord = alignment[word.sentIdx]
            i -= 1
            if i == 0:
                break
        if lastWord == None:
            print "skipping on last"
            print node
            continue
        ptbNodes[(firstWord, lastWord)] = node
    nodeMap = {}
    keys = ptbNodes.keys()
    keys.sort()
    for k in keys:
        print k
    print len(ptbNodes)
    for word in ptbSent.listWords():
        if word.label == '-NONE-' or isSpeech(word):
            continue
        ccgIdx = alignment[word.sentIdx]
        ccgWord = ccgSent.getWord(ccgIdx)
        print "%s %s" % (word, ccgWord)
    for ccgNode in ccgSent.depthList():
        firstWord = ccgNode.getWord(0).sentIdx
        lastWord = ccgNode.getWord(-1).sentIdx
        ptbNode = ptbNodes.get((firstWord, lastWord), None)
        if not ptbNode:
            print (firstWord, lastWord)
            print ccgNode
            raise StandardError
        nodeMap[ccgNode] = ptbNode
    return nodeMap

def isSpeech(word):
    if word.label in ["``", "''"] and word.text in ["`", "'", "''", "``"]:
        return True
    else:
        return False
        

        
        
        
    

ptb = Treebank.makeCorpus('/home/mhonn/Data/Treebank3_wsj/')
ccg = Treebank.CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/AUTO/')
printer = Treebank.NodeVisitors.NodePrinter()
alignmentMaps = pickles.load('trainAlignments')
ptbF = ptb.child(199)
ccgF = ccg.child(199)
partAlign = alignmentMaps[0]
for i, ptbSent in enumerate(ptbF.children()):
    sentAlign, ccgSentIdx = partAlign[i]
    if not sentAlign:
        print "Misaligned sentence at %d" % i
        continue
    ccgSent = ccgF.child(ccgSentIdx)
   # print printer.actOn(ptbSent)
   # print printer.actOn(ccgSent)
    nodeAlign = align(ptbSent, ccgSent, sentAlign)
    break
