import CCG
from rebanking.rebankers import Rebanker
NPfNPbNP = CCG.Category(r'NP/(NP\NP)')
class NoisyTR(Rebanker):
    """
    Handles a noisy analysis:
    (NP/NP
      (NP/(NP\NP)
        (NP some))
      ((NP\NP)/NP of))
    (((N\N)/(S[dcl]\NP))\(NP/NP) which)
    to
    ( NP/NP
      ( (NP/NP)/(PP/NP) some )
      ( PP/NP of )
     )
     ((N\N)/(S[dcl]\NP))\(NP/NP)
     """
    def match(self, trNode):
        if not trNode.isProduction(selfType=NPfNPbNP,
                                   sibling=r'(NP\NP)/NP', parent=r'NP/NP'):
            return False
        if len(trNode) != 1:
            return False
        return True

    def change(self, trNode):
        np = trNode.child(0)
        pp = trNode.sibling()
        # Snip out the type raise node
        trNode.delete()
        # Snip out the child for NP --> unaries etc
        if np.isUnary():
            np.child(0).delete()
        # Make the label changes
        np.changeLabel(CCG.addArg(np.label, 'PP', '/'))
        pp.changeLabel(CCG.Category(r'PP/NP'))
