#!/usr/bin/python2.4
"""
Remove non-type raising unary rules,
in a flexible way (as there are multiple
strategies for dog this)

(NP\NP
  (S[ng]\NP
    ((S[ng]\NP)/NP)
    (NP)
  )
)
Becomes:

(NP\NP
  ??
  (??/NP)
  (NP)
)
"""
import copy
import os, sys
from os.path import join as pjoin
from copy import deepcopy as dcopy
from optparse import OptionParser

import CCG
import CCG.Rules
from Treebank.CCGbank import Writers, CCGNode, CCGbank
from Treebank.CCGbank import Production, setComplexAdj

import preprocessors

def localPath(extension):
    return pjoin(os.path.dirname(__file__), extension)
    



def targetProductions(sentence):
    """
    Generate the non-type raising unary productions
    in a sentence. This ensures that
    the rules are processed one at a
    time, so that the derivation changes
    during the loop.

    Generate punctuation rules too
    """
    global keepPunct, keepConj, replaceN, localiseAdj, changeSAdj, nullMode
    unaries = []
    preprocesses = []
    if lexCommaConj:
        preprocesses.append(doLexicaliseCommaConj)
    if replaceN:
        preprocesses.append(doReplaceN)
    if nAttach:
        preprocesses.append(doNAttach)
    if changeSAdj:
        preprocesses.append(doReplaceSAdj)
    if localiseAdj:
        preprocesses.append(doLocaliseAdj)
    if npSubcat:
        preprocesses.append(doNPSubcat)
    if noPunctAbsorbtion:
        preprocesses.append(doNoPunctAbs)
    for preprocess in preprocesses:
        for node in sentence.depthList():
            if node.isLeaf():
                continue
            # Avoid having multiple points in a subtree match a preprocess
            parent = node.parent()
            if parent and CCG.isIdentical(parent.label, node.label):
                continue
            preprocess(node)
    if zeroMode:
        return []
    for node in sentence.depthList():
        # Punctuation and conj rules
        child = None
        parent = None
        if node.isLeaf() or node.isRoot():
            continue
        if localiseAdj and node.label.isAdjunct() and not node.label.conj:
            parent = node.parent()
            if not CCG.isIdentical(parent.label, node.label):
                head = node.head()
                newAdj = adjToUnary(node)
                if newAdj:
                    unaries.append((newAdj, node))
        if node.length() == 2:
            l, r = node.children()
            newChild = None
            if not keepPunct:
                if l.label.isPunct() or r.label.isPunct():
                    child = handlePunctCued(node, l, r)
                    if child:
                        parent = child.parent()
                        unaries.append((parent, child))
                        continue       
            if not keepConj:
                if l.label == CCG.conj or r.label == CCG.conj:
                    child = conjToUnary(node, l, r)
                    if child:
                        parent = child.parent()
                        unaries.append((parent, child))
        elif node.length() == 1:
            parent = node
            child = node.child(0)
            if not child.isLeaf():
                if CCG.isIdentical(parent.label, child.label):
                    handleSameLabelled(parent, child)
                else:
                    unaries.append((parent, child))
    return unaries

def doLexicaliseCommaConj(comma):
    if not comma.label.isPunct():
        return None
    parent = comma.parent()
    if not comma.parent().label.conj:
        return None
    sibling = comma.sibling()
    if sibling.label.conj:
        return None
    newLabel = CCG.Category('conj')
    comma.changeLabel(newLabel)


NPbNP = CCG.Category('NP\NP')
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
    if not CCG.isIdentical(adnom.label, NPbNP):
        return None
    np = adnom.sibling()
    if not np:
        return None
    if not CCG.isIdentical(np.label, CCG.NP):
        return None
    
    top = adnom.parent()
    if not CCG.isIdentical(top.label, CCG.NP):
        return None
    # Find the highest N node
    for node in np.breadthList():
        if CCG.isIdentical(node.label, CCG.N):
            n = node
            break
    else:
        return None
    # So imagine we have (NP-1 (NP-2 (NP-3 N) ,) (adnom))
    # Collect uncles of N until we hit NP-1
    uncles = []
    node = n.parent()
    while node is not np:
        sibling = node.sibling()
        if sibling and node < sibling:
            uncles.append(sibling)
        node = node.parent()
    # Adnom is last uncle node
    uncles.append(adnom)
    attachPoint = n
    for uncle in uncles:
        if uncle:
            attachPoint = uncle.move(attachPoint, 0)
            if not uncle.label.isPunct():
                newLabel = CCG.Category('N\N')
                uncle.changeLabel(newLabel)
    

