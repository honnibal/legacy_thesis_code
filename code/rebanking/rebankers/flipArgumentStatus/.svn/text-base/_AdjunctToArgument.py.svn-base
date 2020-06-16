import CCG
from Treebank import CCGbank
from _PARGRebanker import PARGRebanker

class AdjunctToArgument(PARGRebanker):
    """
    Changes adjuncts to arguments
    """
    def match(self, parg, argument):
        if parg.label == 'rel':
            return False
        if argument.isRoot() or argument.isLeaf():
            return False
        # Exclude by-agents of passives
        if parg.label == 'ARG0' and argument.head().text.lower() == 'by' and \
           CCG.isIdentical(argument.label, r'(S\NP)\(S\NP)'):
            return False
#        if argument.label.conj or argument.sibling().label.conj:
#            return False
        # isAdjunct instead of adjunctResult because of wsj_0017.2
        isAdjunct = bool(argument.label.isAdjunct() or \
                         argument.label.isAux())
        return bool(isAdjunct and parg.label != 'ARGM' and
                    parg.label.startswith('ARG')
                    and self.canChange(parg, argument))
        
    def doParg(self, arg, head):
        argLabel = self.argLabeller(arg)
        # If there's a unary node, exploit it
        # This is a problem for hat
        if arg.isUnary():
            child = arg.child(0)
            assert not child.label.isAdjunct()
            arg.delete()
            arg = child
        argLabel = CCG.Category(argLabel)
        arg.changeLabel(argLabel)
        # Add NP node when you would make arg label N
        # This is a problem for hat
        if CCG.isIdentical(argLabel, 'N') and head.label.innerResult() == 'S':
            newNode = CCGbank.CCGNode(label=CCG.Category('NP'), headIdx=0)
            arg.insert(newNode)
            arg = newNode
        newLabel = CCG.addArg(head.label, arg.label,self.getArgSlash(arg, head))
        head.changeLabel(newLabel)
        # Update PARGs
        pred = head.head()
        argHead = arg.head()
        for i, slot in enumerate(argHead.stag.goldDeps):
            if any(w for w, l in slot if w is pred):
                argHead.stag.goldDeps.pop(i)
                break
        slot = len(head.label.arguments)
        # Update headIdx
        if argLabel == 'PP' and arg.length() == 2:
            arg.headIdx = 1
        deps = [(h, 'L') for h in arg.heads()]
        pred.stag.goldDeps.insert(slot + 1, deps)
        
        
        
        
        
        
    def canChange(self, parg, argument):
        """
        Constraint 1: don't add leftward arguments
        Constraint 2: don't add arguments for compound nouns
        """
        if not argument.listWords():
            return False
        # Don't let adverbs be arguments, e.g. wsj_0011.3
        if argument.head().label == 'RB':
            return False
        head = argument.sibling()
        if head is None:
            return False
        
        argLabel = self.argLabeller(argument)
        if not argLabel:
            return False
        argLabel = CCG.Category(argLabel)
        # Experiment with N\N arguments
       # if self.resource == 'nombank' and argument.label == 'N/N' and \
       #    head.label.innerResult() ==  'N' and \
       #    not head.label.adjunctResult():
       #     return True
        # These constraints block N/N from becoming arguments
        # e.g. 'decision maker'
        if head > argument:
            return False
        if head.label.innerResult() == 'N' and \
           argLabel.innerResult() == 'N':
            return False
        else:
            return True

    def argLabeller(self, constituent):
        # If it was a unary transformation, use the child label
        if constituent.length() == 1:
            child = constituent.child(0)
            if not child.isLeaf() and not child.label.isAdjunct():
                return child.label
        # If it was a punct-cued binary rule, use the child label
        else:
            nonHead = constituent.child(constituent.headIdx-1)
            child = constituent.child(constituent.headIdx)
            if (nonHead.label.isPunct() or nonHead.label == 'conj') and \
               child.label != constituent.label:
                assert not constituent.label.conj
                return constituent.child(constituent.headIdx).label
        head = constituent.head()
        if head.label == 'DT' and head.stag == r'((S\NP)\(S\NP))/N':
            return 'NP'
        elif head.label.startswith('N') or head.label.startswith('P') or head.label.startswith('J'):
            return 'N'
        elif head.parg == CCG.N or head.parg == CCG.NP:
            return 'NP'
        elif head.text == 'that' and head.stag.argument.innerResult() == 'S':
            return 'S[em]'
        elif head.parg.adjunctResult():
            return 'PP'
        else:
            return None
