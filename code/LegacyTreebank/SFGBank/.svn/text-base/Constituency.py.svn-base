"""
Classes representing constituents for SFG
"""
from Treebank import Nodes
import bisect
from general.Errors import *

# 

class Constituent(Nodes.Node):
    """
    Abstract class defining an interface for constituent nodes
    
    Navigating:
    Navigational methods return surrounding nodes.
    
        clause            method
        rankingClause     method
        clauseConstituent method
        root              method
        parent            method
        child             method
        children          generator
        listWords         method
        
    Restructuring:
    Restructuring methods are void functions that alter the node's subtree or location.
        
        reattach         method
        attachChild      method
        detachChild      method
        prune            method
    Boolean
        isType           method
    Data:
        type             string
        metadata         dictionary
        localID          int
        globalID         int
    Debugging:
        prettyPrint      method
    """
    _baseTypes = {}
    def __init__(self, settings):
        self._initialiseData()
        for key, value in settings.items():
            setattr(self, key, value)
    
    def _initialiseData(self):
        """
        Placing this kind of initialisation outside __init__ makes it easier for
        subclasses to override init while maintaining what they need
        """
        self._rankingClause = None
        self._clause = None
        self._clauseConstituent = None
        self._children = []
        self._parent = None
        self.metadata = {}
        self._observers = []
        self._root = None
        self.quoted = False
        self.ccg = None
        self.systems = {'namesList': []}
        self.identifier = ''
        self.identified = ''
        self._types = {}
        self._types.update(self._baseTypes)
        self._dysfluencies = []
        

    def __hash__(self):
        return self.globalID


    
    def prettyPrint(self):
        return "(%s %s)" % (self.abbr, ' '.join([child.prettyPrint() for child in self.children()]))
        
    def clause(self):
        """
        Look up the tree for ancestor clause just-in-time if clause is not known
        """
        if self._clause: return self._clause
        parent = self.parent()
        while (parent) and (not parent.isType('Clause')) and (not parent.isType('Clause_Complex')):
            try:
                parent = parent.parent()
            except:
                raise SearchError, "Clause not found above constituent: " + self.prettyPrint()
        return parent
        
    def clauseConstituent(self):
        """
        Find the child of the nearest clause self is located under
        """
        if self._clauseConstituent: return self._clauseConstituent
        parent = self
        while (parent.parent()) and (not parent.parent().isType('Clause')) and (not parent.isType('Clause_Complex')):
            try:
                parent = parent.parent()
            except:
                raise SearchError, "Clause constituent not found: " + self.prettyPrint()
        return parent
        
    def root(self):
        if self._root: return self._root
        parent = self
        counter = 0
        while True:
            if not parent.parent():
                return parent
            # Stop it from looping infinitely if something's wrong
            elif counter == 1000:
                raise StandardError
            else:
                parent = parent.parent()
                counter += 1
        
    def attachChild(self, newChild, index = None):
        """
        How to attach a child.
        Overridden by LeafNode, which raises an error.
        """
        # Don't allow bidirectional parenthood
        assert not self is newChild
        if newChild.parent():
            raise AttachmentError, 'Cannot attach node:\n\n%s\n\nto:\n\n%s\n\nNode is already attached to\n\n%s' \
            % (newChild.prettyPrint(), self.prettyPrint(), newChild.parent().prettyPrint())
        if index == None:
            bisect.insort_right(self._children, newChild)
        else:
            self._children.insert(index, newChild)
        newChild.setParent(self)
        
    def rankingClause(self):
        """
        Look up the tree for ranking clause just-in-time if clause is not known
        """
        parent = self
        while (not parent.parent().isType('Clause_Complex')) and (not parent.isType('Ranking_Clause')):
            try:
                parent = parent.parent()
            except:
                raise SearchError, "Clause not found above constituent: " + self.prettyPrint()
        return parent
        
        
    def isType(self, typeString):
        """
        Check whether the typeString describes self
        """
        if self.type == typeString:
            return True
        else:
            return bool(self._types.has_key(typeString))
        
    def _detachFromParent(self):
        self._parent.detachChild(self)
        self._parent = None
        self._clause = None
        self._rankingClause = None
        
        
    def find(self, typeString):
        """
        Find an ancestor of a given type, or give up when you hit the root.
        """
        ancestor = self.parent()
        while ancestor:
            if ancestor.isType(typeString):
                return ancestor
            else:
                ancestor = ancestor.parent()
        else:
            return None
            
    def printLabel(self):
        return self.abbr
        
    def hasWord(self):
        """
        Does the constituent have at least one Word leaf in its subtree?
        """
        if [w for w in self.listWords() if w.isType('Word')]:
            return True
        else:
            return False
            
    def getWordID(self, index):
        """
        Word ID at index. Generally 0 or -1
        """
        wordIDList = [word.wordID for word in self.listWords() if word.isType('Word')]
        wordIDList.sort()
        if not wordIDList:
            return -1
        return wordIDList[index]
        
    def getWord(self, index):
        """
        Word ID at index. Generally 0 or -1
        """
        wordList = [word for word in self.listWords() if word.isType('Word')]
        wordList.sort()
        if not wordList:
            return None
        return wordList[index]
        
    def groups(self):
        if self._finalised:
            return [g for g in self._groups]
        return [g for g in self.children() if g.isType('Group')]
        
    def listLexis(self):
        if self._finalised:
            return [w for w in self._lexisList]
        words = []
        for child in self.children():
            words.extend(child.listWords())
        return words
        
    def group(self, index):
        groups = [g for g in self.children() if g.isType('Group')]
        return groups[index]
    
    def addType(self, typeString):
        self._types[typeString] = 1
        
    
        
    def dysfluencies(self):
        """
        Generate a list of dysfluencies
        """
        for dfl in self._dysfluencies:
            yield dfl
            
    def addDysfluency(self, newChild, index = None):
        """
        Add a dysfluency to self -- much like adding a child
        """
        assert not self is newChild
        if newChild.parent():
            raise AttachmentError, 'Cannot attach node:\n\n%s\n\nto:\n\n%s\n\nNode is already attached to\n\n%s' \
            % (newChild.prettyPrint(), self.prettyPrint(), newChild.parent().prettyPrint())
        if index == None:
            bisect.insort_right(self._dysfluencies, newChild)
        else:
            self._dysfluencies.insert(index, newChild)
        newChild.setParent(self)
        
    def removeDysfluency(self, dysfluency):
        self._dysfluencies.remove(dysfluency)
    
    def rankingClauses(self):
        if self._finalised:
            return self._rankingClauses    
        parent = self.parent()
        while not parent.isType('Clause_Complex'):
            parent = parent.parent()
        return parent.rankingClauses()
        
    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        self._wordList = self.listWords()
        self._lexisList = self.listLexis()
        self._siblings = self.siblings()
        self._breadthList = self.breadthList()
        self._depthList = self.depthList()
        self._groups = self.groups()
        self._rankingClauses = self.rankingClauses()
        self._clauseConstituent = self.clauseConstituent()
        self._root = self.root()
        self._clause = self.clause()
        self._hasEllipsis = self.hasEllipsis()
        self._finalised = True
        
    def unfinalise(self):
        self._finalised = False
        
    def head(self):
        """
        Head finding is non-trivial, but as a default:
            - If there is a sub group, use the first group
            - If there isn't, use the last word
        """
        if self.groups():
            return self.groups()[0].head()
        else:
            words = [l for l in self.listLexis() if l.isType('Word')]
            return words[-1]
        
            
    def hasEllipsis(self):
        if self._finalised:
            return self._hasEllipsis
        for word in self.listWords():
            if word.isType('Ellipsis'):
                return True
        else:
            return False
        

