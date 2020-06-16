from Treebank.Nodes import *
import CCG
from general import debug, log, stats
import copy, os, re
from changeNodeLabel import Production
class CCGNode(Node):
    def setup(self):
        self.label
        
    

    def isAdjunct(self):
        return self.label.isAdjunct()

    
#    def isPunct(self):
#        return self.label.isPunct()


        
    def changeLabel(self, newLabel, changeUnary = True):
        if CCG.isIdentical(self.label, newLabel):
            return None
        if CCG.isIdentical(newLabel, 'NP/N'):
            newLabel = CCG.Category('NP[nb]/N')
        c0 = self.child(0)
        if c0.isLeaf():
            self.label = newLabel
            c0.changeLabel(newLabel)
            return None
        if self.length() == 2:
            c1 = self.child(1)
            production = Production(c0.label, c1.label, self.label)
        else:
            if self.isUnary():
                # Don't produce unary rules like N --> S/S
                # Instead, create a new NP node and place it under self
                # This will make a S/S --> NP --> N chain
                if self.label == CCG.NP and self.child(0).label == CCG.N:
                    new = newNode(CCG.Category('NP'), 0)
                    self.child(0).reattach(new)
                    self.attachChild(new)
            c1 = None
            production = Production(c0.label, None, self.label)
        production.replace(newLabel)
        debug("Changing self from %s to %s" % (self.label, newLabel), 3)
        self.label = newLabel
        if not CCG.isIdentical(production.left, c0.label):
            c0.changeLabel(production.left)
            debug("Left child from %s to %s (%s)" % (c0.label, production.left, production.label), 2)
        if c1:
            debug("Right child from %s to %s (%s)" % (c1.label, production.right, production.label), 2)    
        if c1:
            if not CCG.isIdentical(production.right, c1.label):
                c1.changeLabel(production.right)
            
    def sibling(self):
        """
        If there is a sibling, return it
        """
        for child in self.parent().children():
            if child is not self:
                return child
        return None

    def validate(self):
        """
        Check whether subtree composes
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
            debug("Invalid: %s --> %s %s" % (label, left, right), 0)
            log.msg(self.root().globalID, 'invalid')
            log.msg("Parent Cat: %s" % label, 'invalid')
            log.msg("Child 0: %s" % left, 'invalid')
            if self.length() == 2:
                log.msg("Child 1: %s" % right, 'invalid')
            log.msg('Context: %s' % self, 'invalid')
            log.msg("Answers: %s" % CCG.combine(left, right), 'invalid')
            return False

    def head(self):
        if not self._finalised:
            return self.child(self.headIdx).head()
        else:
            return self._head

    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        self._wordList = self.listWords()
        self._siblings = [s for s in self.parent().children() if s != self]
        self._breadthList = self.breadthList()
        self._depthList = self.depthList()
        self._head = self.head()
        self._finalised = True

    def addCatHeads(self):
        return StandardError, "Currently Broken!"
        # Find the highest left-side node with a head
        left = self._findNode()
        # Ensure that the node to the right of it has a head
        left, right, parent = self._prepareJunction(left)
        # Add the head
        self.addCatHead(parent, left, right)

    def _findNode(self):
        n = self
        while not n.label.hasHead():
            n = n.child(0)
            if n.isLeaf():
                n.parg.addHead(n.text)
                n.parent().label.unify(n.parg)
                return n.parent()
        return n

    def _prepareJunction(self, node):
        while node.parent().length() == 1:
            parent = node.parent()
            CCG.combineChildren(parent.label, node.label, None)
            if parent.isRoot():
                return None, None
            node = parent
        left, right = node.parent().children()
        if not left.label.hasHead():
            left.addCatHeads()
        if not right.label.hasHead():
            right.addCatHeads()
        return left, right, node

    def addCatHead(self, left, right, parent):
        assert left.label.hasHead()
        assert right.label.hasHead()
        CCG.combineChildren(parent.label, left.label, right.label)

    def move(self, destination, headIdx):
        """
        CCG trees are binary branching, so moving a node means inserting a new level in the tree
        and deleting a level at the old destination. This function is not responsible for ensuring valid
        labels, but does check whether moves would cause crossing brackets
        """
        if destination is self.sibling():
            raise StandardError, "Moving to current location!"
        # Do crossing brackets check
        first = self.getWord(0)
        last = self.getWord(-1)
        dFirst = destination.getWord(0)
        dLast = destination.getWord(-1)
        if not first or not dFirst:
            print self
            print destination
        first < dFirst
        last > dLast
        first > dFirst
        last < dLast
        # If it starts before it must finish before, if it starts after it must end after
        if ((first < dFirst) and (last > dLast)) or ((first > dFirst) and (last < dLast)):
            print self
            print destination
            raise StandardError, "Crossing brackets during move"
        labelCopy = CCG.Category(str(destination.label))
        newParent = newNode(labelCopy, headIdx)
        destination.insert(newParent)
        # Trim production by deleting sibling, moving its children up to parent
        oldParent = self.parent()
        oldSibling = self.sibling()
        oldSibling.prune()
        self.reattach(newParent)
        for node in oldSibling.children():
            node.reattach(oldParent)
        if not newParent.listWords():
            print self
            print destination
            raise StandardError
        return newParent
        
        
        
            



class CCGRoot(RootNode, CCGNode):
    def setup(self):
        self.addWordIDs()
        self.headIdx = 0

    def sibling(self):
        return None

    def depraddCatHeads(self):
        """
        Add lexical heads to the categories of each word node, and then
        unify the categories in the parse tree so that the words produce correct
        dependencies.
        """
        import CCG
        for word in self.listWords():
            word.parg.addHead(word.text)
            word.parg.unify(word.parent().label)
        for node in self.breadthList():
            if node.isLeaf(): continue
            if node.length() == 2:
                left = node.child(0).label
                right = node.child(1).label
                answer = CCG.combineChildren(node.label, left, right)
                if right == 'NP\NP':
                    of = node.child(1)
                    chair = node.child(0)
                    ans = answer
            elif node.length() == 1:
                left = node.child(0)
                if left.isLeaf():
               #     node.label.unify(left.parg)
                    continue
                else:
                    left = left.label
                CCG.combineChildren(node.label, left, None)
#        for word in self.listWords():
#            word.parg.unify(word.parent().label)
        w = of.getWord(0)
       # w.parg.result.argument.headShare(chair.label, True)


    
        
                


    def addPargDeps(self, pargDeps):
        headDeps = {}
        for pargDep in pargDeps:
            if len(pargDep) == 6:
                i, j, catJ, argK, formI, formJ = pargDep
                depType = 'L'
            elif len(pargDep) == 7:
                i, j, catJ, argK, formI, formJ, depType = pargDep
            else:
                print pargDeps
                raise StandardError
            i = int(i)
            j = int(j)
            argK = int(argK)
            arg = self.getWord(i)
            head = self.getWord(j)
            if arg.text != formI or head.text != formJ:
                print arg
                print head
                print formI
                print formJ
                print pargDep
                print pargDeps
                raise StandardError
            headDeps.setdefault(head, {}).setdefault(argK, []).append((arg, depType))
        # Initialise dependencies, so there's a slot there for unfilled deps
        for word in self.listWords():
            goldDeps = []
            for arg in word.parg.arguments:
                goldDeps.append([])
            word.parg.goldDeps = goldDeps
        for head, itsDeps in headDeps.items():
            cat = head.parg
            for argNum, deps in itsDeps.items():
                for dep in deps:
                    try:
                        cat.goldDeps[argNum - 1].append(dep)
                    except IndexError:
                        print head
                        print cat
                        print cat.arguments
                        print itsDeps
                        print cat.goldDeps
                        for p in pargDeps:
                            print p
                        cat.goldDeps[argNum - 1].append(dep)
            

                

    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        self._wordList = self.listWords()
        self._siblings = []
        self._breadthList = self.breadthList()
        self._depthList = self.depthList()
        self._head = self.head()
        self._finalised = True
           
                
        

class CCGInternal(CCGNode, InternalNode):
    def _getStag(self):
        return self.label

    stag = property(_getStag)
            

class CCGLeaf(LeafNode, CCGNode):
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

    def _getStag(self):
        return self.parg

    stag = property(_getStag)


#    def changeLabel(self, newLabel):
#        self.parg = newLabel
#        self.parent().changeLabel(newLabel)

            


class CCGCorpus(Corpus):
    pass


class CCGCorpusFile(CorpusFile, CCGNode):
    pargSentsRE = re.compile(r'<s id="[^"]+\.\d+"> \d+\n(?:(\d.+?)\n)?<\\s>', re.DOTALL)
    def addPargDeps(self, pargPath="/home/mhonn/Data/CCGBank/orig/data/PARG"):
        section = self.ID[4:6]
        fileLoc = os.path.join(pargPath, section, self.ID.replace('auto', 'parg'))
        text = open(fileLoc).read().strip()
        for i, matchObj in enumerate(CCGCorpusFile.pargSentsRE.finditer(text)):
            if not matchObj.groups()[0]:
                continue
            pargSent = matchObj.groups()[0]
            deps = [dep.split() for dep in pargSent.split('\n')]
            sentence = self.child(i)
            sentence.addPargDeps(deps)

def newNode(label, headIdx):
    settings = {'label': label, 'headIdx': headIdx, '_parent': None, 'metadata': {}, '_children': None}
    return CCGNode(settings)


if __name__ == '__main__':
    import Treebank.CCGBank
    from Treebank.NodeVisitors import NodePrinter
    from general.Singleton import singleton
    corpus = Treebank.CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/orig/AUTO/')
    f = corpus.child(0)
    f.addPargDeps()
    s = f.child(1)
    printer = singleton(NodePrinter)
    print printer.actOn(s)
#    for word in s.listWords():
#        for dep, depType, num in word.parg.goldDependencies():
#            print '%s %d %s %s' % (word.text, num, dep.text, depType)
    s.addCatHeads()
    for word in s.listWords():
        for head, depNum in word.parg.dependencies():
            print "%s %d %s" % (word.text, depNum, head)
    print printer.actOn(s)
