import re

import pickles

checkCat = False
catDict = {}
#catDict = pickles.load('ccgbankAnnot')
#catDict['S/(S\NP)'] = 'S_1/(S_1\NP)'
parsedCats = pickles.load('parsedCats')
parsedCats.pop(r'(S[wq]/(S[q]/N))/N')
parsedCats.pop(r'(NP/(S[dcl]\N))/N')
parsedCats.pop(r'(NP/(S[dcl]/N))/N')
parsedCats.pop(r'(S[qem]/(S[dcl]/N))/N')
parsedCats.pop(r'(S[qem]/(S[dcl]\N))/N')
parsedCats.pop(r'((NP\NP)/(S[dcl]\N))/N')
indexTable = pickles.load('indexTable')

# These are below to avoid circular import problems
from _AbstractCategory import AbstractCategory
from _AtomicCategory import AtomicCategory
from _ComplexCategory import ComplexCategory

def Category(label):
    global catDict, parsedCats
    if checkCat:
        origLabel = str(label)
        # Hack for the stupid broken category
        if origLabel.endswith('/'):
            origLabel = origLabel[1:-2]
    if isinstance(label, AbstractCategory):
        return copy(label)
    # Take conj off and return it later so we dont have to store separate conj
    # MU entries
    if '[conj]' in label:
        label = label.replace('[conj]', '')
        hasConj = True
    else:
        hasConj = False
    if label in parsedCats:
        pieces = parsedCats[label]
        if len(pieces) == 6:
            result, argument, slash, conj, idx, depType = pieces
            result = Category(result)
            argument = Category(argument)
            cat = ComplexCategory(result, argument, slash, hasConj, idx, depType)
            if checkCat:
                if str(origLabel) != str(cat):
                    print origLabel
                    print cat
                    raise StandardError
            return cat
        else:
            label, idx, depType = pieces
            cat = AtomicCategory(label, idx, depType)
            cat.conj = hasConj
            if checkCat:
                assert str(origLabel) == str(cat)
            return cat
    # Support Clark and Curran style labels
    if '{' in label:
        return _handleMarkedup(label)
    if label in catDict:
        catLabel = catDict[label]
        if catLabel != label:
            cat = Category(catLabel)
            cat.conj = hasConj
            if checkCat:
                assert str(origLabel) == str(cat)
            return cat
    
    else:
        raise StandardError
        try:
            parsed = _parseLabel(label)
            cat = _handleParsed(parsed)
            cat.conj = hasConj
            # Can't check here easily because it comes out looking different
#            if checkCat:
#                assert str(origLabel) == str(cat.fullPrint())
            return cat
        except:
            print origLabel
            raise




def _handleParsed(parsed):
    atomicChars = []
    idx = []
    depType = ''
    collectIdx = False
    collectDep = False
    cats = []
    cat = None
    for element in parsed:
        if type(element) == list:
            cat = element
            collectIdx = False
            collectDep = False
            idx = []
            depType = ''
        elif element in ['/', '\\', '^']:
            if atomicChars:
                assert not cat
                cat = ''.join(atomicChars)
            cats.append(_process(cat, idx, depType))
            if element != '^':
                cats.append(element)
            atomicChars = []
            cat = None
            collectIdx = False
            collectDep = False
            idx = []
            depType = ''
        elif element == '_':
            collectIdx = True
        elif element == ':' and collectIdx:
            collectIdx = False
            collectDep = True
        elif collectIdx:
            idx.append(element)
        elif collectDep:
            depType = ':' + element
        else:
            atomicChars.append(element)
    if ''.join(atomicChars) == '[conj]':
        conj = True
        atomicChars = []
    else:
        conj = False
    if atomicChars:
        assert not cat
        cat = ''.join(atomicChars)
    cats.append(_process(cat, idx, depType))
    idx = []
    depType = ''
    if len(cats) == 1:
        return cats[0]
    elif len(cats) == 2:
        origin = cats[0]
        dest = cats[1]
        origin.morph = dest
        return origin
    elif cats:
        if idx:
            idx = int(''.join(idx))
        else:
            idx = -1
        if len(cats) == 4:
            result, resMorph, slash, argument = cats
            result.morph = resMorph
        else:
            result, slash, argument = cats
        return ComplexCategory(result, argument, slash, conj, idx, depType)
    else:
        print parsed
        raise StandardError


def _process(cat, idx, depType):
    if idx:
        idx = int(''.join(idx))
    else:
        idx = -1
    if type(cat) == list:
        cat = _handleParsed(cat)
        cat.idx = idx
        cat.depType = depType
    else:
        cat = AtomicCategory(cat, idx, depType)
    return cat
                

        

def _parseLabel(label):
    topCat = [[]]
    currentCat = topCat[-1]
    stack = [currentCat]
    depth = 0
    morphDepths = []
    for char in label:
        if char == '(':
            currentCat.append([])
            currentCat = currentCat[-1]
            stack.append(currentCat)
            if morphDepths:
                morphDepths[-1] += 1
        elif char == ')':
            stack.pop(-1)
            currentCat = stack[-1]
            if morphDepths:
                morphDepths[-1] -= 1
                if morphDepths[-1] == 0:
                    morphDepths.pop()
        elif char == '^':
            # Insert a bracket inside the current category, and move the hatted
            # material into it
            hatted = []
            while currentCat and currentCat[-1] not in ['^', '/', '\\']:
                hatted.insert(0, currentCat.pop())
            hatted.append(char)
            currentCat.append(hatted)
            stack.append(hatted)
            currentCat = hatted
            morphDepths.append(0)
        elif morphDepths and morphDepths[-1] == 0 and char in ['/', '\\']:
            stack.pop(-1)
            currentCat = stack[-1]
            currentCat.append(char)
            morphDepths.pop()
        else:
            currentCat.append(char)
       # print topCat
    while len(topCat) == 1 and type(topCat[0]) == list:
        topCat = topCat[0]
    return topCat

_argRE = re.compile(r'<\d+>')
_indexRE = re.compile(r'{\w}')
def _handleMarkedup(label):
    """
    Handle markedup style annotation by simply translating it into the
    CCGbank style and passing it to Category
    """
    global catDict, parsedCats
    # For now, don't support argument annotation
    label = _argRE.sub('', label)
    # If category is known in CCGbank version, ignore the mark up
    bare = _indexRE.sub('', label)
    # Remove brackets (which should always be there for markedup style,
    # if not atomic)
    if bare.startswith('('):
        bare = bare[1:-1]
    if bare in catDict or bare in parsedCats:
        return Category(bare)
    # If the category is novel, then we want to translate the mark up
    headIndices = [('{_}', ''), ('{Y}', '_1'), ('{Z}', '_2'), ('{W}', '_3'), ('{V}', '_4'), ('{U}', '_5'),
                   ('{T}', '_6'), ('{S}', '_7')]
    for old, new in headIndices:
        label = label.replace(old, new)
    parsed = _parseLabel(label)
    handled = _handleParsed(parsed)
    return handled




if __name__ == '__main__':
    cat = Category(r'S[dcl]\NP')