# Wrappers

class WrappedConstituent(Constituent):
    def isType(self, typeString):
        """
        Check whether the typeString describes self
        """
        if typeString == self.type:
            return True
        else:
            return bool(self._types.has_key(typeString))

class ComplexConstituent(WrappedConstituent):
    """
    Complex constituents consist of an initiating constituent, and one or more
    additional constituents. It should be indistinguishable from a simple constituent
    externally
    """
    _baseTypes = {'Complex': 1,
         'Group': 1
        }
    def _initialiseData(self):
        """
        Placing this kind of initialisation outside __init__ makes it easier for
        subclasses to override init while maintaining what they need
        """
        # Generic
        self._rankingClause = None
        self._clause = None
        self._clauseConstituent = None
        self._children = []
        self._root = None
        # Complex specific
        self._initiator = None
        self._additional = []
        self._observers = []
        self._types = {}
        self._types.update(self._baseTypes)
        self._parent = None
        self.abbr = '_C'
        
    def attachChild(self, newChild, index = None):
        """
        How to attach a child.
        Overridden by LeafNode, which raises an error.
        """
        # Don't allow circular parenthood
        assert not self is newChild
        if newChild.parent():
            raise AttachmentError, 'Cannot attach node:\n\n%s\n\nto:\n\n%s\n\nNode is already attached to\n\n%s' \
            % (newChild.prettyPrint(), self.prettyPrint(), newChild.parent.prettyPrint())
        if not index:
            bisect.insort_right(self._children, newChild)
        else:
            self._children.insert(index, newChild)
        newChild.setParent(self)
        if newChild.type == self.type:
            self.abbr = newChild.abbr.split('_')[0] + '_C'
                
    def detachChild(self, node):
        self._children.remove(node)
        
    def head(self):
        """
        No good solution for head finding for complexes. Use the first group's head
        """
        groups = self.groupOne()
        if groups:
           return groups[0].head()
        else:
           return None

    def groupOne(self):
        if not self._children:
            return None
        else:
            return self._children[0]

    def isType(self, typeString):
        if typeString == self.type:
            return True
        elif self.groupOne().isType(typeString):
            return True
        else:
            return bool(typeString in self._types)

    def __getattr__(self, attr):
        return getattr(self.groupOne(), attr)

