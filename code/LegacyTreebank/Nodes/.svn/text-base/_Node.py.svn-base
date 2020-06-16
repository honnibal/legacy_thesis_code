from NodeVisitors import Printer

class Node(object):
    """
    A node in a parse tree
    """
    globalID = 0
    labelRE = re.compile(r'([^-=]+)(?:-([^-=\d]+))?(?:-(\d+))(?:=(\d+))?')
    def __init__(self, **kwargs):
        self.globalID = Node.globalID
        if 'rawLabel' in **kwargs:        
            label, functionLabel, identifier, identified =
            Node._labelRE.groups(label)
        else:
            label = kwargs['label']
            functionLabel = kwargs.get('functionLabel')
            identifier = kwargs.get('identifier')
            identified = kwargs.get('identified')
        self.label = label
        self.functionLabel = functionLabel
        self.identifier = identifier
        self.identified = identified
        self.localID = kwargs['localID']
        self._children = []
        Node.globalID += 1

            
        
    def __hash__(self):
        return hash(self.globalID)

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
        
        
    def _detachFromParent(self):
        self._parent.detachChild(self)
        self._parent = None
        
    def detachChild(self, node):
        self._children.remove(node)
        
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
    # object identity, and less than/greater
    # than comparisons to check ID for sorting
    
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

    def __len__(self):
        return self.length()
        

        
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
        # Avoid recursion, for speed
        queue = list(self.children())
        # Can't use enumerate because changing list in place
        # Must stay 1 ahead of the current index
        i = 0
        for node in queue:
            i += 1
            if not node.isLeaf():
                for j, child in enumerate(node.children()):
                    queue.insert(i+j, child)
        return queue
        
    def breadthList(self):
        """
        Breadth-first node list
        """
        children = [child for child in self.children()]
        for child in children:
            for subChild in child.children():
                children.append(subChild)
        return children
        
    def getWordID(self, index):
        """
        Word ID at index. Generally 0 or -1
        """
        wordIDList = [word.wordID for word in self.listWords()]
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
        List the word yield of the node
        """
        return [n for n in self.depthList() if n.isLeaf()]
        
    def length(self, constraint = None):
        if constraint == None:
            return len(self._children)
        else:
            return len([c for c in self.children() if constraint(c)])
    
    def siblings(self):
        return [s for s in self.parent().children() if s != self]

    def isLeaf(self):
        return False

    def isRoot(self):
        return False

    def root(self):
        if not self.isRoot():
            return self.parent().root()
        else:
            return self

    def isUnary(self):
        if self.length() == 1 and not self.child(0).isLeaf():
            return True
        else:
            return False