def _makeNAttach(adnom, nNode, newLabel):
    newNode = CCGNode(label=CCG.Category('N'), headIdx=0)
    adnom.changeLabel(CCG.Category(newLabel))
    adnom.reattach(newNode)
    nNode.insert(newNode)

            
    
    
    


def doReplaceSAdj(node):
    if not CCG.isIdentical(node.label, 'S[adj]\NP'):
        return None
    sibling = node.sibling()
    head = node.head()
    if head.label.startswith('R'):
        newLabel = CCG.Category('A')
    else:
        newLabel = CCG.Category('J')
    if sibling and sibling.label.isComplex() and sibling.label.argument == node.label:
        newSiblingLabel = CCG.ComplexCategory(sibling.label.result, dcopy(newLabel), sibling.label.slash, sibling.label.conj)
        sibling.changeLabel(newSiblingLabel)
    newLabel.conj = node.label.conj
    node.changeLabel(newLabel)

def doLocaliseAdj(adjNode):
    if not adjNode.label.isAdjunct():
        return None
    if not adjNode.label.result.isComplex():
        return None
    if adjNode.label.conj:
        return None
    innerResult = adjNode.stag.innerResult()
    newLabel = CCG.ComplexCategory(innerResult, innerResult, adjNode.stag.slash, adjNode.stag.conj)
    adjNode.changeLabel(newLabel)       

def doReplaceN(node):
    if node.label != CCG.N:
        return None
    if node.label.feature:
        nodeFeat = ''
    else:
        nodeFeat = ''
    sibling = node.sibling()
    parent = node.parent()
    # If unary, trim parent
    if not sibling and CCG.isIdentical(parent.label, CCG.NP):
        grandParent = parent.parent()
        grandParent.replace(parent, node)
    elif sibling and CCG.isIdentical(sibling.label, 'NP/N[nb]'):
        sibling.changeLabel(CCG.Category('NP/NP'))
    elif sibling and sibling.label.argument == CCG.N:
        if sibling.label.argument.feature:
            feature = sibling.label.argument.feature
        else:
            feature = ''
        newArg = CCG.Category('NP' + feature)
        newLabel = CCG.ComplexCategory(sibling.label.result, newArg, sibling.label.slash, sibling.label.conj)
        sibling.changeLabel(newLabel)
    node.changeLabel(CCG.Category('NP' + nodeFeat))


def doNPSubcat(node):
    """
    The preprocess_defs leave some productions where an NP with arguments is
    is post-modified. Since backwards cross comp is illegal for N and NP, we can either change the modifier or
    subcategorise for it. The modifier's almost always 'of', so change the mod
    """
    def getChild(node):
        if node.child(0).isLeaf():
            return None
        if node.child(0).label.isPunct():
            return node.child(1)
        else:
            return node.child(0)
    if node.label.conj:
        return None
    if not node.label.isComplex():
        return None
    if node.label.isAdjunct():
        return None
    if node.child(0).isLeaf():
        return None
    innerResult = node.label.innerResult()
    if innerResult != CCG.N and innerResult != CCG.NP:
        return None
    child = node
    productions = []
    while child and child.label == node.label:
        sibling = child.sibling()
        if not sibling:
            break
        if sibling.label == 'NP\NP' or sibling.label == 'N\N':
            productions.append((child, sibling))
        if child.isLeaf():
            break
        child = getChild(child)
   # if node.label != 'NP/(S\NP)':
   #     return None
    for head, adjunct in productions:    
        newLabel = CCG.ComplexCategory(head.label, head.label, '\\', False)
        adjunct.changeLabel(newLabel)