class ReplacementConstituent(WrappedConstituent):
    pass
#==============================================================================
class ClauseComplex(Constituent):
    _baseTypes = {
        'Clause_Complex': 1
    }
    abbr = 'Cl_C'

    def performOperation(self, operation):
        """
        Accept a _Visitor_ and call it on each child
        """
        operation.newStructure()
        try:
            operation.actOn(self)
        except Break:
            pass
        for node in getattr(self, operation.listType)():
            try:
                operation.actOn(node)
            # Give operations the opportunity to signal
            # when the work is complete
            except Break:
                break
        while operation.moreChanges:
            operation.moreChanges = False
            try:
                operation.actOn(self)
            except Break:
                break
            for node in getattr(self, operation.listType)():
                try:
                    operation.actOn(node)
                # Give operations the opportunity to signal
                # when the work is complete
                except Break:
                    break
                    
                    
    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        self._wordList = self.listWords()
        self._lexisList = self.listLexis()
        self._breadthList = self.breadthList()
        self._depthList = self.depthList()
        self._groups = self.groups()
        self._rankingClauses = self.rankingClauses()
        self._finalised = True
        
    def rankingClauses(self):
        """
        Return a list of ranking clauses
        """
        if self._finalised:
            return self._rankingClauses
        clauses = [g for g in self.children() if g.isType('Clause')]
        for clause in clauses:
            for child in clause.children():
                if child.isType('Clause') and child not in clauses:
                    clauses.append(child)
        return clauses
        
    def prettyPrint(self):
        lines = []
        for clause in self.rankingClauses():
            lines.append(clause.prettyPrint())
        return '\n'.join(lines)

    def isRoot(self):
        return True
        
    

