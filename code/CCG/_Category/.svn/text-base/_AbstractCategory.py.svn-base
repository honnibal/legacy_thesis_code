import re

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

    
##    def ref(self):
##        ref = self
##        while ref.unified:
##            ref = ref.unified
##        return ref



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

##    def heads(self):
##        """
##        Look up your lexical heads in the dictionary
##        """
##        return self.headRef().headGen()
        

##    def headGen(self):
##        for h in self._heads:
##            yield h

##    def addHead(self, head):
##        if self.unified:
##            self.ref().addHead(head)
##        elif self.headShared:
##            self.headRef().addHead(head)
##        else:
##            self._heads.append(head)

##    def unify(self, other):
##        """
##        Set a reference to delegate head and feature requests to.
##        This is pseudo-recursive, because the reference may pass the buck
##        if it has already been unified with something. Must also be careful
##        not to allow circular references. If self and other already delegate
##        to the same place, do nothing
##        """
##        if self != other:
##            return None
##        selfRef = self.ref()
##        otherRef = other.ref()
##        # Prevent circular references by checking whether they already lead to
##        # the same place
##        if selfRef is otherRef:
##            return True
##        else:
##            i = 0
##            selfRef.headShare(otherRef)
##            if self.argument:
##                self.argument.unify(other.argument)
##            if self.result is not self:
##                self.result.unify(other.result)
##            feature = selfRef.feature
##            morph = selfRef.morph
##            selfRef.unified = otherRef
##            if feature:
##                if feature != '[nb]' or otherRef == 'NP/N':
##                    otherRef.feature = feature
##            if morph:
##                otherRef.morph = morph
##            return True

##    def headShare(self, other):
##        selfRef = self.headRef()
##        otherRef = other.headRef()
##        if selfRef is otherRef:
##            return None
##        for head in selfRef.heads():
##            otherRef.addHead(head)
##        selfRef.headShared = otherRef
##
##    def headRef(self):
##        ref = self.ref()
##        while ref.headShared:
##            ref = ref.headShared
##        return ref

    def strAsPiece(self):
        """
        String representation when the category is used as a piece of a larger category.
        This means the category must be bracketed if it is complex
        """
        if self.isComplex() and not self.morph:
            return '(%s)' % self
        else:
            return str(self)

    def _getMorph(self):
        return self._morph
##        if self.unified:
##            return self.ref().morph
##        else:
##            return self._morph

    def _setMorph(self, newMorph):
        self._morph = newMorph
##        if self.unified:
##            self.ref().morph = newMorph
##        else:
##            self._morph = newMorph

##    morph = property(_getMorph, _setMorph)
##
##    def _getHasMorph(self):
##        if self.morph:
##            return True
##        elif '^' in str(self):
##            return True
##        else:
##            return False
##
##
##    hasMorph = property(_getHasMorph)
