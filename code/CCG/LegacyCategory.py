"""
CCG Category String
"""
import re
featStripRE = re.compile(r'\[\w+\]')
from copy import deepcopy as copy
import pickles

import Markedup

class AbstractCategory(object):

    def __ne__(self, otherCategory):
        """
        Apparently != doesn't call __eq__. Boo, hiss.
        """
        if not self == otherCategory:
            return True
        else:
            return False

    def __str__(self):
        return self.cat

    def __getitem__(self, index):
        return self.cat[index]

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self)

    
    def ref(self):
        ref = self
        while ref.unified:
            ref = ref.unified
        return ref



    def _stripBrackets(self, category):
        """
        Remove extraneous brackets
        """
        if not category:
            return category
        elif not category[0] == '(':
            return category
        depth = 0
        for char in category:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif depth == 0:
                return category    
        return category[1:-1]

    predicateRE = re.compile(r'\(*S(\[\w+\])?[/\\]?')
    def isPredicate(self):
        """
        Use a regular expression to provide a simple test for
        S/$ or S\$.
        """
        return bool(AbstractCategory.predicateRE.match(self.cat))

    def isNull(self):
        return False

    def heads(self):
        """
        Look up your lexical heads in the dictionary
        """
        return self.headRef().headGen()
        

    def headGen(self):
        for h in self._heads:
            yield h

    def addHead(self, head):
        if self.unified:
            self.ref().addHead(head)
        elif self.headShared:
            self.headRef().addHead(head)
        else:
            self._heads.append(head)

    def unify(self, other):
        """
        Set a reference to delegate head and feature requests to.
        This is pseudo-recursive, because the reference may pass the buck
        if it has already been unified with something. Must also be careful
        not to allow circular references. If self and other already delegate
        to the same place, do nothing
        """
        if self != other:
            return None
        selfRef = self.ref()
        otherRef = other.ref()
        # Prevent circular references by checking whether they already lead to
        # the same place
        if selfRef is otherRef:
            return True
        else:
            i = 0
            selfRef.headShare(otherRef)
            if self.argument:
                self.argument.unify(other.argument)
            if self.result is not self:
                self.result.unify(other.result)
            feature = selfRef.feature
            morph = selfRef.morph
            selfRef.unified = otherRef
            if feature:
                if feature != '[nb]' or otherRef == 'NP/N':
                    otherRef.feature = feature
            if morph:
                otherRef.morph = morph
            return True

    def headShare(self, other):
        selfRef = self.headRef()
        otherRef = other.headRef()
        if selfRef is otherRef:
            return None
        for head in selfRef.heads():
            otherRef.addHead(head)
        selfRef.headShared = otherRef

    def headRef(self):
        ref = self.ref()
        while ref.headShared:
            ref = ref.headShared
        return ref

    def strAsPiece(self):
        """
        String representation when the category is used as a piece of a larger category.
        This means the category must be bracketed if it is complex
        """
        if self.isComplex() and not self.morph and not self.feature:
            return '(%s)' % self
        else:
            return str(self)

    def _getMorph(self):
        if self.unified:
            return self.ref().morph
        else:
            return self._morph

    def _setMorph(self, newMorph):
        if self.unified:
            self.ref().morph = newMorph
        else:
            self._morph = newMorph

    morph = property(_getMorph, _setMorph)

    def _getHasMorph(self):
        if self.morph:
            return True
        elif '^' in str(self):
            return True
        else:
            return False


    hasMorph = property(_getHasMorph)
    

        
        