class Clause(Constituent):
    _baseTypes = {
        'Clause': 1
    }
    type = 'Clause'
    abbr = 'Cl'
    
    def verbalGroup(self):
        """
        Return the verbal group, if there is one
        
        If multiple, raise error
        """
        if self._finalised:
            return self._verbalGroup
        verbalGroups = [node for node in self.children() if node.isType('Verbal_Group')]
        if not verbalGroups:
            return None
        # If there are multiple VGs, look for one with words (ck03.mrg~0084)
        if verbalGroups > 1:
            for VG in verbalGroups:
                if VG.listWords():
                    return VG
        return verbalGroups[0]
       # else:
       #     raise StandardError, 'Multiple verbal groups on clause: ' + str(self)
            
    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        self._wordList = self.listWords()
        self._siblings = self.siblings()
        self._breadthList = self.breadthList()
        self._depthList = self.depthList()
        self._groups = self.groups()
        self._verbalGroup = self.verbalGroup()
        self._rankingClause = self._isRankingClause()
        self._hasEllipsis = self.hasEllipsis()
        self._lexisList = self.listLexis()
        self._finalised = True
    
    def isType(self, typeString):
        """
        Check whether the typeString describes self
        """
        if self.type == typeString:
            return True
        elif typeString == 'Ranking_Clause':
            return self._isRankingClause()
        elif typeString == 'Nominalised_Clause':
            return self._isNominalisedClause()
        elif typeString == 'Embedded_Clause':
            return self._isEmbeddedClause()
        else:
            return bool(self._types.has_key(typeString))
    
#    def prettyPrint(self):
#        return "(%s %s)" % (self.abbr, ' '.join([child.prettyPrint() for child in self.children() if not child.isType('Clause')]))
    
        
    def _isRankingClause(self):
        """
        Not ranking if must cross non-clause to get to root
        
        Use isType to get this information from the interface
        """
        if self._finalised:
            return self._rankingClause
        parent = self
        while (parent) and (not parent.isType('Clause_Complex')):
            if not parent.isType('Clause'):
                return False
            elif 'NOM' in parent.functionLabels:
                return False
            elif 'PRD' in parent.functionLabels:
                return False
            else:
                parent = parent.parent()
        return True
        
    def _isNominalised(self):
        """
        Check for NOM or PRD in function labels
        """
        if not self.parent() and self.parent().isType('Nominal_Group'):
            return False
        if 'NOM' in self.functionLabels:
            return True
        elif 'PRD' in self.functionLabels:
            return True
        else:
            return False
            
    def _isEmbeddedClause(self):
        if not self._isNominalisedClause() and not self._isRankingClause():
            return True
        else:
            return False
        
    def head(self):
        """
        Verbal group's head
        """
        return self.verbalGroup().head()
        
    def sibling(self, offset):
        children = [c for c in self.parent().children()]
        position = children.index(self)
        index = position + offset
        if not 0 < index < len(children):
            return None
        else:
            return self.parent().child(index)

        

class Group(Constituent):
    _baseTypes = {'Group': True}
    abbr = 'G'
    type = 'Group'

class VerbalGroup(Group):
    _baseTypes = {
        'Verbal_Group': 1,
        'Group': 1
    }
    abbr = 'VG'
    type = 'Verbal_Group'
    def head(self):
        """
        Return last word of main group, as subgroups are particles.
        
        This is a bit of a problem, as phrasal verbs are treated wrongly.
        However, head() must return a single word, and returning two would break
        it. A possible future solution is to retokenise the verb + particle
        into a single 'word'.
        """
        words = [l for l in self.children() if l.isType('Word')]
        return words[-1]

class OtherGroup(Group):
    _baseTypes = {'Other_Group': 1,
               'Group': 1}
    abbr = 'OG'
    type = 'Group'
    
        
class Dysfluency(OtherGroup):
    _baseTypes = {'Other_Group': 1,
               'Group': 1,
               'Dysfluency': 1}
    abbr = 'DFL'
    
    def replacement(self): return False

class NominalGroup(OtherGroup):
    _baseTypes = {
        'Nominal_Group': 1,
        'Other_Group': 1,
        'Group': 1
    }
    abbr = 'NG'
    type = 'Nominal_Group'
    def head(self):
        """
        Head finding is non-trivial, but for NG take either the first direct word,
        or head of the first NG child, or the last word in the subtree
        """
        words = [l for l in self.children() if l.isType('Word')]
        if words:
            return words[-1]
        for child in self.children():
            if child.isType('Nominal_Group'):
                return child.head()
        else:
            words = [l for l in self.listLexis() if l.isType('Word')]
            return words[-1]
    