def doNoPunctAbs(punct):
    if punct.label.isComplex() or punct.label.conj or not punct.label.isPunct():
        return None
    sibling = punct.sibling()
    if not punct.sibling():
        return None
    parent = punct.parent()
    if not CCG.isIdentical(sibling.label, parent.label):
        return None
    if punct < sibling:
        slash = '/'
    else:
        slash = '\\'
    if sibling.label.conj:
        punct, sibling, parent, slash = _moveConjPunct(punct, sibling, parent, slash)
    forceDep = False
    newHat = CCG.makeAdjunct(parent.label, slash, forceDep)
    # Add the unhatted node
    node = CCGNode(label=newHat, headIdx=0)
    punct.insert(node)
    newLabel = dcopy(punct.label)
    newLabel.morph = newHat
    punct.changeLabel(newLabel)
                            
def _moveConjPunct(punct, sibling, parent, slash):
    """
    If punctuation attaches to a conjunction node, move it the opposite way so that it attaches to the conj
    """
    if slash == '/':    
        nextWord = sibling.getWord(0)
    else:
        nextWord = sibling.getWord(-1)
    sibling = nextWord.parent()
    assert sibling.length() == 1
    parent = sibling.parent()
    node = CCGNode(label=dcopy(sibling.label), headIdx=0)
    sibling.insert(node)
    punct.reattach(node)
    return punct, sibling, node, slash
    
    



def changeSentence(sentence, strategy):
    """
    Apply a modification strategy to a sentence
    """
    global keepNNP, noTRaise, keepPunct, keepConj
    preprocessors.preprocess(sentence)
    if options.debug:
        print sentence
    for parent, left in targetProductions(sentence):
        if not noTRaise and isTypeRaise(parent, left):
            continue
        if keepNNP and CCG.isIdentical(parent.label, CCG.NP) and CCG.isIdentical(left.label, 'N'):
            continue
        strategy(parent, left)

def isTypeRaise(parent, child):
    if child.isLeaf() or parent.isRoot():
        return False
    parentLab = parent.label
    childLab = child.label
    if CCG.Rules.ftRaise(childLab, parentLab) or CCG.Rules.btRaise(childLab, parentLab):
        return True
    else:
        return False

def handlePunctCued(parent, left, right):
    """
    Handle type-changes cued by punctuation
    """
    if typeChangePunct:
        _doPunctTypeChange(parent, left, right)
    else:
        _doPunctToUnary(parent, left, right)

def _doPunctToUnary(parent, left, right):
    """
    Insert a node above a punctuation type changing rule such as:
    (S\NP)\(S\NP) --> NP ,
    So that it can be handled as a unary type change:
    (S\NP)\(S\NP) --> (S\NP)\(S\NP) , --> (S\NP)\(S\NP) --> NP
    """
    if left.label.isPunct():
        punct = left
        other = right
    else:
        punct = right
        other = left
    if not parent.label.conj and not other.label.conj and not CCG.isIdentical(parent.label, other.label):
        newHat = dcopy(parent.label)
        base = dcopy(other.label)
        base.morph = dcopy(newHat)
        node = CCGNode(label=newHat, headIdx=0)
        other.insert(node)
        other.changeLabel(base)
        if noPunctAbsorbtion:
            doNoPunctAbs(punct)
        return other
    return None

def _doPunctTypeChange(parent, left, right):
    """
    Hang the type change on the punctuation category for punct-cued type-changes
    (S\NP)\(S\NP) --> NP ,
    (S\NP)\(S\NP) --> NP (S\NP)\(S\NP)\NP
    Except, use a hat category so we ensure no markedup file clashes:
    (S\NP)\(S\NP) --> NP ,^((S\NP)\(S\NP)\NP)
    """
    if left.label.isPunct():
        punct = left
        other = right
        slash = '/'
    else:
        punct = right
        other = left
        slash = '\\'
    if not parent.label.conj and not other.label.conj and not CCG.isIdentical(parent.label, other.label):
        newHat = CCG.addArgs(parent.label, [(other.label, slash, None)])
        node = CCGNode(label=newHat, headIdx=0)
        punct.insert(node)
        newLabel = dcopy(punct.label)
        newLabel.morph = dcopy(newHat)
        punct.changeLabel(newLabel)
        