class ComplexCategory(AbstractCategory):
    def __init__(self, result, argument, slash, conj, idx = None, depType = '', morph = None):
        global parsedCats
        assert not result.conj
        assert not argument.conj
        self.result = result
        self.conj = conj
        self.unified = None
        self.headShared = None
        self.arguments = []
        self._heads = []
        self._feature = ''
        # Semantic role label, not coindexed
        self.roleLabel = ''
        if argument.conj:
            self.conj = True
            argument.conj = False
        self.argument = argument
        self.slash = slash
        self.cat = self._makeCat()
        if idx == None:
            pieces = parsedCats.get(self.cat)
            if pieces:
                result, argument, slash, conj, idx, depType = pieces
                self.idx = idx
                self.depType = depType
            else:
                self.idx = 0
                self.depType = ''
        else:
            self.idx = idx
            self.depType = depType
        
        self.goldDeps = []
        # Morph is the destination category if we have a form/function distinction -- Y in X^Y
        self.morph = morph
        self.coindex()

    def __eq__(self, otherCategory):
        """
        Recursively check equality of slash, result and argument
        """
        if not isinstance(otherCategory, AbstractCategory):
            if otherCategory and isinstance(otherCategory, str):
                try:
                    otherCategory = Category(otherCategory)
                except:
                    return str(self) == otherCategory
            else:
                return False
        if not otherCategory.isComplex():
            return False
        if not otherCategory.slash == self.slash:
            return False
        # Really shouldn't have feature support for complex
        # Fail on feature if it's there and doesnt match
