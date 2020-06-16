import Nodes
from general.Errors import *
import Treebank
class TreeOperation:
    """
    Define some operation that is called on a series of nodes
    """
##    _leaf     = Nodes.LeafNode
##    _internal = Nodes.InternalNode
##    _root     = Nodes.RootNode
##    _file     = Nodes.CorpusFile
##    _corpus   = Nodes.Corpus
##    listType  = 'depthList'
##    moreChanges = False
##    def __init__(self):
##        self._functionMap = self._makeFunctionMap()
##            
##    def _makeFunctionMap(self):
##        """
##        Map classes to the methods that should be called on them
##        """
##        return {self._leaf: self._visitLeaf,
##            self._internal: self._visitInternal,
##            self._root: self._visitRoot
##        }
##          
##    def newStructure(self):
##        """
##        Reset state for new structure
##        """
##        pass
##
##    def __call__(self, node):
##        self.actOn(node)        
##    
##    def actOn(self, node):
##
##        self._functionMap[node.__class__](node)
##
##    def _visitLeaf(self, node):
##        """
##        Must be overridden in subclasses
##        """
##        raise ImplementationError, "Subclasses must override this function"
##        
##    def _visitInternal(self, node):
##        """
##        Must be overridden in subclasses
##        """
##        raise ImplementationError, "Subclasses must override this function"
##        
##    def _visitRoot(self, node):
##        """
##        Must be overridden in subclasses
##        """
##        raise ImplementationError, "Subclasses must override this function"


class Printer(object):
    """
    Print a parse tree with good formatting
    """
    
    def __call__(self, node):
        return self.actOn(node)
    
    def actOn(self, node):
        if isinstance(node, Nodes.RootNode):
            return self._visitRoot(node)
        else:
            raise Break
    
    def _isLeaf(self, node):
        if isinstance(node, Nodes.LeafNode):
            return True
        else:
            return False

    def _visitRoot(self, node):
        """
        Print each node's label, and track indentation
        """
        self._indentation = 0
        self._lines = []
        # Accrue print state
        self._printNode(node)
        # Ensure that brackets match
        assert self._indentation == 0
        return '\n'.join(self._lines)

            
    def _visitInternal(self, node):
        """
        The visitor must control iteration itself, so only works on root.
        """
        raise Break
            
    def _printNode(self, node):
        """
        Print indentation, a bracket, then the node label.
        Then print the node's children, then a close bracket.
        """
        indentation = '  '*self._indentation
        self._lines.append('%s(%s' % (indentation, node.label))
        self._indentation += 1
        for child in node.children():
            if self._isLeaf(child):
                self._printLeaf(child)
            else:
                self._printNode(child)
        self._lines[-1] = self._lines[-1] + ')'
        self._indentation -= 1

    def _printLeaf(self, node):
        self._lines[-1] = self._lines[-1] + ' %s' % (node.text)

class NodePrinter(Printer):
    """
    Deprecated alias
    """
    pass

class PropbankNodePrinter(Printer):
    """
    Print trees with Propbank annotation
    """
    def setEntries(self, entries):
        nodes = {}
        for entry in entries:
            for parg in entry.pargs:
                for nodeSet in parg.refChain:
                    for node in nodeSet:
                        if parg.feature:
                            label = '%s_%s' % (parg, parg.feature)
                        else:
                            label = parg.label
                        if node in nodes:
                            label = label + '-' + nodes[node]
                        nodes[node] = label
        self.entries = nodes

    def _printNode(self, node):
        """
        Print indentation, a bracket, then the node label.
        Then print the node's children, then a close bracket.
        """
        indentation = '  '*self._indentation
        if node in self.entries:
            self._lines.append('%s(%s-%s' % (indentation, node.label, self.entries[node]))
        else:
            self._lines.append('%s(%s' % (indentation, node.label))
        self._indentation += 1
        for child in node.children():
            if self._isLeaf(child):
                self._printLeaf(child)
            else:
                self._printNode(child)
        self._lines[-1] = self._lines[-1] + ')'
        self._indentation -= 1

    def _printLeaf(self, node):
        if node in self.entries:
            self._lines[-1] = self._lines[-1] + ' %s-%s' % (node.text, self.entries[node])
        else:
            self._lines[-1] = self._lines[-1] + ' %s' % (node.text)

class TreeRearranger(TreeOperation):
    """
    Abstract class for structural tree operations, because these
    operations share common features:
    - they usually work on certain types of nodes and ignore all others
    - they usually check some set of conditions, and ignore the node if they are not met
    - if they are met, they move some node/s to some other place in the tree
    """
    _targetTypes = []
    
    def __init__(self):
        pass
        
    def actOn(self, constituent):
        # Allow TreeRearrangers to visit both nodes and constituents
        for type in self._targetTypes:
            if constituent.isType(type):
                self._visitTarget(constituent)
                break
        else:
            self._rejectNode(constituent)
    
    
    def _visitTarget(self, node):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        if self._checkConstraints(node):
            self._rearrangeTree(node)
        else:
            self._rejectNode(node)
    
    def _rejectNode(self, node):
        """
        Perform any actions (such as raising a Break) that
        should be performed if a node is seen that the Visitor is not
        interested in
        """
        pass
        
    def _checkConstraints(self, node):
        """
        Return a boollean to indicate whether the node meets the criteria
        
        Must be overridden
        """
        raise ImplementationError, "Subclasses of TreeShaper must override _checkConstraints"
        
    def _rearrangeTree(self, node):
        """
        Perform the restructuring
        """
        raise ImplementationError, "Subclasses of TreeShaper must override _checkConstraints"


class FlatFileWriter(TreeOperation):
    _rootClass = 'RootNode'
    _internalClass = 'InternalNode'
    _leafClass = 'LeafNode'
#    _root = Treebank.Nodes.CorpusFile
    
    def setLoc(self, location):
        self.location = location

    def _visitRoot(self, fileNode):
        self.output = open(self.location, 'w')
        self.fileID = fileNode.ID

    def _visitInternal(self, node):
        if node.isRoot():
            parentID = self.fileID
            nodeClass = self._rootClass
        else:
            parentID = str(node.parent().globalID)
            nodeClass = self._internalClass
        data = self._getInternalData(node)
        self.output.write('%s**%s**%s\n' % (parentID, nodeClass, data))

    def _visitLeaf(self, node):
        data = self._getLeafData(node)
        nodeClass = self._leafClass
        parentID = str(node.parent().globalID)
        self.output.write('%s**%s**%s\n' % (parentID, nodeClass, data))
        


    def _getInternalData(self, node):
        data = [
            str(node.globalID),
            str(node.label),
            str(node.functionLabel),
            str(node.identifier),
            str(node.identified)
        ]
        return '\t'.join(data)
            
if __name__ == '__main__':
    # Write flat files
    if 1:
        ptb = Treebank.makeCorpus('/home/mhonn/Data/Treebank3_wsj/')
        flatWriter = FlatFileWriter()
        path = '/home/mhonn/Data/FlatTreebank3/'
        for f in ptb.children():
            flatWriter.setLoc(path + f.ID)
            flatWriter.actOn(f)
