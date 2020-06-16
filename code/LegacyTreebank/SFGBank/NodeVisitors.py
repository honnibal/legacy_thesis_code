"""
Visit each node on a tree and perform some operation on it
"""
from general.Errors import *
from Treebank import Nodes
import Constituency, ConstituentConstructors
import copy
import bisect
from general.Singleton import singleton
import Metafunctions
import FunctionAnalysers
import TraverseNetwork
#from SFG_XML import XMLNode
#import COMLEX

class TreeOperation:
    """
    Define some operation that is called on a series of nodes
    """
    _leaf     = Nodes.LeafNode
    _internal = Nodes.InternalNode
    _root     = Nodes.RootNode
    _file     = Nodes.CorpusFile
    _corpus   = Nodes.Corpus
    listType  = 'depthList'
    moreChanges = False
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
            
    def _makeFunctionMap(self):
        """
        Map classes to the methods that should be called on them
        """
        return {self._leaf: self._visitLeaf,
            self._internal: self._visitInternal,
            self._root: self._visitRoot
        }
          
    def newStructure(self):
        """
        Reset state for new structure
        """
        pass        
    
    def actOn(self, node):

        self._functionMap[node.__class__](node)

    def _visitLeaf(self, node):
        """
        Must be overridden in subclasses
        """
        raise ImplementationError, "Subclasses must override this function"
        
    def _visitInternal(self, node):
        """
        Must be overridden in subclasses
        """
        raise ImplementationError, "Subclasses must override this function"
        
    def _visitRoot(self, node):
        """
        Must be overridden in subclasses
        """
        raise ImplementationError, "Subclasses must override this function"





class IDAdder(TreeOperation):
    """
    Add IDs to nodes in a tree
    """
    _localID = 0
    _globalID = 0
    listType = 'depthList'
    def _makeFunctionMap(self):
        """
        This operation behaves uniformly across classes, so doesn't need a
        map. Instead it overrides actOn and puts its behaviour in it
        """
        return {}
        
    def newStructure(self):
        """
        Reset local ID
        """
        self._localID = 0
    
    def actOn(self, node):
        node.localID = self._localID
        node.globalID = self._globalID
        self._localID += 1
        self._globalID += 1
        

class ChildSorter(TreeOperation):
    """
    Have each node sort its children
    """
    _listType = 'depthList'
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
        
    def actOn(self, node):
        if not node.isType('Lexeme'):
            node.sortChildren()
                
class Printer(TreeOperation):
    """
    Print a parse tree with good formatting
    """
    def actOn(self, node):
        if node.isType('Clause_Complex'):
            return self._visitRoot(node)
        else:
            raise Break
        
        
    def _visitLeaf(self, node):
        """
        The visitor must control iteration itself, so only works on root.
        """
        raise Break
        
    def _visitInternal(self, node):
        """
        The visitor must control iteration itself, so only works on root.
        """
        raise Break
        
    def _visitRoot(self, node):
        """
        Print each node's label, and track indentation
        """
        self._indentation = 0
        self._lines = []
        # Accrue print state
        self._printNode(node)
        # Ensure that brackets match
        assert self._indentation == 0
        return '\n'.join(self._lines)
        
    def _printNode(self, node):
        """
        Print indentation, a bracket, then the node label.
        Then print the node's children, then a close bracket.
        """
        indentation = '  '*self._indentation
        self._lines.append('%s(%s' % (indentation, node.printLabel()))
        self._indentation += 1
        for child in node.children():
            if self._isLeaf(child):
                self._printLeaf(child)
            else:
                self._printNode(child)
        self._lines[-1] = self._lines[-1] + ')'
        self._indentation -= 1
        
        
    def _printLeaf(self, node):
        self._lines[-1] = self._lines[-1] + ' %s' % (node.text)
        
    def _isLeaf(self, node):
        if node.isType('Lexeme'):
            return True
        else:
            return False

class NodePrinter(Printer):
    """
    Adapt Printer to work on Node trees, instead of Constituent trees
    """
    def actOn(self, node):
        if isinstance(node, Nodes.RootNode):
            return self._visitRoot(node)
        else:
            raise Break

    def _isLeaf(self, node):
        if isinstance(node, Nodes.LeafNode):
            return True
        else:
            return False
            
    def _printNode(self, node):
        """
        Print indentation, a bracket, then the node label.
        Then print the node's children, then a close bracket.
        """
        indentation = '  '*self._indentation
        self._lines.append('%s(%s' % (indentation, node.label))
        self._indentation += 1
        for child in node.children():
            if self._isLeaf(child):
                self._printLeaf(child)
            else:
                self._printNode(child)
        self._lines[-1] = self._lines[-1] + ')'
        self._indentation -= 1


class MetafunctionPrinter(TreeOperation):
    """
    Print the metafunctional analysis of a clause
    """
    def actOn(self, node):
        if node.isType('Clause_Complex'):
            return self._visitRoot(node)
        else:
            raise Break
        
        
    def _visitLeaf(self, node):
        """
        The visitor must control iteration itself, so only works on root.
        """
        raise Break
        
    def _visitInternal(self, node):
        """
        The visitor must control iteration itself, so only works on root.
        """
        raise Break
        
    def _visitRoot(self, node):
        """
        Print each node's label, and track indentation
        """
        clauses = []
        for clause in node.depthList():
            if not clause.isType('Clause'):
                continue
            clauses.append(self._printSystems(clause))
            for metafunction in ['experiential', 'interpersonal', 'textual']:
                if not clause.isType('Clause'):
                    continue
                clauses.append(self._printClauseMetafunction(metafunction, clause))
        return '\n\n'.join(clauses)
    
    
    def _printClauseMetafunction(self, metafunction, node):
        if metafunction == 'interpersonal':
            return self._printInterpersonal(node)
        elif metafunction == 'textual':
            return self._printTextual(node)
        elif metafunction == 'experiential':
            return self._printExperiential(node)
    
        
    def _printInterpersonal(self, node):
        """
        Print indentation, a bracket, the node's function. Then a new line and
        Then print the node's children, then a close bracket.
        """
        lines = []
        for child in node.children():
            if child.isType('Verbal_Group'):
                lines.append('FINITE: %s' % node.interpersonal.finite)
                lines.append('PREDICATOR: %s' % ' '.join([w.text for w in node.interpersonal.childFunctions.get('predicator', )]))
            elif child.isType('Group'):
                lines.append('%s: %s' % (child.interpersonal.function.upper(), ' '.join([w.text for w in child.listWords()])))
        return '\n'.join(lines)
        
        
    def _printTextual(self, node):
        lines = []
        for child in node.groups():
            lines.append('%s: %s' % (child.textual.function.upper(), ' '.join([w.text for w in child.listWords()])))
        return '\n'.join(lines)
        
    def _printExperiential(self, node):
        lines = []
        for child in node.groups():
            if not child.experiential.function:
                continue
            lines.append('%s: %s' % (child.experiential.function.upper(), ' '.join([w.text for w in child.listWords()])))
        return '\n'.join(lines)
            
    
    def _printSystems(self, node):
        """
        Get system names and selections
        """
        systems = []
        for system in node.systems['namesList']:
            systems.append('%s: %s' % (system, node.systems[system]))
        return '\n'.join(systems)
    
    
        
    def _printLeaf(self, node):
        self._lines[-1] = self._lines[-1] + ' %s' % (node.text)
        
    def _isLeaf(self, node):
        if node.isType('Lexeme'):
            return True
        else:
            return False
        
class XMLPrinter(Printer):
    """    
    Test the SFG_Instance schema by trying to use it
    """
    def actOn(self, node):
        if node.isType('Clause_Complex'):
            expression  = self._makeExpression(node)
            constituent = self._makeConstituent(node, 3)
            return """<Collection xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="C:\workspace\Schemas\SFG_Instantial.xsd">
    <Text>
%s
        <Grammar>
%s
        </Grammar>
    </Text>
</Collection>""" % (expression.prettyPrint(), constituent.prettyPrint())
        else:
            raise Break
            
    
    def _makeExpression(self, clauseComplex):
        """
        Make the expression plane string that words will index into
        """
        words = clauseComplex.listLexis()
        self._expressionIndex = {}
        length = 0
        text = []
        for word in words:
            start = length
            length += len(word.text)
            end = length
            self._expressionIndex[word.globalID] = ('%d:%d' % (start, end))
            text.append(word.text)
            # Increment length for whitespace
            length += 1
        xml = XMLNode('ExpressionPlane', 2)
        xml.addText(' '.join(text))
        return xml
            
        
    def _makeConstituent(self, constituent, depth):
        xml = XMLNode('Constituent', depth)
        if constituent.isType('Lexeme'):
            xml.addAttr('id', 'w%s' % constituent.wordID)
        else:
            xml.addAttr('id', 'c%s' % constituent.globalID)
        xml.addAttr('type', self._getType(constituent))
        if not constituent.isType('Lexeme'):
            constituency = XMLNode('Constituents', depth + 1)
            for child in constituent.children():
                constituency.addNode(self._makeConstituent(child, depth + 2))
            xml.addNode(constituency)
            features = self._makeFeatures(constituent, depth + 1)
            if features.hasContent():
                xml.addNode(features)
        else:
            realisation = XMLNode('Realisation', depth + 1)
            if constituent.isType('Ellipsis'):
                realisation.addAttr('type', 'ellipsis')
                realisation.addAttr('ref', 'w' + str(constituent.ref().globalID))
            else:
                realisation.addAttr('type', 'string')
                realisation.addAttr('ref', self._expressionIndex[constituent.globalID])
            xml.addNode(realisation)
        return xml
        
    def _getType(self, constituent):
        type = constituent.type
        if type == 'Clause_Complex':
            return type
        elif constituent.isType('Complex'):
            return type + '_Complex'
        elif constituent.isType('Ellipsis'):
            return 'Ellipsis'
        else:
            return type
        
    def _makeFeatures(self, node, depth):
        xml = XMLNode('Features', depth)
        for system in node.systems['namesList']:
            if not node.systems[system]:
                continue
            selection = XMLNode('SystemFeature', depth + 1)
            selection.addAttr('selection', '%s.%s' % (system, node.systems[system]))
            xml.addNode(selection)
        for metafunctionName in ['interpersonal', 'textual', 'experiential']:
            metafunction = getattr(node, metafunctionName, None)
            try:
                functions = metafunction.childFunctions.keys()
            except:
                continue
            functions.sort()
            for functionName in functions:
                functionXML = XMLNode('Function', depth + 1)
                functionXML.addAttr('metafunction', metafunctionName)
                functionXML.addAttr('name', functionName)
                realisation = XMLNode('Realisation', depth + 2)
                realisation.addAttr('type', 'node')
                try:
                    realisation.addAttr('ref', 'c%s' % metafunction.childFunctions[functionName].globalID)
                except AttributeError:
                    realisation.addAttr('ref', '%s' % ', '.join(['c' + str(r.globalID) for r in metafunction.childFunctions[functionName]]))
                functionXML.addNode(realisation)
                xml.addNode(functionXML)
        return xml

    
class TraceIndexer(TreeOperation):
    """            
    Build an index that links trace nodes to their references
    """
    def actOn(self, constituent):
        if not constituent.isType('Lexeme'):
            self._visitInternal(constituent)
            
    

    
    def newStructure(self):
        """
        Initialise the trace index
        """
        self._traceIndex = {}
    
    def _visitRoot(self, node):
        """
        Initialise the index
        """
        self.newStructure()
    
    def _visitInternal(self, constituent):
        if constituent.identifier:
            self._traceIndex.setdefault(constituent.identifier, []).append(constituent)
    
    def traceIndex(self):
        """
        Format the trace index and return it
        """
        return self._traceIndex

            
