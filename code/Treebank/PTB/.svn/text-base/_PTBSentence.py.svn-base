import re

from Treebank.Nodes import Sentence
from _PTBNode import PTBNode
from _PTBLeaf import PTBLeaf

class PTBSentence(PTBNode, Sentence):
    """
    The root of the parse tree
    
    Has no parent, and one or more children
    """
    def __init__(self, **kwargs):
        if 'string' in kwargs:
            node = self._parseString(kwargs.pop('string'))
        elif 'node' in kwargs:
            node = kwargs.pop('node')
        globalID = kwargs.pop('globalID')
        PTBNode.__init__(self, label='S', **kwargs)
        self.globalID = globalID
        self.attachChild(node)


    bracketsRE = re.compile(r'(\()([^\s\)\(]+)|([^\s\)\(]+)?(\))')
    def _parseString(self, text):
        openBrackets = []
        parentage = {}
        nodes = {}
        nWords = 0
        
        # Get the nodes and record their parents
        for match in self.bracketsRE.finditer(text):
            open_, label, text, close = match.groups()
            if open_:
                assert not close
                assert label
                openBrackets.append((label, match.start()))
            else:
                assert close
                label, start = openBrackets.pop()
                if text:
                    newNode = PTBLeaf(label=label, text=text, wordID=nWords)
                    nWords += 1
                else:
                    newNode = PTBNode(string=label)
                if openBrackets:
                    # Store parent start position
                    parentStart = openBrackets[-1][1]
                    parentage[newNode] = parentStart
                else:
                    top = newNode
                # Organise nodes by start
                nodes[start] = newNode
        self._connectNodes(nodes, parentage)
        return top
        



    
