import sys
from os.path import join as pjoin
import data
import CCG
from Treebank import CCGbank
from Treebank.CCGbank import Writers
from general import stats, log, debug

applications = {}
def doSentence(sentence):
    global applications
    processes = [doNCoord, doPartitiveGenitive,
                 doNAttach, doNoisyTR, doCleanup]
    for process in processes:
        # Breadthlist is important; depthlist processes nodes out of order
        # e.g. wsj_0010.auto~5
        changes = [True]
        while any(changes):
            changes = []
            for node in sentence.breadthList():
                if node.isLeaf():
                    continue
                hasChanged = process(node)
                changes.append(hasChanged)
            if any(changes):
                applications.setdefault(
                    sentence.globalID, set()).add(process.func_name)

def doSqemApplication(sqem):
    """
    Deprecated
    Handle application instances of S[qem], converting them to NP
    """
    if not sqem.isProduction(selfType='S[qem]'):
        return None
    sibling = sqem.sibling()
    # Handle PSG rule at wsj_0349.17 and wsj_2116.3
    if sqem.isProduction(selfType='S[qem]', sibling='conj'):
        sqem.changeLabel(CCG.Category('NP'))
        return True
    if not sibling or not CCG.isIdentical(sibling.label.argument, 'S[qem]'):
        return None
    if sibling < sqem:
        slash = '/'
    else:
        slash = '\\'
    newSiblingLabel = CCG.addArgs(sibling.label.result, [(CCG.Category('NP'),
                                                          slash, False)])
    sibling.changeLabel(newSiblingLabel)
    sqem.changeLabel(CCG.Category('NP'))
    return True

def doSqemComposition(sqemTR):
    """
    Deprecated
    Handle case where S[qem] is type raised and composed
    e.g. wsj_1856.61
    """
    if not sqemTR.isProduction(
        selfType=r'(S\NP)\((S\NP)/S[qem])', left='S[qem]'):
        return None
    sibling = sqemTR.sibling()
    newSiblingLabel = CCG.Category(str(sibling.label).replace('S[qem]', 'NP'))
    sqemTR.changeLabel(CCG.Category(r'(S\NP)\((S\NP)/NP)'))
    sibling.changeLabel(newSiblingLabel)
    sqem = sqemTR.child(0)
    sqem.changeLabel(CCG.Category(r'NP'))
    return True
                       

def doNCoord(np):
    """
    Change case where NP coordinates after raising to NP
    (NP
      (N president)
    (NP[conj]
      (NP
        (N CEO)
       )
       and
    )
    """
    if np.label != CCG.NP:
        return None
    if np.length() != 2:
        return None
    leftNP, conjNP = np.children()
    if not conjNP.label.conj:
        return None
    if leftNP.label != CCG.NP or conjNP.label != CCG.NP:
        return None
    if not leftNP.isUnary():
        return None
    leftN = leftNP.child(0)
    if not leftN.label == CCG.N:
        return None
    rightNP = conjNP.child(1)
    if not rightNP.isUnary():
        return None
    rightN = rightNP.child(0)
    if not rightN.label == CCG.N:
        return None
    leftNP.delete()
    rightNP.delete()
    np.changeLabel(CCG.Category('N'))
    newParent = CCGbank.CCGNode(label=CCG.Category('NP'), headIdx=0)
    np.insert(newParent)
    return True

