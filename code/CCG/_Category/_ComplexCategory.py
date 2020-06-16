import re

from _AbstractCategory import AbstractCategory
from _parse import catDict
from utils import isIdentical

class ComplexCategory(AbstractCategory):
    def __init__(self, result, argument, slash, conj, idx = None, depType = '', morph = None):
        global parsedCats
        assert not result.conj
        assert not argument.conj
        self.result = result
        self.conj = conj
        if argument.conj:
            self.conj = True
            argument.conj = False
        self.argument = argument
        self.slash = slash
        self.cat = self._makeCat()
        # Morph is the destination category if we have a form/function distinction -- Y in X^Y
        self.morph = morph
        self.goldDeps = []
#        if idx == None:
#            pieces = parsedCats.get(self.cat)
#            if pieces:
#                result, argument, slash, conj, idx, depType = pieces
#                self.idx = idx
#                self.depType = depType
#            else:
#                self.idx = 0
#                self.depType = ''
#        else:
#            self.idx = idx
#            self.depType = depType
#        self.unified = None
#        self.headShared = None
##        self.arguments = []
##        self._heads = []
#        self.coindex()

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
        if self.argument == otherCategory.argument and self.result == otherCategory.result:
            return True
        else:
            return False
        




    def _makeCat(self):
        resultStr = self.result.strAsPiece()
        argStr = self.argument.strAsPiece()
        return '%s%s%s' % (resultStr, self.slash, argStr)



    def innerResult(self):
        return self.result.innerResult()
            



    def _getFeat(self):
        return ''
        if self.unified:
            return self.ref().feature()
        else:
            return self.result.feature()

    feature = property(_getFeat)

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


    def __str__(self):
        pieces = []
        if self.morph:
            pieces = ['(%s)' % self.cat]
            pieces.append('^')
            pieces.append(self.morph.strAsPiece())
        else:
            pieces.append(self.cat)
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


##    def fullPrint(self, asPiece = False):
##        if not asPiece and self.cat in catDict:
##            cat = catDict[self.cat]
##           # if self.conj:
##           #      cat += '[conj]'
##        else:
##            resPrint = self.result.fullPrint(True)
##            argPrint = self.argument.fullPrint(True)
##            label = resPrint + self.slash + argPrint
##            assert type(self.idx) == int
##            if self.idx > 0:
##                suffix = '_%d%s' % (self.idx, self.depType)
##            else:
##                suffix = ''
##            if suffix:
##                label = '(%s)' % label
##            # Is conj necessary in fullPrint? How could a lexical category need conj?
##           # if self.conj:
##           #     conj = '[conj]'
##           # else:
##           #     conj = ''
##           # cat = label + suffix + conj
##            cat = label + suffix
##        if self.morph:
##            cat = '(%s)^%s' % (cat, self.morph.fullPrint(True))
##        if asPiece:
##            cat = '(%s)' % cat
##        if '[conj]' in cat:
##            cat = cat.replace('[conj]', '')
##            cat = cat + '[conj]'
##        return cat
 

##    def coindex(self):
##        global indexTable
##        # Turned off coindexing for validation, as there's bug on file 137
##        # What does turning this off break?? :( Head passing I think?
##        # Nope, breaks features in validation
##        self._getArgs()
##        coindexed = indexTable.get(str(self).replace('[conj]', ''))
##        if coindexed:
##            self.coindexFromTable(coindexed)
##        elif '_' in self.fullPrint():
##            self.unifyCoindexed({self.idx: [self]})
##        # Unify adjunct
##        elif self.isAdjunct():
##            self.argument.unify(self.result)
##        # Check for type raise
##        elif self.argument.isComplex() and isIdentical(self.argument.result, self.result):
##            self.argument.result.unify(self.result)
                
##    def coindexFromTable(self, coindexed):
##        for firstAddr, otherAddrs in coindexed:
##            firstCat = self._followAddr(firstAddr)
##            for otherAddr in otherAddrs:
##                otherCat = self._followAddr(otherAddr)
##                # Don't allow unification if features don't match.
##                # Otherwise, when there's a mistake, we pass features before
##                # We do anything. EG: (S/S)/(S[pt]
##                # This is a coindex mistake, that would produce (S[pt]/S[pt])/S[pt]
##                if str(firstCat) != str(otherCat):
##                    firstCat.headShare(otherCat)
##                elif not firstCat.unify(otherCat):
##                    firstCat.headShare(otherCat)

##    def _followAddr(self, address):
##        reffed = self
##        for item in address:
##            if item == 0:
##                reffed = reffed.result
##            elif item == 1:
##                reffed = reffed.argument
##        return reffed
##
##
##    
##
##
##    def unifyCoindexed(self, idxDict):
##        if self.idx != 0:
##            cats = idxDict.setdefault(self.idx, [])
##            for otherCat in cats:
##                if str(self) == str(otherCat):
##                    self.unify(otherCat)
##                    break
##                else:
##                    self.headShare(otherCat)
##            else:
##                cats.append(self)
##        self.argument.unifyCoindexed(idxDict)
##        self.result.unifyCoindexed(idxDict)
        
#    def _setFeat(self, feature):
#        if self.unified:
#            self.ref().addFeature(feature)
#        else:
#            self.result.addFeature(feature)     


from _parse import parsedCats, indexTable