class AdverbialGroup(OtherGroup):
    _baseTypes = {
        'Adverbial_Group': 1,
        'Other_Group': 1,
        'Group': 1
    }
    abbr = 'ADV'
    type = 'Adverbial_Group'
    
class PrepositionalPhrase(OtherGroup):
    _baseTypes = {
        'Prepositional_Phrase': 1,
        'Other_Group': 1,
        'Group': 1
    }
    abbr = 'PP'
    type = 'Prepositional_Phrase'
    
class ConjunctionGroup(OtherGroup):
    _baseTypes = {
        'Conjunction_Group': 1,
        'Other_Group': 1,
        'Group': 1
    }
    abbr = 'CJ'
    type = 'Conjunction_Group'


class TracedConstituent(Constituent):
    """
    A node referred to by a trace, so that other elements can pretend
    it's actually the original
    """
    def __init__(self, trace, target):
        """
        Store the target and the trace's constituent
        """
        self.trace = trace
        self.target = target
        self.traceType = trace.text.split('-')[0]
        self._parent = None
        self.globalID = trace.globalID
        self.label = trace.parent().label
        self.functionLabels = trace.parent().functionLabels

    def getWordID(self, worNum):
        return self.trace.wordID

    def __getattr__(self, attr):
        return getattr(self.target, attr)

    
class Lexeme(Constituent):
    """
    Leaf nodes -- Words, Punctuation and Traces
    """
    _baseTypes = {'Lexeme': 1}
    
    def prettyPrint(self):
        return "%s" % (self.text)
        
    def listWords(self):
        return [self]
        
    def printLabel(self):
        return self.text
        
    def attachChild(self, node):
        raise AttributeError
        
    def getWordID(self, index):
        """
        Word ID at index. Generally 0 or -1
        """
        if index > 0:
            return IndexError
        else:
            return self.wordID
            
    def finalise(self):
        """
        Once the changes to the tree are complete, it is worth building final word
        lists etc, and then telling methods to use them instead
        """
        pass
        
    def head(self):
        return self
        
    def listLexis(self):
        return [self]

    def lemma(self):
        """
        Get lemma from COMLEX entry, otherwise text
        """
        if self.ccg:
            return self.ccg.lemma
        elif self.metadata.get('COMLEX'):
            return self.metadata['COMLEX'][0].features['ORTH'][0][1:-1]
        elif self.label in ['NNP', 'NNPS']:
            return self.text
        else:
            return self.text.lower()

    def isLeaf(self):
        return True
    

class Word(Lexeme):
    _baseTypes = {
        'Word': 1,
        'Lexeme': 1
    }
    abbr = 'W'


    
class Punctuation(Lexeme):
    _baseTypes = {
        'Punctuation': 1,
        'Lexeme': 1
    }
    abbr = 'P'
    def head(self):
        raise AttributeError
    
class Trace(Lexeme):
    _baseTypes = {
        'Trace': 1,
        'Lexeme': 1
    }
    abbr = 'T'

        
        
class EllipsedLexeme(Lexeme):
    _baseTypes = {
        'Ellipsis': 1
    }
        
    def addRef(self, constituent):
        """
        Specify the reference constituent
        """
        self._constituent = constituent
        self.label = constituent.label
        self.type = constituent.type
        self.functionLabels = constituent.functionLabels
        self.text = constituent.text
        self.abbr = constituent.abbr
        self.type = constituent.type
        self.metadata = constituent.metadata
        self.senses = constituent.senses

    def isType(self, typeString):
        """
        Check whether the typeString asks about ellipsis
        If not, pass it to _constituent
        """
        if self._types.has_key(typeString):
            return True
        else:
            return self._constituent.isType(typeString)
            
    def ref(self):
        return self._constituent
            
    def listWords(self):
        return [self]
        
    def listLexis(self):
        return []
