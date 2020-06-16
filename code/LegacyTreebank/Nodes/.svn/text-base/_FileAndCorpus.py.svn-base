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