#        selfFeat = self.feature
#        otherFeat = otherCategory.feature
#        if selfFeat and otherFeat and selfFeat != otherFeat:
#            return False
        if self.argument == otherCategory.argument and self.result == otherCategory.result:
            return True
        else:
            return False
        

    def coindex(self):
        global indexTable
        # Turned off coindexing for validation, as there's bug on file 137
        # What does turning this off break?? :( Head passing I think?
        # Nope, breaks features in validation
        self._getArgs()
        coindexed = indexTable.get(str(self).replace('[conj]', ''))
        if coindexed:
            self.coindexFromTable(coindexed)
        elif '_' in self.fullPrint():
            self.unifyCoindexed({self.idx: [self]})
        # Unify adjunct
        elif self.isAdjunct():
            self.argument.unify(self.result)
        # Check for type raise
        elif self.argument.isComplex() and isIdentical(self.argument.result, self.result):
            self.argument.result.unify(self.result)


    def _makeCat(self):
        resultStr = self.result.strAsPiece()
        argStr = self.argument.strAsPiece()
        label = '%s%s%s' % (resultStr, self.slash, argStr)
        if self.feature:
            label = '(%s)%s' % (label, self.feature)
        return label
                            
                
    def coindexFromTable(self, coindexed):
        for firstAddr, otherAddrs in coindexed:
            firstCat = self._followAddr(firstAddr)
            for otherAddr in otherAddrs:
                otherCat = self._followAddr(otherAddr)
                # Don't allow unification if features don't match.
                # Otherwise, when there's a mistake, we pass features before
                # We do anything. EG: (S/S)/(S[pt]
                # This is a coindex mistake, that would produce (S[pt]/S[pt])/S[pt]
                if str(firstCat) != str(otherCat):
                    firstCat.headShare(otherCat)
                elif not firstCat.unify(otherCat):
                    firstCat.headShare(otherCat)

    def _followAddr(self, address):
        reffed = self
        for item in address:
            if item == 0:
                reffed = reffed.result
            elif item == 1:
                reffed = reffed.argument
        return reffed


    


    def unifyCoindexed(self, idxDict):
        if self.idx != 0:
            cats = idxDict.setdefault(self.idx, [])
            for otherCat in cats:
                if str(self) == str(otherCat):
                    self.unify(otherCat)
                    break
                else:
                    self.headShare(otherCat)
            else:
                cats.append(self)
        self.argument.unifyCoindexed(idxDict)
        self.result.unifyCoindexed(idxDict)
        


    def innerResult(self):
        return self.result.innerResult()
            

    def _setFeat(self, feature):
        if self.unified:
            self.ref().feature = feature
        else:
            self._feature = feature

    def _getFeat(self):
        if self.unified:
            return self.ref().feature
        else:
            return self._feature

    feature = property(_getFeat, _setFeat)

    def isComplex(self):
        return True

    def isPunct(self):
        return False

    def isTypeRaise(self):
        if self.argument.isComplex() \
        and self.slash != self.argument.slash \
        and isIdentical(self.result, self.argument.result):
            return True
        else:
            return False

    auxRE = re.compile(r'\(S\[(\w+)\]\\NP\)/\(S\[(\w+)\]\\NP\)')
    def isAux(self):
        """
        loose definition of auxiliary
        """
        verbFeats = self.auxRE.match(self.cat)
        return bool(verbFeats)
    
    def isTrueAux(self):
        """
        This returns whether it's a proper auxiliary, excluding e.g. to
        """
        verbFeats = self.auxRE.match(self.cat)
        if not verbFeats:
            return False
        feat1, feat2 = verbFeats.groups()
        if feat1 == feat2:
            return False
        # This might still not be correct...
        auxFeats = ['dcl', 'b', 'pss', 'ng', 'pt']
        if feat1 in auxFeats and feat2 in auxFeats:
            return True
        else:
            return False

    def isAdjunct(self):
        # Should be identical and featureless, except for 'adj'
        if self.result.featLess() == str(self.result).replace('[adj]', '') == self.argument.featLess() == str(self.argument).replace('[adj]', ''):
            return True
        return False

    def adjunctResult(self):
        if self.isAdjunct():
            return True
        else:
            return self.result.adjunctResult()

    def dependencies(self):
        cat = self
        dependencies = []
        for i, arg in enumerate(self.arguments):
            for head in arg.heads():
                dependencies.append((head, i+1))
               # dependencies.append(self._makeDep(lexeme, head, i + 1))
        return dependencies

    def goldDependencies(self):
        dependencies = []
        for i, argDeps in enumerate(self.goldDeps):
            for head, depType in argDeps:
                dependencies.append((head, depType, i+1))
        return dependencies

    def _getArgs(self):
        args = list(self.result.arguments)
        args.append(self.argument)
        self.arguments = args

    def _makeDep(self, head, argument, argNum):
        return '%s %s %d' % (head, argument, argNum)

    def fullPrint(self, asPiece = False):
        if not asPiece and self.cat in catDict:
            cat = catDict[self.cat]
           # if self.conj:
           #      cat += '[conj]'
        else:
            resPrint = self.result.fullPrint(True)
            argPrint = self.argument.fullPrint(True)
            label = resPrint + self.slash + argPrint
            assert type(self.idx) == int
            if self.idx > 0:
                suffix = '_%d%s' % (self.idx, self.depType)
            else:
                suffix = ''
            if self.feature:
                label = '(%s)%s' % (label, self.feature)
            elif suffix:
                label = '(%s)' % label
            cat = label + suffix
        if self.morph:
            cat = '(%s)^%s' % (cat, self.morph.fullPrint(True))
        if asPiece and not suffix:
            cat = '(%s)' % cat
        if '[conj]' in cat:
            cat = cat.replace('[conj]', '')
            cat = cat + '[conj]'
        return cat
 

        

    def __str__(self):
        pieces = []
        if self.morph:
            pieces = ['(%s)' % self._makeCat()]
            pieces.append('^')
            pieces.append(self.morph.strAsPiece())
        else:
            pieces.append(self._makeCat())
        if self.conj:
            pieces.append('[conj]')
        cat = ''.join(pieces)
        return cat

    def morphLess(self, asPiece = False):
        resultStr = self.result.morphLess(True)
        argStr = self.argument.morphLess(True)
        if self.conj:
            conj = '[conj]'
        else:
            conj = ''
        if asPiece:
            openBrack = '('
            closeBrack = ')'
            conj = ''
        else:
            openBrack = ''
            closeBrack = ''
        return ''.join((openBrack, resultStr, self.slash, argStr, closeBrack, conj))

    def featLess(self, asPiece = False):
        resultStr = self.result.featLess(True)
        argStr = self.argument.featLess(True)
        if asPiece:
            openBrack = '('
            closeBrack = ')'
            conj = ''
        else:
            openBrack = ''
            closeBrack = ''
        return ''.join((openBrack, resultStr, self.slash, argStr, closeBrack))

    def deconstruct(self):
        """
        Generate the result and argument pairs
        """
        cat = self
        while cat.isComplex():
            yield (cat.result, cat.argument, cat.slash, cat.morph)
            cat = cat.result


        