def conjToUnary(parent, left, right):
    """
    Change conjunction cases where a type change gets magicked in during conjunction, so that
    it's handled as a unary case
    """
    if left.label == CCG.conj:
        conj = left
        other = right
    else:
        conj = right
        other = left
    if parent.label.conj and not other.label.conj and parent.label != other.label:
        conjLess = str(parent.label).replace('[conj]', '')
        if conjLess != str(other.label):
            # If other is unary, use its child, to avoid a 2-unary chain. Do this even if unary
            # is valid type-raise, because the node's been type raised into an invalid conjunction,
            # which is broken anyway
            if other.length() == 1 and not other.child(0).isLeaf():
                child = other.child(0)
                parent.replace(other, child)
                other = child
            newLabel = dcopy(parent.label)
            newLabel.conj = False
            node = CCGNode(label=newLabel, headIdx=0)
            parent.replace(other, node)
            node.attachChild(other)
            return other
    return None

def adjToUnary(adjNode):
    assert not adjNode.label.result.isComplex()
    if adjNode.length() == 1 and not adjNode.child(0).isLeaf():
        return None
    newLabel = findNodeType(adjNode)
    if not newLabel:
        return None
    newNode = CCGNode(label=adjNode.label, headIdx=0)
    # Swap the node labels so that we can insert above
    adjNode.changeLabel(newLabel)
    parent = adjNode.parent()
    parent.replace(adjNode, newNode)
    newNode.attachChild(adjNode)
    return newNode




def findNodeType(adjNode):
    """
    None if clause typed
    NP
    PP
    Advp
    """
    head = adjNode.head()
    headLabel = str(head.parg).replace('[adj]', '')
    if 'S[' in headLabel:
        return None
    if head.label == 'DT':
        return None
    if head.isPunct():
        return None
    if head.label == 'CC':
        return None
    if head.label.startswith('W'):
        return None
    if head.label.startswith('PP'):
        return None
    if head.label.startswith('J'):
        return CCG.Category('J')
    if head.label == 'PDT':
        return CCG.Category('N')
    if head.label in ['IN', 'TO', 'RP']:
        return CCG.Category('PP')
    elif head.label.startswith('RB'):
        return CCG.Category('A')
    elif adjNode.label.innerResult() == 'N':
        return CCG.Category('N')
    else:
        return CCG.Category('NP')

def handleSameLabelled(parent, child):
    """
    Trim branch when parent and child have the same label in a unary production
    """
    child.delete()



            
    
    

##############################
# Compile parent into result #
##############################

def compileUnary(parent, child):
    """
    Remove non-type raising unary rules by
    replacing the child category with the parent
    category
    """
    if child.length() == 1:
        child.changeLabel(parent.label)
    else:
        left, right = child.children()
        child.changeLabel(parent.label)
    # Replace parent with child in tree
    grandParent = parent.parent()
    result = _getProductionPieces(parent, child)
    parent.prune()
    child.reattach(grandParent)
    

def _compileComposition(parent, child, production):
    pass



########################################################
# Handles hat/morph/whatever we call it transformation #
########################################################



