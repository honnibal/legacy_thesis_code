"""
Visit each node on a tree and perform some operation on it
"""
from general.Errors import *
from Treebank import Nodes
import Constituency, ConstituentConstructors
import copy
import bisect
from general.Singleton import singleton
#import Metafunctions
#import FunctionAnalysers
#import TraverseNetwork
#from SFG_XML import XMLNode
#import COMLEX
from NodeVisitors import *

class NegMover(TreeOperation):
    """
    Move negative particles to their own adverb node
    """
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    
    def actOn(self, word):
        if word.isType('Word') and word.text in ['not', "n't"]:
            self._rearrangeTree(word)

    def _rearrangeTree(self, word):
        clause = word.clause()
        adverb = self._constituentConstructor.make(Constituency.AdverbialGroup, {'type': 'Adverbial_Group'})
        word.reattach(adverb)
        clause.attachChild(adverb)

class AuxRaiser(TreeOperation):
    """
    Make the auxiliary an independent constituent from the rest of
    the predicator.
    """
    _targetTypes = ['Verbal_Group']
    _verbTags = ['GW', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'BES', 'HVS', 'MD']
    _finites = {'be': True, 'been': True, 'being': True, 'is': True, 'are': True, 'was': True, 'were': True, 'has': True, 'had': True, 'have': True, 'having': True, 'do': True, 'does': True, 'doing': True, 'did': True, 'will': True, 'would': True, 'shall': True, 'should': True, 'may': True, 'might': True, 'can': True, 'could': True, 'must': True, "'s": True, "'re": True, "'m": True, "'ll": True, "'d": True, 'ca': True, 'wo': True}
    _constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)

    def actOn(self, vg):
        """
        Find verbal groups with more than one word whose first
        word is a finite
        """
        if not vg.isType('Verbal_Group'):
            return False
        if not vg.parent().isType('Clause'):
            return False
        words = [w for w in vg.children() if w.isType('Word')]
        if not len(words) > 1:
            return False
        aux = vg.getWord(0)
        if aux.text in AuxRaiser._finites:
            self._rearrangeTree(aux, vg)

    def _rearrangeTree(self, aux, vg):
        """
        Make an aux node, move the auxiliary to it, and attach it to the clause
        """
        auxNode = self._constituentConstructor.make(Constituency.OtherGroup, {'type': 'Auxiliary'})
        auxNode.abbr = 'Aux'
        aux.reattach(auxNode)
        vg.parent().attachChild(auxNode)
        

class MorleyVGFlattener(VGFlattener):
    """
    Just like the NodeVisitors one, except handle (VP stopped (VP using))
    type cases differently -- insert a clause, instead of making them a
    hypotactic VG complex
    """
    def _handleComplex(self, parent, vg):
        settings = {'type': 'Clause', 'functionLabels': {'SBAR': True}, 'label': 'S'}
        clause = self._constituentConstructor.make(Constituency.Clause, settings)
        vg.insert(clause)

    def _checkConstraints(self, constituent):
        """
        Check whether the node has two or more verb phrase children
        """
        childVPs = [vp for vp in constituent.children() if vp.label == 'VP' and vp.hasWord()]
        if len(childVPs) > 1:
            return True
        else:
            return False


class MorleyEllipsisHandler(EllipsisHandler):

    def _rearrangeTree(self, constituent):
        """
        Identify original VP, sharing VPs, shared items and parent clause
        Create one new clause for each sharing VP.

        Unlike Halliday version, do not copy or trace the shared elements
        Attach the new clauses to the parent clause
        """
        # Find elements
        sharingVPs = [vp for vp in constituent.children() if vp.label == 'VP']
        sharingVPs.sort()
        originalVP = sharingVPs.pop(0)
        origClause = constituent.clause()
        if not origClause.parent().isType('Clause_Complex'):
            clauseComplex = self._constituentConstructor.make(Constituency.ComplexConstituent, {'type': 'Clause'})
            origClause.insert(clauseComplex)
        else:
            clauseComplex = origClause.parent()
        for vp in sharingVPs:
            clause = self._constituentConstructor.make(Constituency.Clause, {'type': 'Clause', 'label': 'S', 'functionLabels': [], 'metadata': {}})
            vp.reattach(clause)
            clauseComplex.attachChild(clause)
        
    
        
class Controller(TreeOperation):
    """
    Call Visitors sequentially on a parse tree
    """
    _operations = [
        (ConstituentTyper(), 'Node'),
        (ConstituentConnector(), 'Node'),
        (PunctuationReassigner(), 'Node'),
        (RetypeConsistuents(), 'Constituent'),
        (CorrectedItemMover(), 'Constituent'),
        (StrictTruncater(), 'Constituent'),
       # (GappedClauseHandler(), 'Constituent'),
        (MinorClauseInserter(), 'Constituent'),
        (QuotationClauseInserter(), 'Constituent'),
       # (VerbalGroupInserter(), 'Constituent'),
        # Above VerbMover for WSJ 81.2
        (MWConjunctionGrouper(), 'Constituent'),
       # (VerbMover(), 'Constituent'),
        (RelativeClauseInserter(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (ConjunctionGrouper(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (STruncater(), 'Constituent'),
        (SBARTruncater(), 'Constituent'),
        (Truncater(), 'Constituent'),
        # Needs to be followed by conjunction reassigner
        (MorleyEllipsisHandler(), 'Constituent'),
        # WSJ 122.7
        (ConjunctionAndWHReassigner(), 'Constituent'),
        (ETCConjunctionReassigner(), 'Constituent'),
       # (ClauseNominaliser(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (QuotationChecker(), 'Node'),
       # (VerbalGroupHComplexer(), 'Constituent'),
        # Trace movement below H Complexing, above ellipsis handling (wsj 543.6)
       # (TraceMover(), 'Constituent'),
        (AdjunctDTInserter(), 'Constituent'),
        # Shift punctuation now so that it doesn't get misnumbered (all 68.23)
        (PunctuationLowerer(), 'Constituent'),
        (FillerLowerer(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
       # 
       # (VerbalGroupPComplexer(), 'Constituent'),
        (SmallClauseDeleter(), 'Constituent'),
        (NegMover(), 'Constituent'),
        (Truncater(), 'Constituent'),
        (MorleyVGFlattener(), 'Constituent'),
        (AuxRaiser(), 'Constituent'),
        (PredicateRaiser(), 'Constituent'),
        (GroupComplexer(), 'Constituent'),
       # (ClauseRaiser(), 'Constituent'),
        # Wsj 1730.37
        (ChildSorter(), 'Constituent'),
        (VerblessADVClauseRemover(), 'Constituent'),
        (Pruner(), 'Constituent'),
        (Truncater(), 'Constituent'),
        # WSJ 490.1
       # (VGFlattener(), 'Constituent'),
        # WSJ 612.19
        (ConjunctionRaiser(), 'Constituent'),
        (ChildSorter(), 'Constituent'),
        (FillerLowerer(), 'Constituent'),
        (PunctuationLowerer(), 'Constituent'),
        (PunctuationRaiser(), 'Constituent')
        # Comment out to let constraint checking work
       # (DFLPruner(), 'Constituent'),
       # (Finaliser(), 'Constituent'),
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
            if node.constituent:
                before = printer.actOn(node.constituent)
            else:
                before = 'None'
            if type == 'Node':
                node.performOperation(operation)
            else:
                node.constituent.performOperation(operation)
            after = printer.actOn(node.constituent)
           # print operation
           # if before != after:
           #     print after
                
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
