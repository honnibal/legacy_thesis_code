"""
These are _Composite_ parse-tree nodes that maintain a Constituent _State_.

They are _Visited_ by operations which change their structures, moving them towards
SFG parses.
"""
import bisect
import sys

from general.Errors import *
from NodeVisitors import Printer

class Node(object):
    """
    A node in a parse tree
    """
    _finalised = False
    globalID = 0
    def __init__(self, settings):
        self._intialiseData()
        self.globalID = Node.globalID
        self.current = {}
        for key, value in settings.items():
            setattr(self, key, value)
        self._children = []
        Node.globalID += 1
        
    def __hash__(self):
        return hash(self.globalID)
    
    def _intialiseData(self):
        """
        Placing this kind of initialisation outside __init__ makes it easier for
        subclasses to override init while maintaining what they need
        """
        pass

    def setup(self):
        """
        House keeping after a node has been built
        """
        pass
    
    def reattach(self, newParent, index = None):
        """
        Detach from current location and move to a new location
        in the tree
        """
        depthList = self.depthList()
        lookup = {}
        for n in depthList:
            lookup[n] = True
        assert not newParent in lookup
        self._detachFromParent()
    	newParent.attachChild(self, index)
        
    def attachChild(self, newChild, index = None):
        """
        How to attach a child.
        Overridden by LeafNode, which raises an error.
        """
        # Don't allow bidirectional parenthood
        assert not self is newChild
        if newChild.parent():
            raise AttachmentError, 'Cannot attach node:\n\n%s\n\nto:\n\n%s\n\nNode is already attached to\n\n%s' \
            % (newChild.prettyPrint(), self.prettyPrint(), newChild.parent().prettyPrint())
        if index == None:
            bisect.insort_right(self._children, newChild)
        else:
            self._children.insert(index, newChild)
        newChild.setParent(self)
        self.update()
        
        
    def _detachFromParent(self):
        self._parent.detachChild(self)
        self._parent = None
        
    def detachChild(self, node):
        self._children.remove(node)
        self.update()
        
    def setParent(self, node):
        """
        Set a node as _parent
        """
        self._parent = node
 
        
    def prettyPrint(self):
        return "(%s %s)" % (self.label, ' '.join([child.prettyPrint() for child in self.children()]))

    def parent(self):
        """
        Returns _parent
        
        The indirection allows RootNode, which overrides this,
        to raise an error instead.
        """
        return self._parent
        
        
    def child(self, index):
        """
        Returns _children[index]
        
        The indirection allows LeafNodes, which override this,
        to raise an error instead.
        """
        return self._children[index]    
        
    def children(self):
        """
        Generator function
        
        Iterate through children
        """
        # Must use list copy, lest the list change out from under the iteration
        for child in list(self._children):
            yield child
            
    def allocate(self, possibleParents, direction = 'Right'):
        """
        Decide which, from a set of parents, a node should be attached to by
        getting the word closest to it
        """
        if len(possibleParents) < 2:
            self.reattach(possibleParents[0])
        elif not possibleParents:
            raise StandardError, "No parents to allocated node to: " + str(node)
        else:
            decoratedWords = []
            for parent in possibleParents:
                for word in parent.listWords():
                    # Ellipsed words dont count
                    if word.isType('Ellipsis'):
                        continue
                    # Doesn't count if the word is in the node, either
                    if word in self.listWords():
                        continue
                    # ID, parent tuple so that the list can be sorted without a function and the parent determined
                    decoratedWords.append( (word.wordID, parent) )
            # If all of the words are ellipsis, relax that constraint
            if not decoratedWords:
                for parent in possibleParents:
                    decoratedWords.extend([(w.wordID, parent) for w in parent.listWords() if w != self])
            decoratedWords.sort()
            decoratedSelf = (self.getWordID(0), self)
            # Use bisect to get the index self fits into the list
            index = bisect.bisect_right(decoratedWords, decoratedSelf)
            if direction != 'Right' and index > 0:
                index = bisect.bisect_left(decoratedWords, decoratedSelf) - 1
            if index == len(decoratedWords):
                self.reattach(decoratedWords[-1][1])
            else:
                self.reattach(decoratedWords[index][1])
            
            
    def insert(self, node):
        """
        Insert a node above self
        """
        self.parent().replace(self, node)
        node.attachChild(self)

    def delete(self):
        """
        Delete self from the tree, reattaching children to parent
        """
        parent = self.parent()
        self.prune()
        for node in self.children():
            node.reattach(parent)

    def replace(self, currentChild, replacement):
        """
        Insert a new node where an old one was
        """
        index = self._children.index(currentChild)
        if replacement.parent():
            replacement.reattach(self, index)
        else:
            self.attachChild(replacement, index)
        currentChild.prune()
    
    def prune(self):
        """
        Detach node and subtree
        """
        self._detachFromParent()
    
    # 'Rich comparison' must be used, because I want equality tests to check
    # object identity, and less than/greater than comparisons to check ID for sorting
    
    def __eq__(self, other):
        return bool(self is other)
    
    def __ne__(self, other):
        return bool(self is not other)
    
    def __cmp__(self, obj):
        """
        The deprecated complicated (and crushingly slow) cmp is used in the SFG
        stuff
        """
       # return cmp(self.globalID, obj.globalID)
        selfID = float(self.getWordID(0))
        objID = float(obj.getWordID(0))
        if selfID == -1:
            return 0
        elif objID == -1:
            return 0
        else:
            return cmp(selfID, objID)
        

        
    def __str__(self):
        return self.prettyPrint()
        
    def sortChildren(self):
        decorated = [(c.getWordID(0), c) for c in self._children]
        decorated.sort()
        self._children = [d[1] for d in decorated]
        
    def depthList(self):
        """
        Depth-first node list
        """
        if 'depthList' in self.current:
            return list(self.current['depthList'])
        if self._finalised:
            return [n for n in self._depthList]
        nodes = []
        for child in self.children():
            nodes.append(child)
            nodes.extend(child.depthList())
        self.current['depthList'] = list(nodes)
        return nodes
        
    def breadthList(self):
        """
        Breadth-first node list
        """
        if self._finalised:
            return [n for n in self._breadthList]
        children = [child for child in self.children()]
        for child in children:
            for subChild in child.children():
                children.append(subChild)
        return children
        
    def getWordID(self, index):
        """
        Word ID at index. Generally 0 or -1
        """
        if index == 0:
            if 'wordID0' in self.current:
                return self.current['wordID0']
        if index == -1:
            if 'wordID0-1' in self.current:
                return self.current['wordID-1']
        wordIDList = [word.wordID for word in self.listWords()]
        if not wordIDList:
            self.current['wordID0'] = -1
            self.current['wordID-1'] = -1
            return -1
        self.current['wordID0'] = wordIDList[0]
        self.current['wordID-1'] = wordIDList[-1]
        return wordIDList[index]
        
    def getWord(self, index):
        """
        Word ID at index. Generally 0 or -1
        """
        wordList = self.listWords()
        if not wordList:
            return None
        return wordList[index]
        
    def listWords(self):
        """
        Try avoiding recursion, for speed
        """
        if 'listWords' in self.current:
            return list(self.current['listWords'])
        words = []
        nodes = list(self._children)
        while nodes:
            node = nodes.pop(0)
            if node.isLeaf():
                words.append(node)
            else:
                nodes.extend(node._children)
        words.sort()
        self.current['listWords'] = list(words)
        return words
        
    def length(self, constraint = None):
        if constraint == None:
            return len(self._children)
        else:
            return len([c for c in self.children() if constraint(c)])
    
    def siblings(self):
    	if self._finalised:
    	    return [s for s in self._siblings]
        return [s for s in self.parent().children() if s != self]

    def isLeaf(self):
        return False

    def isRoot(self):
        return False
    
    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        self._wordList = self.listWords()
        self._siblings = [s for s in self.parent().children() if s != self]
        self._breadthList = self.breadthList()
        self._depthList = self.depthList()
        self._finalised = True

    def root(self):
        if not self.isRoot():
            return self.parent().root()
        else:
            return self

    def update(self):
        self.current = {}
        if self._parent:
            self._parent.update()

    def isUnary(self):
        if self.length() == 1 and not self.child(0).isLeaf():
            return True
        else:
            return False    
    
