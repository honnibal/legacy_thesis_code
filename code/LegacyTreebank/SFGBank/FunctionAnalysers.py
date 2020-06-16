"""
Classes to calculate functional role analyses of constituents
"""
from general.Errors import *
class FunctionAnalyser:
    """
    Abstract class for the metafunctional analysis of a constituent
    """
    def __init__(self):
        raise ImplementationError
    
    def analyse(self, constituent):
        """
        Template method for the performance of some kind of analysis,
        which is built into the functions dict
        """
        raise ImplementationError, "Child classes must subclass this method"



class InterpersonalClauseAnalyser(FunctionAnalyser):
    """
    Build a list of (realisation, function) tuples for a clause's interpersonal
    analysis
    """
    def __init__(self):
        self._incrementCount()
    
    def _incrementCount(self, count = [0]):
        """
        Abstract class, so count should not be incremented
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceConstructor instantiated"
    
    def analyse(self, clause):
        """
        Determine the finite, then the subject, then the residue functions
        """
        self._functions = []
        if clause.verbalGroup():
            self._assignFinite(clause)
            self._assignPredicator(clause)
        else:
            self._finite = []
            self._functions.append(([], 'finite'))
        if self._finite:
            self._assignSubject(clause)
        else:
            self._subject = []
            
        self._assignResidueFunctions(clause)
        return self._functions
        
    def _assignFinite(self, clause):
        """
        The Finite is the first tensed verb in the verbal group
        """
        # Get the left-most verbal group simplex
        verbalGroup = clause.verbalGroup()
        while verbalGroup.isType('Complex'):
            verbalGroup = verbalGroup.group(0)
        verbPos = {'TO': True, 'VBG': True, 'VBN': True, 'VB': True}
        for word in verbalGroup.listWords():
            # Ignore punctuation
            if not word.isType('Word'):
                continue
            # Ignore negative markers
            elif word.label == 'RB':
                continue
            # If tensed, it's the finite 
            elif word.label not in verbPos:
                self._functions.append(([word], 'finite'))
                self._finite = word
                break
            # If untensed, there is no finite
            else:
                self._functions.append(([], 'finite'))
                self._finite = []
                break
        else:
            self._functions.append(([], 'finite'))
            # No words found, no finite
            self._finite = []
                    
    
    
    def _assignPredicator(self, clause):
        """
        Look for the right-most verb in the verbal group. Try to catch phrasal verbs
        """
        # Get the right-most verbal group simplex
        verbalGroup = clause.verbalGroup()
        while verbalGroup.isType('Complex'):
            verbalGroup = verbalGroup.group(-1)
        predicator = []
        words = verbalGroup.listWords()
        # Iterate through the word list backwards
        words.reverse()
        for word in words:
            # Ignore punctuation
            if not word.isType('Word'):
                continue
            # Ignore negative markers
            elif word.text.lower() in ["n't", "not"]:
                continue
            predicator.append(word)
            # Break when a relevant word is a member of the VG proper
            if word.parent() == verbalGroup:
                break
            # ie not a particle
            elif (not word.parent().isType('Particle')) and (not word.parent().isType('Dysfluency')):
                print word
                print word.parent()
                assert word.parent().isType('Particle')
        predicator.reverse()
        # Predicator must be list, not word, to allow for phrasal verbs
        self._functions.append((predicator, 'predicator'))     
    
        
    
    def _assignSubject(self, clause):
        """
        Assign subject to group, add to reverse index
        """
        # Look for groups function-labelled as subject (or failing that, WHNP's)
        subjects = self._getSubjects(clause)
        if not subjects:
            self._functions.append(([], 'subject'))
            self._subject = []
        # In clauses like "Help them move!", 'them' is a fake subject,
        # so check that either subject^finite or SQ/SBARQ
        elif (self._finite < subjects[0]) and not (clause.label in ['SQ', 'SBARQ', 'SINV']):
            self._functions.append(([], 'subject'))
            self._subject = []
        else:
            # Assign 0 so that 'I made him help me move', I gets subject, not 'him' or 'me'
            self._functions.append(([subjects[0]], 'subject'))
            self._subject = subjects[0]
                
    def _getSubjects(self, clause):
        """
        Return a list of potential subjects
        """
        subjects = [group for group in clause.children() if 'SBJ' in group.functionLabels]
        if not subjects:
            #  look for WHNP's 
            subjects = [group for group in clause.children() if (group.label in ['WHNP', 'WDT'])]
        return subjects        

    
    def _assignResidueFunctions(self, clause):
        """
        Complements = NGs that arent tagged as adverbial
        Adjuncts    = Prepositional phrases, adverbial phrases
        """
        adverbialLabels = {'TMP': True, 'DIR': True, 'LOC': True, 'MNR': True, 'TMP': True, 'PNR': True, 'ETC': True, 'ADV': True}
        # Initialise residue functions
        for group in clause.groups():
            # Ignore the subject
            if group == self._subject:
                continue
            elif group.isType('Nominal_Group'):
                if 'VOC' in group.functionLabels:
                    self._functions.append(([group], 'vocative'))
                elif [adverbialLabel for adverbialLabel in group.functionLabels if adverbialLabel in adverbialLabels]:
                    self._functions.append(([group], 'adjunct'))
                else:
                    self._functions.append(([group], 'complement'))
            elif group.isType('Interjection'):
                self._functions.append(([group], 'conjunctiveAdjunct'))
            else:
                for type in ['Adverbial_Group', 'Prepositional_Phrase', 'Particle']:
                    if group.isType(type):
                        self._functions.append(([group], 'adjunct'))
                        break
                else:
                    self._functions.append(([group], 'untyped'))
                    
                    
                    
                    
                    
                    
                    
class TextualClauseAnalyser(FunctionAnalyser):
    """
    Analyse a clause for its Theme/Rheme structure
    """
    def __init__(self):
        self._incrementCount()
    
    def _incrementCount(self, count = [0]):
        """
        Abstract class, so count should not be incremented
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceConstructor instantiated"
    
    def analyse(self, clause):
        self._functions = []
        if (not clause.interpersonal.finite) and (clause.interpersonal.predicator) and (clause.interpersonal.predicator[0].label in ['VBG', 'VBN', 'TO']):
            # Non-finite clauses have no theme
            self._assignThematicRoles(clause, True)
        else:
            self._assignThematicRoles(clause, False)
            self._checkThematicFinite(clause)
        self._functions.sort()
        return self._functions
    
    def _checkThematicFinite(self, clause):
        """
        Check whether the finite is an interpersonal theme
        """
        if not clause.interpersonal.subject:
            return None
        finite = clause.interpersonal.finite
        subject = clause.interpersonal.subject.getWord(0)
        # Only applies to clauses where the finite isn't the predicator
        if finite not in clause.interpersonal.predicator:
           secondVerb = clause.verbalGroup().listWords()[1] 
        else:
            return None
        # index 0 used to accomodate cleft or otherwise interrupted subjects
        
        # Check whether the finite is before the subject, and the predicator is after the subject
        if (finite < subject) and (secondVerb > subject):
            self._functions.append(([finite], 'interpersonalTheme'))
    
    def _assignThematicRoles(self, clause, seenTopical):
        for group in clause.groups():
            # All elements after the topical theme are rheme
            if seenTopical:
                self._functions.append(([group], 'rheme'))
                continue
            if group.isType('Conjunction_Group'):
                self._functions.append(([group], 'textualTheme'))
            elif group.interpersonal.function == 'conjunctiveAdjunct':
                self._functions.append(([group], 'textualTheme'))
            # Vocatives, comment adjuncts and mood adjuncts are intp themes
            elif group.interpersonal.function in ['vocative', 'moodAdjunct', 'commentAdjunct']:
                self._functions.append(([group], 'interpersonalTheme'))
            elif group.interpersonal.function in ['subject', 'complement', 'adjunct']:
                self._functions.append(([group], 'topicalTheme'))
                seenTopical = True
            elif group.isType('Verbal_Group'):
                self._functions.append(([group], 'topicalTheme'))
            else:
                print group
                print group.interpersonal.function
                raise StandardError, "Unknown interpersonal function"
    
    
