import CCG, general
from copy import deepcopy as copy
from Treebank import CCGBank
from Propbank import Propbank

class Predicate:
    """
    node
    entry
    branches
    arguments
    adjuncts
    trunk
    """
    def __init__(self, entry):
        self.node = entry.rel
        self.entry = entry
        self._branches = []
        self._branchNodes = {}
        self._arguments = []
        self._adjuncts = []
        self._trunk = []
        self._trunkNodes = {}
        self._pargIdx = {}

    def addBranch(self, branch):
        self._branches.append(branch)
        self._branchNodes[branch.node] = branch
        trunkNode = branch.node.sibling()
        self._trunk.append(trunkNode)
        self._trunkNodes[trunkNode] = branch
        branch.preds[self] = True
        pargIdx = self._pargIdx
        for parg in self.entry.pargs:
            for constituent in parg.refChain.constituents():
                if constituent == branch.node:
                    prevParg = pargIdx.get(branch, None)
                    if not prevParg:
                        pargIdx[branch] = parg
                    elif prevParg.label == 'ARGM' and parg.label != 'ARGM':
                        pargIdx[branch] = parg



    def removeBranch(self, branch):
        branch.preds.pop(self)
        self._branchNodes.pop(branch.node)
        i = self._branches.index(branch)
        trunk = branch.node.sibling()
        trunkNode = self._trunk[i]
        assert trunk == trunkNode
        self._trunk.pop(i)
        self._branches.pop(i)
        self._trunkNodes.pop(trunkNode)


    def branches(self):
        for branch in self._branches:
            yield branch

    def trunk(self):
        for trunk in self._trunk:
            yield trunk

    def priority(self, node):
        """
        Decide the 'priority' of the node, based on its parg label if it is
        a branch, or the last parg label if it is a trunk
        """
        if node in self._branchNodes:
            return self.branchPriority(self._branchNodes[node])
        elif node in self._trunkNodes:
            return self.branchPriority(self._trunkNodes[node])
        else:
            return 3


    def branchPriority(self, branch):
        parg = self.getParg(branch)
        if not parg:
            return 2
        if parg.label == 'ARGM':
            return 1
        else:
            return 0

    def trunkPriority(self, trunk):
        # Find the last branch
        branch = self._branchFromTrunk(trunk.node)
        if not branch:
            raise StandardError
        return self.branchPriority(branch)
            
    
    def getParg(self, branch):
        return self._pargIdx.get(branch, None)




    def trimNodes(self):
        """
        Trim branches and trunks after the last argument/adjunct
        """
        branches = [b for b in self.branches()]
        branches.reverse()
        print self.entry
        for branch in branches:
            priority = self.branchPriority(branch)
            if priority > 1:
                self.removeBranch(branch)
            else:
                break
                
                
                

        
    def truncateAt(self, node):
        """
        Truncate branch list at the given branch
        """
        branchNodes = self._branchNodes
        branches = self._branches
        trunks = self._trunk
        trunkNodes = self._trunkNodes
        branch = branchNodes.get(node, self._trunkNodes.get(node))
        if not branch:
            return None
        i = branches.index(branch)
        for branch in branches[i-1:]:
            self.removeBranch(branch)

    def traverseUp(self):
        """
        Generate (parent, uncle) nodes above the predicate until we hit a
        non-NP
        """
        node = self.node.parent()
        while not node.isRoot():
            parent = node.parent()
            innerResult = parent.label.innerResult()
            if innerResult != 'N' and innerResult != 'NP':
                break
            sibling = node.sibling()
            if not sibling:
                break
            yield (parent, sibling)
            node = parent


    def detachBranches(self):
        if not self._branches:
            return []
        left, right = self._stripBranches()
        attachOrder = self._getAttachOrder(left, right)
        self._setTrunkLabels(attachOrder)
        return attachOrder
        



    def reattachBranches(self, attachOrder):
        for trunkNode, branchAndType in zip(self.trunk(), attachOrder):
            direction, attachType, parent, branch = branchAndType
            parent.attachChild(branch.node)
            self._setBranchLabel(trunkNode, branch, direction, attachType)


    def oldReattachBranches(self):
        """
        Recalculate branch labels and attachment points based on the nombank labels
        """
        if not self._branches:
            return None
        left, right = self._stripBranches()
        attachOrder = self._getAttachOrder(left, right)
        self._setTrunkLabels(attachOrder)
        for trunkNode, branchAndType in zip(self.trunk(), attachOrder):
            parent = trunkNode.parent()
            direction, attachType, parent, branch = branchAndType
            parent.attachChild(branch.node)
            self._setBranchLabel(trunkNode, branch, direction, attachType)


    def __cmp__(self, other):
        return cmp(self.node, other.node)


    def __hash__(self):
        return hash(self.node)


    def _setBranchLabel(self, trunkNode, branch, direction, attachType):
        """
        Permutations:

        - Branch is argument
        - Branch is adjunct
        """
        if branch.node.label.isPunct():
            return None
        if branch.node.label == 'conj':
            return None
        if branch.node.label.conj:
            if branch.node.label != trunkNode.label:
                branch.node.changeLabel(copy(trunkNode.label))
                branch.node.label.conj = True
        elif attachType == 0:
            self._branchArg(trunkNode, branch, direction)
        else:
            self._branchAdjunct(trunkNode, branch, direction)

    

    def _branchAdjunct(self, trunk, branch, direction):
        """
        The new label will be an adjunct category on the inner result of the
        trunk. Assume the trunk label and its parent is correct
        """
        innerResult = trunk.label.innerResult()
        if direction == 0:
            slash = '\\'
        else:
            slash = '/'
        newLabel = CCG.ComplexCategory(copy(innerResult), copy(innerResult), slash, False)
        # Need to propagate better
        if newLabel != branch.node.label:
            branch.node.changeLabel(newLabel)


    def _branchArg(self, trunk, branch, direction):
        branchType = branch.getNodeCat()
        # Need to propagate better
        if branchType != branch.node.label:
            branch.node.changeLabel(branchType)
        print self.node.text
        print branch.node.parent()
        

    def _stripBranches(self):
        pargIdx = self._pargIdx
        left = []
        right = []
        pred = self.node
        for branch in self.branches():
            priority = self.branchPriority(branch)
            branch.node.prune()
            if branch.node < self.node:
                left.append((priority, branch))
            else:
                right.append((priority, branch))
        return left, right



    def _getAttachOrder(self, left, right):
        newBranches = []
        for trunkNode in self.trunk():
            parent = trunkNode.parent()
            if not left:
                newBranches.extend([(0, sorter, parent, branch) for sorter, branch in right])
                break
            elif not right:
                newBranches.extend([(1, sorter, parent, branch) for sorter, branch in left])
                break
            elif left[0] < right[0]:
                sorter, branch = left.pop(0)
                newBranches.append((1, sorter, parent, branch))
            else:
                sorter, branch = right.pop(0)
                newBranches.append((0, sorter, parent, branch))
        return newBranches


    def _setTrunkLabels(self, attachOrder):
        """
        Set the labels of the trunk nodes, moving downwards and adding arguments
        """
        argCats = self._getArgCats(attachOrder)
        trunkNodes = [n for n in self.trunk()]
        currCat = trunkNodes[0].label.innerResult()
        if trunkNodes[0].label.conj:
            raise StandardError
        trunkNodes.reverse()
        argCats.reverse()
        for trunkNode in trunkNodes:
            arg = argCats.pop(0)
            if arg:
                argLab, slash = arg
                currCat = CCG.ComplexCategory(copy(currCat), copy(argLab), slash, trunkNode.label.conj)
            if False:
                trunkNode.label = copy(currCat)
                trunkNode.label.conj = True
            else:
                trunkNode.label = copy(currCat)
        trunkNodes.reverse()



    def _getArgCats(self, attachOrder):
        """
        Get the categories of the argument branches. If the branch isn't an argument, add a place-holder
        """
        args = []
        for direction, attachType, parent, branch in attachOrder:
            if attachType == 0:
                argCat = branch.getNodeCat()
                if direction == 0:
                    slash = '/'
                else:
                    slash = '\\'
                args.append((argCat, slash))
            else:
                args.append(None)
        return args



        


    

