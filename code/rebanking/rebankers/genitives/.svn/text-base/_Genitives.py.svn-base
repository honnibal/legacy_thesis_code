import CCG
from rebanking.rebankers import Rebanker

class PPGenitives(PARGRebanker):
    """
    Handle genitives as PPs:
    The|NP/N city|N 's|(NP/N)\NP destruction|N
    -->
    The|NP/N city|N 's|(NP/(N/PP))\NP destruction|N/PP
    (NP
      (NP[nb]/N
        (NP
         (N Chicago))
        ((NP[nb]/N)\NP 's))
      (N
        (N/N Goodman)
        (N Theatre)))
    -->
    (NP
      (NP/(N/PP)
        (NP
         (N Chicago))
        ((NP/(N/PP))\NP 's))
      (N/PP
        (N/N Goodman)
        (N/PP Theatre)))
    """
    def match(self, parg, clitic):
        """
        Match the genitive determiner, but only when noted as an argument
        """
        if parg.label in ['rel', 'ARGM']:
            return False
        if argument.isRoot() or argument.isLeaf():
            return False
        if len(clitic.listWords()) == 1 and clitic.head().label == 'PRP$' \
           and clitic.isProduction(selfType=r'NP/N'):
            return True
        elif not clitic.isProduction(selfType=r'(NP/N)\NP', sibling='NP'):
            return False
        
        return True

    def change(self, clitic):
        if clitic.label == 'NP/N':
            genDeterminer = clitic
        else:
            genDeterminer = clitic.parent()
        while genDeterminer.sibling().label.conj:
            genDeterminer = genDeterminer.parent()
        genDeterminer.changeLabel(CCG.Category(r'NP/(N/PP)'))
        n = genDeterminer.sibling()
        # Support N having arguments unfilled (composition)
        n.changeLabel(CCG.addArg(n.label, 'PP', '/'))

class GenitiveSuperlatives(Rebanker):
    """
    When there's a superlative qualified by a genitive, make the superlative
    subcategorise for the PP, thus (N/PP)/(N/PP)
    """
    def match(self, superlative):
        if not superlative.isProduction(selfType='N/N', sibling='N/PP'):
            return False
        if superlative.getWord(0).pos not in ['JJR', 'JJS']:
            return False
        #return False
        return True

    def change(self, superlative):
        words = superlative.listWords() 
        if len(words) > 1:
            w1 = words[0]
            w1.parent().changeLabel(CCG.Category(r'((N/PP)/(N/PP))/(N/N)'))
        superlative.changeLabel(CCG.Category(r'(N/PP)/(N/PP)'))
                                      
