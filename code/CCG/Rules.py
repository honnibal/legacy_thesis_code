"""
Combinatory rules
"""
from LegacyCategory import ComplexCategory, Category, isIdentical, addArgs, combine, N, NP
import cPickle, pickles
import sys
def fApp(left, right):
    """
    Forward Application: X/Y Y -> X
    """
   # if left.conj or right.conj:
   #     return None
    # HAT CONSTRAINT: application fails if functor is not an adjunct and either
    # have hats
    if not left.isAdjunct():
        if right.morph or left.morph:
            return None
    if (left.slash == '/') and left.argument.unify(right):
        if str(left.result) == 'NP[nb]':
            left.result.feature = ''
        return left.result
    
def bApp(left, right):
    """
    Backward Application: Y X\Y -> X
    """
    # HAT CONSTRAINT: application fails if functor is not an adjunct and it
    # has a hat, or if either have hats
    if not right.isAdjunct():
        if left.morph or right.morph:
            return None
    if left.conj or right.conj:
        return None
    if (right.slash == '\\') and right.argument.unify(left):
        return right.result
    
def lConjApp(left, right):
    """
    Left conjunction application: conj X -> X[conj]
    """
    if left.cat == 'conj':
        # Special case for conj\conj so that we don't produce multiple rules
        if right == 'conj\conj':
            return False
        right.conj = True
        return right
    
def rConjApp(left, right):
    """
    Right conjunction application: X conj -> X[conj]
    """
    if right.cat == 'conj':
        # Special case for conj/conj so that we don't produce multiple rules
        if left == 'conj/conj':
            return False
        left.conj = True
        return left
    
def lConjAbs(left, right):
    """
    Left conjunction application: conj X -> X
    """
    if left.cat == 'conj':
        return right
    
def rConjAbs(left, right):
    """
    Right conjunction absorption: X conj -> X
    """
    if right.cat == 'conj':
        return left
    
def lPuncAbs(left, right):
    """
    Left punct absorbtion: , X -> X
    """
    if left.isPunct():
        return right

def rPuncAbs(left, right):
    """
    Right punc absorption: X , -> X
    """
    if right.isPunct():
        return left

def lPuncConj(left, right):
    """
    Left punct absorbtion: , X -> X
    """
    if left.isPunct():
        right.conj = True
        return right

def rPuncConj(left, right):
    """
    Right punc absorption: X , -> X
    """
    if right.isPunct():
        left.conj = True
        return left

def lConj(left, right):
    """
    Left conjunction: X[conj] X -> X
    """
    if left.conj and right.unify(left):
        # Doesn't matter which we return
        left.conj = False
        return left

def rConj(left, right):
    """
    Right conjunction: X X[conj] -> X
    """
    # Doesn't matter which we return
    if right.conj and left.unify(right):
        right.conj = False
        return right
        return right
    
def funnyConj(left, right):
    if left == 'conj':
        innerResult = right.innerResult()
        if  innerResult == N or innerResult == NP:
            return right
    elif right == 'conj':
        innerResult = left.innerResult()
        if innerResult == N or innerResult == NP:
            return left
    return None

def fComp(left, right):
    """
    Forward composition: X/Y Y/Z -> X/Z
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if left.morph:
        return None
    if left.conj or right.conj:
        return None
    if left.slash == '/' and right.slash == '/' and left.argument.unify(right.result):
        answer = ComplexCategory(left.result, right.argument, '/', False, 0, '')
        answer.morph = right.morph
        return answer
    
def fxComp(left, right):
    """
    Forward crossed composition: X/Y Y\Z -> X\Z
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if left.morph:
        return None
    if left.conj or right.conj:
        return None
    if left.slash == '/' and right.slash == '\\' and left.argument.unify(right.result):
        answer = ComplexCategory(left.result, right.argument, '\\', False, 0, '')
        answer.morph = right.morph
        return answer
    
def bComp(left, right):
    """
    Backward composition: Y\Z X\Y -> X\Z
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if right.morph:
        return None
    if left.conj or right.conj:
        return None
    if left.slash == '\\' and right.slash == '\\' and right.argument.unify(left.result):
        answer = ComplexCategory(right.result, left.argument, '\\', False, 0, '')
        answer.morph = left.morph
        return answer
    
def bxComp(left, right):
    """
    Backward crossed composition: Y/Z X\Y -> X/Z
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if right.morph:
        return None
    if left.conj or right.conj:
        return None
    if left.slash == '/' and right.slash == '\\' and right.argument.unify(left.result):
        innerResult = left.innerResult()
        if innerResult == NP or innerResult == N:
            return None
        answer = ComplexCategory(right.result, left.argument, '/', False, 0, '')
        answer.morph = left.morph
        return answer
    
