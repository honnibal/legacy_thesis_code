import CCG
from rebanking.rebankers import Rebanker

_partNouns = """All, Another, Average, Both, Each, Much, Several,
Some, Something, Those, all, another, any, anything, both, certain, each,
either, enough, few, five, half, little, million, most, much,
neither, nothing, one-fifth, one-third, other, part, plenty,
several, some, something, that, those, three,
three-fourths, two, %""".replace('\n', '').replace(' ', '').lower().split(',')

class PartitiveGenitive(Rebanker):
    """
    Transform partitive genitives:
    (NP
       (NP (DT *))
       (NP\NP
         ((NP\NP)/NP of)
         (NP )
       )
    )
    -->
    (NP
       (NP/PP (DT *))
       (PP
         (PP/NP of)
         (NP )
       )
    )
    """
    def match(self, np):
        # These checks are used by the unary case as well, so split them
        # off to be inherited
        if not self._checkNP(np):
            return False
        head = np.head()
        if not CCG.isIdentical(head.parg, 'NP'):
            return False
        return self._checkPP(np)

    def _checkNP(self, np):
        global _partNouns
        if not np.isProduction(selfType='NP', parent='NP', sibling=r'NP\NP'):
            return False
        # Heads must be in set of partitive nouns, or have label CD
        head = np.head()
        if head.text.lower() not in _partNouns and head.pos != 'CD':
            return False
        return True
        

    def _checkPP(self, np):
        pp = np.sibling()
        head = np.head()
        # Must have 'of' pp
        of = pp.head()
        if of.text.lower() != 'of':
            # Handle "something like" case as partitive genitive too
            if not (of.text.lower() == 'like' and
                    head.text.lower().endswith('thing')):
                return None
        return True

    def change(self, np):
        pp = np.sibling()
        np.changeLabel(CCG.addArg(np.label, 'PP', '/'))
        pp.changeLabel(CCG.Category('PP'))
        pp.headIdx = 1
        np.parent().headIdx = 1

class UnaryPartitiveGenitive(PartitiveGenitive):
    """
    Handle partitive genitives where there's a unary
    NP-->N rule
    """
    def match(self, np):
        if not self._checkNP(np):
            return False
        head = np.head()
        if CCG.isIdentical(head.parg, 'NP'):
            return False
        if not (len(np) == 1 and CCG.isIdentical(np.child(0).label, 'N')):
            return False
        return self._checkPP(np)

    def change(self, np):
        n = np.child(0)
        np.delete()
        pp = n.sibling()
        n.changeLabel(CCG.addArg(CCG.Category('NP'), CCG.Category('PP'), '/'))
        pp.changeLabel(CCG.Category('PP'))
        pp.headIdx = 1
        n.parent().headIdx = 1
            
        
