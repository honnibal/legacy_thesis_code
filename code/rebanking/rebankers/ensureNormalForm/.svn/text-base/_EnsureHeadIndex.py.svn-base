"""
Ensure the head indices are correct
"""
from rebanking.rebankers import Rebanker
from Treebank.CCGbank import Production

class HeadCorrecter(Rebanker):
    def match(self, node):
        if node.length() != 2:
            return False
        left, right = node.children()
        production = Production(left.label, right.label, node.label)
        return bool(not self.isIdxCorrect(production, node.headIdx))

    def change(self, node):
        node.headIdx = -(node.headIdx-1)

    def isIdxCorrect(self, production, idx):
        # Specific productions where we want to overrule the rules
        specialCases = {
            'a NP --> NP/PP PP': 1,
            'a PP --> PP/NP NP': 1,
            'a NP --> NP/(N/PP) N/PP': 1,
        }
        strP = str(production)
        if strP in specialCases:
            return bool(specialCases[strP] == idx)
        direction = 0 if production.head is production.left else 1
        return bool(direction == idx)
            
        