class ConstituentTyper(TreeOperation):
    """
    Attach an SFG representation to a node by discerning what
    constituent type it is, usually done by looking up the node's label
    in a dictionary
    """
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _verbTags = ['VP', 'AUX']
    _nominalTags = ['ADJP', 'NP', 'NX', 'QP', 'WHADJP', 'WHNP', 'UCP', 'X']
    _prepositionTags = ['PP', 'WHPP']
    _adverbialTags = ['ADVP', 'WHADVP', 'ADV']
    _particleTags = ['PRT']
    _conjunctionTags = ['CONJP', 'LST', 'NAC', 'UH']
    _correctionTags = ['@', 'EDITED', 'TYPO', 'RM', 'IP', 'RS']
    _intjTags = ['INTJ']
    _clauseTags = ['RRC', 'S', 'SBAR', 'SBARQ', 'SINV', 'SQ', 'PRN', 'FRAG', 'CODE']
    _wordTags = ['$', '!!', 'GW', 'XX', 'BES', 'HVS', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
    _punctTags = [',', '.', '-LRB-', '-RRB-', ':', "''", '``', '#']
    _traceTags = ['-DFL-', 'XXX', '-NONE-']
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
        self._makeTypeMaps()
    
    def _visitRoot(self, node):
        """
        Roots should always be clause complexes
        """
      #  print repr(node)
        assert not node.constituent
        node.constituent = self._constituentConstructor.make(Constituency.ClauseComplex, {'type': 'Clause_Complex', 'label': node.label, 'functionLabels': [fL for fL in node.functionLabels], 'globalID': node.globalID})
        
        
    def _visitInternal(self, node):
        """
        Internals should always be groups
        """
        assert not node.constituent
        typeString, typeClass = self._groupTypeMap[node.label]
        # Decide the constituent by looking up the node's label in a dictionary
        node.constituent = self._constituentConstructor.make(typeClass, {'type': typeString, 'label': node.label, 'functionLabels': [fL for fL in node.functionLabels], 'identifier': node.identifier, 'identified': node.identified})
        assert node.functionLabels == node.constituent.functionLabels
        
    def _visitLeaf(self, node):
        """
        Leaves should be word, punctuation or traces
        """
        assert not node.constituent
        # Decide the constituent by looking up the node's label in a dictionary
        typeString, typeClass = self._lexisTypeMap[node.label]
        node.constituent = self._constituentConstructor.make(typeClass, {'text': node.text, 'type': typeString, 'wordID': node.wordID, 'label': node.label, 'functionLabels': [fL for fL in node.functionLabels], 'senses': node.senses, 'metadata': node.metadata})
 
    def _makeTypeMaps(self):
        """
        Map labels to the constituency class that must be instantiated for them
        """
        self._groupTypeMap = {}
        self._lexisTypeMap = {}
        for tag in self._clauseTags:
            self._groupTypeMap[tag] = ('Clause', Constituency.Clause)
        for tag in self._verbTags:
            self._groupTypeMap[tag] = ('Verbal_Group', Constituency.VerbalGroup)
        for tag in self._nominalTags:
            self._groupTypeMap[tag] = ('Nominal_Group', Constituency.NominalGroup)
        for tag in self._prepositionTags:
            self._groupTypeMap[tag] = ('Prepositional_Phrase', Constituency.PrepositionalPhrase)
        for tag in self._adverbialTags:
            self._groupTypeMap[tag] = ('Adverbial_Group', Constituency.AdverbialGroup)
        for tag in self._particleTags:
            self._groupTypeMap[tag] = ('Particle', Constituency.OtherGroup)
        for tag in self._intjTags:
            self._groupTypeMap[tag] = ('Interjection', Constituency.OtherGroup)
        for tag in self._conjunctionTags:
            self._groupTypeMap[tag] = ('Conjunction_Group', Constituency.ConjunctionGroup)
        for tag in self._correctionTags:
            self._groupTypeMap[tag] = ('Dysfluency', Constituency.Dysfluency)
        for tag in self._wordTags:
            self._lexisTypeMap[tag]  = ('Word', Constituency.Word)
        for tag in self._punctTags:
            self._lexisTypeMap[tag]  = ('Punctuation', Constituency.Punctuation)
        for tag in self._traceTags:
            self._lexisTypeMap[tag]  = ('Trace', Constituency.Trace)
            
         
class ConstituentConnector(TreeOperation):
    """        
    Connect constituents together to form a tree
    """
    listType = 'depthList'
    def _makeFunctionMap(self):
        """
        Map classes to the methods that should be called on them
        """
        return {self._leaf: self._visitLeaf,
            self._internal: self._visitNonLeaf,
            self._root: self._visitNonLeaf
        }
            
    def _visitNonLeaf(self, node):
        for child in node.children():
            node.constituent.attachChild(child.constituent)

    def _visitLeaf(self, node):
        pass
 
 
class RetypeConstituents(TreeOperation):
    """       
    Certain labels are ambiguous. Replace nodes that were assigned the wrong constituent
    """
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    def _makeFunctionMap(self):
        """
        Map classes to the methods that should be called on them
        """
        return {'PRN': self._resolvePRN,
            'NAC': self._resolveNAC
        }
          
    def newStructure(self):
        """
        Reset state for new structure
        """
        pass        
    
    def actOn(self, node):
        if node.isType('Clause_Complex'):
            return None
        if self._functionMap.has_key(node.label):
            typeString, typeClass = self._functionMap[node.label](node)
            self._retypeConstituent(node, typeString, typeClass)

     
    def _resolvePRN(self, node):
        seen = {}
        i = 0
        for child in node.children():
            seen[child.abbr] = i
            i += 1
        # If VP, consider it a clause
        if seen.has_key('VG'):
            return ('Clause', Constituency.Clause)
        elif seen.has_key('Cl'):
            return ('Clause', Constituency.Clause)
        elif seen.has_key('PP'):
            return ('Prepositional_Phrase', Constituency.PrepositionalPhrase)
        elif seen.has_key('ADV'):
            return ('Adverbial_Group', Constituency.AdverbialGroup)
        else:
            return ('Nominal_Group', Constituency.NominalGroup)

    def _resolveNAC(self, node):
        for group in node.children():
            # SWBD 0.127: If there's a clause or a VP inside, NG
            if group.isType('Verbal_Group') or group.isType('Clause'):
                return ('Nominal_Group', Constituency.NominalGroup)
        # If parent is VP or clause, conjunction
        if node.parent().isType('Clause') or node.parent().isType('Clause_Complex') or node.parent().isType('Verbal_Group'):
            for group in node.children():
                # All 55.95: If there's a preposition inside, preposition
                if group.isType('Prepositional_Phrase'):
                    return ('Prepositional_Phrase', Constituency.PrepositionalPhrase)
                elif group.isType('Adverbial_Group'):
                    return ('Adverbial_Group', Constituency.AdverbialGroup)
                # All 694.32
                elif group.isType('Nominal_Group'):
                    return ('Nominal_Group', Constituency.NominalGroup)
            else:
                return ('Conjunction_Group', Constituency.ConjunctionGroup)
        else:
            # Otherwise, NP
            return ('Nominal_Group', Constituency.NominalGroup)
            
    def _resolveINTJ(self, node):
        """
        Deprecated -- INTJ is now treated unambiguously as Interjection
        """
        # All 2.97
        if not node.hasWord():
            return ('Conjunction_Group', Constituency.ConjunctionGroup)
        # If multi-word, conjunction
        elif node.getWord(0) != node.getWord(-1):
            return ('Conjunction_Group', Constituency.ConjunctionGroup)
        # If word is uh, um, dysfluency
        elif node.getWord(0).label == 'UH':
            # WSJ 101.40: Minor clause unbracketed
            return ('Interjection', Constituency.OtherGroup)
        else:
            return ('Conjunction_Group', Constituency.ConjunctionGroup)
            
    def _retypeConstituent(self, node, typeString, typeClass):
        newConstituent = self._constituentConstructor.make(typeClass, {'type': typeString, 'label': node.label, 'functionLabels': [fL for fL in node.functionLabels], 'identifier': node.identifier, 'identified': node.identified})
        for child in node.children():
            child.reattach(newConstituent)
        node.parent().replace(node, newConstituent)
        

class QuotationChecker(TreeOperation):
    """
    Note which constituents are quoted text
    """
    def actOn(self, node):
        if node.__class__ == Nodes.RootNode:
            self._visitTarget(node)
        else:
            raise Break
    
    def _visitTarget(self, node):
        """
        Iterate through the node's words
        
        When a start quote is seen, the following non-punctuation
        word's clause is quoted. When a close quote is seen, the preceding
        non-punctuation word's clause is quoted.
        """
        wordList = node.listWords()
        lastLexical = None
        seenStartQuote = False
        for word in wordList:
            if word.text in ["``", "`"]:
                self._quoteClauses2(word)
        # In SWBD corpus, quotations are marked as -SEZ
        for clause in node.constituent.depthList():
            if 'SEZ' in clause.functionLabels:
                clause.quoted = True
            """
            if word.constituent.isType('Word'):
                lastLexical = word
                if seenStartQuote:
                    self._quoteClauses(word)
                    seenStartQuote = False
            elif word.text == "''":
                if lastLexical:
                    # WSJ 549.36
                    pass
                   # lastLexical.constituent.clause().quoted = True
            elif word.text in ["``", "`"]:
                seenStartQuote = True
            """
    def _quoteClauses(self, word):
        """
        Make all clauses which start with the word quoted==True
        """
        parent = word.parent()
        while parent.getWord(0) == word:
            for clause in parent.constituent.children():
                if not clause.isType('Clause'):
                    continue
                clause.quoted = True
            parent = parent.parent()
    
    def _quoteClauses2(self, openQuote):
        for sibling in openQuote.siblings():
            if sibling < openQuote:
                continue
            if sibling.constituent.isType('Clause'):
                sibling.constituent.quoted = True
        
class PunctuationReassigner(TreeOperation):
    """
    Punctuation is erratically assigned in the Treebank, which
    causes two problems:
        1. Sometimes punctuation will make a clause 'interrupt' another when 
        the only lexemes occurring before or after the clause are punctuation
        2. Quotation marks are necessary for determining that a clause is a
        direct projection
    The solution to both of these is to attach punctuation that encloses a clause
    to that clause.
    """     
    def actOn(self, node):
        index = self._checkConstraints(node)
        if index != -1:
            self._rearrangeTree(node.parent(), index)
        
    def _checkConstraints(self, node):
        if not node.constituent.isType('Clause'):
            return -1
        # Find out whether it is enclosed by punctuation
        i = 0
        for child in node.parent().children():
            if child == node:
                try:
                    if (node.parent().child(i-1).constituent.isType('Punctuation')):
                        if (node.parent().child(i+1).constituent.isType('Punctuation')):
                            return i
                except IndexError:
                    return -1
            i += 1
        return -1

    def _rearrangeTree(self, node, index):
        offset = 1
        children = [child for child in node.children()]
        punctuation = []
        while ((index + offset) < len(children)) and (node.child(index + offset).constituent.isType('Punctuation')):
            punctuation.append(node.child(index + offset))
            offset += 1
        offset = 1
        while ((index - offset) > -1) and (node.child(index - offset).constituent.isType('Punctuation')):
            punctuation.append(node.child(index - offset))
            offset += 1
        targetNode = node.child(index)
        for p in punctuation:
            p.constituent.reattach(targetNode.constituent)




class TreeRearranger(TreeOperation):
    """
    Abstract class for structural tree operations, because these
    operations share common features:
    - they usually work on certain types of nodes and ignore all others
    - they usually check some set of conditions, and ignore the node if they are not met
    - if they are met, they move some node/s to some other place in the tree
    """
    _targetTypes = []
    
    def __init__(self):
        pass
        
    def actOn(self, constituent):
        # Allow TreeRearrangers to visit both nodes and constituents
        for type in self._targetTypes:
            if constituent.isType(type):
                self._visitTarget(constituent)
                break
        else:
            self._rejectNode(constituent)
    
    
    def _visitTarget(self, node):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        if self._checkConstraints(node):
            self._rearrangeTree(node)
        else:
            self._rejectNode(node)
    
    def _rejectNode(self, node):
        """
        Perform any actions (such as raising a Break) that
        should be performed if a node is seen that the Visitor is not
        interested in
        """
        pass
        
    def _checkConstraints(self, node):
        """
        Return a boollean to indicate whether the node meets the criteria
        
        Must be overridden
        """
        raise ImplementationError, "Subclasses of TreeShaper must override _checkConstraints"
        
    def _rearrangeTree(self, node):
        """
        Perform the restructuring
        """
        raise ImplementationError, "Subclasses of TreeShaper must override _checkConstraints"


class StrictTruncater(TreeRearranger):
    """
    Some sentences have unforking branches, where the child node is identically labelled to the parent:
    VP
      VP
        VP
    becomes:
    VP
    I think these occurrences are errors in the original Treebank
    """
    _targetTypes = ['Group']
    def _checkConstraints(self, constituent):
        """
        Check that exactly one child (even including punctuation)
        and that the child is labelled and function labelled identically
        """
        if constituent.length() != 1:
            return False
        if constituent.child(0).label != constituent.label:
            return False
        if constituent.child(0).functionLabels != constituent.functionLabels:
            return False
        if constituent.identifier and constituent.child(0).identifier:
            return False
        if constituent.identified and constituent.child(0).identified:
            return False
       # self._moreChanges = True
        return True
    
    def _rearrangeTree(self, constituent):
        """
        Cut constituent out of the tree
        """
        constituent.child(0).identifier = constituent.identifier
        constituent.child(0).identified = constituent.identified
        constituent.child(0).reattach(constituent.parent())
        constituent.prune()


class STruncater(TreeRearranger):
    """
    Extended clause trees cause problems (wsj 559.59), so should be truncated:
    
    S
      S
      S
    becomes
    S
    S
    
    prsguide1.ps section 7c discusses these constructions.
    """
    _targetTypes = ['Clause']
    
    def _checkConstraints(self, constituent):
        """
        Check that a constituent is a clause with no non-clause children
        """
        # Not sure why I had SBARs excluded, but included them for 511.1 and changed
        # the constraint to specify that the child's label must be the same as self label
        """
        if constituent.label in ['SBAR', 'SBARQ']:
            return False
        elif 'SBAR' in constituent.functionLabels:
            return False
        """
        seenClause = 0
        for child in constituent.children():
            if child.isType('Punctuation'):
                continue
            if child.isType('Trace'):
                continue
            if child.isType('Conjunction_Group'):
                continue
            if child.isType('Adverbial_Group'):
                continue
            if not child.isType('Clause'):
                return False
            if not child.label == constituent.label:
                return False
            else:
                seenClause = 1
        if seenClause:
            return True
        else:
            return False
        
    def _rearrangeTree(self, clause):
        """
        Attach clause children to the clause's parent, non clause children
        (ie conjunctions and punctuation) to one of those clauses
        """
        childClauses = [c for c in clause.children() if c.isType('Clause')]
        otherChildren = [c for c in clause.children() if not c.isType('Clause')]
        for childClause in childClauses:
            childClause.functionLabels.extend(clause.functionLabels)
            childClause.reattach(clause.parent())
        for punctOrConj in otherChildren:
            punctOrConj.allocate(childClauses)
        clause.prune()

                            

class SBARTruncater(TreeRearranger):
    """
    Replace SBAR nodes with their S children, attaching any other groups to the S child
    SBAR-NOM
        WHNP What
        S
            NP we
            VP are pleased to call
            NP real life
    becomes
    S-SBAR-NOM
        WHNP What
        NP we
        VP are pleased to call
        NP real life
    (brown 3.50)
    """
    _targetTypes = ['Clause']
    _verbTags = ['GW', 'NEG', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'BES', 'HVS']
    _finites = ['to', 'be', 'been', 'being', 'is', 'are', 'was', 'were', 'has', 'had', 'have', 'having', 'do', 'does', 'doing', 'did', 'will', 'would', 'shall', 'should', 'may', 'might', 'can', 'could', 'must', "'s", "'re", "'m", "'ll", 'going', 'about']
    
    def _checkConstraints(self, constituent):
        """
        Look for SBAR function labels that have at least one clause child
        """
        if constituent.label in ['SBAR', 'SBARQ']:
            if [clause for clause in constituent.children() if (clause.isType('Clause')) and (clause.label in ['S', 'SQ', 'SINV'])]:
                return True
            else:
                return False
        else:
            return False
    
    def _rearrangeTree(self, constituent):
        """
        Assuming only one clause child, replace self with that child
        
        Currently differs from old flattenSBARTrees. Consult that function if
        there are any problems, as I suspect I've forgotten about structures that
        I need to account for (I've reduced constraints)
        """
        clauseChild = [clause for clause in constituent.children() if clause.isType('Clause') and (clause.label in ['S', 'SQ', 'SINV'])]
        clauseChild = clauseChild[0]
        clauseChild.functionLabels.extend(constituent.functionLabels)
        clauseChild.functionLabels.append('SBAR')
        if constituent.label == 'SBARQ':
            # Weird decision to use 'Q'. I'll add both to ensure compatibility
            clauseChild.functionLabels.append('Q')
            clauseChild.functionLabels.append('SBARQ')
        for child in constituent.children():
            if child == clauseChild: continue
            child.reattach(clauseChild)
        if constituent.identifier:
            # Hope that this never happens. If it does, uh, think of something
            assert not clauseChild.identifier
            clauseChild.identifier = constituent.identifier
        if constituent.identified:
            # Hope that this never happens. If it does, uh, think of something
            assert not clauseChild.identified
            clauseChild.identified = constituent.identified
        clauseChild.sortChildren()
        clauseChild.reattach(constituent.parent())
        constituent.prune()
        
        
class PredicateRaiser(TreeRearranger):
    """
    Raise children of a verbal group, so that
    all constituents in a clause are equally ranked:
        
    "Clause
        NP The dog
        VP bit
             NP the boy
             PP on
                NP the arm"
    Becomes:
    "Clause
        NP The dog
        VP bit
        NP the boy
        PP on
            NP the arm"
    """
    _targetTypes = ['Verbal_Group']
    
    def _checkConstraints(self, node):
        """            
        Applies to all verbal groups
        """
        return True
        
    def _rearrangeTree(self, node):
        constituent = getattr(node, 'constituent', node)
        clause = constituent.clause()
        for child in constituent.children():
            if child.isType('Verbal_Group'):
                continue
            if child.isType('Particle'):
                continue
            if child.isType('Lexeme'):
                continue
            if child.isType('Conjunction_Group'):
                continue
            child.reattach(clause)
            
class ConjunctionRaiser(TreeRearranger):
    """
    Raise conjunctions that are children of a verbal group and are not part
    of a complex: eg "there's either an answer or there isn't
    
    WSJ 612.19
    """
    _targetTypes = ['Conjunction_Group']
    
    def _checkConstraints(self, node):
        """
        Check that the conjunction's parent is a verbal group and not a verbal group
        complex
        """
        if node.parent().isType('Verbal_Group') and not node.parent().isType('Complex'):
            return True
        else:
            return False
    
    def _rearrangeTree(self, node):
        """
        Just raise the node one
        """
        moreChanges = True
        node.reattach(node.parent().parent())
    

class MinorClauseInserter(TreeRearranger):
    """
    Sometimes single constituent sentences are not beneath fragment nodes -- 
    they are simply the root node. This must be fixed.
    """
    _targetTypes = ['Group', 'Lexeme']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _clause = Constituency.Clause
    
    def _checkConstraints(self, constituent):
        """
        The constituent should not be a clause,
        should have no siblings,
        and should be directly attached to a clause complex
        """
        # WSJ 101.40
        if len([c for c in constituent.parent().children() if not c.isType('Punctuation')]) > 1:
            return False
        if not constituent.parent().isType('Clause_Complex'):
            return False
        return True
        
    def _rearrangeTree(self, constituent):
        clause = self._constituentConstructor.make(self._clause, {'type': 'Clause', 'label': 'FRAG', 'functionLabels': []})
        constituent.insert(clause)
        
    def _rejectNode(self, constituent):
        raise Break


class QuotationClauseInserter(TreeRearranger):
    """
    Insert a clause for a minor quoted clause that is not bracketed with an S
    
    WSJ 101.40
    """
    _targetTypes = ['Verbal_Group']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _clause = Constituency.Clause
    
    def _checkConstraints(self, verbalGroup):
        words = []
        # Add this restriction for safety until further notice
        for child in verbalGroup.children():
            if child.label == 'INTJ':
                break
        else:
            return False
        for child in verbalGroup.children():
            if child.isType('Lexeme') and child.label != '``':
                continue
            words.extend([w.text for w in child.listWords()])
        # If start quote begins siblings,
        if words[0] in ['``', '`']:
            if "''" not in words[:-1]:
                return True
        return False
        
    def _rearrangeTree(self, verbalGroup):
        clause = self._constituentConstructor.make(self._clause, {'type': 'Clause', 'label': 'FRAG', 'functionLabels': []})
        for child in verbalGroup.children():
            if child.isType('Word'):
                continue
            child.reattach(clause)
        verbalGroup.attachChild(clause)

class RelativeClauseInserter(TreeRearranger):
    """
    Reduced relative clauses are often bracketed incorrectly -- the clause
    node is omitted and should be restored:
    NP
      NP The plan
      VP proposed
        PP by
          NP
    becomes:
    
    NP
      NP The plan
      RRC
        VP proposed
          PP by
            NP    
    (1368.30)
    """
    _targetTypes = ['Verbal_Group']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _clause = Constituency.Clause
    
    def _checkConstraints(self, constituent):
        """
        Look for a verb phrase with a noun phrase parent
        """
        if constituent.parent().isType('Nominal_Group'):
            return True
        else:
            return False
    
    def _rearrangeTree(self, constituent):
        """
        Insert a reduced relative clause node above the VP
        """
        clause = self._constituentConstructor.make(self._clause, {'type': 'Clause', 'label': 'RRC', 'functionLabels': []})
        constituent.insert(clause)


class VerbalGroupInserter(TreeRearranger):
    """
    If the clause has no verbal group, and theres a verbal word,
    make a verbal group for the word
    """
    _targetTypes = ['Word']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _vg = Constituency.VerbalGroup
    _verbTags = ['GW', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'BES', 'HVS']
    
    def _checkConstraints(self, constituent):
        """
        Check that the parent is a clause with no verbal group and the word is a verb
        """
        if not constituent.parent().isType('Clause'):
            return False
        if constituent.parent().verbalGroup():
            return False
        if constituent.label not in self._verbTags:
            return False
        return True
        
    def _rearrangeTree(self, verb):
        """
        Insert a verbal group
        """
        verbalGroup = self._constituentConstructor.make(self._vg, {'type': 'Verbal_Group', 'label': 'VP', 'functionLabels': []})
        verb.insert(verbalGroup)
        

class AdjunctDTInserter(TreeRearranger):
    """
    Deals only with cases where 'all' is attached directly to VP:
    NP-SBJ we
    VP 're all
      VP thinking
    
    becomes:
    NP-SBJ we
    VP 're
      NP-ADV all
      VP thinking
    wsj 42.22
    """
    _targetTypes = ['Word']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _ng = Constituency.NominalGroup
    
    def _checkConstraints(self, word):
        """
        Check that the word's text is "all", its label is DT, and its parent is a VP
        """
        if not word.text.lower() in ['all', 'both', 'either', 'each', 'neither']:
            return False
        if not word.label == 'DT':
            return False
        if not word.parent().isType('Verbal_Group'):
            return False
        return True
    
    def _rearrangeTree(self, word):
        """
        Create an appropriate parent and insert it into the tree
        """
        parent = self._constituentConstructor.make(self._ng, {'type': 'Nominal_Group', 'label': 'NP', 'functionLabels': ['ADV']})
        word.insert(parent)
      


class VerbMover(TreeRearranger):
    """
    Move loose verb words to the verbal group
    """
    _targetTypes = ['Word']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _vg = Constituency.VerbalGroup
    _finites = ["n't", 'not', 'to', 'be', 'been', 'being', 'is', 'are', 'was', 'were', 'has', 'had', 'have', 'having', 'do', 'does', 'doing', 'did', 'will', 'would', 'shall', 'should', 'may', 'might', 'can', 'could', 'must', "'s", "'re", "'m", "'ll", 'going', 'about', 'wo']
    _verbTags = ['GW', 'NEG', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'BES', 'HVS', 'MD', 'TO', 'RB']
    
    def _checkConstraints(self, constituent):
        """
        Look for a 'not' or "n't" that is attached directly to a clause,
        and attach it to a verb phrase
        """
        if constituent.label not in self._verbTags:
            return False
        if constituent.text.lower() not in self._finites:
            return False
        if not constituent.parent().isType('Clause'):
            return False
        # Don't move 'not', "n't" if there are no other verbs (WSJ 669.9)
        if not (constituent.parent().verbalGroup() and constituent.parent().verbalGroup().hasWord()):
            if constituent.label in ['RB', 'NEG']:
                return False
        return True
        
    def _rearrangeTree(self, word):
        """
        Move the neg word to its clause's verbal group
        If there is no verbal group, make one
        """
        if not word.parent().verbalGroup():
            verbalGroup = self._constituentConstructor.make(self._vg, {'type': 'Verbal_Group', 'label': 'VP', 'functionLabels': []})
            word.parent().attachChild(verbalGroup)
        word.reattach(word.parent().verbalGroup())




class SmallClauseDeleter(TreeRearranger):
    """
    Delete clauses for structures like:
        VP make
          Clause
            NP-SBJ them
            VP Trace 
    """
    _targetTypes = ['Clause']
    
    def _checkConstraints(self, clause):
        """
        Look for clauses with a subject and a trace verb phrase
        """
        if (clause.verbalGroup()) and (clause.verbalGroup().listWords()):
            return False
        # Don't delete SBAR'd clauses (wsj 1119.16)
        if 'SBAR' in clause.functionLabels:
            return False
        # Parentheticals sometimes shouldnt even be clauses (17.0)
        if clause.label == 'PRN':
            # If within a nominal group, just delete it (WSJ 17.0)
            if clause.parent().isType('Nominal_Group'):
                return True
            elif clause.parent().isType('Adverbial_Group'):
                return True
            elif clause.parent().isType('Prepositional_Phrase'):
                return True
            # If parent is a clause, verbal group or clause complex, return false
            elif [type for type in ['Clause', 'Verbal_Group', 'Clause_Complex'] if clause.parent().isType(type)]:
                return False
            # If a parent is a dysfluency group, return false
            elif clause.parent().isType('Dysfluency'):
                return False
            # SWBD 292.17
            elif clause.parent().label == 'INTJ':
                return False
            elif clause.label == 'PRN':
                return False
            # Otherwise complain, so I can assess those examples
            else:
                raise InformationError, str(clause.parent())
        for child in clause.children():
            if 'SBJ' in child.functionLabels:
                return True
        return False
    
    def _rearrangeTree(self, clause):
        """
        Move the clause's children to its parent, then prune the clause
        """
        # Track how often small clause complexes occur -- wsj 2099.50
       # assert not [s for s in clause.siblings() if s.isType('Clause') and not s.verbalGroup()]
        for child in clause.children():
            child.reattach(clause.parent())
        clause.prune()


        
class ClauseRaiser(TreeRearranger):
    """
    Raise ranking clauses to be children of the root node
    """
    _targetTypes = ['Clause']
    
    def _visitTarget(self, node):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        possibleClauseParent = self._checkConstraints(node)
        if possibleClauseParent:
            self._rearrangeTree(node, possibleClauseParent)
        else:
            self._rejectNode(node)
    
    def _checkConstraints(self, constituent):
        """
        Check whether the clause is ranking by seeing whether it is a child of
        a nominal group
        """
        ancestor = constituent.parent()
        while ancestor:
            if ancestor.isType('Nominal_Group'):
                return False
            if ancestor.isType('Verbal_Group'):
                return False
            if ancestor.isType('Adverbial_Group'):
                return False
            elif ancestor.label == 'EDITED':
                return False
            elif ancestor.isType('Clause'):
                return ancestor
            else:
                ancestor = ancestor.parent()
        else:
            return False
            
    def _rearrangeTree(self, constituent, clause):
        """
        Find the root node and reattach the clause to it
        """
        constituent.reattach(clause.parent())
        self.moreChanges = True
 
 
 
 
 
                    
class VGFlattener(TreeRearranger):
    """
    Flatten VP-VP branches.
    
    Linguistically, this can be one of three operations:
        If the first VP contains only a finite, it is flattening a VG simplex
        If the first VP contains a lexical verb (typically a 'stopped going' kind of structure)
          it is flattening a VG complex
        If the parent VP has two VP children, it moves its lexis to the first one
    These two operations output different trees.
    """
    _targetTypes = ['Verbal_Group']
    _verbTags = ['GW', 'NEG', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'BES', 'HVS', 'MD', 'TO']
    _finites = ["n't", 'not', 'to', 'be', 'been', 'being', 'is', 'are', 'was', 'were', 'has', 'had', 'have', 'having', 'do', 'does', 'doing', 'did', 'will', 'would', 'shall', 'should', 'may', 'might', 'can', 'could', 'must', "'s", "'re", "'m", "'ll", "'d", 'going', 'about', 'ca', 'wo']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _vgGroup = Constituency.VerbalGroup
    
    def _visitTarget(self, constituent):
        """
        Overrides this so that rearrangeTree doesn't have to refind the verbPhrase
        """
        verbPhrase = [group for group in constituent.groups() if group.isType('Verbal_Group')]
        if len(verbPhrase) == 1:
            self._rearrangeTree(constituent, verbPhrase[0])
        elif len(verbPhrase) > 1:
            self._moveFinite(constituent, verbPhrase[0])
        else:
            self._rejectNode(constituent)

           
            
    def _rearrangeTree(self, constituent, verbChild):
        """
        Two kinds of flattening: finite only and non-finite only
        Choose one, then execute
        Move the children of the predicator to the finite's node
        Should only be one predicator (after EllipsisHandler)
        """
        for word in constituent.children():
            if word.isType('Word'):
                if word.label not in self._verbTags:
                    if word.text.lower() not in ['about', "n't", 'not']:
                        print word
                        print word.label
                        raise StandardError
                if word.text.lower() not in self._finites:
                    self._handleComplex(constituent, verbChild)
                    break
        else:
            self._flattenSimplex(constituent, verbChild)
            
    def _handleComplex(self, constituent, verbChild):
        """
        VP stopped
          VP using
        becomes:
        VP
          VP stopped
          VP using
        """
        VG = self._constituentConstructor.make(self._vgGroup, {'type': 'Verbal_Group', 'label': 'VP', 'functionLabels': []})
        constituent.insert(VG)
        verbChild.reattach(VG)
    
    def _flattenSimplex(self, constituent, verbChild):
        """
        VP was
          VP going
        becomes:
        VP was going
        """
        for subChild in verbChild.children():
            subChild.reattach(constituent)
            self.moreChanges = True
        verbChild.prune()
        
    def _moveFinite(self, parentVP, firstVG):
        """
        Move a finite in a VG complex to one of the VG children
        VP has
           VP managed
           VP to get
        becomes:
        VP
          VP has managed
          VP to get
        WSJ 40.49
        """
        for word in parentVP.children():
            if word.isType('Lexeme'):
                word.reattach(firstVG)
        
        

                
class VerbalGroupHComplexer(TreeRearranger):
    """
    Create verbal group complexes from verbal group projections:
    VP
        trying
        S
            to
            keep
    becomes:
    VP
        VP
            trying
        VP
            to keep
    
    GroupComplexer will later convert this structure to a complex
    """
    _targetTypes = ['Verbal_Group']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _vgGroup = Constituency.VerbalGroup
    
    def _visitTarget(self, node):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        possibleProjection = self._checkConstraints(node)
        if possibleProjection:
            self._rearrangeTree(node, possibleProjection)
        else:
            self._rejectNode(node)
    
    def _checkConstraints(self, constituent):
        """
        Find out whether the VP has a clause child that meets the (complicated) constraints:
        """
        # Find clauses that meet the following constraints:
        for clause in constituent.children():
            if not clause.isType('Clause'):
                continue
            # Don't raise clauses that are subordinated
            if 'SBAR' in clause.functionLabels:
                continue
            if [adverbialLabel for adverbialLabel in clause.functionLabels if adverbialLabel != 'CLR']:
                continue
            if clause.label == 'SBAR':
                continue
            # Don't raise nominalised clauses or adverbials
            # Don't raise parentheticals
            if clause.label == 'PRN':
                continue
            # Try to avoid raising ellipsed clauses.
            # Counterexample: wsj 1825.3
            # if clause.isType('Ellipsis'):
            #     continue
            if not clause.verbalGroup():
                continue
            if not clause.verbalGroup().hasWord():
                continue
            # Try to avoid raising direct projections
            if clause.quoted:
                continue
            # All 185.78 wants this constraint for postposed subjects
            if clause.identifier:
                continue
            return clause
        else:
            return False
            
    def _rearrangeTree(self, verbalGroup, projection):
        """ 
        Move own VP children to a VP node
        Move the VG of the clause to self
        Move all other clause children to own clause
        """
        for child in projection.children():
            child.reattach(verbalGroup)
            self.moreChanges = True
        
    def _makeVP(self, node):
        
        for child in node.children():
            child.reattach(selfVP)
        node.attachChild(selfVP)
        return selfVP
        
        
        
class VerbalGroupPComplexer(TreeRearranger):
    """        
    Paratactic (co-ordination) complexing of verbal groups
    VG
        VBG maintaining
        CC  or
        VBG incrreasing
    becomes:
    VG
        VG
            maintaining
        CC or
        VG
            increasing
    """
    _targetTypes = ['Verbal_Group']
    _verbTags = ['GW', 'NEG', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'BES', 'HVS', 'RB']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _vgGroup = Constituency.VerbalGroup
    _finites = ["n't", 'not', 'to', 'be', 'been', 'being', 'is', 'are', 'was', 'were', 'has', 'had', 'have', 'having', 'do', 'does', 'doing', 'did', 'will', 'would', 'shall', 'should', 'may', 'might', 'can', 'could', 'must', "'s", "'re", "'m", "'ll", 'going', 'about']
    def _checkConstraints(self, constituent):
        """
        Look for multiple head words
        """
        lexis = [word for word in constituent.children() if (word.isType('Lexeme')) and (word.label in self._verbTags)]
        lexis.sort()
        if len(lexis) < 2:
            return False
        else:
            if (lexis[-1].text.lower() not in self._finites) and (lexis[-2].text.lower() not in self._finites):
                return True
            else:
                return False
    
    def _rearrangeTree(self, constituent):
        """
        Just want a VG with two VG children, so that the structure will match GroupComplexer's constraints
        """
        lexis = [word for word in constituent.children() if (word.isType('Lexeme')) and (word.label in self._verbTags)]
        lexis.sort()
        groups = [g for g in constituent.groups()]
        newVGs = []
        for lexeme in lexis:
            VG = self._constituentConstructor.make(self._vgGroup, {'type': 'Verbal_Group', 'label': 'VP', 'functionLabels': []})
            lexeme.insert(VG)
            newVGs.append(VG)
        # Allocate groups (EG particles) to the new VGs (WSJ 1771.10)
        for group in groups:
            group.allocate(newVGs)


class MWConjunctionGrouper(TreeRearranger):
    """
    Group multi-word conjunctions that are attached to an SBAR
    """
    _targetTypes = ['Clause']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _cjGroup = Constituency.ConjunctionGroup
                 
    
    def _visitTarget(self, node):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        words = self._checkConstraints(node)
        if words:
            self._rearrangeTree(words)
        else:
            self._rejectNode(node)
    
    def _checkConstraints(self, clause):
        """
        Look for SBAR nodes that have word sets in the list immediately attached
        """
        if not clause.label in ['SBAR', 'SBARQ']:
            return False
        initialWords = []
        for child in clause.children():
            if not child.isType('Lexeme'):
                break
            elif child.isType('Word'):
                initialWords.append(child)
        if len(initialWords) > 1:
            string = ' '.join([w.text.lower() for w in initialWords])
            return initialWords
        return None
        
    def _rearrangeTree(self, words):
        """
        Insert a CJ group over the first word, attach the other words to it
        """
        conjunctionGroup = self._constituentConstructor.make(self._cjGroup, {'type': 'Conjunction_Group', 'label': 'CONJP', 'functionLabels': []})
        words[0].insert(conjunctionGroup)
        for w in words[1:]:
            w.reattach(conjunctionGroup)
        
        
    
                
class ConjunctionGrouper(TreeRearranger):
    """
    Create group nodes for conjunctions, and move the lexis to them
    """
    _targetTypes = ['Word']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _cjGroup = Constituency.ConjunctionGroup
    
    def _checkConstraints(self, constituent):
        """
        Check that word is a conjunction
        """
        # Only these POS can be conjunctions
        if not constituent.label in ['IN', 'CC', 'CS', 'RB']:
            return False
        if constituent.parent().isType('Clause'):
            return True
        # If it's a verbal group, check that the constituent isn't "n't" or "not"
        elif constituent.parent().isType('Verbal_Group'):
            if constituent.text.lower() in ["n't", 'not', 'about']:
                return False
            else:
                return True
        # Don't raise for other parents (the problem only really applies to VG or clauses)
        else:
            return False
    
    def _rearrangeTree(self, constituent):
        """
        Create a conjunction group and move the word to it
        """
        conjunction = self._constituentConstructor.make(self._cjGroup, {'type': 'Conjunction_Group', 'label': 'CONJP', 'functionLabels': []})
        constituent.insert(conjunction)





class ConjunctionAndWHReassigner(TreeRearranger):
    """
    Reassign conjunctions that end a clause to the following clause
    """
    _targetTypes = ['Group']
    
    def _visitTarget(self, constituent):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        correctClause = self._checkConstraints(constituent)
        if correctClause:
            self._rearrangeTree(constituent, correctClause)
        else:
            self._rejectNode(constituent)
    
    def _checkConstraints(self, conjunction):
        """
        Look for a conjunction that is the last group of its parent,
        when the word immediately after it is the first word of a clause
        
        WSJ 122.10
        """
        # WSJ 7.3
        if not conjunction.hasWord():
            return False
        if not conjunction.isType('Conjunction_Group'):
            if not conjunction.label in ['WHNP', 'WHADVP']:
                return False
        if conjunction.parent().group(-1) != conjunction:
            return False
        complex = conjunction.parent()
        while not complex.isRoot():
            complex = complex.parent()
        words = complex.listWords()
        # ATIS 0.1271
        if conjunction == words[-1]:
            return False
        index = words.index(conjunction.getWord(-1))
        if index == len(words) - 1:
            return False
        nextWord = words[index + 1]
        parent = nextWord.parent()
        while nextWord == parent.getWord(0):
            if parent.isType('Clause'):
                return parent
            else:
                parent = parent.parent()
        else:
            return False
        
            
    def _rearrangeTree(self, conjunction, rightClause):
        """
        Reattach the conjunction to the clause to its right
        """
        assert rightClause.isType('Clause')
        self.moreChanges = True
        conjunction.reattach(rightClause)
        
class ETCConjunctionReassigner(TreeRearranger):
    """
    SWBD has a special -ETC construction for "and stuff" adjuncts.
    Conjunctions need to be moved to these NPs
    """
    _targetTypes = ['Conjunction_Group']
    
    def _visitTarget(self, conjunction):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        etcGroup = self._checkConstraints(conjunction)
        if etcGroup:
            self._rearrangeTree(conjunction, etcGroup)
        else:
            self._rejectNode(conjunction)
            
    def _checkConstraints(self, conjunction):
        """
        Look for a conjunction where the group immediately following has a
        -ETC function label
        """
        siblings = conjunction.parent().groups()
        if conjunction == siblings[-1]:
            return False
        cjIndex = siblings.index(conjunction)
        if 'ETC' in siblings[cjIndex + 1].functionLabels:
            return siblings[cjIndex + 1]
            
    def _rearrangeTree(self, conjunction, etcGroup):
        """
        Move the conjunction to the etcGroup
        """
        conjunction.reattach(etcGroup)
    
        
class ClauseNominaliser(TreeRearranger):
    """
    Move nominalised clauses to a nominal group node
    """
    _targetTypes = ['Clause']
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _ngGroup = Constituency.NominalGroup
    
    def _checkConstraints(self, constituent):
        """
        Check NOM tag in function labels
        """
        if 'NOM' in constituent.functionLabels:
            return True
        elif 'PRD' in constituent.functionLabels:
            return True
        # WSJ 2259.45
        elif 'TTL' in constituent.functionLabels:
            return True
        else:
            return False
   
    def _rearrangeTree(self, clause):
        """
        Create a NG node and insert it into the tree above constituent
        """
        nominalGroup = self._constituentConstructor.make(self._ngGroup, {'type': 'Nominal_Group', 'label': 'NP', 'functionLabels': []})
        clause.insert(nominalGroup)
        # Grab function labels, e.g. subject (WSJ 12.? "What matters...")
        nominalGroup.functionLabels.extend(clause.functionLabels)
        # Don't Add metadata
       # nominalGroup.metadata['Nominalisation'] = True





    
class VerblessADVClauseRemover(TreeRearranger):
    """
    In the treebank, adverbial adjective phrases are treated as separate clauses.
    Move them to the following clause, and add an ADV function label:
        
    S-ADV
      ADJP Unable to handle the pressure,
    S
      NP stuff
      VP happened
    becomes:
    S
      NP-ADV Unable to handle the pressure,
      NP stuff
      VP happened
    Real example at wsj 117.58
    Another at wsj_2454.mrg~0009
    """
    _targetTypes = ['Clause']
    _advTags = ['DIR', 'TMP', 'ADV', 'MNR', 'LOC', 'EXT']
    
    def _checkConstraints(self, constituent):
        """
        Look for verbless adverbial clauses
        """
        # Don't flatten if it's the only clause in the complex
        # (WSJ 886.14)
        otherRankingClauses = [rc for rc in constituent.rankingClauses() if rc != constituent]
       # for orc in otherRankingClauses:
       #     print orc
        if not otherRankingClauses:
            return False
        # Don't flatten unfinished clauses (SWBD 207.237)
        if 'UNF' in constituent.functionLabels:
            return False
        # Don't flatten if within a dysfluency -- SWBD 52.31
        if constituent.parent().isType('Dysfluency'):
            return False
        # WSJ 147.13
        if constituent.label == 'SBAR':
            return False
        if not [l for l in constituent.functionLabels if l in self._advTags]:
            groups = [c for c in constituent.children() if c.isType('Group')]
            if len(groups) == 1:
                if [l for l in groups[0].functionLabels if l in self._advTags]:
                    return True
            return False
        if constituent.verbalGroup():
            return False
        return True
    
    def _rearrangeTree(self, constituent):
        """
        Allocate the children to siblings
        """
        otherRankingClauses = [rc for rc in constituent.rankingClauses() if rc != constituent]
        for child in constituent.children():
            if child in otherRankingClauses:
                child.reattach(constituent.parent())
                continue
            child.functionLabels.extend(constituent.functionLabels)
            child.allocate(otherRankingClauses)
        constituent.prune()





class TraceMover(TreeRearranger):
    """
    ICH ('insert constituent here') traces are used to connect interrupted
    constituents. Since the constituency tree allows interruptions, these
    constituents-by-reference should be moved to their appropriate location
    """
    _traceIndexer = singleton(TraceIndexer)
    _copyConstructor = singleton(ConstituentConstructors.CopyCreator)

    
    def actOn(self, constituent):
        if constituent.isType('Clause_Complex'):
            self._movedRNRNodes = {}
            self._visitRoot(constituent)
        elif constituent.isType('Trace'):
            self._visitLeaf(constituent)
        else:
            self._rejectNode(constituent)
    
    def _visitRoot(self, constituent):
        """
        When the root node is visited, build a trace index using a second node visitor
        """
       # if self._traceIndexer.traceIndex():
       #     print self._traceIndexer.traceIndex()
        constituent.performOperation(self._traceIndexer)
        self._traceIndex = self._traceIndexer.traceIndex()

        
    def _visitLeaf(self, trace):
        """
        If the leaf is an ICH trace, move its reference node to its parent
        """
        # If text starts with one of the following labels:
        # TPC removed
        firstID = trace.parent().getWordID(0)
        lastID = trace.parent().getWordID(-1)
        node = trace.parent()
        index = [c for c in node.children()].index(trace)
        # Hackishly reject ICH movement for now
       # if [label for label in ['*ICH*', '*EXP*'] if trace.text.startswith(label)]:
        if 0:
            traceKey = trace.text.split('-')[1]
            references = self._traceIndex.get(traceKey, [])
            try:
                assert len(references) == 1
            except:
                print len(references)
                for reference in references:
                    print reference
                print traceKey
                assert len(references) == 1
            trace.parent().replace(trace, references[0])
        elif trace.text.startswith('*RNR*'):
            traceKey = trace.text.split('-')[1]
            references = self._traceIndex[traceKey]
            assert len(references) == 1
            if not self._movedRNRNodes.has_key(traceKey):
                self._presetIDs(trace.wordID, references[0])
                # HACK -- For sw2645.mrg~2645
                try:
                    references[0].reattach(trace.parent(), index)
                except StandardError:
                    return None
                self._movedRNRNodes[traceKey] = 1
            elif self._checkCopyConstraints(references[0], trace.parent()):
                newCopy = self._copyConstructor.make(references[0])
                self._presetIDs(trace.wordID, newCopy)
                trace.parent().attachChild(newCopy, index)
       # self._fixIDs(node, firstID, lastID)
        
                
    def _checkCopyConstraints(self, node, newPosition):
        """
        Check that the node to be copied will not end up being a ranking clause
        """
        if not node.isType('Clause'):
            return True
        elif [t for t in ['Verbal_Group', 'Clause', 'Clause_Complex'] if newPosition.isType(t)]:
            return False
        else:
            return True
    
    def _presetIDs(self, traceID, reference):
        """
        Renumber the reference's words using the trace's ID
        """
        # FIX ME -- HACK
        # Surely the reference shouldn't be renumbered -- if so, there's no way to
        # retrieve the original word order...But no idea how this impacts on ellipsis...
        # Leaving this dangling, since unclear whether RNR should even be ellipsis.
        for word in reference.listWords():
           # word.wordID = traceID
            traceID += 0.00001
    
    def _fixIDs(self, node, firstID, lastID):
        """
        Items are in correct order, just get a range of IDs and ensure that they fall between it
        """
        difference = float(lastID - firstID)
        increment = difference/float(len(node.listWords()))
        words = node.listWords()
        words.sort()
        for word in words:
            word.wordID = firstID
            firstID += increment
    
    def _calculateIncrement(self, firstID, lastID, length):
        difference = float(lastID - firstID)
        increment = difference/float(length)
        return increment

                
class EllipsisHandler(TreeRearranger):
    """
    Handle ellipsed clauses by creating a new clause with the sharing verbal groups,
    identifying the shared elements, and adding wrapped copies to the new clause
    """
    _targetTypes = ['Verbal_Group', 'Clause']
    _clauseClass = Constituency.Clause
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    _ellipsisConstructor = singleton(ConstituentConstructors.CopyCreator)
    _verbTags = ['GW', 'NEG', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'BES', 'HVS', 'MD', 'TO', 'RB']
    counter = 0
    
    def _checkConstraints(self, constituent):
        """
        Check whether the node has two or more verb phrase children
        """
        childVPs = [vp for vp in constituent.children() if vp.label == 'VP' and vp.hasWord()]
        if len(childVPs) > 1:
            return True
        else:
            return False
    
    def _rearrangeTree(self, constituent):
        """
        Identify original VP, sharing VPs, shared items and parent clause
        Create one new clause for each sharing VP, and add wrapped versions of
        each shared item to it.
        Attach the new clauses to the parent clause
        """
        # Find elements
        sharingVPs = [vp for vp in constituent.children() if vp.label == 'VP']
        sharingVPs.sort()
        originalVP = sharingVPs.pop(0)
        parentClause = constituent.clause()
        sharedItems = self._findShared(originalVP)
#        # Hackishly circumvent sharing for now
#        sharedItems = []
        conjunctions = [child for child in constituent.children() if child.isType('Conjunction_Group')]
        sharedItems = [item for item in sharedItems if item not in conjunctions]
        clauses = []
        # Create clauses, attach their children, attach them to the tree
        for VP in sharingVPs:
            clause = self._constituentConstructor.make(self._clauseClass, {'type': 'Clause', 'label': 'S', 'functionLabels': [], 'metadata': {}})
            firstID = VP.getWordID(0)
            lastID = VP.getWordID(-1)
            VP.reattach(clause)
            EllipsisHandler.counter += 1
            for sharedOriginal in sharedItems:
                ellipsedNode = self._ellipsisConstructor.make(sharedOriginal)
                # Assume words are finites
                if ellipsedNode.isType('Word'):
                    # Check that assumption
                    assert ellipsedNode.label in self._verbTags
                    # Attach the ellipsed node in a place that doesn't upset the word order
                    self._attachEllipsis(VP, ellipsedNode, sharedOriginal)
                else:
                    # Attach the ellipsed node in a place that doesn't upset the word order
                    self._attachEllipsis(clause, ellipsedNode, sharedOriginal)
            # This must be inherited to stop VG-H complexing
            if 'SBAR' in parentClause.functionLabels:
                clause.functionLabels.append('SBAR')
            clauses.append(clause)
#            if parentClause.parent():
#                parentClause.parent().attachChild(clause)
#            else:
            parentClause.attachChild(clause)
            self._fixIDs(clause, firstID, lastID)
        # Append the constituent's clause, so that it is an option for allocation
        clauses.append(constituent.clause())
        for conjunction in conjunctions:
            conjunction.allocate(clauses)
        
        

        
        
    def _findShared(self, constituent):
        """
        Get a list of nodes adjacent to the path between constituent and its clause
        
        That is, iterate up the tree, and collect the siblings of each node.
        """
        currentNode = constituent
        ellipsedNodes = []
        # Iterate up the tree
        while (not currentNode.isType('Clause')) and (not currentNode.isType('Clause_Complex')):
            # Check each node at the given level for constraints\
            for sibling in currentNode.parent().children():
                if sibling.isType('Verbal_Group'):
                    continue
                if sibling.isType('Clause'):
                    continue
                if sibling in ellipsedNodes:
                    continue
                if sibling == currentNode:
                    continue
                # wsj 295.18
                if sibling.isType('Conjunction_Group'):
                    continue
                # Try not to copy sentence-final markers
                if sibling.label == '.':
                    continue
                # Untested, but suggested by a problem with an ellipseme's reference being deleted
                parent = sibling
                while parent:
                    if parent.isType('Dysfluency'):
                        break
                    parent = parent.parent()
                else:
                    ellipsedNodes.append(sibling)
            # Move up the tree
            currentNode = currentNode.parent()
        if currentNode.isType('Clause'):
            for sibling in currentNode.siblings():
                if sibling < constituent and sibling.label.startswith('W'):
                    ellipsedNodes.append(sibling)
        return ellipsedNodes
        
    
    def _attachEllipsis(self, parent, ellipsed, original):
        """
        Change the IDs on ellipsed node so that it occurs at the same child offset
        in the new parent as it does for its old parent
        """
        original.parent().sortChildren()
        if original.hasWord():
            ellipsisOffset = [c for c in original.parent().children() if c.hasWord()].index(original)
        else:
            ellipsisOffset = 0
        if parent.isType('Clause') and original.parent().isType('Clause'):
            vgOffset = 0
            for c in parent.children():
                if c == parent.verbalGroup():
                    break
                vgOffset += 1
            realOffset = 0
            for c in original.parent().children():
                if c.hasWord():
                    if c == original.parent().verbalGroup():
                        break
                    ellipsisOffset += 1
            # Check whether before or after VP
            if ellipsisOffset < realOffset:
                # Attach before VP
                parent.attachChild(ellipsed, vgOffset)
            else:
                # Attach after VP
                parent.attachChild(ellipsed, vgOffset + 1)
        else:
            parent.attachChild(ellipsed, ellipsisOffset)
        

        
    def _fixIDs(self, clause, firstID, lastID):
        """
        Items are in correct order, just get a range of IDs and ensure that they fall between it
        """
        modFirstID = float(firstID) - 0.05
        modLastID = float(lastID)
        for word in clause.listWords():
            if word.wordID < firstID:
                modFirstID += 0.001
                word.wordID = modFirstID
            elif word.wordID > lastID:
                modLastID += 0.001
                word.wordID = modLastID
        
        

        

class GappedClauseHandler(TreeRearranger):
    _targetTypes = ['Clause_Complex']
    _traceIndexer = singleton(TraceIndexer)
    _copyConstructor = singleton(ConstituentConstructors.CopyCreator)
    counter = 0
    
    def _checkConstraints(self, clauseComplex):
        """
        If no nodes identify a parrallel node, there is no gapping.
        On the parse tree, this looks like:
        S
          NP-1
          VG
          PP-2
        S
          NP=1
          PP=2
        Where -2 specifies 2 as a template for =2.
        During construction, the = references are stored in 'identified',
        which are then used as keys into a trace index.
        """
        for node in clauseComplex.depthList():
            if node.identified:
                return True
        return False
        
    
    def _rearrangeTree(self, clauseComplex):
        """
        Find the original node and all the gapped nodes. Then create copies of
        the original, and substitute in the specific nodes for the template nodes
        """
        self._IDOffset = 1000
        # Get a trace index
        clauseComplex.performOperation(self._traceIndexer)
        traceIndex = self._traceIndexer.traceIndex()
        # Find template parent
        templateParent = self._findOriginalClause(traceIndex, clauseComplex)
        # Find the gapped nodes
        replacementSets = self._findGappedNodes(templateParent)
        # Replace the gapped nodes with appropriately adjusted copies of the original
        for replacedNode, replacements in replacementSets:
            GappedClauseHandler.counter += 1
            self._makeReplacement(replacedNode, replacements, templateParent)
        # Remake the trace index, because trace indexes may have changed to prevent ambiguity
        self._traceIndexer.newStructure()
        self._traceIndexer.actOn(clauseComplex)
            
            
    
    def _makeReplacement(self, replacedNode, replacements, templateNode):
        """
        Make a copy of the template clause and replace the template nodes with
        the substitutes
        """
        copyNode = self._copyConstructor.make(templateNode)
        realIDs = [w.wordID for w in replacedNode.listWords()]
        for node in copyNode.depthList():
            replacement = replacements.get(node.identifier)
            if replacement:
                # Detach the original node and insert the replacement at the original's index
                node.parent().replace(node, replacement)
        templateNode.parent().attachChild(copyNode)
        assert replacedNode.parent() == templateNode.parent()
        # Move non-parallel nodes to the new copy ie nodes which are not substitutes
        # of templates
        for child in replacedNode.children():
            if not child.identified:
                child.reattach(copyNode)
        replacedNode.prune()
        # Fix IDs
        self._fixIDs(realIDs, copyNode)
        # Fix ambiguated trace references
        self._fixTraceLinks(copyNode)
        
    
    def _findGappedNodes(self, templateParent):
        """
        Get a list of the template parent's siblings that contain a linking node
        Output a list of (parent, hash) tuples, where the hashes match identifiers
        to replacement nodes
        """
        siblings = templateParent.siblings()
        replacementSets = []
        for sibling in siblings:
            dict = {}
            for node in sibling.depthList():
                if node.identified:
                    dict[node.identified] = node
            if dict:
                replacementSets.append((sibling, dict))
        return replacementSets
            
        
    def _findOriginalClause(self, traceIndex, clauseComplex):
        """
        Search the complex's tree for a node that governs all template nodes
        """
        # Get a list of nodes that link to a template
        substitutionNodes = [n for n in clauseComplex.depthList() if n.identified]
        # Get a list of the IDs used by template nodes
        uniqueIDs = []
        for node in substitutionNodes:
            if node.identified not in uniqueIDs:
                uniqueIDs.append(node.identified)
        # Get the template nodes
        templateNodes = [traceIndex[ID][0] for ID in uniqueIDs]
        # Find the lowest common ancestor of the identified and template nodes
        lowestCommonAncestor = self._lowestCommonAncestor(templateNodes + substitutionNodes)
        # Look through its children for the node that dominates the template nodes
        for node in lowestCommonAncestor.children():
            if node in templateNodes:
                return node
            for child in node.depthList():
                if child in templateNodes:
                    return node
        # Complain if you can't find it
        raise StandardError, "Original clause not found!"
        
        
    def _lowestCommonAncestor(self, nodes):
        """
        Find the lowest common ancestor of two nodes
        """
        parent = nodes[0].parent()
        while not self._isCommonAncestor(parent, nodes):
            parent = parent.parent()
        return parent
        
    def _isCommonAncestor(self, parent, nodes):
        """
        Check whether all of a list of nodes are in a parent's node list
        """
        nodeList = [n for n in parent.depthList()]
        for node in nodes:
            if node not in nodeList:
                return False
        return True
        
        
    def _fixIDs(self, realIDs, copyNode):
        """
        Assume that he nodes in the copy are in the correct order, but must be renumbered
        so that when they are sorted later, they are not moved out of order.
        
        Iterate through the words of the copy and template. If a word isn't
        in realWords, renumber it so that it immediately follows the last valid
        word ID
        """
        words = copyNode.listWords()
        lastValidID = float(realIDs[0])
        lastValidID -= 0.05
        for word in words:
            if word.wordID in realIDs:
                lastValidID = float(word.wordID)
            else:
                lastValidID += 0.001
                word.wordID = lastValidID
        
    def _fixTraceLinks(self, parentNode):
        """
        Because gapping is dealt with before general trace movement, it can cause
        trace-reference replication -- that is, the reference of a trace node is replicated,
        and so the reference becomes ambiguous. To avoid this, the trace and its reference's
        identifier need to be altered to be made unique.
        """
        self._IDOffset += 1
        for node in parentNode.depthList():
            if node.isType('Trace') and '-' in node.text:
                text, traceNumber = node.text.split('-')
                # Don't change for RNR -- hopefully the node will be outside (wsj 1825.3)
                if text == '*RNR*':
                    continue
                traceNumber = int(traceNumber)
                traceNumber += self._IDOffset
                node.text = text + '-' + str(traceNumber)
            if node.identifier:
                newID = int(node.identifier) + self._IDOffset
                node.identifier = str(newID)
            if node.identified:
                newID = int(node.identified) + self._IDOffset
                # Changing the identified to identifier allows the reference to connect with a trace
                # All 1.38
                if not node.identifier:
                    node.identifier = str(newID)

    


    
    
class GroupComplexer(TreeRearranger):
    _constituentConstructor = singleton(ConstituentConstructors.GroupComplexCreator)
    
    def actOn(self, constituent):
        if constituent.isType('Clause'):
            self._rejectNode(constituent)
        elif constituent.isType('Clause_Complex'):
            self._rejectNode(constituent)
        elif constituent.isType('Word'):
            self._rejectNode(constituent)
        elif constituent.isType('Dysfluency'):
            self._rejectNode(constituent)
        else:
            self._visitTarget(constituent)
    
    def _visitTarget(self, node):
        """
        If the visitor lands on a node of the correct type, check constraints
        and then perform the restructuring
        """
        if self._checkConstraints(node):
            self._rearrangeTree(node)    
        else:
            self._rejectNode(node)
    
        
    def _checkConstraints(self, constituent):
        """
        Checks that a node has two or more direct children
        with the same label as itself
        """
        # Children with the same type as node (as opposed to stricter label -- wsj 1523.1)
        sameLabelled = [child for child in constituent.children() if (child.abbr == constituent.abbr) and (child.listWords())]
        # Check whether there's at least two
        if len(sameLabelled) > 1:
            return True
        else:
            return False
        
        
    def _rearrangeTree(self, constituent):
        """
        Replace node's constituent with a complex constituent instead
        """
        wrappedConstituent = self._constituentConstructor.make(constituent)
        for child in constituent.children():
            child.reattach(wrappedConstituent)
        constituent.parent().attachChild(wrappedConstituent)
        constituent.prune()



class CorrectedItemMover(TreeRearranger):
    """
    Move EDITED groups to the node that replaces them, as a dysfluency
    
    Also truncate TYPO groups, adding metadata to their words
    """
    _targetTypes = ['Dysfluency']
    
    def _checkConstraints(self, dysfluency):
        """
        Deal only with EDITs that have not been moved
        """
        if dysfluency.label == 'TYPO':
            self._handleTypo(dysfluency)
            return False
        if dysfluency.label != 'EDITED':
            return False
        if dysfluency.replacement():
            return False
        # If the dysfluent unit is a clause, don't move it
        if [g for g in dysfluency.children() if g.isType('Clause')]:
            return False
        return True
        
    def _handleTypo(self, dysfluency):
        """
        Move words to the dysfluency's parent, making sure they are words, and
        add metadata to note they are typos
        """
        for word in dysfluency.children():
            assert word.isType('Lexeme') or word.label == 'INTJ'
            word.metadata['typo'] = True
            word.reattach(dysfluency.parent())
        dysfluency.prune()
    
    def _rearrangeTree(self, editedDFL):
        """
        Find the replacement group and attach the editedDFL to it as a dysfluency
        """
        replacement = self._findReplacement(editedDFL)
        if replacement:
            editedDFL.reattach(replacement)
        
        
    def _findReplacement(self, editedDFL):
        """
        This looks wrong. Re-evaluate it late
        """
        if [c for c in editedDFL.children() if c.label == 'RS']:
            # Don't attach to dysfluency SWBD 0.214
            siblings = [s for s in editedDFL.siblings() if not s.isType('Lexeme') and not s.isType('Dysfluency')]
            if not siblings:
                return None
            else:
                # Right, not left: All 277.326
                editedDFL.allocate(siblings, 'Right')
        # Now look for the first rightward sibling with an RS
        seenSelf = False
        for c in editedDFL.parent().children():
            if seenSelf:
                if [sc for sc in c.children() if sc.label == 'RS']:
                    return c
            elif c == editedDFL:
                seenSelf = True
        return None
        


    
        
class Pruner(TreeRearranger):
    """
    Remove subtrees that do not terminate in Lexemes
    """
    def actOn(self, constituent):
        self._visitTarget(constituent)
    
    def _checkConstraints(self, constituent):
        """
        Check whether word list is empty
        """
        if constituent.isType('Lexeme'):
            return False
        elif constituent.listWords():
            return False
        else:
            return True
    
    def _rearrangeTree(self, constituent):
        # May still be punctuation
        for child in constituent.children():
            child.reattach(constituent.parent())
        if constituent.parent():
            constituent.prune()
        
        
class TracePruner(TreeRearranger):
    """
    Remove traces
    """
    _targetTypes = ['Trace']
    
    def _checkConstraints(self, constituent):
        """
        Check whether word list is empty
        """
        return True
    
    def _rearrangeTree(self, constituent):
        constituent.prune()
        
class DFLPruner(TreeRearranger):
    """
    Remove traces
    """
    _targetTypes = ['Dysfluency']
    
    def _checkConstraints(self, constituent):
        """
        Check whether word list is empty
        """
        return True
    
    def _rearrangeTree(self, constituent):
        constituent.prune()
        
        
class Truncater(TreeRearranger):
    """
    Replace nodes with one child with that child, thereby
    shortening branches that do not fork
    """
    def actOn(self, constituent):
        if constituent.isType('Lexeme'):
            self._rejectNode(constituent)
        elif constituent.isType('Clause_Complex'):
            self._rejectNode(constituent)
        # Do not truncate edited groups (swbd 0.2)
        elif constituent.isType('Dysfluency'):
            self._rejectNode(constituent)
        # Truncate small clauses (sentence 1204.16)
        elif constituent.isType('Clause'):
            self._visitClause(constituent)
        else:
            self._visitTarget(constituent)
    
    def _checkConstraints(self, constituent):
        """
        Check length of _children
        """
        children = [child for child in constituent.children() if (not child.isType('Punctuation')) and (not child.isType('Trace'))]
        if len(children) == 1:
            if children[0].isType('Word'):
                return False
            if children[0].isType('Clause'):
                return False
            elif constituent.parent():
                self.moreChanges = True
                return True
            else:
                return False
        else:
            return False
            
    def _rearrangeTree(self, constituent):
        for child in constituent.children():
            if type(child.functionLabels) == list:
                child.functionLabels.extend(constituent.functionLabels)
            else:
                for fl in constituent.functionLabels:
                    child.functionLabels[fl] = True
           # Interferes with SWBD 0.112 ... Example where it's needed?
           # if constituent.parent().isType('Clause_Complex'):
           #     child.allocate([c for c in constituent.parent().children()])
           # else:
            child.reattach(constituent.parent())
        constituent.prune()

    def _visitClause(self, clause):
        """
        Clauses have special truncation rules:
            if there are no siblings and parent isnt clause, don't truncate
            if there is a verbal or nominal group, don't truncate
            if there isn't, allocate the children to siblings if any. if no
            siblings, allocate to parent
        """
        # For complex clauses, check length of children
        if clause.isType('Complex') and clause.length() > 1:
            return None
        # SWBD 102.47
        if (not [c for c in clause.siblings() if c.isType('Clause')]) and (not clause.parent().isType('Clause')):
            return None
        if clause.quoted and clause.hasWord():
            return None
        for child in clause.children():
            if not child.hasWord():
                continue
            if child.isType('Verbal_Group'): return None
            if child.isType('Nominal_Group'): return None
        # Added for WSJ 669.9
        else:
            # WSJ 113.15: Attach conjunctions in verbless clauses to a constituent
            conjunctions = [c for c in clause.groups() if c.isType('Conjunction_Group')]
            nonConjunctionGroups = [g for g in clause.groups() if not g.isType('Conjunction_Group')]
            if nonConjunctionGroups:
                for c in conjunctions:
                    c.allocate(nonConjunctionGroups)
            clauseSiblings = [c for c in clause.parent().children() if c.isType('Clause') and c != clause]
            if clauseSiblings:
                for child in clause.children():
                    child.allocate(clauseSiblings)
            else:
                for child in clause.children():
                    child.reattach(clause.parent())
            clause.prune()
            
class PunctuationRaiser(TreeRearranger):
    """
    Rationalise the assignment of punctuation, so that it does not ever interrupt groups or clauses
    
    Step 1: Assign punctuation to the immediate parent of the word that immediately proceeds it
    Step 2: Raise it to the highest group where that word is the last word
    
    all 1.17
    """
    _targetTypes = ['Punctuation', 'Trace']
    
    def _checkConstraints(self, constituent):
        if constituent.parent().isType('Clause_Complex'):
            return False
        else:
            return True
    
    def _rearrangeTree(self, punctuation):
        nearestSibling = self._findNearestSibling(punctuation)
        parent = punctuation.parent()
        while (parent.parent().getWord(-1) == nearestSibling) and (not parent.parent().isType('Clause_Complex')):
            parent = parent.parent()
        punctuation.reattach(parent)

        
    def _findNearestSibling(self, punctuation):
        words = [w for w in punctuation.parent().listWords() if w.isType('Word')]
        words.sort()
        index = bisect.bisect_right(words, punctuation)
        if index:
            index -= 1
        return words[index]
        
            

class PunctuationLowerer(TreeRearranger):
    """
    Rationalise the assignment of punctuation, so that it does not ever interrupt groups or clauses
    
    Step 1: Assign punctuation to the immediate parent of the word that immediately proceeds it
    """
    _targetTypes = ['Clause_Complex']
    def _checkConstraints(self, complex):
        return complex.hasWord()
    
    def _rearrangeTree(self, complex):
        words = [w for w in complex.listWords() if w.isType('Word')]
        words.sort()
        pAndT = [w for w in complex.listWords() if not w.isType('Word')]
        for w in pAndT:
            index = bisect.bisect_right(words, w)
            if index:
                index -= 1
            parent = words[index].parent()
            w.reattach(parent)
        
 

class FillerLowerer(TreeRearranger):
    """
    Lower um, er, uh etc gap fillers in much the same way punctuation is lowered
    """
    _targetTypes = ['Clause_Complex']
    def _checkConstraints(self, complex):
        # If there are words to attach filler to
        if [w for w in complex.listWords() if w.isType('Word') and w.label != 'UH']:
            return True
        else:
            return False
    
    def _rearrangeTree(self, complex):
        words = [w for w in complex.listWords() if w.isType('Word') and w.label != 'UH']
        words.sort()
        # Extra constraint for WSJ 101.40
        fillers = [w for w in complex.listWords() if w.label == 'UH' and w.parent().label == 'INTJ' and w.parent().isType('Dysfluency')]
        for um in fillers:
            index = bisect.bisect_right(words, um)
            if index >= len(words):
                index -= 1
            parent = words[index].parent()
            if parent != um.parent() and parent not in um.parent().depthList():
                um.parent().reattach(parent)
        
        
        
class ConstraintChecker(TreeOperation):
    """
    Check that SFG constraints are met, and complain if they aren't,
    thus alerting me to problems in the script.
    """
    _printer = Printer()
    def actOn(self, constituent):
        if constituent.isType('Clause_Complex'):
            self._visitClauseComplex(constituent)
        elif constituent.isType('Clause'):
            self._visitClause(constituent)
        elif constituent.isType('Group'):
            self._visitGroup(constituent)
        elif constituent.isType('Lexeme'):
            self._visitLexeme(constituent)
        else:
            raise ConstraintError, "Constituent was neither clause complex, clause, group or leaf: " + str(constituent)
    
    def _visitAny(self, constituent):
        raise ImplementationError, "Subclasses must override this function"
    
    def _visitClauseComplex(self, constituent):
        raise ImplementationError, "Subclasses must override this function"
        
    def _visitClause(self, constituent):
        raise ImplementationError, "Subclasses must override this function"
        
    def _visitGroup(self, constituent):
        raise ImplementationError, "Subclasses must override this function"

    def _visitLexeme(self, constituent):
        raise ImplementationError, "Subclasses must override this function"


class LexOrderConstraint(ConstraintChecker):
    """
    Verify that the number and order of tokens has been preserved
    """
    def actOn(self, node):
        if isinstance(node, Nodes.RootNode):
            self._visitRoot(node)
        else:
            pass
    
    def _visitRoot(self, rootNode):
        """
        Zip the node and constituent's tokens, then verify them
        """
        nWords = rootNode.listWords()
        cWords = [w for w in rootNode.constituent.listWords() if not w.isType('Ellipsis')]
        nWords.sort()
        cWords.sort()
       # print [(w.wordID, w.text) for w in nWords]
       # print [(w.wordID, w.text) for w in cWords]
        assert len(nWords) == len(cWords)
        words = zip(nWords, cWords)
        for nWord, cWord in words:
            if cWord.isType('Trace'):
                if '-' in cWord.text:
                    continue
            try:
                assert nWord.text == cWord.text
            except:
                print [(w.wordID, w.text) for w in nWords]
                print [(w.wordID, w.text) for w in cWords]
                print nWord.text
                print cWord.text
                print
                raise ConstraintError, "Words do not match!"
    

class FinalConstraints(ConstraintChecker):
    """
    Constraints that the parse should obey by the end
    """
    def _visitAny(self, constituent):
        pass

    def _visitClauseComplex(self, constituent):
        """
        If at least one clause has a verbal group, all clauses should
        have a verbal group
        """
        if [c for c in constituent.children() if c.isType('Clause') and c.verbalGroup()]:
            for clause in constituent.children():
                if not clause.isType('Clause'):
                    continue
                if clause.quoted:
                    continue
                if clause.verbalGroup():
                    continue
                # Allow clauses of one constituent if that constituent is an NP
                children = [c for c in clause.children() if c.isType('Group')]
                if (children[0].isType('Nominal_Group')) and (clause.label == 'FRAG'):
                    continue
                # Allow minor clause conditionals
                elif children[0].listWords()[0].text.lower() == 'if':
                    continue
                else:
                    raise ConstraintError, 'At least one clause has a verbal group, and at least one other clause does not'
        
    def _visitClause(self, constituent):
        pass
        
    def _visitGroup(self, constituent):
        if constituent.parent().isType('Clause_Complex'):
            raise ConstraintError, "Group attached directly to complex: " + str(constituent.parent())
        
    def _visitLexeme(self, constituent):
        """
        Lexis should:
            1. Always have a group parent (as opposed to clause or clause complex
        """
        if (constituent.isType('Word')) and (not constituent.parent().isType('Group')):
            raise ConstraintError, "Lexeme's parent is not a group:\n\n%s\n\nParent:\n\n%s" % (str(constituent), str(constituent.parent()))


class Finaliser(TreeOperation):
    """
    Once the tree changes are finished, a few parts of the interface
    can be optimised by storing their values instead of calculating them freshly
    
    Tell each node to build those lists
    """
    def actOn(self, node):
        node.finalise()
        
class Unfinaliser(TreeOperation):
    """
    Once the tree changes are finished, a few parts of the interface
    can be optimised by storing their values instead of calculating them freshly
    
    Tell each node to build those lists
    """
    def actOn(self, node):
        node.unfinalise()

class COMLEXAssociator(TreeOperation):
    """
    Associate the first COMLEX entry with each word
    This allows lematisation for WN sense association later
    """
    def __init__(self):
        TreeOperation.__init__(self)
        self._COMLEX = COMLEX.buildLexicon()
    
    def actOn(self, node):
        """
        Forward words for sense attachment, reject other nodes
        """
        if node.isType('Word'):
            self._addSyntax(node)
        
    def _addSyntax(self, node):
        entries = self._COMLEX.get(node.lemma(), [])
        node.metadata['COMLEX'] = []
        for entry in entries:
            if self._POSMatch(node.label, entry.label):
                node.metadata['COMLEX'].append(entry)
                
    def _POSMatch(self, tb, cl):
        """
        Check whether the Treebank POS and the COMLEX POS match eg
        NN matches with NOUN, JJ does not match with VERB
        """
        if cl == 'NOUN':
            if tb.startswith('N'):
                return True
            else:
                return False
        elif cl == 'VERB':
            if tb.startswith('V'):
                return True
            else:
                return False
        elif cl == 'PREP':
            if tb == 'IN':
                return True
            else:
                return False
        elif cl in ['ADVPART', 'ADVERB']:
            if tb.startswith('R'):
                return True
            else:
                return False
        elif cl == 'ADJECTIVE':
            if tb == 'JJ':
                return True
            else:
                return False
        else:
            return False
        

                
        
                    

class SenseAssociator(TreeOperation):
    """
    Associate the most common WordNet sense with each word
    """
    def actOn(self, node):
        """
        Forward words for sense attachment, reject other nodes
        """
        if node.isType('Word'):
            self._addSense(node)
            
    def _addSense(self, word):
        POSFile = self._wnPOSFile(word.label)
        # Many POS don't have wn senses, eg determiners
        if not POSFile:
            word.metadata['senses'] = None
        else:
            word.metadata['senses'] = POSFile.get(word.lemma(), [])
         
    def _wnPOSFile(self, POS):
        """
        Map TreeBank POS tags to WordNet POS files: N, V, ADJ, ADV
        """
        if POS.startswith('N'):
            return wordnet.N
        elif POS.startswith('V'):
            return wordnet.V
        elif POS.startswith('R'):
            return wordnet.ADV
        elif POS.startswith('J'):
            return wordnet.ADJ
        else:
            return None
            
    


class MetafunctionAdder(TreeOperation):
    """
    Add Interpersonal and Textual structures to clauses
    """
    _intpClauseAnalyser = singleton(FunctionAnalysers.InterpersonalClauseAnalyser)
    _txtClauseAnalyser = singleton(FunctionAnalysers.TextualClauseAnalyser)
    _expClauseAnalyser = singleton(FunctionAnalysers.ExperientialClauseAnalyser)
   # _posWordAnalyser   = singleton(FunctionAnalysers.PossessiveAnalyser)
    
    def __init__(self):
        pass
        
    def actOn(self, constituent):
        """
        Call the appropriate analyser for the rank
        """
        if constituent.isType('Clause_Complex'):
            self._visitClauseComplex(constituent)
        elif constituent.isType('Clause'):
            self._visitClause(constituent)
        elif constituent.isType('Group'):
            self._visitGroup(constituent)
        elif constituent.isType('Word'):
            self._visitWord(constituent)
        
    def _visitClause(self, clause):
        """
        Work performed in metafunction.py
        """
        self._addMetafunction('interpersonal', clause, '')
        self._addChildFunctions('interpersonal', clause, self._intpClauseAnalyser.analyse(clause))
        self._addMetafunction('textual', clause, '')
        self._addChildFunctions('textual', clause, self._txtClauseAnalyser.analyse(clause))
        self._addMetafunction('experiential', clause, '')
        self._addChildFunctions('experiential', clause, self._expClauseAnalyser.analyse(clause))
    
    def _visitClauseComplex(self, clauseComplex):
        """
        Adds empty metafunction
        """
        self._addMetafunction('interpersonal', clauseComplex, '')                
        
    def _visitGroup(self, group):
        """
        Adds empty metafunction
        """
        if not hasattr(group, 'interpersonal'):
            self._addMetafunction('interpersonal', group, '')
        if not hasattr(group, 'experiential'):
            self._addMetafunction('experiential', group, '')
        
    def _visitWord(self, word):
        """
        Adds empty metafunction
        """
        if not hasattr(word, 'interpersonal'):
            self._addMetafunction('interpersonal', word, '')
        if not hasattr(word, 'experiential'):
            self._addMetafunction('experiential', word, '')
       # self._addMetafunction('possession', word, '')
       # self._addChildFunctions('possession', word, self._posWordAnalyser.analyse(word))
        
    
    def _addMetafunction(self, metafunctionName, realisation, functionName):
        """
        Add a metafunction instance to a constituent
        """
        # Initialise the metafunction
        setattr(realisation, metafunctionName, Metafunctions.Metafunction())
        # Set the label
        getattr(realisation, metafunctionName).label = metafunctionName
        # Set the function
        getattr(realisation, metafunctionName).function = functionName
    
    
    def _addChildFunctions(self, metafunctionName, constituent, functions):
        """
        Add child functions to a constituent
        """
        metafunction = getattr(constituent, metafunctionName)
        for realisations, function in functions:
            metafunction.childFunctions.setdefault(function, [])
            if not type(realisations) == type([]):
                print function
            for realisation in realisations:
                metafunction.childFunctions[function].append(realisation)
                self._addMetafunction(metafunctionName, realisation, function)
        
class SystemSelector(TreeOperation):
    """    
    Annotate a clause with the set of nodes passed on a path through the
    system network
    """
    def actOn(self, constituent):
        """
        Call the appropriate analyser for the rank
        """
        setattr(constituent, 'systems', TraverseNetwork.selectFromSystems(constituent))
        

        
        
        
class Controller(TreeOperation):
    """
    Call Visitors sequentially on a parse tree
    """
    # Set which operations will be performed on parse trees
    _operations = [
        (ConstituentTyper(), 'Node'),
        (ConstituentConnector(), 'Node'),
        (PunctuationReassigner(), 'Node'),
        (RetypeConstituents(), 'Constituent'),
        (CorrectedItemMover(), 'Constituent'),
        (StrictTruncater(), 'Constituent'),
        (GappedClauseHandler(), 'Constituent'),
        (MinorClauseInserter(), 'Constituent'),
        (QuotationClauseInserter(), 'Constituent'),
        (VerbalGroupInserter(), 'Constituent'),
        # Above VerbMover for WSJ 81.2
        (MWConjunctionGrouper(), 'Constituent'),
        (VerbMover(), 'Constituent'),
        (RelativeClauseInserter(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (ConjunctionGrouper(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        # WSJ 122.7
        (ConjunctionAndWHReassigner(), 'Constituent'),
        (ETCConjunctionReassigner(), 'Constituent'),
        (ClauseNominaliser(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (QuotationChecker(), 'Node'),
        (VerbalGroupHComplexer(), 'Constituent'),
        # Trace movement below H Complexing, above ellipsis handling (wsj 543.6)
       # (TraceMover(), 'Constituent'),
        (STruncater(), 'Constituent'),
        (SBARTruncater(), 'Constituent'),
        (Truncater(), 'Constituent'),
        (AdjunctDTInserter(), 'Constituent'),
        # Shift punctuation now so that it doesn't get misnumbered (all 68.23)
        (PunctuationLowerer(), 'Constituent'),
        (FillerLowerer(), 'Constituent'),
        (EllipsisHandler(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (VGFlattener(), 'Constituent'),
        (VerbalGroupPComplexer(), 'Constituent'),
        (SmallClauseDeleter(), 'Constituent'),
        (PredicateRaiser(), 'Constituent'),
        (GroupComplexer(), 'Constituent'),
       # (ClauseRaiser(), 'Constituent'),
        # Wsj 1730.37
        (ChildSorter(), 'Constituent'),
        (VerblessADVClauseRemover(), 'Constituent'),
        (Pruner(), 'Constituent'),
        (Truncater(), 'Constituent'),
        # WSJ 490.1
        (VGFlattener(), 'Constituent'),
        # WSJ 612.19
        (ConjunctionRaiser(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (FillerLowerer(), 'Constituent'),
        (PunctuationLowerer(), 'Constituent'),
        (PunctuationRaiser(), 'Constituent'),
        # Comment out to let constraint checking work
        (DFLPruner(), 'Constituent'),
        (Finaliser(), 'Constituent'),
       # (COMLEXAssociator(), 'Constituent'),
       # (SenseAssociator(), 'Constituent'),
       # (MetafunctionAdder(), 'Constituent'),
       # (SystemSelector(), 'Constituent'),
       # (Unfinaliser(), 'Constituent'),
       # (TracePruner(), 'Constituent'),
       # (IDAdder(), 'Constituent'),
       # (Finaliser(), 'Constituent')
    ]
    """
    ,
            (FinalConstraints(), 'Constituent')
    """        

    def _makeFunctionMap(self):
        """
        Map classes to the methods that should be called on them
        """
        return {self._leaf: self._visitLeaf,
            self._internal: self._visitInternal,
            self._root: self._visitRoot,
            self._file: self._visitRoot
        }
    
    def _visitRoot(self, node):
        """
        Iterate through the specified operations, and have them performed
        on the tree
        """
        printer = singleton(Printer)
        for operation, type in self._operations:
            if type == 'Node':
                node.performOperation(operation)
            else:
                node.constituent.performOperation(operation)
           # print operation
           # print printer.actOn(node.constituent)
    
    def _visitInternal(self, node):
        """
        Only root nodes can accept operations, so if a non-root node is seen,
        signal to the node that is performing the Controller operation to stop
        looping
        """
        raise Break
        
    def _visitLeaf(self, node):
        """
        Only root nodes can accept operations, so if a non-root node is seen,
        signal to the node that is performing the Controller operation to stop
        looping
        """
        raise Break
