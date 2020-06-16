"""
Classes for constucting Constituent objects
"""
from Treebank.TreeConstructors import *
from general.Singleton import singleton
import Constituency


class ConstituentConstructor(CompositeConstructor):
    """
    Make constituent mirrors of nodes, so that Visitors can choose to traverse and check
    on the original, or on the developing SFG parse
    """
    def _incrementCount(self, count = [0]):
        """
        Abstract class, so count should not be incremented
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceConstructor instantiated"
    
    def make(self, constituentClass, arguments = {}):
        """
        Hides the construction of constituents
        """
        defaultArgs = {'_children': [], '_parent': None, 'metadata': {}}
        defaultArgs.update(arguments)
        return constituentClass(defaultArgs)
        
    def _getSettings(self, rawData):
        """
        Template for getting settings to pass to
        a Node constructor
        """
        settings = {}
        settings['_children'] = []
        settings['_parent'] = None
        settings['metadata'] = {}
        return settings
        
class WrappedConstituentCreator(CompositeConstructor):
    """
    Abstract class defining how to construct wrapped constituents
    """
    _constituentClass = None
    
    def _incrementCount(self, count = [0]):
        """
        Abstract class, so count should not be incremented
        """
        raise InstanceNumberError, "WrappedConstituentCreator is an abstract class, and should not be instantiated"
    
    def make(self, constituent):
        """
        Hides the construction of constituents
        """
        settings = self._getSettings(constituent)
        constituentClass = self._discernClass(settings['type'])
        return constituentClass(settings)
        
    def _getSettings(self, constituent):
        """
        Compile the complex's data attributes from the constituent's
        """
        settings = {}
        settings['type'] = constituent.type
        settings['metadata'] = constituent.metadata
        settings['_parent'] = None
        settings['localID'] = -1
        settings['globalID'] = -1
        settings['label'] = constituent.label
        settings['functionLabels'] = constituent.functionLabels
        return settings
        
    def _discernClass(self, constituentType):
        """
        Template method to allow more complex typing
        """
        return self._constituentClass

class GroupComplexCreator(WrappedConstituentCreator):
    """
    Instantiate group or phrase complexes by extracting settings from
    the node whose constituent it will replace
    """
    _constituentClass = Constituency.ComplexConstituent
    
    def _incrementCount(self, count = [0]):
        """
        Ensure that _Singleton_ constraint is not violated
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class GroupComplexConstructor instantiated"
        
class EllipsisConstructor(ConstituentConstructor):
    """
    Create an ellipsed copy of a leaf node
    """
    _constituentClass = Constituency.EllipsedLexeme
    
    def _incrementCount(self, count = [0]):
        """
        Ensure that _Singleton_ constraint is not violated
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class EllipsisConstructor instantiated"
        
    def make(self, constituent):
        """
        Instantiate a node
        """
        ellipsedConstituent = self._constituentClass({})
        ellipsedConstituent.addRef(constituent)
        # This can't go inside the addRef, in case it overrides an existing wordID,
        # as when the constituent is created from XML
        ellipsedConstituent.wordID = constituent.wordID
        return ellipsedConstituent
            
            
            
class CopyCreator(CompositeConstructor):
    """
    Create a new copy of a subtree, except for the leaves, which
    will be wrapped instances
    """
    _leafWrapper = singleton(EllipsisConstructor)
    
    def __init__(self):
        self._incrementCount()
        
    def _incrementCount(self, count = [0]):
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class NewEllipsisCreator instantiated"
    
    def make(self, original):
        """
        Create a copy of a tree
        """
        parent = original
        while parent:
            if parent.isType('Dysfluency'):
                raise StandardError, "Should not copy dysfluency"
            parent = parent.parent()
        if not self.isLeaf(original):
            settings = self._getSettings(original)
            copy = original.__class__(settings)
            self._parseChildren(copy, original)
        else:
            copy = self._leafWrapper.make(original)
        # Commented out for XML handling
       # copy.addType('Ellipsis')
        return copy
            
    def _parseChildren(self, copy, original):
        """
        Attach copies of the original's children to the copy
        """
        for child in self._getChildren(original):
            copy.attachChild(self.make(child))
            
            
    def isLeaf(self, node):
        if node.isType('Lexeme'):
            return True
        else:
            return False
            
    def _getSettings(self, node):
        settings = {}
        settings['type'] = node.type
        settings['label'] = node.label
        settings['functionLabels'] = node.functionLabels
        settings['identifier'] = node.identifier
        settings['identified'] = node.identified
        settings['_children'] = []
        settings['_parent'] = None
        settings['metadata'] = node.metadata
        return settings
            
    def _getChildren(self, node):
        """
        Generator function
        
        Iterates through top level brackets in a section of
        text
        """
        for child in node.children():
            if child.isType('Dysfluency'):
                continue
            # Try to avoid raising sentence-final periods etc WSJ_0006 sentence 1
            elif child.label == '.':
                continue
            else:
                yield child
            
            
            
    
