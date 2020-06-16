import doctest

from _File import CorpusFile

asbestos = '/home/matt/code/repos/data/CCGbank1.2/data/AUTO/00/wsj_0003.auto'
def testFile():
    """
    >>> f = CorpusFile(path=asbestos)
    >>> print len(list(f.children()))
    30
    >>> s = f.child(0)
    >>> print ' '.join([w.text for w in s.listWords()])
    A form of asbestos once used to make Kent cigarette filters has caused a high percentage of cancer deaths among a group of workers exposed to it more than 30 years ago , researchers reported .
    >>> s = f.child(-1)
    >>> print ' '.join([w.text for w in s.listWords()])
    It has no bearing on our work force today .
    >>> print s.globalID
    wsj_0003.30
    """
    pass

if __name__ == '__main__':
    doctest.testmod()