partNouns = """All, Another, Average, Both, Each, Many, Many, Much, Several,
Some, Something, Those, all, another, any, anything, both, certain, each,
either, enough, few, five, half, little, many, many, million, most, much,
neither, neither, nothing, one-fifth, one-third, other, part, plenty,
several, some, something, that, third, those, three,
three-fourths, two""".replace('\n', '').replace(' ', '').lower().split(',')
def doPartitiveGenitive(np):
    """
    Transform partitive genitives:
    (NP
       (NP (DT *))
       (NP\NP
         ((NP\NP)/NP of)
         (NP )
       )
    )
    -->
    (NP
       (NP/PP (DT *))
       (PP
         (PP/NP of)
         (NP )
       )
    )
    """
    if not np.isProduction(selfType=CCG.NP, parent=CCG.NP, sibling=NPbNP):
        return None
    # Head must be DT or NN or JJ
    # NN heads are something of etc. Not quite partitive, but needs same
    # analysis
    head = np.head()
    if head.text.lower() not in partNouns and head.pos != 'CD':
        return None
    if not CCG.isIdentical(head.parg, CCG.NP):
        # Look for a unary rule to trim
        if len(np) == 1 and np.child(0).label == CCG.N:
            child = np.child(0)
            child.changeLabel(np.label)
            np.delete()
            np = child
        else:
            return None
    # Must have 'of' pp
    pp = np.sibling()
    of = pp.head()
    if of.text.lower() != 'of':
        # Handle "something like" case as partitive genitive too
        if not (of.text.lower() == 'like' and
                head.text.lower().endswith('thing')):
            return None
    np.changeLabel(CCG.addArgs(np.label, [(CCG.Category('PP'), '/', False)]))
    pp.changeLabel(CCG.Category(r'PP'))
    pp.headIdx = 1
    np.parent().headIdx = 1
    return True

def doNAttach(adnom):
    """
    Change
    (NP
      (NP (NP/N N))
      (NP\NP)
    )
    to
    (NP
      (NP/N)
      (N (N N\N))
    )
    """
    # Find NP --> NP NP\NP production
    if not adnom.isProduction(selfType=NPbNP, parent=CCG.NP, sibling=CCG.NP):
        return None
    np = adnom.sibling()
    assert np < adnom
    adnomEdge = adnom.getWord(0).wordID
    n = np.head().parent()
    nEdge = n.getWord(-1).wordID + 1
    while (adnomEdge != nEdge) or not CCG.isIdentical(n.label, CCG.N) \
          or n.parent().label.conj:
        if n is np:
            return None
        n = n.parent()
        nEdge = n.getWord(-1).wordID + 1
    adnom.move(n, 0)
    adnom.changeLabel(CCG.Category('N\N'))
    return True

def doThose(np):
    """
    Provide a handler for "those PP" cases to make debugging easier
    """
    if not np.isProduction(selfType=CCG.NP, sibling=NPbNP, parent=CCG.NP):
        return None
    w = 'something,anything,nothing,someone,everything,everyone,everybody,those'
    w = w.split(',')
    w.extend('anyone,anybody,nobody,some,all,that,he,you,me,we,i,that,more,less,this'.split(','))
    if np.head().text.lower() not in w:
        return None
    adnom = np.sibling()
    newParent = CCGbank.CCGNode(label=CCG.Category('NP'), headIdx=0)
    np.insert(newParent)
    np.changeLabel(CCG.Category('N'))
    adnom.move(np, 0)
    adnom.changeLabel(CCG.Category(r'N\N'))
    return True
    

NPbNPfNP = CCG.Category(r'(NP\NP)/NP')
nnSdcl = CCG.Category(r'(N\N)/S[dcl]')
nnSdclNPbNPfNP = CCG.Category('((N\N)/S[dcl])\((NP\NP)/NP)')
def doCleanup(node):
    # ((N\N)/S[dcl]
    #   ((NP\NP)/NP under)
    #   (((N\N)/S[dcl])\((NP\NP)/NP) which))
    if node.isProduction(selfType=NPbNPfNP):
        sibling = node.sibling()
        # If sibling comes after node and applies it, change the argument
        if sibling > node and CCG.isIdentical(sibling.label.argument, NPbNPfNP):
            result = sibling.label.result
            newLabel = CCG.addArgs(result, [(CCG.Category(r'(N\N)/NP'), '\\',
                                                          False)])
            sibling.changeLabel(newLabel)
            node.changeLabel(CCG.Category('(N\N)/NP'))
            return True
    
    
