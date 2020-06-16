from Treebank.NodeVisitors import FlatFileWriter
from Treebank.CCGBank.CCGConstructors import *
from Treebank.CCGBank.CCGNodes import *
import Treebank
from os.path import join as pjoin
import os, os.path
class CCGFlatFileWriter(FlatFileWriter):
    _rootClass = 'CCGRoot'
    _internalClass = 'CCGInternal'
    _leafClass = 'CCGLeaf'
    _leaf     = CCGLeaf
    _internal = CCGInternal
    _root     = CorpusFile

    def _makeFunctionMap(self):
        """
        Map classes to the methods that should be called on them
        """
        return {CCGLeaf: self._visitLeaf,
            CCGInternal: self._visitInternal,
            CCGRoot: self._visitInternal,
            CorpusFile: self._visitRoot
        }


    def _getInternalData(self, node):
        data = [str(node.globalID), str(node.label), str(node.headIdx)]
        return '\t'.join(data)

    def _getLeafData(self, node):
        data = [
            str(node.globalID),
            str(node.pos),
            str(node.label),
            str(node.text),
            str(node.parg),
            str(node.wordID),
            str(node.sentIdx)
        ]
        return '\t'.join(data)

class AutoFileWriter:
    """
    Write a .auto format file
    """
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
        if not leaf.parg:
            print leaf
            print leaf.parent()
            raise StandardError
        properties = [
            str(node.label),
            leaf.pos,
            leaf.label,
            leaf.text,
            leaf.parg.fullPrint()]
        leafString = '(<L %s>)' % ' '.join(properties)
        return leafString


class PargFileWriter(AutoFileWriter):


    def writeFile(self, fileID, sentences):
        path = self._getPath(fileID)
        output = open(path, 'w')
        for sentence in sentences:
            output.write(sentence + '\n')
        output.close()

    def getSentenceStr(self, sentence):
        idLine = self._getIDLine(sentence)
        deps = []
        for word in sentence.listWords():
            for argHead, depType, argNum in word.parg.goldDependencies():
                depStr = self._makeDep(word, argHead, argNum, depType)
                deps.append('%d \t %d \t %s' % (argHead.sentIdx, word.sentIdx, depStr))
        deps.sort()
        deps.insert(0, idLine)
        deps.append('<\s>')
        return '\n'.join(deps)
        

    def _getPath(self, fileID):
        dirSect = fileID[4:6]
        directory = pjoin(self.directory, dirSect)
        if not os.path.exists(directory):
            os.mkdir(directory)
        return pjoin(directory, fileID.replace('auto', 'parg'))

    def _getIDLine(self, sentence):
        idLine = '<s id="%s"> %d' % (sentence.globalID, sentence.getWord(-1).sentIdx)
        return idLine
        

    def _makeDep(self, head, arg, argNum, depType):
        """
        A depedency between the ith word and the jth word (wordI and wordJ)
        where the jth word has the lexical (functor) category catJ, and the
        ith word is head of the constituent which fills the kth argument slot
        of catJ is described as:
        i j cat_j arg_k word_i word_j
        """
        i = arg.sentIdx
        j = head.sentIdx
        catJ = str(head.parg)
        argK = argNum
        wordI = arg.text
        wordJ = head.text
        dep = '%d \t %d \t %s \t %d \t %s %s' % (i, j, catJ, argNum, wordI, wordJ)
        if depType != 'L':
            dep = dep + ' ' + depType
        return dep
                                    

if __name__ == '__main__':
    from os.path import join as pjoin
    import psyco
    psyco.full()
    # Write AUTO files
    if 0:
        ccgBank = Treebank.CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/Flat/')
        writer = AutoFileWriter()
        writer.setDir('/home/mhonn/Data/CCGBank/NewPargs')
        for f in ccgBank.children():
            writer.actOn(f)
    elif 1:
        ccgBank = Treebank.CCGBank.ccgBankFromFlat('/home/mhonn/Data/CCGBank/Flat/')
        writer = PargFileWriter()
        writer.setDir('/home/mhonn/Data/CCGBank/NewParg')
        for f in ccgBank.children():
            f.addPargDeps()
            writer.actOn(f)
    else:
        ccgBank = Treebank.CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/AUTO/')
        writer = CCGFlatFileWriter()
        for j in xrange(570, ccgBank.length()):
            oldFile = ccgBank.child(j)
            writer.setLoc(pjoin('/home/mhonn/Data/CCGBank/Flat', oldFile.ID))
            oldFile.performOperation(writer)
            writer.output.close()
        
            
        