def gfComp(left, right):
    """
    Generalised forward composition: X/Y Y/$ -> X/$
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if left.morph:
        return None
    if left.conj or right.conj:
        return None
    if left.slash != '/':
        return False
    answer = _genComp(right, left.result, left.argument, '/')
    return answer
    
def gfxComp(left, right):
    """
    Generalised forward crossing composition: X/Y Y\$ -> X\$
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if left.morph:
        return None
    if left.conj or right.conj:
        return None
    if left.slash != '/':
        return False
    answer = _genComp(right, left.result, left.argument, '\\')
    return answer
    
def gbComp(left, right):
    """
    Generalised backward composition: Y\$ X\Y -> X\$
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if right.morph:
        return None
    if left.conj or right.conj:
        return None
    if right.slash != '\\':
        return False
    answer = _genComp(left, right.result, right.argument, '\\')
    return answer
    
    
def gbxComp(left, right):
    """
    Generalised backward crossing composition: Y/$ X\Y -> X/$
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if right.morph:
        return None
    if left.conj or right.conj:
        return None
    if right.slash != '\\':
        return False
    answer = _genComp(left, right.result, right.argument, '/')
    return answer

def _genComp(dollarCat, x, y, slash):
    # Generalised forward composition: X/Y (Y/Z)/$ -> (X/Z)/$
    # Generalised forward crossing composition: X/Y (Y\Z)\$ -> X\$
    # Generalised backward composition: (Y\Z)\$ X\Y -> (X\Z)\$
    # Generalised backward crossing composition: (Y/Z)/$ X\Y -> (X/Z)/$
    # ((S[dcl]\NP)/PP)/PP
    # (S\NP)\(S\NP)
    if slash not in ['/', '\\'] or not x or not y:
        return False
    i = 0
    arguments = []
    for result, argument, dollarSlash, morph in dollarCat.deconstruct():
        arguments.append((argument, dollarSlash, morph))
        i += 1
        if dollarSlash == slash and result.unify(y):
            break
        if i == 4:
            break
    else:
        return False
    # Don't match for non-general composition
    if len(arguments) == 1:
        return False
    # Make a new category preserving the heads somehow
    arguments.reverse()
    newCat = addArgs(x, arguments)
    return newCat
    
def fSub(left, right):
    """
    Forward substitution: (X/Y)/Z Y/Z -> X/Z
    Where Y is a predicate category
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if left.hasMorph:
        return None
    if left.slash == right.slash == left.result.slash == '/' \
    and left.argument == right.argument \
    and left.result.argument == right.result \
    and right.result.isPredicate():
        left.argument.unify(right.argument) # Unify Zs
        left.result.argument.unify(right.result) # Unify Ys
        # Make a new category X/Z
        # result, argument, slash, conj, idx, depType
        return ComplexCategory(left.result.result, left.argument, '/', False, -2, '')
    
def fxSub(left, right):
    """
    Forward crossing substitution: (X/Y)\Z Y\Z -> X\Z
    Where Y is a predicate category
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if left.hasMorph:
        return None
    if left.slash == right.slash == '\\' and left.result.slash == '/' \
    and left.argument == right.argument \
    and left.result.argument == right.result \
    and right.result.isPredicate():
        left.argument.unify(right.argument) # Unify Zs
        left.result.argument.unify(right.result) # Unify Ys
        # Make a new category X\Z
        # result, argument, slash, conj, idx, depType
        return ComplexCategory(left.result.result, left.argument, '\\', False, -2, '')
    