class AtomicCategory(AbstractCategory):
    def __init__(self, label, idx, depType, morph = None):
        if label.endswith('[conj]'):
            self.conj = True
            label = label[:-6]
        else:
            self.conj = False
        self.result = self
        self.argument = None
        self.arguments = []
        self.idx = idx
        self._heads = []
        self._feat = ''
        # Semantic role label, not coindexed
        self.roleLabel = ''
        self.unified = None
        self.headShared = None
        self.depType = depType
        if label[-1] == ']':
            try:
                label, feature = label.split('[')
            except:
                print label
                raise StandardError
            self.feature = '[' + feature
        self.cat = label
        self.slash = ''
        self.goldDeps = []
        # Morph is the destination category if we have a form/function distinction -- Y in X^Y
        self.morph = morph

    def __eq__(self, otherCategory):
        """
        Check whether the featureless version of the
        other category matches self. Note that this means
        equality is not commutative
        """
        if not isinstance(otherCategory, AbstractCategory):
            if otherCategory and isinstance(otherCategory, str):
                otherCategory = Category(otherCategory)
            else:
                return False
        if otherCategory.isComplex():
            return False
        # Fail on feature if it's there and doesnt match
        selfFeat = self.feature
        otherFeat = otherCategory.feature
        # Does S[dcl]/S[dcl] unify with S? But then what about
        # composing (S[b]\NP)/NP (S\NP)\(S\NP)?
        if selfFeat and otherFeat and selfFeat != otherFeat:
            return False
        # Fail on morph if it's there and doesn't match
        selfMorph = self.morph
        otherMorph = otherCategory.morph
        if selfMorph and otherMorph and selfMorph != otherMorph:
            return False
        if self.cat == otherCategory.cat:
            return True
        else:
            return False
        

    def unifyCoindexed(self, idxDict):
        if self.idx != 0:
            cats = idxDict.setdefault(self.idx, [])
            for cat in cats:
                if str(self) == str(cat):
                    self.unify(cat)
                    break
                else:
                    self.headShare(cat)
            else:
                cats.append(self)
                
            
    

    def _setFeat(self, feature):
        if self.unified:
            self.ref().feature = feature
        else:
            self._feat = feature

    def _getFeat(self):
        if self.unified:
            return self.ref().feature
        else:
            return self._feat

    feature = property(_getFeat, _setFeat)
            
    def isComplex(self):
        return False

    def isAdjunct(self):
        return False

    def isTypeRaise(self):
        return False

    def adjunctResult(self):
        return False

    def innerResult(self):
        return self

    def isAux(self):
        return False

    def isTrueAux(self):
        return False

    def isPredicate(self):
        if self.cat == 'S':
            return True
        else:
            return False


    def isPunct(self):
        return bool(self.cat in punct)

    def fullPrint(self, asPiece = False):
        pieces = [self.cat, self.feature]
        if self.idx != -1:
            pieces.append('_%d%s' % (self.idx, self.depType))
        cat = ''.join(pieces)
        if self.morph:
            cat = '%s^%s' % (cat, self.morph.fullPrint(True))
            if asPiece:
                cat = '(%s)' % cat
        if self.conj:
            cat += '[conj]'
        return cat

    def __str__(self):
        pieces = [self.cat, self.feature]
        cat = ''.join(pieces)
        if self.morph:
            cat = '%s^%s' % (cat, self.morph.strAsPiece())
        if self.conj:
            cat += '[conj]'
        return cat

    def morphLess(self, asPiece = False):
        pieces = [self.cat, self.feature]
        if self.conj and not asPiece:
            pieces.append('[conj]')
        cat = ''.join(pieces)
        return cat

    def featLess(self, asPiece = False):
        return str(self.cat)

    def dependencies(self):
        return []

    def goldDependencies(self):
        return []

    def deconstruct(self):
        yield (self, None, None, self.morph)


def Category(label):
    global catDict, parsedCats
    if checkCat:
        origLabel = str(label)
        # Hack for the stupid broken category
        if origLabel.endswith('/'):
            origLabel = origLabel[1:-2]
    if isinstance(label, AbstractCategory):
        label = str(label)
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
    feature = ''
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
            feature = ''
            cats.append(_process(cat, idx, depType))
            if element != '^':
                cats.append(element)
            atomicChars = []
            cat = None
            collectIdx = False
            collectDep = False
            idx = []
            depType = ''
        elif element == '>' and cat:
            feature = ''.join(atomicChars) + '>'
            atomicChars = []
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
        if feature:
            cats[0].feature = feature
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
        cat = ComplexCategory(result, argument, slash, conj, idx, depType)
        if feature:
            cat.argument.feature = feature
        
        return cat
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

