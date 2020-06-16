#!/usr/bin/python2.4
"""
Classify a CCG category into a heirarchy
"""
import CCG, re
class HeirNode(object):
    def __init__(self, parent):
        self.parent = parent
        self.nodes = []
        self.name = self.__class__.__name__
        self.setNodes()
        
    def setNodes(self):
        pass

    def addNode(self, node):
        self.nodes.append(node(self))
    
    def classify(self, category):
        for node in self.nodes:
            if node.accept(category):
                if not node.nodes:
                    return node
                else:
                    return node.classify(category)
                

    def accept(self, category):
        pass

    def printParents(self):
        parent = self
        parents = []
        while parent and parent.name != 'Top':
            if not parent.name.startswith('_'):
                parents.append(parent.name)
            parent = parent.parent
        parents.reverse()
        return '/'.join(parents)

    

class Top(HeirNode):
    def accept(self, category):
        raise StandardError

    def setNodes(self):
        self.addNode(Adj)
        self.addNode(Arg)

class Adj(HeirNode):
    def accept(self, category):
        if not category.isComplex():
            return False
        if category.isAdjunct():
            return True
        for result, argument, slash, hat in category.deconstruct():
            if result.isAdjunct():
                return True
        else:
            return False

    def setNodes(self):
        self.addNode(_Class)

    

class _Class(HeirNode):
    def accept(self, category):
        return True

    def setNodes(self):
        self.addNode(Nom)
        self.addNode(Pred)
        self.addNode(Adv)
        self.addNode(PP)
        self.addNode(Punct)
        self.addNode(Conj)
        self.addNode(Misc)


class Nom(HeirNode):
    def accept(self, category):
        inner = category.innerResult()
        if inner == CCG.N or inner == CCG.NP:
            return True
        else:
            return False

    def setNodes(self):
        self.addNode(N)
        self.addNode(NP)

class Pred(HeirNode):

    def accept(self, category):
        inner = category.innerResult()
        if inner == CCG.S and not CCG.isIdentical(inner, 'S[adj]'):
            return True
        else:
            return False

    


class Adv(HeirNode):
    def accept(self, category):
        inner = category.innerResult()
        if CCG.isIdentical(inner, 'S[adj]'):
            return True
        else:
            return False

    def setNodes(self):
        self.addNode(BefSubj)
        self.addNode(AftSubj)
        self.addNode(SAdj)
        self.addNode(Misc)


class BefSubj(HeirNode):
    def accept(self, category):
        s = CCG.Category(r'S')
        for result, argument, slash, hat in category.deconstruct():
            if CCG.isIdentical(result, s) and CCG.isIdentical(argument, CCG.NP):
                return True
        else:
            return False


class AftSubj(HeirNode):
    def accept(self, category):
        s = CCG.Category(r'S')
        for result, argument, slash, hat in category.deconstruct():
            if CCG.isIdentical(result, s) and CCG.isIdentical(argument, s):
                return True
        else:
            return False

class PP(HeirNode):
    def accept(self, category):
        pp = category.innerResult()
        if pp == 'PP':
            return True
        else:
            return False

class Punct(HeirNode):
    def accept(self, category):
        if category.isPunct():
            return True
        else:
            return False

class Conj(HeirNode):
    def accept(self, category):
        if category == 'conj':
            return True
        else:
            return False


class SAdj(HeirNode):
    def accept(self, category):
        inner = category.innerResult()
        if CCG.isIdentical(inner, 'S[adj]'):
            return True
        else:
            return False

class Misc(HeirNode):
    def accept(self, category):
        return True


class N(HeirNode):
    name = 'N'
    def accept(self, category):
        inner = category.innerResult()
        if inner == CCG.N:
            return True
        else:
            return False

class NP(HeirNode):
    def accept(self, category):
        inner = category.innerResult()
        if inner == CCG.NP:
            return True
        else:
            return False

class Arg(HeirNode):
    def accept(self, category):
        if not category.isAdjunct():
            return True
        else:
            return False

    def setNodes(self):
        self.addNode(_Class)


        

def getMUCats(muLoc):
    catRE = re.compile(r'(?<=\n)[^=\s#]+')
    cats = {}
    for cat in catRE.findall(open(muLoc).read()):
        cats[cat] = True
    return cats

def classify(category):
    return tree.classify(category).printParents()


tree = Top(None)

if __name__ == '__main__':
    tests = [
        r'NP\NP',
        r'N',
        r'((S\NP)\(S\NP))/NP',
        r'PP/NP',
        r'((S\NP)\(S\NP))/NP',
        r'(NP\NP)/NP',
        r'N/N',
        r'PP/NP',
        r'(NP\NP)/(NP\NP)',
        r'(N/N)/(N/N)',
        r'(NP\NP)/NP',]
    #for test in tests:
    #    cat = CCG.Category(test)
    #    node = tree.classify(cat)
    #    print cat
    #    print node.printParents()
    muCats = getMUCats('/home/mhonn/Data/markedupFiles/markedup_v1')
    for cat in muCats:
        node = tree.classify(CCG.Category(cat))
        print node.printParents(),
        print cat


