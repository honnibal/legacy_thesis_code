import CCG
from rebanking.rebankers import Rebanker
from Treebank import CCGbank

class NCoord(Rebanker):
    """
    Change case where NP coordinates after raising to NP
    (NP
      (N president)
    (NP[conj]
      (NP
        (N CEO)
       )
       and
    )
    """
    def match(self, np):
        if not np.isProduction(selfType='NP', left='NP'):
            return False
        if np.length() != 2:
            return False
        leftNP, conjNP = np.children()
        if not conjNP.label.conj:
            return False
        if not leftNP.isUnary():
            return False
        leftN = leftNP.child(0)
        if not leftN.label == CCG.N:
            return False
        rightNP = conjNP.child(1)
        if not rightNP.isUnary():
            return False
        rightN = rightNP.child(0)
        if not rightN.label == CCG.N:
            return False
        return True

    def change(self, np):
        leftNP, conjNP = np.children()
        rightNP = conjNP.child(1)
        leftNP.delete()
        rightNP.delete()
        np.changeLabel(CCG.Category('N'))
        newParent = CCGbank.CCGNode(label=CCG.Category('NP'), headIdx=0)
        np.insert(newParent)
        