class Branch:
    """
    node
    predicates
    """
    def __init__(self, node):
        self.node = node
        self.preds = {}


    def decidePred(self):
        """
        Decide which predicate the branch belongs to
        """
        if len(self.preds) == 1:
            return None
        

    def __str__(self):
        text = [w.text for w in self.node.listWords()]
        return ' '.join(text)



    def getNodeCat(self):
        node = self.node
        if node.label.innerResult() == 'S':
            return node.label
        if node.head().label == 'IN':
            cat = CCG.Category('PP')
            return cat
        if node.label == 'conj':
            return node.label
        else:
            cat = CCG.Category('NP')
        cat.conj = node.label.conj
        return cat
        
    

class Argument:
    """
    parg
    """
    pass

class Adjunct(Argument):
    pass

def initPreds(entries):
    preds = []
    for entry in entries:
        predicate = Predicate(entry)
        preds.append(predicate)
    return preds

def initBranchesAndTrunks(predicates):
    branches = {}
    trunks = {}
    for predicate in predicates:
        for parent, sibling in predicate.traverseUp():
            if sibling in branches:
                branch = branches[sibling]
            else:
                branch = Branch(sibling)
            predicate.addBranch(branch)
            branches[sibling] = branch
           # if parent in trunks:
           #     trunk = trunks[parent]
           # else:
           #     trunk = Trunk(parent)
           # predicate.addTrunk(trunk)
        predicate.trimNodes()