class RootNode(Node):
    """
    The root of the parse tree
    
    Has no parent, and one or more children
    """
    _printer = Printer()
    def setup(self):
        self.addWordIDs()

    def __str__(self):
        return self._printer(self)
        
    def parent(self):
        """
        Raises an error, because the root node has no parent
        """
        raise AttributeError, "Cannot retrieve the parent of the root node! Current parse state:\n\n%s" % self.prettyPrint()
        
    def performOperation(self, operation):
        """
        Accept a _Visitor_ and call it on each child
        """
        operation.newStructure()
        operation.actOn(self)
        for node in self.depthList():
            try:
                operation.actOn(node)
            # Give operations the opportunity to signal
            # when the work is complete
            except Break:
                break
        while operation.moreChanges:
            operation.actOn(self)
            for node in getattr(self, operation.listType)():
                try:
                    operation.actOn(node)
                # Give operations the opportunity to signal
                # when the work is complete
                except Break:
                    break

    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        self._wordList = self.listWords()
        self._siblings = []
        self._breadthList = self.breadthList()
        self._depthList = self.depthList()
        self._finalised = True

    def isRoot(self):
        return True

    def addWordIDs(self):
        wordID = 0
        for word in self.listWords():
            setattr(word, 'sentIdx', wordID)
            wordID += 1

            

