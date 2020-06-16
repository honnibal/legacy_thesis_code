import CCG
from Treebank.CCGbank import Production

from _PARGRebanker import PARGRebanker

class ArgumentToAdjunct(PARGRebanker):
    """
    Changes arguments to adjuncts
    """
    def match(self, parg, argument):
        
        if argument.isRoot() or argument.isLeaf():
            return False
        if not argument.listWords():
            return False
        sibling = argument.sibling()
        if not sibling:
            return False
        if argument.label.conj or sibling.label.conj:
            return False
        if CCG.isIdentical(argument.label, 'conj') or \
           CCG.isIdentical(sibling.label, 'conj'):
            return False
        if parg.label != 'ARGM':
            return False
        if argument.label.adjunctResult():
            return False
        if argument.label.isAux():
            return False
        # Don't allow argments that are currently functors at all
        l, r = sorted((argument, sibling))
        production = Production(l.label, r.label, argument.parent().label)
        if production.functor == argument.label:
            return False
        if argument.label == 'NP/N':
            return False
        elif argument.label == 'NP/(N/PP)':
            return False
        head = argument.sibling()
        # Added to deal with noisy Propbank cases e.g. wsj_0326.1
        if head.label.isAdjunct():
            return False
        return self.canChange(parg, argument)
        
    def doParg(self, arg, head):
        slash = self.getAdjSlash(arg, head)
        # Using parent's label automatically handles type-raising too
        # Change parent before adjunct so that we don't make the adjunction
        # invalid
        head.changeLabel(head.parent().label)
        adjunctCat = CCG.makeAdjunct(arg.sibling().label, slash, True)
        # This is a problem for hat
        if arg.isUnary():
            # Delete unary rules, but leave N there so that change label forms
            # N --> NP
            child = arg.child(0)
            if child.label != 'N':
                arg.delete()
                arg = child
        arg.changeLabel(adjunctCat)
        # Update pargs
        pred = head.head()
