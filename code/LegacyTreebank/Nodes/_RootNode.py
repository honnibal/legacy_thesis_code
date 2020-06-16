from _Node import Node

class RootNode(Node):
    """
    The root of the parse tree
    
    Has no parent, and one or more children
    """
    _printer = Printer()
    def __init__(self, **kwargs):
        if 'string' in kwargs:
            node = self._parseString(kwargs['string'])
        elif 'node' in kwargs:
            node = kwargs['node']
        super(self.__class__).__init__(self, {})
        self.attachChild(node)
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

    def isRoot(self):
        return True

    def addWordIDs(self):
        wordID = 0
        for word in self.listWords():
            setattr(word, 'sentIdx', wordID)
            wordID += 1

    ################
    # Parsing Code #
    ################
    bracketsRE = re.compile(r'(\()(\S+)|(\S+)?(\))')
    def _parseString(self, text):
        openBrackets = []
        parentage = {}
        nodeOffsets = {}
        # Get the nodes and record their parents
        for match in self.bracketsRE.finditer(text):
            if match.group(0) == '(':
                openBrackets.append((match.group(1), match.start()))
            else:
                label, start = openBrackets.pop()
                text = match.group(3)
                if text:
                    newNode = self._makeLeaf(label, text)
                else:
                    newNode = self._makeNode(label)
                if not openBrackets:
                    top = newNode
                else:
                    # Store parent start position
                    parentStart = openBrackets[-1][1]
                    parentage[newNode] = parentStart
                    # Organise nodes by start
                    nodes[start] = newNode
        # Build the tree
        for node, parentOffset in parentage.items():
            parent = nodes[parentOffset]
            parent.attachChild(node)
        return top
            
    def _makeLeaf(self, label, text):