#            if not isNoun(parent):
#                break
    return branches

def allocateBranches(predicates):
    for pred in predicates:
        for branch in pred.branches():
            decorated = [(pred.priority(branch.node), pred) for pred in predicates]
            decorated.sort()
            # Remove all branches after this one for the other predicates
            if decorated[0] == 3:
                raise StandardError
            for sorter, predicate in decorated[1:]:
                predicate.truncateAt(branch.node)


def reattachBranches(preds):
    predsAndBranches = []
    for pred in preds:
        branches = pred.detachBranches()
        predsAndBranches.append((pred, branches))
    for pred, branches in predsAndBranches:
        if branches:
            pred.reattachBranches(branches)
        
    

            

def preprocess(sentence):
    """
    Change all N to NP
    """
    for node in sentence.depthList():
        if node.isLeaf():
            label = node.parg
        else:
            label = node.label
        if label == 'N':
            if label.conj:
                newLabel = CCG.Category('NP[conj]')
            else:
                newLabel = CCG.Category('NP')
            node.changeLabel(newLabel)
        elif label.isComplex() and label.argument.cat == 'N':
            newLabel = CCG.ComplexCategory(copy(label.result), CCG.Category('NP'), label.slash, label.conj)
            node.changeLabel(newLabel)

def main(entries):
    preds = initPreds(entries)
    branches = initBranchesAndTrunks(preds)
    allocateBranches(preds)
   # reattachBranches(preds)
    for pred in preds:
        pred.oldReattachBranches()
         
                
if __name__ == '__main__':
    corpus = CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/AUTO')
    nombank = Propbank.Propbank('/home/mhonn/code/mhonn/CCG/corpusReform/alignment/ccgNombank.txt', False)
    f = corpus.child(10)
    import Treebank.NodeVisitors
    printer = Treebank.NodeVisitors.NodePrinter()
    general.DEBUG_LEVEL = -1
    for sentence, entries in nombank.fileEntries(f):
        preprocess(sentence)
        print printer.actOn(sentence)
        main(entries)
        print printer.actOn(sentence)
        break