def unaryFormFunc(parent, child):
    """
    We want to keep the unary production, and just add the parent's label to the child's
    as a morph cat
    """
    # If parent is non-tr unary, trim it
    if not parent.sibling() and not parent.parent().isRoot() and not \
       isTypeRaise(parent.parent(), parent):
        
        grandParent = parent.parent()
        parent.prune()
        child.reattach(grandParent)
        # Just proceed as though we were dealing with the grandparent -> child unary
        parent = grandParent
    if not child.length():
        print parent
        raise StandardError
    if child.length() == 1:
        # For unaries, just copy the label
        newLabel = dcopy(child.label)
        newLabel.morph = parent.label
        child.changeLabel(newLabel)
    else:
        left, right = child.children()
        production = Production(left.label, right.label, child.label)
        if production.label == 'j':
            _handleConj(parent, child)
        else:
            newLabel = dcopy(child.label)
            labStr = str(newLabel).replace('[nb]', '').replace('[conj]', '')
            morphStr = str(parent.label).replace('[nb]', '').replace('[conj]', '')
            if labStr == morphStr:
                print parent
                print child
                raise StandardError
            newLabel.morph = parent.label
            child.changeLabel(newLabel)
            result = _getProductionPieces(parent, child)
           # autoDefs.add(origin, result, parent)

######################################################
# Null changes for CCGbank preprocessing experiments #
######################################################

def doZero(parent, child):
    pass


def _getProductionPieces(parent, child):
    leftGrand = child.child(0).label
    if child.length() == 2:
        rightGrand = child.child(1).label
    else:
        rightGrand = None
    return (parent.label, child.label, leftGrand, rightGrand)
        
def _handleConj(parent, child):
    """
    Move the non-conjunct to attach to the parent instead. This moves the unary
    down one, so that the child now 'heads' the unary (and so takes the parent's
    label)
    """
    left, right = child.children()
    if left.label.conj:
        conj = left
        other = right
    else:
        conj = right
        other = left
    conj.reattach(parent)
    newConjLabel = dcopy(parent.label)
    newConjLabel.conj = True
    conj.changeLabel(newConjLabel)
    child.label = dcopy(parent.label)
    newLabel = dcopy(other.label)
    newLabel.morph = dcopy(parent.label)
    other.changeLabel(newLabel)


def _deprformFuncComposition(parent, child, production):
    """
    Parent is of the form X$; child should be of the form (Y^X)$
    NP\NP --> S[dcl]/NP --> S/(S\NP) (S[dcl]\NP)/NP
    X=NP; Y=S[dcl]; $=/NP
    NP\NP --> (S[to]\NP)/NP --> (S[to]\NP)/(S[b]\NP) (S[b]\NP)/NP
    X=NP; Y=(S[to]\NP); $=/NP
    """
    print parent
    print child
    print production
    raise StandardError
    # Find child label
    pieces = _getChildLabel(parent, child)
    if not pieces:
        return None
    newChildLab, x, y = pieces
    # Find the head
    headChild = child.child(child.headIdx)
    # Construct its label
    args = []
    for result, arg, slash, unused in headChild.label.deconstruct():
        args.append((arg, slash, None))
        if CCG.isIdentical(result, y):
            break
    result = dcopy(result)
    result.morph = dcopy(x)
    newLabel = CCG.addArgs(result, args)
    headChild.changeLabel(newLabel)
    child.label = newChildLab
            


def _getChildLabel(parent, child):
    """
    Strip off arguments from parent and child until we find a non-match.
    The remaining result of the parent is the X category, which the child
    category will be shifted to. Then re-add the args.
    """
    parentPieces = list(parent.label.deconstruct())
    childPieces = list(child.label.deconstruct())
    dollarArgs = []
    while parentPieces:
        pResult, pArg, pSlash, unused = parentPieces.pop(0)
        cResult, cArg, cSlash, unused = childPieces.pop(0)
        if pArg == cArg:
            dollarArgs.append((pArg, cSlash, None))
            y = cResult
            x = pResult
            firstSlash = pSlash
        else:
            break
        if pSlash != cSlash:
            break
    if not dollarArgs:
        return None
        print parent
        print child
        raise AnalysisError
    # Construct the child
    newChild = dcopy(y)
    newChild.morph = dcopy(x)
    newChild = CCG.addArgs(newChild, dollarArgs)
    # Construct the parent label to check it works
    firstArg = dollarArgs[0][0]
    parentLabel = CCG.ComplexCategory(dcopy(x), dcopy(firstArg), firstSlash,
                                      False)
    parentLabel = CCG.addArgs(parentLabel, dollarArgs[1:])
    if parentLabel != parent.label:
        return None
    return newChild, x, y
     
    
