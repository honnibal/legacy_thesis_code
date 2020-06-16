import doctest
from Treebank.PTB import PTBNode as Node

def plainLabel():
    """
    >>> node = Node(string='NP')
    >>> print node.label
    NP
    """
    pass

def functionLabel():
    """
    >>> node = Node(string='NP-TMP')
    >>> print node.label
    NP
    >>> print node.functionLabel
    TMP
    """
    pass

def identifierLabel():
    """
    >>> node = Node(string='NP-2')
    >>> print node.label
    NP
    >>> node.identifier
    '2'
    """
    pass

def identifiedLabel():
    """
    >>> node = Node(string='NP=2')
    >>> print node.label
    NP
    >>> node.identified
    '2'
    """
    pass

def functionIdentifierLabel():
    """
    >>> node = Node(string='NP-SBJ-2')
    >>> print node.label
    NP
    >>> print node.functionLabel
    SBJ
    >>> node.identifier
    '2'
    """
    pass

def functionIdentifierIdentifiedLabel():
    """
    >>> node = Node(string='NP-SBJ-22=45')
    >>> print node.label
    NP
    >>> print node.functionLabel
    SBJ
    >>> node.identifier
    '22'
    >>> node.identified
    '45'
    """
    pass

def kwargLabels():
    """
    >>> node = Node(label='NP', functionLabel='SBJ',\
                          identifier='22', identified='45')
    >>> print node.label
    NP
    >>> print node.functionLabel
    SBJ
    >>> node.identifier
    '22'
    >>> node.identified
    '45'
    """
    pass

if __name__ == '__main__':
    doctest.testmod()
