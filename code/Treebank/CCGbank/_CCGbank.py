import sys
import re

from Treebank.PTB import PennTreebank
from _CCGNode import CCGNode
from _CCGFile import CCGFile

class CCGbank(PennTreebank, CCGNode):
    fileClass = CCGFile
    def child(self, index):
        """
        Read a file by zero-index offset
        """
        path = self._children[index]
        print >> sys.stderr, path
        return self.fileClass(path=path)

    def sentence(self, key):
        fileID, sentID = key.split('~')
        f = self.file(fileID)
        pargLoc = fileID.rsplit('/', 2)[0].replace('AUTO', 'PARG')
        f.addPargDeps(pargLoc)
        sentID = key.split('/')[-1].replace('.auto~', '.')
        return f.sentence(sentID)

    def tokens(self):
        """
        Generate tokens without parsing the files properly
        """
        tokenRE = re.compile(r'<L (\S+) \S+ (\S+) (\S+) \S+>')
        for path in self._children:
            string = open(path).read()
            for cat, pos, form in tokenRE.findall(string):
                yield form, pos, cat
            
