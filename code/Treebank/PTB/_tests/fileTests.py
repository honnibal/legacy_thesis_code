from Treebank.PTB import PTBFile as CorpusFile

import doctest

pierreLoc = '/home/matt/code/repos/data/TreeBank3/parsed/mrg/wsj/00/wsj_0001.mrg'
def testPierre():
    """
    >>> f = CorpusFile(path=pierreLoc)
    >>> s = f.child(0)
    >>> print ' '.join([w.text for w in s.listWords()])
    Pierre Vinken , 61 years old , will join the board as a nonexecutive director Nov. 29 .
    """
    pass

asbestosLoc = '/home/matt/code/repos/data/TreeBank3/parsed/mrg/wsj/00/wsj_0003.mrg'
def testAsbestos():
    """
    >>> f = CorpusFile(path=asbestosLoc)
    >>> sentences = [s for s in f.children()]
    >>> len(sentences)
    30
    >>> s = sentences[-1]
    >>> print ' '.join([w.text for w in s.listWords()])
    It has no bearing on our work force today .
    >>> print s.globalID
    wsj_0003.mrg~0030
    """
    pass
    

if __name__ == '__main__':
    doctest.testmod()
