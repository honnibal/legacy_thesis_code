import CCG
from _PARGRebanker import PARGRebanker

class GenitiveArguments(PARGRebanker):
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
    def rebank(self, entries):
        for entry in entries:
            for arg in entry.args:
                const = arg.getConstituent()
                if const and const.listWords():
                    try:
                        const.head()
                    except:
                        print const
                        raise
                if const and const.listWords() and self.match(arg, const):
                    self.doParg(const, None)
                        
    def match(self, parg, argument):
        """
        Match the genitive determiner, but only when noted as an argument
        """
        if parg.label in ['rel', 'ARGM']:
            return False
        clitic = self.getClitic(argument)
        if not clitic or clitic.isRoot() or clitic.isLeaf():
            return False
        
        if len(clitic.listWords()) == 1 and clitic.head().label == 'PRP$' \
           and clitic.isProduction(selfType=r'NP/N') and not clitic.isUnary():
            
            return True
        elif not clitic.isProduction(selfType=r'(NP/N)\NP', sibling='NP'):
            return False
        return True

    def doParg(self, argument, null):
        clitic = self.getClitic(argument)
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


    def getClitic(self, argument):
        lastWord = argument.getWord(-1)
        if lastWord.label in ['POS', 'PRP$']:
            return lastWord.parent()
        while not argument.sibling() and not argument.isRoot():
            argument = argument.parent()
        return argument.sibling()