def makeAdjunct(category, catSlash, forceDep = False):
    global VP
    new = copy(category)
    if not new.isComplex():
        x = new
    if forceDep and new.isAdjunct():
        x = new
    elif new == r'S\NP':
        x = new
    elif new.innerResult() != 'S':
        x = new
    else:
        lastCat = new
        #Select either: an adjunct, S\NP, or an atom
        for result, argument, slash, morph in new.deconstruct():
            # Ensure the slash directions work
            # If the functor's to the left, cannot cross-compose into a backslash -- unless not complexAdj!s
            if catSlash == '/' and slash == '\\':
                continue
            # Don't back-cross compose into non-S
            if catSlash == '\\' and slash == '/' and result.innerResult() != 'S':
                continue
            if result == r'S\NP':
                x = result
                break
            elif not result.isComplex():
                x = result
                break
            elif result.isAdjunct():
                x = result
                break
            # In case the slashes don't work out for a while (ie cross composition), store the last valid
            # place to compose into, and its arg set
            lastCat = result
        else:
            x = lastCat
    # Don't remove features if it's a "fake" adjunct like S[dcl]/S[ng]
    if not (x.result == x.argument) and not x.isAdjunct():
        x = copy(x)
        _removeFeatures(x)
    newFunctor = ComplexCategory(x, x, catSlash, False)
    return newFunctor

def _removeFeatures(cat):
    if cat.isComplex():
        cat.morph = None
        for result, argument, slash, morph in cat.deconstruct():
            _removeFeatures(result)
            _removeFeatures(argument)
    else:
        cat.feature = ''
        cat.morph = None



                


def testAdjunct(forceDep):
    cats, index = Markedup.getEntries('~/Data/markedupFiles/markedup_v4.2')
    for category in index.keys():
        category = Category(category)
        for slash in ['/', '\\']:
            adjunct = makeAdjunct(category, slash, forceDep)
            print "Category: %s" % category
            print slash
            print "Adjunct: %s" % adjunct
            if slash == '/':
                combined = validate(adjunct, category, category, True)
            else:
                combined = validate(category, adjunct, category, True)
            if not combined:
                print 'Fail'
            else:
                print 'Pass'



def validate(origLeft, origRight, label):
    """
    See which (if any) rules can generate the label from the two
    other categories
    """
    global functions, unaryFunctions, unaryRules, binaryRules, ruleFreq
    def new():
        return copy(origLeft), copy(origRight)
    if origRight == None:
        if unaryRules.get(str(origLeft), {}).get(str(label), 0):
            return True
        elif label == 'TOP':
            return True
        else:
            for function in unaryFunctions:
                guess = function(origLeft, label)
                # Unary rules are 'open ended', so compare against the parent within the rule
                if guess:
                    return True
                left, right = new()
            return False
   # bKey = (origLeft.morphLess(), origRight.morphLess())
    bKey = (str(origLeft), str(origRight))
    if binaryRules.get(bKey, {}).get(str(label), 0) > ruleFreq:
        return True
    labelStr = str(label)
    left, right = new()
    for function in functions:
        guess = function(left, right)
        # Hack to never produce nb feat
        guessStr = str(guess).replace('[nb]', '')
        if guessStr == labelStr.replace('[nb]', ''):
            return True
        if guess != None:
            left, right = new()
    return False

def combine(origLeft, origRight):
    """
    Get the set of labels that could be applied to the two cats
    """
    global unaryRules
    if not origRight:
        return unaryRules.get(str(origLeft), {})
    cats = {}
    def new():
        return copy(origLeft), copy(origRight)
    left, right = new()
    for function in Rules.tightFunctions:
        newCat = function(left, right)
        if newCat:
            cats[newCat] = True
            left, right = new()
    return cats

