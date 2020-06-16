import CCG
from rebanking.rebankers import Rebanker
from Treebank import CCGbank

class PiedPiping(Rebanker):
    """
    Fix pied-piped prepositions
    ((N\N)/S[dcl]
        ((NP\NP)/NP under)
        (((N\N)/S[dcl])\((NP\NP)/NP) which))
    """
    def match(self, node):
        if not node.isProduction(selfType=r'(NP\NP)/NP'):
            return False
        sibling = node.sibling()
        # If sibling comes after node and applies it, valid
        if sibling < node:
            return False
        if not CCG.isIdentical(sibling.label.argument, r'(NP\NP)/NP'):
            return False
        return True

    def change(self, node):
        sibling = node.sibling()
        newLabel = CCG.addArg(sibling.label.result, r'(N\N)/NP', '\\')
        sibling.changeLabel(newLabel)
        node.changeLabel(CCG.Category('(N\N)/NP'))

class BinariseNonRestrictive(Rebanker):
    """
    Non-restrictive relatives are now identified by punctuation,
    so make unary NP\NP --> S[pss]\NP productions binary
    
    (, )
    (NP\NP
      (S[pss]\NP )
    )
    -->
    (NP\NP
      (, )
      (S[pss]\NP )
    )
    """
    reducedRelative = 0
    def match(self, node):
        if not node.isUnary():
            return False
        if not CCG.isIdentical(node.label, r'NP\NP'):
            return False
        if (not node.sibling()) or node.sibling().label.conj:
            return False
        punct = self.getPunct(node)
        if not punct:
            return False
        return True

    def change(self, node):
        BinariseNonRestrictive.reducedRelative += 1
        punct = self.getPunct(node)
        punct.parent().delete()
        punct.reattach(node)

    def getPunct(self, node):
        if not node > node.sibling():
            return False
        previousWord = node.sibling().getWord(-1)
        if not previousWord.isPunct():
            return False
        if previousWord.label == 'RQU':
            return False
        return previousWord.parent()


class NAttachNP(Rebanker):
    """
    Handle cases like "those leading the pack"
    Done in post-process to avoid interfering with partitive genitives etc
    It's a bad analysis, so leave to last.
    """
    def match(self, adnom):
        if not adnom.isProduction(selfType=r'NP\NP', parent='NP', sibling='NP'):
            return False
        np = adnom.sibling()
        if not np.child(0).isLeaf():
            return False
        return True

    def change(self, adnom):
        np = adnom.sibling()
        n = CCGbank.CCGNode(label=CCG.Category('N'), headIdx=0)
        for child in np.children():
            child.reattach(n)
            child.changeLabel(CCG.Category('N'))
        np.attachChild(n)
        adnom.move(n, 0)
        adnom.changeLabel(CCG.Category(r'N\N'))


      
        
    
