from Treebank import CCGbank
from Treebank.CCGbank import CCGSentence
import re, CCG
def makeTree(manualDef):
    """
    Decorate the manual definition with CCGbank style annotation,
    so that we can use the CCGbank constructor

    (<S[dcl]\NP> becomes (<T S[dcl]\NP 0 0>
    """
    # Use a regex to add dummy head idx for leaves
    manualDef = re.sub('(?<!\d)>', ' 0>', manualDef)
    manualDef = manualDef.replace('<', '<T ').replace('>', ' 0>')
    root = CCGSentence(string=manualDef, globalID=-1, localID=-1)
    # Don't want the sentence node itself
    return root.child(0)

def replaceTree(before, after, node):
    """
    Align the trees so that we can look up
    """
    node, nodeLeaves = alignTree(before, node)
    if not node:
        return False
    leaves = zip(nodeLeaves, list(_getLeaves(after)))
    parent = node.parent()
    parent.replace(node, after)
    after.globalID = node.globalID
    for origNode, afterNode in leaves:
        afterNode.parent().replace(afterNode, origNode)
        origNode.changeLabel(afterNode.label)
    if after.label == 'Q':
        print after
        print parent
    return parent

def _getLeaves(nodeSpec):
    for node in nodeSpec.depthList():
        if node.length() == 0:
            yield node

def alignTree(before, node):
    if not CCG.isIdentical(node.label, before.label):
        return False, []
    leafList = []
    # Leaf list is populated as leaves are encountered
    if _checkSubtree(node, before, leafList):
        return node, leafList
    else:
        return False, []

def _checkSubtree(node, specNode, leafList):
    if not CCG.isIdentical(node.label, specNode.label):
        return False
    # Spec leaves must always pass, so long as their labels align,
    # because the tree cuts at some point
    if not specNode.length():
        leafList.append(node)
        return True
    if node.length() != specNode.length():
        return False
    for child, specChild in zip(node.children(), specNode.children()):
        if not _checkSubtree(child, specChild, leafList):
            return False
    return True



def findNodes(corpus, spec):
    global printer
    spec = makeTree(spec)
    print spec
    for j in xrange(0, corpus.length()):
        f = corpus.child(j)
        for i, s in enumerate(f.children()):
            for node in s.depthList():
                if alignTree(spec, node)[0]:
                    print printer.actOn(s)
                    print node
                    raw_input("File %d, Sentence %d. Press any key to continue.\n" % (j, i))
    

def preprocess(sentence):
    global defs
    nodeIdx = {}
    for node in sentence.depthList():
        if not node.isLeaf():
            nodeIdx.setdefault(getHash(node), []).append(node)
    removed = {}
    for key, defin in defs:
        nodes = nodeIdx.get(key, [])
        before, after, afterStr = defin
        if not nodes:
            continue
        i = 0
        for node in nodes:
            if node in removed:
                continue
            newNode = replaceTree(before, after, node)
            if newNode:
                after = makeTree(afterStr)
                defin[1] = after
                for subNode in node.depthList():
                    removed[subNode] = True    
                for subNode in newNode.depthList():
                    if not subNode.isLeaf() and node.length():
                        newKey = getHash(subNode)
                        nodeIdx.setdefault(newKey, []).append(subNode)
            else:
                i += 1
    return sentence

                

def getHash(node):
    if node.length() == 1:
        return hash((node.label, node.child(0).label))
    else:
        return hash((node.label, node.child(0).label, node.child(1).label))

def readDefs(defsLoc):
    global defs
    defStrs = open(defsLoc).read().strip().split('\n\n\n')
    feats = ['[pss]', '[ng]', '[dcl]', '[b]', '[to]']
    for defStr in defStrs:
        if not defStr.strip():
            continue
        beforeStr, afterStr = defStr.split('\n')
        if '[a]' in beforeStr or '[a]' in afterStr:
            for feat in feats:
                beforeFeat = beforeStr.replace('[a]', feat)
                afterFeat = afterStr.replace('[a]', feat)
                before = makeTree(beforeFeat)
                after = makeTree(afterFeat)
                key = getHash(before)
                defs.append((key, [before, after, afterFeat]))
        else:
            before = makeTree(beforeStr)
            after = makeTree(afterStr)
            key = getHash(before)
            defs.append((key, [before, after, afterStr]))            
        
#    before = makeTree("<NP> (<NP>) (<NP\NP> (<S[pss]\NP>))")
#    afterStr = "<NP 0> (<NP/(S[pss]\NP)>) (<S[pss]\NP>)"
#    after  = makeTree(afterStr)
#    defs = [(getHash(before), [before, after, afterStr])]
#    before = makeTree("<NP/(S[pss]\NP)> (<(NP/(S[pss]\NP))/N>) (<N>)")
#    afterStr = "<NP/(S[pss]\NP) 0> (<NP[nb]/N>) (<N/(S[pss]\NP)>)"
#    after = makeTree(afterStr)
#    defs.append((getHash(before), [before, after, afterStr]))

defs = []
if __name__ == '__main__':
    import psyco
    psyco.full()
    if 0:
        readDefs('/home/mhonn/code/mhonn/CCG/corpusReform/formFunction/preprocDefs.txt')
        ccgbank = CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/orig/AUTO/')
        s = ccgbank.child(2).child(0)
        preprocess(s)
        print printer.actOn(s)
    elif 1:
        spec = "<NP\NP> (<S[dcl]>)"
        ccgbank = CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/orig/')
        findNodes(ccgbank, spec)