class ExperientialClauseAnalyser(FunctionAnalyser):
    """
    Analyse a clause as a Process configuration
    """
    def __init__(self):
        self._incrementCount()
    
    def _incrementCount(self, count = [0]):
        """
        Abstract class, so count should not be incremented
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceConstructor instantiated"
    
    def analyse(self, clause):
        """
        Build a list of (realisation, function) tuples
        """
        self._functions = []
        for group in clause.groups():
            if group.interpersonal.function in ['subject', 'complement']:
                self._functions.append( ([group], 'participant') )
            # This is wrong for by-agents in passive clauses. Fixing this is
            # probably complicated. Fix FileVisiters.FrameNetFeatureExtractor if
            # this bug is fixed
            elif group.interpersonal.function == 'adjunct':
                self._functions.append( ([group], 'circumstance') )
        if clause.verbalGroup():
            self._functions.append( ([clause.verbalGroup()], 'process') )
        self._functions.sort()
        return self._functions
                
#class PossessiveAnalyser(FunctionAnalyser):
#    """
#    Hackish visiter to add Possessor/Possessed functions
#    """
#    def __init__(self):
#        self._incrementCount()
#    
#    def _incrementCount(self, count = [0]):
#        """
#        Abstract class, so count should not be incremented
#        """
#        count[0] += 1
#        if count[0] > 1:
#            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceConstructor instantiated"
#            
#    def analyse(self, word):
#        if not word.parent().isType('Nominal_Group'):
#            return []
#        self._functions = []
#        siblings = [c for c in word.parent().children() if c.isType('Word')]
#        if (word != siblings[-1]):
#            index = siblings.index(word)
#            # Genitive
#            if (siblings[index + 1].label == 'POS') and (word.parent().parent().isType('Nominal_Group')):
#                self._functions.append( (word.parent().parent().head(), 'possessed') )
#        else:
#            if word.parent().parent().isType('Prepositional_Phrase') and word.parent().parent().getWord(0).text == 'of' and word.parent().parent().parent().isType('Nominal_Group'):
#                self._functions.append( (word.parent().parent().parent().head(), 'possessed') )
#        return self._functions
     
