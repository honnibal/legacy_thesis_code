import re
import bisect

from Treebank.Nodes import Node


class PTBNode(Node):
    """
    A node in a parse tree
    """
    _labelRE = re.compile(r'([^-=]+)(?:-([^-=\d]+))?(?:-(\d+))?(?:=(\d+))?')
    def __init__(self, **kwargs):
        string = kwargs.pop('string', None)
        if string is not None:        
            pieces = PTBNode._labelRE.match(string).groups()
            label, functionLabel, identifier, identified = pieces
        else:
            label = kwargs.pop('label')
            functionLabel = kwargs.pop('functionLabel', None)
            identifier = kwargs.pop('identifier', None)
            identified = kwargs.pop('identified', None)
        if kwargs:
            raise StandardError, kwargs
        self.functionLabel = functionLabel
        self.identifier = identifier
        self.identified = identified
        
        Node.__init__(self, label)

            
        

