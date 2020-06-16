import copy

from rebanking.rebankers import Rebanker
import CCG
from Treebank import CCGbank


class RemoveNB(Rebanker):
    """
    Kill the dastardly [nb] feature
    """
    def match(self, node):
        if 'nb' not in str(node.label):
            return False
        return True

    def change(self, node):
        label = str(node.label).replace('[nb]', '')
        
        node.changeLabel(CCG.Category(label))

class FixNPtoAdverbAttach(Rebanker):
    """
    Fix annotation errors like wsj_0004.2:
    ((S\NP)\(S\NP)
      (NP a fraction)
    )
    (((S\NP)\(S\NP))\((S\NP)\(S\NP)) )
    -->
    ((S\NP)\(S\NP)
      (NP a fraction)
      (NP\NP of a percent)
    )
    """
    def match(self, node):
        # This seems to do more harm than good
        return False
        if not node.isProduction(selfType=r'(S\NP)\(S\NP)',
                                 sibling=r'((S\NP)\(S\NP))\((S\NP)\(S\NP))'):
            return False
        if not (node.isUnary() or
                node.child(0).label == r'((S\NP)\(S\NP))/N'):
            return False
        siblingHead = node.sibling().head()
        adverbAdjunctPP = r'(((S\NP)\(S\NP))\((S\NP)\(S\NP)))/NP'
        if not CCG.isIdentical(siblingHead.stag, adverbAdjunctPP):
            return False
        return True

    def change(self, adverb):
        if not adverb.isUnary():
            np = CCGbank.CCGNode(label=adverb.label,
                                 headIdx=1)
            for child in adverb.children():
                child.reattach(np)
            np.changeLabel(CCG.Category('NP'))
            adverb.attachChild(np)
        else:
            np = adverb.child(0)
        sibling = adverb.sibling()
        sibling.move(np, 0)
        sibling.changeLabel(CCG.Category(r'NP\NP'))
        

class FixPredeterminer(Rebanker):
    """
    Fix error where pre-determiners are attached to the determiner,
    rather than attached as NP/NP, ala wsj_0092.1
    (NP
      (NP/N
        (NP/NP half)
        (NP/N his)
      )
      (N money)
    )
    -->
    (NP
      (NP/NP half)
      (NP
        (NP/N his)
        (N money)
      )
    )
    """
    def match(self, preDet):
        if not preDet.isProduction(selfType=r'NP/NP', parent=r'NP/N',
                                   sibling=r'NP/N'):
            return False
        # For noise case in wsj_0351.50
        uncle = preDet.parent().sibling()
        if not CCG.isIdentical(uncle.label, 'N'):
            return False
        return True

    def change(self, preDet):
        det = preDet.sibling()
        n = preDet.parent().sibling()
        np = CCGbank.CCGNode(label=CCG.Category('NP'), headIdx=1)
        n.insert(np)
        det.reattach(np)
        preDet.parent().delete()
        
class FixNominalNounAdjuncts(Rebanker):
    """
    Nominal adjuncts like "last month" sometimes occur as NP\NP.
    "Blame" the determiner the same way we do for verbal adjuncts.
    
    (NP\NP
      ((NP\NP)/(NP\NP) last)
      (NP\NP month)))
    )
    -->
    (NP\NP
      ((NP\NP)/N )
      (N )
    """
    def match(self, det):
        if not det.isProduction(selfType=r'(NP\NP)/(NP\NP)', sibling=r'NP\NP'):
            return False
        if len(det.listWords()) > 1:
            return False
        if det.getWord(0).text.lower() not in ['last', 'next', 'early']:
            return False
        if det.getWord(0).label not in ['DT', 'JJ']:
            return False
        sib = det.sibling()
        if not sib.head().label.startswith('N'):
            return False
        
        return True

    def change(self, det):
        sib = det.sibling()
        det.changeLabel(CCG.Category(r'(NP\NP)/N'))
        sib.changeLabel(CCG.Category('N'))

class FixQuantifiedNP(Rebanker):
    """
    Some quantifiers affect determinate NPs directly. They're analysed
    badly in CCGbank
    (NP
      (NP/N
        (NP/N all )
        (NP\NP its )
      )
    N
    -->
    (NP
      (NP/NP )
      (NP
        (NP/N )
        (N )
      )
    )
    """
    def match(self, quantifier):
        if not quantifier.isProduction(selfType=r'NP[nb]/N', sibling=r'NP\NP',
                                parent='NP[nb]/N'):
            return False
        n = quantifier.parent().sibling()
        if not CCG.isIdentical(n.label, 'N'):
            return False
        return True

    def change(self, quantifier):
        # Very round about way of doing this because I couldn't get
        # the more direct move to work :(
        det = quantifier.sibling()
        n = det.parent().sibling()
        
        det.move(n, 1)
        det.changeLabel(CCG.Category('NP[nb]/N'))
        det.parent().changeLabel(CCG.Category('NP'))
        quantifier = det.parent().sibling()
        quantifier.changeLabel(CCG.Category('NP/NP'))

