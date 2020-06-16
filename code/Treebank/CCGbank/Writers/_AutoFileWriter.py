import os
from os.path import join as pjoin

import CCG.Markedup

class AutoFileWriter:
    """
    Write a .auto format file
    """
    def __init__(self, **kwargs):
        if 'directory' in kwargs:
            self.setDir(kwargs.pop('directory'))
        if 'markedup' in kwargs:
            muLoc = kwargs.pop('markedup')
            entries, unused = CCG.Markedup.getEntries(muLoc)
            markedup = {}
            for entry in entries:
                markedup[entry.cat] = entry.toJulia()
            self.markedup = markedup
        else:
            self.markedup = {}
        assert not kwargs
        
    def setDir(self, directory):
        if not os.path.exists(directory):
            print "Making %s" % directory
            os.makedirs(directory)
        self.directory = directory
        
    def getSentenceStr(self, sentence):
        lines = []
        idLine = self._getIDLine(sentence.globalID)
        lines.append(idLine)
        lines.append(self._nodeString(sentence.child(0)))
        return '\n'.join(lines)

    def writeFile(self, fileID, sentences):
        path = self._getPath(fileID)
        output = open(path, 'w')
        for sentence in sentences:
            output.write(sentence + '\n')
        output.close()

    def _getPath(self, fileID):
        dirSect = fileID[4:6]
        directory = pjoin(self.directory, dirSect)
        if not os.path.exists(directory):
            os.mkdir(directory)
        return pjoin(directory, fileID)
            

    def _getIDLine(self, sentenceID):
        return "ID=%s PARSER=GOLD NUMPARSE=1" % sentenceID
        
        
    def _nodeString(self, node):
        if node.child(0).isLeaf():
            return self._leafString(node)
        else:
            childStrings = []
            for child in node.children():
                childStrings.append(self._nodeString(child))
            nodeString = '(<T %s %d %d> %s )' % (node.label, node.headIdx, len(childStrings), ' '.join(childStrings))
            return nodeString

    def _leafString(self, node):
        leaf = node.child(0)
        #if not leaf.parg:
        #    print leaf
        #    print leaf.parent()
        #    raise StandardError
        annotated = self.markedup.get(leaf.stag, leaf.stag.fullPrint())
        #if leaf.stag != node.label:
        #    print node.root().globalID
        #    print node
        #    print leaf
        #    print leaf.stag
        #    raise StandardError
        properties = [
            str(node.label),
            leaf.pos,
            leaf.label,
            leaf.text,
            annotated]
        try:
            leafString = '(<L %s>)' % ' '.join(properties)
        except:
            print properties
            raise
        return leafString