def getRule(origLeft, origRight, answer = None):
    def new():
        return Category(str(origLeft)), Category(str(origRight))
    answers = {}
    seenRight = False
    for function in Rules.tightFunctions:
        left, right = new()
        combined = function(left, right)
        if combined:
            if answer and isIdentical(combined, answer):
                seenRight = True
            answers[function] = combined
    return seenRight, answers

def combineChildren(parent, origLeft, origRight):
    if not origRight:
        newCat = parent.unify(origLeft)
        if newCat:
            return newCat
        typeRaised = parent
        while typeRaised != origLeft:
            if typeRaised.isComplex():
                typeRaised = typeRaised.argument
            else:
                break
        # If we can't unify, we at least need to head share.
        newCat = typeRaised.unify(origLeft)
        if not newCat:
            origLeft.headShare(parent)
            return parent
        else:
            return newCat
    def new():
        return copy(origLeft), copy(origRight)
    left, right = new()
    assert parent
    for function in Rules.tightFunctions:
        newCat = function(left, right)
        if str(newCat) == str(parent):
            newerCat = function(origLeft, origRight)
            newerCat.unify(parent)
            return newerCat
        elif newCat:
            left, right = new()
    return False

def setRuleFreq(newFreq):
    global ruleFreq
    ruleFreq = newFreq


def isIdentical(cat1, cat2):
    """
    Do a string based comparison of the categories
    """
    if str(cat1) == str(cat2):
        return True
    else:
        return False


def addArgs(result, args):
    """
    Build the category that results from progressively adding the
    given arguments
    """
    if isinstance(result, str):
        result = Category(result)
    else:
        result = copy(result)
    for arg, slash, morph in args:
        result = ComplexCategory(result, copy(arg), slash, False)
        result.morph = copy(morph)
    return result

def addArg(result, arg, slash, morph=False):
    """
    Add a single argument to the result
    """
    if isinstance(arg, str):
        arg = Category(arg)
    return addArgs(result, [(arg, slash, morph)])

def debug():
    print ruleFreq

def testHatParse():
    """
    Permutations are:
    Atom hat
    Result hat
    Argument hat
    Cat hat

    Where hat can be any of above. So sixteen permutations.
    """
    atomicHats = [
        'A',
        'R/H',
        'A^H',
        'R^H/A',
        'R/A^H',
        '(R/A)^H'
    ]
    # Test atomic hats
    for cat in atomicHats:
        print 'String: %s' % cat
        parsed = Category(cat)
        print 'Parsed: %s' % parsed
        if str(parsed) != cat:
            print "Mismatch!"
    complexHats = [
        'R/(HR/HA)',
        'A^(HR/HA)',
        'R^(HR/HA)/A',
        'R/A^(HR/HA)',
        '(R/A)^(HR/HA)'
    ]
    for cat in complexHats:
        print 'String: %s' % cat
        parsed = Category(cat)
        print 'Parsed: %s' % parsed
        if str(parsed) != cat:
            print "Mismatch!"
    hatAtomHats = [
        'R/H^I',
        'A^H^I',
        'R^H^I/A',
        'R/A^H^I',
        '(R/A)^H^I'
    ]
    for cat in hatAtomHats:
        print 'String: %s' % cat
        parsed = Category(cat)
        print 'Parsed: %s' % parsed
        if str(parsed) != cat:
            print "Mismatch!"
    hatComplexHats = [
        'R/(HR/HA)^I',
        'A^(HR/HA)^I',
        'R^(HR/HA)^I/A',
        'R/A^(HR/HA)^I',
        '(R/A)^(HR/HA)^I',
        'R/(HR^I/HA)',
        'A^(HR/HA^I)^I',
        'R^(HR^(IR/IA)/HA)^I/A',
        'R/A^(HR/HA^(IR/IA))^I',
        '(R/A)^(HR/HA)^I']
    observedCats = ['(S[adj]\\NP)^((S[pss]\\NP)^(NP\\NP)\\(S[adj]\\NP))',
                    '(S[adj]\\NP)^((S[pss]\\NP)^(NP\\NP)\\(S[adj]\\NP))/NP']
    hatComplexHats.extend(observedCats)
    for cat in hatComplexHats:
        print 'String: %s' % cat
        parsed = Category(cat)
        print 'Parsed: %s' % parsed
        if str(parsed) != cat:
            print "Mismatch!"

