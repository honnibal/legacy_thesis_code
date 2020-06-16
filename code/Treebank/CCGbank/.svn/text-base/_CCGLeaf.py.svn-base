from Treebank.Nodes import Leaf
from _CCGNode import CCGNode
import CCG

class CCGLeaf(Leaf, CCGNode):
    def __init__(self, **kwargs):
        self.text = kwargs.pop('text')
        self.pos = kwargs.pop('pos')
        self.parg = kwargs.pop('parg')
        self.wordID = kwargs.pop('wordID')
        CCGNode.__init__(self, headIdx=0, **kwargs)
        
    def sibling(self):
        return None

    def validate(self):
        return True

    def isAdjunct(self):
        return False

    
    def isPunct(self):
        return bool(self.label in CCG.punct)

    def changeLabel(self, newLabel):
        """
        Change predicate-argument category
        """
        oldLabel = self.parg
        newLabel = CCG.Category(newLabel)
        newLabel.goldDeps = oldLabel.goldDeps
        for head in oldLabel.heads():
            newLabel.addHead(head)
        self.parg = newLabel

    def head(self):
        return self

    def heads(self):
        return [self]

    def _getStag(self):
        return self.parent().label

    stag = property(_getStag)
