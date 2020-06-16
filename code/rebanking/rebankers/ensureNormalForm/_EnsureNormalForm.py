from rebanking.rebankers import Rebanker
import CCG
from Treebank import CCGbank
from CCG.Rules import fComp, gfComp, bComp, bxComp, gbComp, gbxComp

class EnsureNormalForm(Rebanker):
    def match(self, node):
        """
        Find nodes that is the parent of a composition production,
        and who is the functor of its production
        with the same directionality as the composition
        Does not handle punctuation problems, e.g. wsj_0018.20
        """
        if node.length() != 2:
            return False
        if not node.sibling():
            return False
        left, right = node.children()
        direction = self._isComposition(node.label, left.label, right.label)
        if direction is False:
            return False
        p = node.parent()
        left, right = p.children()
        production = CCGbank.Production(left.label, right.label, p.label)
        if production.label not in ['a', 't']:
            return False
        if not CCG.isIdentical(production.functor, node.label):
            return False
        if direction != node.label.slash:
            return False
        return True

    def _isComposition(self, parent, left, right):
        
        fwdComp = set((fComp, gfComp))
        bwdComp = set((bComp, bxComp, gbComp, gbxComp))
        l = CCG.Category(str(left))
        r = CCG.Category(str(right)) if right else None
        for rule in fwdComp.union(bwdComp):
            produced = rule(l, r)
            if produced:
                if CCG.isIdentical(produced, parent):
                    if rule in fwdComp:
                        return '/'
                    else:
                        return '\\'
                else:
                    l = CCG.Category(str(left))
                    r = CCG.Category(str(right))
            
        else:
            return False

    def change(self, node):
        """
        (X
          (X/Y <-- node
            (X/X)
            (X/Y)) <-- head
          (Y)) <-- arg
        -->
        (X
          (X/X)
          (X <-- parent
            (X/Y)
            (Y)))
        """
        # This is more reliable than headIdx, because
        # we tested directionality of composition above,
        # and verified it corresponds to node's directionality.
        # See wsj_0004.2
        if node.label.slash == '/':
            head = node.child(1)
        else:
            head = node.child(0)
        arg = node.sibling()
        parent = arg.move(head, arg.parent().headIdx)
        parent.changeLabel(parent.label.result)
        
