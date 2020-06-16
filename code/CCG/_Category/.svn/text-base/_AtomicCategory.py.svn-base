from _AbstractCategory import AbstractCategory

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
#        self._heads = []
#        self._feat = ''
#        self.unified = None
#        self.headShared = None
        self.depType = depType
        if label[-1] == ']':
            try:
                label, feature = label.split('[')
            except:
                print label
                raise StandardError
            self.feature = '[' + feature
        else:
            self.feature = ''
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
        

##    def unifyCoindexed(self, idxDict):
##        if self.idx != 0:
##            cats = idxDict.setdefault(self.idx, [])
##            for cat in cats:
##                if str(self) == str(cat):
##                    self.unify(cat)
##                    break
##                else:
##                    self.headShare(cat)
##            else:
##                cats.append(self)
                
##            
##    
##
##    def _setFeat(self, feature):
##        if self.unified:
##            self.ref().feature = feature
##        else:
##            self._feat = feature
##
##    def _getFeat(self):
##        if self.unified:
##            return self.ref().feature
##        else:
##            return self._feat
##
##    feature = property(_getFeat, _setFeat)
            
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

    def isPredicate(self):
        if self.cat == 'S':
            return True
        else:
            return False


    def isPunct(self):
        return bool(self.cat in punct)

##    def fullPrint(self, asPiece = False):
##        pieces = [self.cat, self.feature]
##        if self.idx != -1:
##            pieces.append('_%d%s' % (self.idx, self.depType))
##        cat = ''.join(pieces)
##        if self.morph:
##            cat = '%s^%s' % (cat, self.morph.fullPrint(True))
##            if asPiece:
##                cat = '(%s)' % cat
##        if self.conj:
##            cat += '[conj]'
##        return cat

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