class FixConjConj(Rebanker):
    """
    Fix CCGbank error where a comma is used as a conj immediately before
    an actual conjunction
    (NP[conj]
      (conj )
      (NP[conj]
       (, ,)
       (NP )
      )
    )
    -->
    (NP[conj]
      (conj )
      (NP
       (, ,)
       (NP )
      )
    )
    """
    def match(self, conj):
        if not conj.label == 'conj':
            return False
        if not conj.sibling().label.conj:
            return False
        if not conj.parent().label.conj:
            return False
        return True

    def change(self, conj):
        sibling = conj.sibling()
        newLabel = copy.deepcopy(sibling.label)
        newLabel.conj = False
        sibling.changeLabel(newLabel)

class FixWhoseApposition(Rebanker):
    """
    Fix rare error where an appositive is attached badly at NP level
    when the category isn't NP
    ((NP\NP)/(S[dcl]\NP)
      ((NP\NP)/(S[dcl]\NP)
        (((NP\NP)/(S[dcl]\NP))/N whose)
        (N
          (N/N new)
          (N novel)))
      (, ,))
    ((NP\NP)\(NP\NP)
    -->
    ((NP\NP)/(S[dcl]\NP)
      ((NP\NP)/(S[dcl]\NP)
        (((NP\NP)/(S[dcl]\NP))/N whose)
        (N
          (N
            (N/N new)
            (N novel)))
          (N[conj]
            (, ,)
            (N
        )
    """
    def match(self, whose):
        if not whose.isProduction(selfType=r'(NP\NP)/(S[dcl]\NP)',
                                  sibling=r'(NP\NP)\(NP\NP)'):
            return False
        if whose.length() == 1:
            return False
        child, comma = whose.children()
        # Errors like wsj_0983.18 still to be fixed
        if not comma.label.isPunct():
            return False
        if child.length() == 1:
            return False
        return True

    def change(self, whose):
        apposed = whose.sibling()
        child, comma = whose.children()
        det, n = child.children()
        assert n.label == 'N'
        nConj = CCGbank.CCGNode(label=CCG.Category(r'N[conj]'), headIdx=1)
        comma.reattach(nConj)
        apposed.changeLabel(CCG.Category('N'))
        apposed.reattach(nConj)
        n.insert(CCGbank.CCGNode(label=CCG.Category(r'N'), headIdx=0))
        n.parent().attachChild(nConj)
        
class FixPunctHeads(Rebanker):
    def match(self, punct):
        if not punct.label.isPunct():
            return False
        sibling = punct.sibling()
        if not sibling:
            return False
        if sibling.label.isPunct():
            return False
        if not sibling:
            return False
        parent = punct.parent()
        if punct < sibling and parent.headIdx == 1:
            return False
        elif punct > sibling and parent.headIdx == 0:
            return False
        return True

    def change(self, punct):
        sibling = punct.sibling()
        if punct < sibling:
            punct.parent().headIdx = 1
        else:
            punct.parent().headIdx = 0


class FixNfNDeterminer(Rebanker):
    def match(self, node):
        if not node.isProduction(selfType='N', left='N/N', right='N',
                                 parent='NP'):
            return False
        if self.headIdx != 0:
            return False
        if node.head().label != 'DT':
            return False
        return True

    def change(self, node):
        left = node.child(0)
        node.delete()
        left.changeLabel(CCG.Category(r'NP/N'))
        left.parent().headIdx = 1
        

class FixVPVPfPP(Rebanker):
    """
    Fix stupid --|((S\NP)\(S\NP))/PP PP construction
    """
    def match(self, node):
        sibling = node.sibling()
        if not sibling:
            return False
        if not CCG.isIdentical(sibling.label, CCG.PP):
            return False
        if not CCG.isIdentical(node.label.argument, CCG.PP):
            return False
        if not node.label.result.isAdjunct():
            return False
        if not node.head().text == '--':
            return False
        return True

    def change(self, node):
        pp = node.sibling()
        pp.changeLabel(node.label.result)
        node.changeLabel(CCG.Category(':'))