class InternalNode(Node):
    """
    Node with exactly one parent and one or more children
    """
    pass
    
class LeafNode(Node):
    """
    A leaf of the parse tree -- ie, a word, punctuation or trace
    Cannot attach or retrieve children
    """
    def _intialiseData(self):
        """
        Placing this kind of initialisation outside __init__ makes it easier for
        subclasses to override init while maintaining the interface
        """
        self.metadata = {}
        self.senses = []

    def __hash__(self):
        return self.wordID

    def isLeaf(self):
        return True
    
    def attachChild(self, newChild, index = None):
        raise AttachmentError, "Cannot add node\n\n%s\n\nto leaf:\n\n%s\n\nLeaves cannot have children." \
        % (newChild.prettyPrint(), self.prettyPrint())

    def length(self, constraint = None):
        return 0
        
    def child(self, index):
        """
        Raises an error, because leaf nodes have no children
        """
        raise AttributeError, "Cannot retrieve children from leaf nodes! Attempted on leaf:\n\n%s" % self.prettyPrint()
        
    def detachChild(self, node):
        """
        Raises an error, because leaf nodes have no children
        """
        raise AttributeError, "Cannot remove children from leaf nodes! Attempted on leaf:\n\n%s" % self.prettyPrint()
        
    def prettyPrint(self):
        return "(%s %s)" % (self.label, self.text) 
    
    def listWords(self):
        return [self]
        
    def lemma(self):
        """
        Get lemma from COMLEX entry, otherwise text
        """
        if self.metadata.get('COMLEX'):
            return self.metadata['COMLEX'][0].features['ORTH'][0][1:-1]
        elif self.label in ['NNP', 'NNPS']:
            return self.text
        else:
            return self.text.lower()

    def isTrace(self):
        return bool(self.label == '-NONE-')
        

    def isPunct(self):
        punct = {
        ',': True,
        ':': True,
        '.': True,
        ';': True,
        'RRB': True,
        'LRB': True
        }
        return bool(self.label in punct)



