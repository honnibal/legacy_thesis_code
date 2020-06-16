import CCG
from rebanking.rebankers import Rebanker

class NAttach(Rebanker):
    applied = 0
    nonRestrictive = 0
    restrictiveRelative = 0
    nonRestrictiveRelative = 0
    def match(self, adnom):
        # Find NP --> NP NP\NP production
        if not adnom.isProduction(selfType=r'NP\NP', parent='NP', sibling='NP'):
            return False
        # Don't change em-dashes etc e.g. wsj_0013.14
        if adnom.head().isPunct():
            return False
        n = self._getN(adnom)
        return bool(n)

    def change(self, adnom):
        NAttach.applied += 1
        if adnom.head().stag.innerResult() == 'S' or \
           adnom.sibling().head().label.startswith('W'):
            NAttach.restrictiveRelative += 1
        
        n = self._getN(adnom)
        adnom.move(n, 0)
        adnom.changeLabel(CCG.Category('N\N'))

    def _getN(self, adnom):
        """
        Find the lowest N node that still has a word boundary with the
        adnominal, but isn't made with a conjunction. Return None
        if there's no such node
        """
        np = adnom.sibling()
        assert np < adnom
        adnomEdge = adnom.getWord(0).wordID
        n = np.head().parent()
        nEdge = n.getWord(-1).wordID + 1
        if np.getWord(-1).isPunct():
            NAttach.nonRestrictive += 1
            if adnom.head().stag.innerResult() == 'S' or \
               adnom.head().label.startswith('W'):
                NAttach.nonRestrictiveRelative += 1
        while (adnomEdge != nEdge) or not CCG.isIdentical(n.label.morphLess(),
                                                          CCG.N) \
              or n.parent().label.conj:
            if n is np:
                return None
            n = n.parent()
            nEdge = n.getWord(-1).wordID + 1
        return n
        