NPfNPbNP = CCG.Category(r'NP/(NP\NP)')
NPfNP = CCG.Category(r'NP/NP')
def doNoisyTR(trNode):
    """
    Handles a noisy analysis:
    (NP/NP
      (NP/(NP\NP)
        (NP some))
      ((NP\NP)/NP of))
    (((N\N)/(S[dcl]\NP))\(NP/NP) which)
    to
    ( NP/NP
      ( (NP/NP)/(PP/NP) some )
      ( PP/NP of )
     )
     ((N\N)/(S[dcl]\NP))\(NP/NP)
     """
    if not trNode.isProduction(selfType=NPfNPbNP, sibling=NPbNPfNP,
                              parent=NPfNP):
        return None
    if len(trNode) != 1:
        return None
    np = trNode.child(0)
    pp = trNode.sibling()
    # Snip out the type raise node
    trNode.delete()
    # Snip out the child for NP --> unaries etc
    if np.isUnary():
        np.child(0).delete()
    # Make the label changes
    np.changeLabel(CCG.addArgs(np.label, [(CCG.Category('PP'), '/', False)]))
    pp.changeLabel(CCG.Category(r'PP/NP'))
    return True
    

def _makeNAttach(adnom, nNode, newLabel):
    newNode = Treebank.CCGBank.Node(label=CCG.Category('N'), headIdx=0)
    adnom.changeLabel(CCG.Category(newLabel))
    adnom.reattach(newNode)
    nNode.insert(newNode)

def main(inLoc, outLoc):
    openLogs(outLoc)
    autoWriter = Writers.AutoFileWriter()
    pargWriter = Writers.PargFileWriter()
    pargPath = pjoin(inLoc, 'data/PARG')
    ccgbank = CCGbank.CCGbank(path=inLoc)
    autoWriter.setDir(pjoin(outLoc, 'data/AUTO'))
    for f in ccgbank.children():
        changed = []
        f.addPargDeps(pargPath)
        for sentence in f.children():
            before = autoWriter.getSentenceStr(sentence)
            prettyBefore = str(sentence)
#            if sentence.validate():
#                validBefore = True
#            else:
#                validBefore = False
            doSentence(sentence)
            changed.append(autoWriter.getSentenceStr(sentence))
#            if not validBefore:
#                changed.append(autoWriter.getSentenceStr(sentence))
#            elif sentence.validate():
#                changed.append(autoWriter.getSentenceStr(sentence))
#            else:
#                changed.append(autoWriter.getSentenceStr(sentence))
#                print prettyBefore
#                print sentence
#                changed.append(before)
        autoWriter.writeFile(f.ID, changed)
    reportApplications()

def reportApplications():
    global applications
    sortable = sorted(applications.items(), key=lambda a: len(a[0]))
    for sentence, processes in sortable:
        print '%s\t%s' % (sentence, '\t'.join(sorted(processes)))
        

def debug(inLoc, key):
    log.openLog('/dev/null', 'invalid')
    log.openLog('/dev/null', 'nConj')
    ccgbank = CCGbank.CCGbank(path=inLoc)
    key = pjoin(inLoc, 'data', 'AUTO', key[4:6], key.replace('.', '.auto~'))
    s = ccgbank.sentence(key)
    print s
    print s.validate()
    doSentence(s)
    print s
    print s.validate()

def openLogs(outLoc):
    log.openLog(pjoin(outLoc, 'logs/invalid.log'), 'invalid')
    log.openLog(pjoin(outLoc, 'logs/nConj.log'), 'nConj')

NPbNP = CCG.Category('NP\NP')
if __name__ == '__main__':
    if sys.argv[1] == '-d':
        debug(data.ccgbank, sys.argv[2])
        sys.exit(1)
    if len(sys.argv) != 3:
        print "USAGE: nAttach.py [-d address] <ccgbank loc> <out loc>"
        sys.exit(1)
    corpusLoc = data.getLoc(sys.argv[1])
    outLoc = data.getLoc(sys.argv[2])
    main(corpusLoc, outLoc)
