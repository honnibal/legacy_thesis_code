from rebanking.rebankers import Rebanker
import CCG
from Treebank.CCGbank import CCGNode


class FixNfPPToNPfPP(Rebanker):
    """
    Fix N/PP --> NP/PP, by moving intervening
    adnominals and punctuation to the N level
    (NP
      (NP/PP
        (NP/PP
          (N/PP
            (N/N intense)
            (N/PP competition)))
        (, ,))
      (PP )
    -->
    (NP
      (N
        (N/PP
          (N/PP
            (N/N intense)
            (N/PP competition)))
          (, ,))
        (PP )
      )
    )
    """
    def rebank(self, sentence):
        for node in sentence.depthList():
            if node.isRoot() or node.isLeaf():
                continue
            if self.match(node):
                self.change(node)
                
    def match(self, npfpp):
        if not npfpp.isProduction(selfType='NP/PP', left='N/PP'):
            return False
        return True

    def getNP(self, node):
        while not node.isRoot():
            if CCG.isIdentical(node.label, 'NP'):
                return node
            else:
                node = node.parent()
        print node
        raise StandardError

    def change(self, npfpp):
        np = self.getNP(npfpp)
        np.changeLabel(CCG.Category('N'))
        npfpp.delete()
        np.insert(CCGNode(label=CCG.Category('NP'), headIdx=0))

class DoAdjectivesAfterPP(Rebanker):
    """
    Currently there are many non-normal form derivations due to
    incorrect attachment position of the PP. Fix this up
    """
    pass

class TrimUnary(Rebanker):
    """
    Trim any unary productions which are X --> X
    """
    def rebank(self, sentence):
        for node in sentence.depthList():
            if self.match(node):
                self.change(node)
                
    def match(self, parent):
        if not parent.isUnary():
            return False
        if not CCG.isIdentical(parent.label, parent.child(0).label):
            return False
        return True

    def change(self, parent):
        c = parent.child(0)
        p = parent.parent()
        parent.delete()