# Tells Category whether to check that categories are exactly as entered
checkCat = True
ruleFreq = 0
catDict = pickles.load('ccgbankAnnot')
catDict['S/(S\NP)'] = 'S_1/(S_1\NP)'
parsedCats = pickles.load('parsedCats')
parsedCats.pop(r'(S[wq]/(S[q]/N))/N')
parsedCats.pop(r'(NP/(S[dcl]\N))/N')
parsedCats.pop(r'(NP/(S[dcl]/N))/N')
parsedCats.pop(r'(S[qem]/(S[dcl]/N))/N')
parsedCats.pop(r'(S[qem]/(S[dcl]\N))/N')
parsedCats.pop(r'((NP\NP)/(S[dcl]\N))/N')
indexTable = pickles.load('indexTable')
# Some category constants for comparison
NP = Category('NP')
N = Category('N')
S = Category('S')
PP = Category('PP')
VP = Category('S\NP')
conj = Category('conj')
from Rules import *
import Rules
punct = {
        ',': True,
        ':': True,
        '.': True,
        ';': True,
        'RRB': True,
        'LRB': True,
        '-RRB-': True,
        '-LRB-': True,
        'LQU': True,
        'RQU': True
    }

if __name__ == '__main__':
    import sys
    if 1:
        print Category(r'(S[b]\NP)/NP').result
        print Category(r'NP[nb]/N')
        #parsed = _parseLabel(r'((S[b]\NP)/(S[to]\NP)[A1])/NP')
        #parsed = _parseLabel(r'(NP/(S[to]\NP)[A1])/NP')
        #print parsed
        #print _handleParsed(parsed)
    sys.exit(1)
    catsAndRules = [
('N/N[num]', 'N', 'N', 'Forward application', fApp),
('S[pss]\NP', '(S\NP)\(S\NP)', 'S[pss]\NP', "Backward application", bApp),
('N/N', 'N/N', 'N/N', "Forward composition", fComp),
('NP', ',', 'NP', "Left punct absorption", lPuncAbs),
(',', 'NP', 'NP', "Right punct absorption", rPuncAbs),
('conj', 'NP', 'NP[conj]', "Left conj absorption", lConjApp),
('NP', 'conj', 'NP[conj]', "Right conj absorption", rConjApp),
('NP[conj]', 'NP', 'NP', "Left conjunction", lConj),
('S[adj]\NP', 'S[adj]\NP[conj]', 'S[adj]\NP', "Right conjunction", rConj),
('NP[nb]/N', 'N', 'NP', "Determiner application", fApp),
('S[dcl]/(S[dcl]\NP)', '(S[dcl]\NP)/NP', 'S[dcl]/NP', "Forward composition", fComp),
('S[dcl]\NP', 'S[adj]\S[dcl]', 'S[adj]\NP', "Backward composition", bComp),
('(S[pss]\NP)/PP', '(S\NP)\(S\NP)', '(S[pss]\NP)/PP', "Backward crossing composition", bxComp),
('(S[dcl]\S[dcl])\NP', 'S\S', '(S[dcl]\S[dcl])\NP', "Generalised backward composition", gbComp),
('((S[dcl]\NP)/PP)/NP', '(S\NP)\(S\NP)', '((S[dcl]\NP)/PP)/NP', "Generalised backward crossing composition", gbxComp)
    ]
    for cat1, cat2, answer, desc, rule in catsAndRules:
        cat1 = Category(cat1)
        cat2 = Category(cat2)
        answer = Category(answer)
        isTrue, answers = getRule(cat1, cat2, answer)
        if not isTrue:
            print desc
            print cat1
            print cat2
            print "Produces: %s" % answer
            for rule, guess in answers.items():
                print "Guessed %s via %s" % (guess, rule)
                print isIdentical(guess, answer)
            print len(answers)
            if not answers:
                print "No answers"
            raise StandardError
    else:
        print "Rules applied successfully!"
        sys.exit(1)