class TracedNode(Node):
    """
    A node referred to by a trace, so that other elements can pretend
    it's actually the original
    """
    def __init__(self, trace, target):
        """
        Store the target and the trace's constituent
        """
        self.trace = trace
        self.target = target
        self.traceType = trace.text.split('-')[0]
        self._parent = None
        self.globalID = trace.globalID
        self.label = trace.parent().label
        self.functionLabels = trace.parent().functionLabels
       # self.localID = trace.localID

    def getWordID(self, worNum):
        return self.trace.wordID

    def children(self):
        return [self.target]
        

        
    
    
#==============================================================================

"""
Classes representing files from different corpora
"""

class Corpus(Node):
    """
    Node Interface:
        child            method
        parent           method
        children         generator
        reattach         method
        attachChild      method
        prettyPrint      method
        metadata         extra information (eg speaker)
    
    Root node
    """ 
    def _intialiseData(self):
        """
        Placing this kind of initialisation outside __init__ makes it easier for
        subclasses to override init while maintaining what they need
        """
        self._children = []
            
    def parent(self):
        """
        Raises an error, because the root node has no parent
        """
        raise AttributeError, "Cannot retrieve the parent of the root node! Current parse state:\n\n%s" % self.prettyPrint()
        
    def attachChild(self, newChild):
        """
        Security isn't really an issue for Files, so just stick it onto the list
        """
        self._children.append(newChild)
        
        
    def listNodes(self):
        """
        Return a breadth-first node list
        """
        for child in self.children():
            for node in child.listNodes():
                yield node

        
    def performOperation(self, operation):
        """
        Accept a _Visitor_ and call it on each child
        """
        operation.newStructure()
        operation.actOn(self)
        for node in self.children():
            operation.actOn(node)
            
    def child(self, index):
        """
        Make a file
        """
        print >> sys.stderr, self._children[index]
        return self._childConstructor.make(self._children[index], self._leafClass)
     
    def settings(self, childConstructor, leafClass):
        self._childConstructor = childConstructor
        self._leafClass = leafClass       
    
    def children(self):
        """
        Generator function
        
        Iterate through children
        """
        for i in xrange(len(self._children)):
            yield self.child(i)
    
    def file(self, key):
        return self._childConstructor.make(key, self._leafClass)
            
    def sentence(self, key):
        filename, sentenceKey = key.split('~')
        file = self.file(filename)
        return file.sentence(key)

    def twoTo21(self):
        for i in xrange(200, 2074):
            yield self.child(i)

    def section00(self):
        for i in xrange(99):
            yield self.child(i)



class CorpusFile(Node):
    """
    Internal node
    Contains parses and metadata
       
    Node Interface:
        child            method
        parent           method
        children         generator
        reattach         method
        attachChild      method
        prettyPrint      method
        metadata         extra information (eg speaker)
    """
    def _intialiseData(self):
        """
        Placing this kind of initialisation outside __init__ makes it easier for
        subclasses to override init while maintaining what they need
        """
        self._children = []
        self._IDDict = {}
    
    def attachChild(self, newChild):
        """
        Security isn't really an issue for Files, so just append the new Sentence without complaint
        """
        self._children.append(newChild)
        self._IDDict[newChild.globalID] = newChild
    
    def detachChild(self, node):
        self._children.remove(node)
        self._IDDict.pop(node.globalID)
    
    def sentence(self, key):
        return self._IDDict[key]
    
    def prettyPrint(self):
        return "(%d %s)" % (self.localID, '\n\n\n'.join([child.prettyPrint() for child in self.children()]))
        
    def performOperation(self, operation):
        """
        Accept a _Visitor_ and call it on each child
        """
        operation.newStructure()
        operation.actOn(self)
        for node in getattr(self, operation.listType)():
            try:
                operation.actOn(node)
            # Give operations the opportunity to signal
            # when the work is complete
            except Break:
                break
        while operation.moreChanges:
            operation.actOn(self)
            for node in getattr(self, operation.listType)():
                try:
                    operation.actOn(node)
                # Give operations the opportunity to signal
                # when the work is complete
                except Break:
                    break

    def finalise(self):
        for child in self.children():
            child.finalise()
        self._finalised = True
            


