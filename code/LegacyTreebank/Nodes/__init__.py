import sys

from general.Errors import *

from _Node import Node
from _RootNode import RootNode
from _LeafNode import LeafNode
from _FileAndCorpus import Corpus, FileNode



class InternalNode(Node):
    """
    Node with exactly one parent and one or more children
    """
    pass
    




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



            


