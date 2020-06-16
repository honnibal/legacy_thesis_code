from Treebank.Nodes import Corpus
from _PTBNode import PTBNode
from _PTBFile import PTBFile

import os
import sys
from os.path import join as pjoin

class PennTreebank(PTBNode, Corpus):
    """
    The Penn Treebank, specifically the WSJ
    Children are built just-in-time
    """
    fileClass = PTBFile
    def __init__(self, **kwargs):
        self.path = kwargs.pop('path')
        PTBNode.__init__(self, label='Corpus', **kwargs)
        for fileLoc in self._getFileList(self.path):
            self.attachChild(fileLoc)
                            

    def section00(self):
        for i in xrange(99):
            yield self.child(i)

    def twoTo21(self):
        for i in xrange(199, 2074):
            yield self.child(i)

    def section23(self):
        for i in xrange(2157, 2257):
            yield self.child(i)

    def _getFileList(self, location):
        """
        Get all files below location
        """
        paths = []
        for path in [pjoin(location, f) for f in os.listdir(location)]:
            if path.endswith('CVS'):
                continue
            elif path.startswith('.'):
                continue
            if os.path.isdir(path):
                paths.extend(self._getFileList(path))
            elif path.endswith('.mrg') or path.endswith('.auto'):
                paths.append(path)
        paths.sort()
        return paths

