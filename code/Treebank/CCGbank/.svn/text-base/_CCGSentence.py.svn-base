import re
import sys

from _CCGNode import CCGNode
from _CCGLeaf import CCGLeaf
from Treebank.Nodes import Sentence
import CCG

class CCGSentence(Sentence, CCGNode):
    def __init__(self, **kwargs):
        if 'string' in kwargs:
            node = self._parseString(kwargs.pop('string'))
        elif 'node' in kwargs:
            node = kwargs.pop('node')
        globalID = kwargs.pop('globalID')
        self.localID = kwargs.pop('localID')
        CCGNode.__init__(self, label="S", headIdx=0, **kwargs)
        self.globalID = globalID
        self.attachChild(node)
        self.headIdx = 0
        

    def sibling(self):
        return None

    def addPargDeps(self, pargDeps):
        headDeps = {}
        for pargDep in pargDeps:
            if len(pargDep) == 6:
                i, j, catJ, argK, formI, formJ = pargDep
                if formI == '-colon-':
                    formI = ':'
                if formJ == '-colon-':
                    formJ = ':'
                depType = 'L'
            elif len(pargDep) == 7:
                i, j, catJ, argK, formI, formJ, depType = pargDep
            else:
                print pargDeps
                raise StandardError
            i = int(i)
            j = int(j)
            argK = int(argK)
            arg = self.getWord(i)
            head = self.getWord(j)
            if arg.text != formI or head.text != formJ:
                if formI == 'null' or formJ == 'null':
                    continue
                #else:
                #    print >> sys.stderr, "Mismatched dependency"
                #    return None
                print self.globalID
                print '\n'.join('%d-%s' % (w.wordID, w.text) for w in self.listWords())
                print arg
                print head
                print formI
                print formJ
                print pargDep
                print '\n'.join([' '.join(d) for d in pargDeps])
                print self
                raise StandardError, "Mismatched dependency"
            headDeps.setdefault(head, {}).setdefault(argK, []).append((arg, depType))
        # Initialise dependencies, so there's a slot there for unfilled deps
        for word in self.listWords():
            goldDeps = []
            for arg in word.parg.arguments:
                goldDeps.append([])
            word.parg.goldDeps = goldDeps
        for head, itsDeps in headDeps.items():
            cat = head.parg
            for argNum, deps in itsDeps.items():
                for dep in deps:
                    try:
                        cat.goldDeps[argNum - 1].append(dep)
                    except IndexError:
                    #    print >> sys.stderr, "Index error"
                    #    return None
                        print self.globalID
                        print '\n'.join('%d-%s' % (w.wordID, w.text) for w in self.listWords())
                        print head
                        print cat
                        print cat.arguments
                        print itsDeps
                        print cat.goldDeps
                        for p in pargDeps:
                            print p
                        cat.goldDeps[argNum - 1].append(dep)

    # This returns 4 groups for compatibility with the
    # Root.parseString method
    bracketsRE = re.compile(r'(\()<([^>]+)>|()(\))')
    def _parseString(self, text):
        # The algorithm here is roughly, find and build the nodes,
        # and keep track of the parent. Then, later, connect the nodes together
        # into a tree
        # This is very similar to Root's, but it's not worth making
        # both unreadable/slow to shoe-horn them together...
        openBrackets = []
        parentage = {}
        nodes = {}
        nWords = 0
        for match in self.bracketsRE.finditer(text):
            open_, nodeData, null, close = match.groups()
            if open_:
                assert not close
                openBrackets.append((nodeData, match.start()))
            else:
                assert close
                nodeData, start = openBrackets.pop()                
                if nodeData.startswith('L'):
                    newNode = self._makeLeaf(nodeData, nWords)
                    nWords += 1
                else:
                    newNode = self._makeNode(nodeData)
                if openBrackets:
                    parentStart = openBrackets[-1][1]
                    parentage[newNode] = parentStart
                else:
                    top = newNode
                nodes[start] = newNode
        # Can use Root's method for this bit
        self._connectNodes(nodes, parentage)
        return top

    def _makeNode(self, nodeData):
        try:
            T, cat, headIdx, nChildren = nodeData.split()
        except:
            print >> sys.stderr, nodeData
            raise
        return CCGNode(label=CCG.Category(cat), headIdx=int(headIdx))

    def _makeLeaf(self, nodeData, wordID):
        L, cat, ccgPos, ptbPos, text, annotCat = nodeData.split()
        cat = CCG.Category(cat)
        parent = CCGNode(label=cat, headIdx=0)
        leaf = CCGLeaf(label=ptbPos, pos=ccgPos, text=text,
                       parg=cat, wordID=wordID)
        parent.attachChild(leaf)
        return parent
        
                            
                            
        
                    
                

    
