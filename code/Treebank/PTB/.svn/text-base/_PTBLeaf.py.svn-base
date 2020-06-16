from Treebank.Nodes import Leaf
from _PTBNode import PTBNode

class PTBLeaf(Leaf, PTBNode):
    def __init__(self, **kwargs):
        self.wordID = kwargs.pop('wordID')
        self.text = kwargs.pop('text')
        PTBNode.__init__(self, **kwargs)