#####################################
# Generic changing method           #
#####################################

def makeChanges(corpus, strategy, fileRange, outDir):
    autoWriter = Writers.AutoFileWriter(directory=pjoin(outDir, 'data/AUTO'))
    for i in fileRange:
        f = corpus.child(i)
        allChangedAuto = []
        for j, sentence in enumerate(f.children()):
            changeSentence(sentence, strategy)
            afterAuto = autoWriter.getSentenceStr(sentence)
            allChangedAuto.append(afterAuto)
        autoWriter.writeFile(f.ID, allChangedAuto)


class AnalysisError(StandardError):
    pass

    

def debugSentence(ccgbank, sentID, strategy):
    fID, sentID = sentID.split('.')
    sentID = int(sentID)
    if fID.isdigit():
        fID = int(fID)
        f = ccgbank.child(fID)
    else:
        subdir = fID[4:6]
        filePath = pjoin(options.corpusPath, 'data/AUTO', subdir, fID + '.auto')
        print filePath
        f = ccgbank.file(filePath)
    s = f.child(sentID)
    print s
    changeSentence(s, strategy)
    print s
    print s.validate()

def getOptions():
    op = OptionParser()
    op.add_option('-i', '--input', action="store", type="string", dest="corpusPath",
    help="CCGbank path", default="/home/mhonn/Data/CCGBank/orig/")
    op.add_option('-o', '--output', action="store", type="string", dest="outDir",
                  help="Destination directory")
    op.add_option('-a', '--hat', action="store_true", dest="doMorph",
                  help="Convert to hat categories")
    op.add_option('-n', '--nounary', action="store_true", dest="doNoUnary",
                  help="Convert to NoUnary")
    op.add_option('-y', '--hybrid',  action="store_true", dest="doHybrid",
                  help="Convert to hybrid")
    op.add_option('-z', '--zero',    action="store_true", dest="doZero",
                  help="Zero PSG-rule conversion (used to implement preprocesses on vanilla CCGbank)")
    op.add_option('-t', '--thresh', action="store", type="int",
                  dest="ruleThresh", default=0,
                  help="Frequency above which a rule is considered valid")
    op.add_option('-e', '--extent', action="store", type="int",
                  dest="endIdx", default=2312, help="Convert until this file")
    op.add_option('-s', '--start', action="store", type="int",
                  dest="startIdx", default=0, help="Convert from this file")
    op.add_option('--notraise', action="store_true",
                  dest="noTRaise", default=False,
                  help="Preserve type raise rules")
    op.add_option('--keeppunct', action="store_true",
                  dest="keepPunct", default=False,
                  help="Preserve punctuation type-changes")
    op.add_option('--keepconj', action="store_true",
                  dest="keepConj", default=False,
                  help="Preserve conjunction type-changes")
    op.add_option('--keepnnp', action="store_true",
                  dest="keepNNP", default=False,
                  help="Preserve N->NP unary rule")
    op.add_option('--replacen', action="store_true",
                  dest="replaceN", default=False,
                  help="Preprocess N, changing it to NP[b]")
    op.add_option('--changesadj', action="store_true",
                  dest="changeSAdj", default=False,
                  help="Preprocess S[adj]\NP, changing it to AP or JP")
    op.add_option('--localiseadj', action="store_true",
                  dest="localiseAdj", default=False,
                  help="Ensure adjuncts always refer to atomic cats")
    op.add_option('--nattach', action="store_true",
                  dest="nAttach", default=False,
                  help="Change all NP\NP to attach at N\N level, removing need for N^NP^X. WARNING: Broken!")
    op.add_option('--npsubcat', action="store_true", dest="npSubcat",
                  default=False,
                  help="Make adjuncts subcategorise for NP argument structures if you'd need bxcomp")
    op.add_option('--lexcommaconj', action="store_true",
                  dest="lexCommaConj", default=False,
                  help="For , X-->X[conj], give the comma a conj supertag")
    op.add_option('--tcpunct', action="store_true",
                  dest="typeChangePunct", default=False,
                  help="Hang type changes on punctuation binary rules instead of converting them to unary")
    op.add_option('--nopunctabs', action="store_true",
                  dest="noPunctAbs", default=False,
                  help="Lexicalise punctuation absorbtion rules by adding categories like ,^(X\X)")
    op.add_option('-d', '--debug', action="store",
                  dest="debug", type="string",
                  help="Debug sentence at ID, e.g. wsj_003.1")
    op.add_option('-v', '--version', action="store",
                  dest="version", type="string", help="Version label")
    op.add_option('--novalidate', action="store_true",
                  dest="dontValidate", default=False,
                  help="Suppress validation for speed")
    op.add_option('--profile', action="store_true",
                  dest="profile", default=False,
                  help="Speed profile using hotshot")
    options, args = op.parse_args()
    if options.doMorph:
        options.output = 'Morph'
    elif options.doNoUnary:
        options.output = 'NoUnary'
    elif options.doHybrid:
        options.output = 'Hybrid'
    elif options.doZero:
        options.output = 'Preproced'
    else:
        op.print_help()
        sys.exit(1)
    return options