def bSub(left, right):
    """
    Backward substitution: Y\Z (X\Y)\Z -> X\Z
    Where Y is a predicate category
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if right.hasMorph:
        return None
    if left.slash == right.slash == right.result.slash == '\\' \
    and left.argument == right.argument \
    and right.result.argument == left.result \
    and left.result.isPredicate():
        left.argument.unify(right.argument) # Unify Zs
        right.result.argument.unify(left.result) # Unify Ys
        # Make a new category X\Z
        # result, argument, slash, conj, idx, depType
        return ComplexCategory(right.result.result, right.argument, '\\', False, -2, '')
    
def bxSub(left, right):
    """
    Backward crossing substitution: Y/Z (X\Y)/Z -> X/Z
    Where Y is a predicate category
    """
    # HAT CONSTRAINT:
    # Composition fails if functor has a hat
    if right.hasMorph:
        return None
    if left.slash == right.slash == '/' and right.result.slash == '\\' \
    and left.argument == right.argument \
    and right.result.argument == left.result \
    and left.result.isPredicate(): # Y must be a predicate
        left.argument.unify(right.argument) # Unify Zs
        right.result.argument.unify(left.result) # Unify Ys
        # Make a new category X\Z
        # result, argument, slash, conj, idx, depType
        return ComplexCategory(right.result.result, right.argument, '\\', False, -2, '')

def ftRaise(child, parent):
    """
    Forward type raising:

    X -> Y/(Y\X)
    """
    if child.hasMorph:
        return None
    y = parent.result
    x = child
    if parent.argument and parent.argument.result == y and parent.argument.argument == x:
        if parent.slash == '/' and parent.argument.slash == '\\':
            return parent


def btRaise(child, parent):
    """
    Backward type raising:

    X -> Y\(Y/X)
    """
    if child.hasMorph:
        return None
    y = parent.result
    x = child
    if parent.argument and parent.argument.result == y and parent.argument.argument == x:
        if parent.slash == '\\' and parent.argument.slash == '/':
            return parent

def tMorph(child, parent):
    if child.morph == parent:
        return parent
    else:
        return False
        
def gtMorph(child, parent):
    """
    (Y^X)$ -> X$
    """
    if not child.hasMorph:
        return False
    x, y, args, slash = _getMorphBits(child)
    builtParent = addArgs(x, args)
    if isIdentical(builtParent, parent):
        return builtParent
    else:
        return False
    

    
def gbxtMorph(child, parent):
    """
    (Y^X)\$ -> X/$
    """
    answer = _gxMorph(child, parent, '\\', '/')
    return answer
    

def gfxtMorph(child, parent):
    """
    (Y^X)/$ -> X\$
    """
    answer = _gxMorph(child, parent, '/', '\\')
    return answer


def _gxMorph(child, parent, childSlash, parentSlash):
    if not child.hasMorph:
        return False
    x, y, args, slash = _getMorphBits(child)
    if slash != childSlash:
        return False
    args[0][1] = parentSlash
    builtParent = addArgs(x, args)
    if isIdentical(builtParent, parent):
        return builtParent
    else:
        return False


def _getMorphBits(child):
    """
    Find the x, y and $ and firstSlash items for a type morph case
    """
    args = []
    for result, argument, slash in child.deconstruct():
        args.append([argument, slash])
        if result.morph:
            x = result.morph
            y = result
            return x, y, args, slash


tightFunctions = [fApp, bApp,
             lConj, rConj,
             lConjApp, rConjApp,
            lPuncAbs, rPuncAbs,
             fComp, bComp, bxComp,
             gfComp, gbComp, gbxComp]

functions = [fApp, bApp,
             lConj, rConj,
             lConjApp, rConjApp,
            lPuncAbs, rPuncAbs,
             lPuncConj, rPuncConj,
             funnyConj,
             fComp, bComp, bxComp,
             gfComp, gbComp, gbxComp, fxComp, gfxComp]
unaryFunctions = [ftRaise, btRaise, tMorph]

try:
    binaryRules = pickles.load('binaryRules')
except:
    binaryRules = {}
try:
    unaryRules = pickles.load('unaryRules')
except:
    unaryRules = {}

if __name__ == '__main__':
    cat1 = Category('N/N')
    cat2 = Category('N^NP')
    print combine(cat1, cat2)
    cat1 = Category('NP')
    cat2 = Category('(S[ng]\NP)^(NP\NP)')
    print combine(cat1, cat2)
    sys.exit(1)
    cat1 = Category('S/(S\NP)')
    cat2 = Category('((S[dcl]\NP)/S[dcl])^(S\S)')
    print combine(cat1, cat2)
    sys.exit(1)
    cat1 = Category('NP')
    cat2 = Category('NP/(NP\NP)')
    print "Forward type-raising"
    print ftRaise(cat1, cat2)
    cat1 = Category('PP')
    cat2 = Category('(S\NP)\((S\NP)/PP)')
    print "Backward type-raising"
    print btRaise(cat1, cat2)
    cat1 = Category('NP[nb]/N')
    cat2 = Category('N')
    print "Forward application"
    print fApp(cat1, cat2)
    cat1 = Category('NP')
    cat2 = Category('S[dcl]\NP')
    print "Backward application"
    print bApp(cat1, cat2)
    cat1 = Category('conj')
    cat2 = Category('S[dcl]\NP')
    print "Left conjunction application"
    print lConjApp(cat1, cat2)
    cat1 = Category('S[dcl]\NP')
    cat2 = Category('conj')
    print "Right conjunction application"
    print rConjApp(cat1, cat2)
    cat1 = Category('conj')
    cat2 = Category('S[dcl]\NP')
    print "Left conjunction absorption"
    print lConjAbs(cat1, cat2)
    cat1 = Category('S[dcl]\NP')
    cat2 = Category('conj')
    print "Right conjunction absorption"
    print rConjAbs(cat1, cat2)
    cat1 = Category('S[adj]\NP[conj]')
    cat2 = Category('S[adj]\NP')
    print "Left conjunction"
    print lConj(cat1, cat2)
    cat1 = Category('S[adj]\NP')
    cat2 = Category('S[adj]\NP[conj]')
    print "Right conjunction"
    print rConj(cat1, cat2)
    cat1 = Category(',')
    cat2 = Category('S[dcl]\NP')
    print "Left punctuation absorption"
    print lPuncAbs(cat1, cat2)
    cat1 = Category('S[dcl]\NP')
    cat2 = Category(',')
    print "Right punctuation absorption"
    print rPuncAbs(cat1, cat2)
    cat1 = Category('S/(S\NP)')
    cat2 = Category('(S[dcl]\NP)/NP')
    print "Forward composition"
    print fComp(cat1, cat2)
    # Forward crossing composition X/Y Y\Z -> X\Z
    cat1 = Category('(S[dcl]/NP)/S[em]')
    cat2 = Category('S[em]\NP')
    print "Forward crossing composition"
    print fxComp(cat1, cat2)
    # Backward composition Y\Z X\Y -> X\Z
    cat1 = Category('S[dcl]\NP')
    cat2 = Category('S[adj]\S[dcl]')
    print "Backward composition"
    print bComp(cat1, cat2)
    # Backward crossing composition: Y/Z X\Y -> X/Z    
    cat1 = Category('(S[pss]\NP)/PP')
    cat2 = Category('(S\NP)\(S\NP)')
    print "Backward crossing composition"
    print bxComp(cat1, cat2)
    # Generalised backward composition
    cat1 = Category('(S[dcl]\S[dcl])\NP')
    cat2 = Category('S\S')
    print "Generalised backward composition"
    print gbComp(cat1, cat2)
    # Generalised backward crossing composition: Y/$ X\Y -> X/$
    cat1 = Category('((S[dcl]\NP)/PP)/NP')
    cat2 = Category('(S\NP)\(S\NP)')
    print "Generalised backward crossing composition"
    print gbxComp(cat1, cat2)
    # Forward substitution: (X/Y)/Z Y/Z -> X/Z where Y is S*$
    cat1 = Category('((S[dcl]\NP)/(S[to]\NP))/NP')
    cat2 = Category('(S[to]\NP)/NP')
    print "Forward substitution"
    print fSub(cat1, cat2)
    # Forward crossing substitution: (X/Y)\Z Y\Z -> X\Z where Y is S*$
    cat1 = Category('(PP/(S[to]\NP))\NP')
    cat2 = Category('(S[to]\NP)\NP')
    print "Forward crossing substitution"
    print fxSub(cat1, cat2)
    # Backward substitution: Y\Z (X\Y)\Z -> X\Z where Y is S*$
    cat2 = Category('(((S\NP)\(S\NP))\((S\NP)\(S\NP)))\NP')
    print "Backward substitution"
    print bSub(cat1, cat2)
    # Backward crossing substitution: Y/Z (X\Y)/Z -> X/Z where Y is S*$
    cat1 = Category('(S\NP)/NP')
    cat2 = Category('((S\NP)\(S\NP))/NP')
    print "Backward crossing substitution"
    print bxSub(cat1, cat2)
    child = Category("((S[to]\NP)^NP)/NP")
    parent = Category("NP\NP")
    print "Generalised forward crossing type morph"
    print gfxtMorph(child, parent)
