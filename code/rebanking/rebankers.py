import sys

import CCG

class Rebanker(object):
    def rebank(self, entries):
        for entry in entries:
            for parg in entry.pargs:
                if parg.constituent and self.match(parg, parg.constituent):
                    self.doParg(parg, parg.constituent)

    def match(self, parg, constituent):
        pass

    def doParg(self, parg, constituent):
        pass

class ArgAdjunctFlipper(Rebanker):
    """
    Changes arguments to adjuncts or adjuncts to arguments
    """
    

    def canChange(self, parg, argument):
        return True

    def doParg(self, parg, constituent):
        head = constituent.sibling()
        print >> sys.stderr, parg
        return self.flipArgAdjunct(constituent, head)

    def getArgSlash(self, arg, head):
        if arg > head:
            return '/'
        else:
            return '\\'

    def getAdjSlash(self, arg, head):
        if arg > head:
            return '\\'
        else:
            return '/'

class ArgumentToAdjunct(ArgAdjunctFlipper):
    """
    Changes arguments to adjuncts
    """
    def match(self, parg, argument):
        isAdjunct = bool(argument.label.adjunctResult() or \
                         argument.label.isAux())
        return bool(isAdjunct and parg.label == 'ARGM' and \
                    self.canChange(parg, argument))
        
    def flipArgAdjunct(self, arg, head):
        slash = self.getAdjSlash(arg, head)
        adjunctCat = CCG.makeAdjunct(head.label, slash, True)
        # Using parent's label automatically handles type-raising too
        head.changeLabel(head.parent().label)
        arg.changeLabel(adjunctCat)

class AdjunctToArgument(ArgAdjunctFlipper):
    """
    Changes adjuncts to arguments
    """
    def match(self, parg, argument):
        isAdjunct = bool(argument.label.adjunctResult() or \
                         argument.label.isAux())    
        return bool(isAdjunct and parg.label.startswith('ARG')
                    and self.canChange(parg, argument))
        
    def flipArgAdjunct(self, arg, head):
        argLabel = self.argLabeller(arg)
        if not argLabel:
            return None
        argLabel = CCG.Category(argLabel)
        newHeadLabel = head.parent().label
        arg.changeLabel(argLabel)
        slash = self.getArgSlash(arg, head)
        newLabel = CCG.addArgs(head.label, [(argLabel, slash, False)])
        head.changeLabel(newLabel)

    def canChange(self, parg, argument):
        """
        Constraint 1: don't add leftward arguments
        Constraint 2: don't add arguments for compound nouns
        """
        head = argument.sibling()
        if head > argument:
            return False
        if head.label.innerResult() == 'N' and \
           argument.label.innerResult() == 'N':
            return False
        else:
            return True

    def argLabeller(self, constituent):
        # If it was a unary transformation, use the child label
        if constituent.length() == 1:
            child = constituent.child(0)
            if not child.isLeaf() and not child.label.isAdjunct():
                return child.label
        head = constituent.head()
        if head.label.startswith('N') or head.label.startswith('P') or head.label.startswith('J'):
            return 'N'
        elif head.parg == CCG.N or head.parg == CCG.NP:
            return 'NP'
        elif head.parg.adjunctResult():
            return 'PP'
        else:
            return None