def main():
    global manualDefs, autoDefs
    if options.doMorph:
        if options.localiseAdj:
            # Tell changeNodeLabel to produce S|S instead of (S\NP)|(S\NP)
            setComplexAdj(False)
        preprocessors.readDefs(localPath('morph_preprocDefs.txt'))
        if options.debug:
            debugSentence(ccgbank, options.debug, unaryFormFunc)
        else:
            fileRange  = xrange(options.startIdx, options.endIdx)
            makeChanges(ccgbank, unaryFormFunc, fileRange, options.outDir)
    elif options.doHybrid:
        if options.localiseAdj:
            # Tell changeNodeLabel to produce S|S instead of (S\NP)|(S\NP)
            setComplexAdj(False)
        preprocessors.readDefs(localPath('hybrid_preprocDefs.txt'))
        if options.debug:
            debugSentence(ccgbank, options.debug, unaryFormFunc)
        else:
            makeChanges(ccgbank, unaryFormFunc, xrange(options.startIdx, options.endIdx), options.outDir)
            stats.report()
    elif options.doZero:
        preprocessors.readDefs(localPath('zero_preprocDefs.txt'))
        if options.debug:
            debugSentence(ccgbank, options.debug, doZero)
        else:
            makeChanges(ccgbank, doZero, xrange(options.startIdx, options.endIdx), options.outDir)
            stats.report()
    elif options.doNoUnary:
        preprocessors.readDefs(localPath('nounary_preprocDefs.txt'))
        if options.debug:
            debugSentence(ccgbank, options.debug, compileUnary)
        else:
            makeChanges(ccgbank, compileUnary, xrange(options.startIdx, options.endIdx), corpusLabel, options.version)


manualDefs = None
autoDefs = None
if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except:
        pass
    options = getOptions()
    ccgbank = CCGbank(path=options.corpusPath)
    CCG.setRuleFreq(0)
    # Flags controlling conversion logic
    keepNNP = options.keepNNP
    noTRaise = options.noTRaise
    keepPunct = options.keepPunct
    keepConj = options.keepConj
    changeSAdj = options.changeSAdj
    replaceN = options.replaceN
    changeSAdj = options.changeSAdj
    localiseAdj = options.localiseAdj
    nAttach = options.nAttach
    npSubcat = options.npSubcat
    lexCommaConj = options.lexCommaConj
    typeChangePunct = options.typeChangePunct
    noPunctAbsorbtion = options.noPunctAbs
    zeroMode = options.doZero
    if options.profile:
        import hotshot, hotshot.stats
        prof = hotshot.Profile('test.prof')
        prof.runcall(main)
        prof.close()
        stats = hotshot.stats.load('test.prof')
        stats.strip_dirs()
        stats.sort_stats('time', 'calls')
        stats.print_stats(20)
    else:
        main()
       
