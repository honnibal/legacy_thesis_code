import sys

from _Production import Production
import CCG
from Treebank.Nodes import Node

class CCGNode(Node):
    def __init__(self, **kwargs):
        self.headIdx = kwargs.pop('headIdx')
        label = kwargs.pop('label')
        Node.__init__(self, label)
        
    def isProduction(self, **kwargs):
        """
        Check whether the node matches a given production, by checking
        its label, and some combination of the labels of its sibling,
        parent, and children
        """
        # Do this first for speed
        selfType = kwargs.pop('selfType')
        assert not '^' in selfType
        if not CCG.isIdentical(self.label.morphLess(), selfType):
            return False
        for nodeType, specified in kwargs.items():
            assert not '^' in specified
            if nodeType == 'parent':
                node = self.parent()
            elif nodeType == 'sibling':
                node = self.sibling()
            elif nodeType == 'left':
                if self.length() < 1:
                    return False
                node = self.child(0)
            elif nodeType == 'right':
                if self.length() < 2:
                    return False
                node = self.child(1)
            else:
                print nodeType
                raise StandardError
            if not node:
                return False
            try:
                label = node.label.morphLess()
            except AttributeError:
                label = CCG.Category(node.label).morphLess()
            if not CCG.isIdentical(label, specified):
                return False
        return True
            
    
    def changeLabel(self, newLabel):
        """
        Replace the node's category with a new one, propagating the changes
        as appropriate. The propagation code is controlled by Production,
        using logic roughly documented in my thesis.
        """
        if CCG.isIdentical(self.label, newLabel):
            return None
        #if CCG.isIdentical(newLabel, 'NP[nb]/N'):
        #    newLabel = CCG.Category('NP/N')
        c0 = self.child(0)
        if c0.isLeaf():
            self.label = newLabel
            c0.changeLabel(newLabel)
            return None
        if self.length() == 2:
            c1 = self.child(1)
            production = Production(c0.label, c1.label, self.label)
        elif self.isUnary():
            if self.isProduction(selfType=CCG.NP, left=CCG.N):
                # Don't produce unary rules like N --> S/S
                # Instead, create a new NP node and place it under self
                # This will make a S/S --> NP --> N chain
                # The exception is when we're adding arguments to NP.
                # Then what we want to do is add the arguments to N
                if newLabel.innerResult() == 'NP' and not newLabel.isAdjunct():
                    if not newLabel.isComplex():
                        nLabel = CCG.Category('N')
                    else:
                        args = [(a, s, h) for (r, a, s, h) in
                            newLabel.deconstruct()]
                        nLabel = CCG.addArgs(CCG.Category('N'), args)
                    self.child(0).changeLabel(nLabel)
                    self.label = newLabel
                    return None
                else:
                    new = CCGNode(label=CCG.Category('NP'), headIdx=0)
                    self.child(0).reattach(new)
                    self.attachChild(new)
            c1 = None
            production = Production(c0.label, None, self.label)
        production.replace(newLabel)
        self.label = newLabel
        
        if not CCG.isIdentical(production.left, c0.label):
            c0.changeLabel(production.left)
        if c1 and not CCG.isIdentical(production.right, c1.label):
            c1.changeLabel(production.right)
            
    def sibling(self):
        """
        If there is a sibling, return it, else return None
        """
        for child in self.parent().children():
            if child is not self:
                return child
        return None

    def validate(self):
        """
        Check whether subtree composes

        Currently broken
        """
        for child in self.children():
            if not child.validate():
                return False
            if child.isLeaf():
                return True
        if self.isRoot():
            return True
        label = self.label
        left = self.child(0).label
        if self.length() == 1:
            right = None
        else:
            right = self.child(1).label
        if CCG.validate(left, right, label):
            return True
        else:
            w1 = self.getWord(0).globalID
            return False

    def head(self):
        """
        Return the leaf node that the CCGbank indices designate as the head
        Warning: These indices are sometimes unreliable, so this function
        may give incorrect results.

        Warning++!! Be especially careful of bugs introduced during rebanking,
        where the head indices have not been updated appropriately during node
        movement.
        """
        head = self
        while not head.isLeaf():
            if head.headIdx >= head.length():
                print >> sys.stderr, "Bad head idx: %s" % head
                head = head.child(-1)
            else:
                head = head.child(head.headIdx)
        return head

    def heads(self):
        if self.headIdx >= self.length():
                print >> sys.stderr, "Bad head idx: %s" % self
                head = self.child(-1)
        else:
            head = self.child(self.headIdx)
        heads = []
        if head.sibling() and head.sibling().label.conj:
            heads.extend(head.sibling().heads())
        heads.extend(head.heads())
        heads.sort()
        return heads
                

    def move(self, destination, headIdx):
        """
        CCG trees are binary branching, so moving a node means inserting a
        new level in the tree and deleting a level at the old destination.
        This function is not responsible for ensuring valid labels, but does
        check whether moves would cause crossing brackets, and checks whether
        any words are stranded. Requires an index noting head directionality,
        so that the head() function does not break.
        """
        if destination is self.sibling():
            raise StandardError, "Moving to current location!"
        if destination.isLeaf():
            raise StandardError, "Cannot move to leaf!"
        # Store the word list so that we can check it isn't disrupted
        origWords = ' '.join([w.text for w in self.root().listWords()])
        # Check for crossing brackets
        firstNode, lastNode = sorted([self, destination])
        lastYield = lastNode.listWords()
        edgeWords = [w for w in firstNode.listWords() if w not in lastYield]
        if not edgeWords:
            print firstNode
            print lastNode
            raise StandardError
        rightEdge = edgeWords[-1]
        leftEdge = lastYield[0]
        if rightEdge.wordID != (leftEdge.wordID - 1):
            raise StandardError, "Move would create non-contiguous word seq"
        # The actual move operation
        labelCopy = CCG.Category(str(destination.label))
        newParent = CCGNode(label=labelCopy, headIdx=headIdx)
        destination.insert(newParent)
        # Trim production by deleting sibling, moving its children up to parent
        oldParent = self.parent()
        oldSibling = self.sibling()
        oldSibling.prune()
        self.reattach(newParent)
        for node in oldSibling.children():
            node.reattach(oldParent)
        # Post-validation
        # Parent should have same head idx as before, as it has same children
        oldParent.headIdx = oldSibling.headIdx
        if not newParent.listWords():
            print self
            print destination
            raise StandardError
        newWords = ' '.join([w.text for w in self.root().listWords()])
        if origWords != newWords:
            print origWords
            print newWords
            raise StandardError
        return newParent
        

    def typeRaise(self, tCat, slash):
        """
        Add a type-raise node
        """
        assert not tCat.conj
        assert not self.label.conj
        innerSlash = '\\' if slash == '/' else '/'
        inner = CCG.addArg(tCat, self.label, innerSlash)
        newCat = CCG.addArg(tCat, inner, slash)
        newNode = CCGNode(headIdx=0, label=newCat)
        self.insert(newNode)
        
