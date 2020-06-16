"""
Ensure all absorbtion rules are rightward, where rightward
means that the comma occurs /after/ the constituent
"""
from rebanking.rebankers import Rebanker
import CCG

class EnsureRightAbs(Rebanker):
    """
    (NP
      (NP )
    
      (NP\NP
        (, )
        (NP\NP )
      )
    )
    -->
    (NP
      (NP
        (NP )
        (, )
       )
       (NP\NP )
    )
    """
    def match(self, punctNode):
        """
        Check that the node is a punctuation symbol, and
        then check that it is absorbtion. Finally, check that
        it's left absorbtion
        """
        child = punctNode.child(0)
        if not child.isLeaf() or not child.stag.isPunct():
            return False
        if child.label == 'LRB' or child.label == 'LQU':
            return False
        if not punctNode.sibling() or punctNode.sibling() < punctNode:
            return False
        if not CCG.isIdentical(punctNode.parent().label,
                               punctNode.sibling().label):
            return False
        # Check that there's an uncle to move to
        uncle = self.leftUncle(punctNode)
        if not uncle:
            return False
        return True

    def change(self, punctNode):
        uncle = self.leftUncle(punctNode)
        punctNode.move(uncle, 0)
        
        

    def leftUncle(self, punctNode):
        def ancestors(node):
            while not node.isRoot():
                node = node.parent()
                yield node
                
        for parent in ancestors(punctNode):
            uncle = parent.sibling()
            if uncle and uncle < parent:
                return uncle
        return False
            
    