##    def finalise(self):
##        """
##        Once the changes to the tree are complete, it is worth building final word
##        lists etc, and then telling methods to use them instead
##        """
##        self._wordList = self.listWords()
##        self._siblings = [s for s in self.parent().children() if s != self]
##        self._breadthList = self.breadthList()
##        self._depthList = self.depthList()
##        self._head = self.head()
##        self._finalised = True

##    def addCatHeads(self):
##        return StandardError, "Currently Broken!"
##        # Find the highest left-side node with a head
##        left = self._findNode()
##        # Ensure that the node to the right of it has a head
##        left, right, parent = self._prepareJunction(left)
##        # Add the head
##        self.addCatHead(parent, left, right)

##    def _findNode(self):
##        n = self
##        while not n.label.hasHead():
##            n = n.child(0)
##            if n.isLeaf():
##                n.parg.addHead(n.text)
##                n.parent().label.unify(n.parg)
##                return n.parent()
##        return n
##
##    def _prepareJunction(self, node):
##        while node.parent().length() == 1:
##            parent = node.parent()
##            CCG.combineChildren(parent.label, node.label, None)
##            if parent.isRoot():
##                return None, None
##            node = parent
##        left, right = node.parent().children()
##        if not left.label.hasHead():
##            left.addCatHeads()
##        if not right.label.hasHead():
##            right.addCatHeads()
##        return left, right, node

##    def addCatHead(self, left, right, parent):
##        assert left.label.hasHead()
##        assert right.label.hasHead()
##        CCG.combineChildren(parent.label, left.label, right.label)        
