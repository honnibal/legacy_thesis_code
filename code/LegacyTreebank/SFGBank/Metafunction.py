"""
Configure Interpersonal and Textual analyses of a clause
"""

class Metafunction:
    """
    Interface
    """
    def __init__(self, clause):
        self.clause = clause
        self.parent = clause.parent()
        self.functionsDict = {}
        
        
    def assignFunction(self, functionName, realisation, append = 0):
        """
        Assign the realisation to __dict__
        Add the realisation to functions dict
        """
        if append:
            self.__dict__.setdefault(functionName, []).append(realisation)
        else:
            getattr(self.__dict__[functionName] = realisation
            
            
            
        
        
    def printSystems(self):
        printString = ''
        for systemName in self.clause.systems['namesList']:
            if self.clause.systems[systemName]:
                printString += systemName + ': ' + str(self.clause.systems[systemName]) + '\n'
        return printString
            
                        
        
        
            
        

class Interpersonal(Metafunction):
    """
    Labels and realisation index for Interpersonal metafunction
    """
    def __init__(self, clause):
        """
        Discern properties of self and assign function labels to groups
        """
        Metafunction.__init__(self, clause)
        self.vocatives = []
        self.moodAdjunct = []
        self.commentAdjunct = []
        self.conjunctiveAdjunct = []
        self.adjunct = []
        self.complement = []
        self.modality = {}
        self.assignFinite()
        self.assignSubject()
        self.assignResidueFunctions()
        self.subtypeAdjuncts()
    
    
    
    def printString(self):
        print 'Subject: %s' % self.subject
        printString = ''
       # printString += self.printSystems()
        return printString + '\n'
    
    
    
    def getXMLLines(self):
        xmlLines = ['<Interpersonal>']
        for systemName in self.clause.systems['namesList']:
            if self.clause.systems[systemName]:
                xmlLines.append('<System name="' + systemName + '" value="' + self.clause.systems[systemName] + '"/>')
        xmlLines.append('</Interpersonal>')
        return xmlLines
        
        
        
   
            
            
            
    def assignFinite(self):
        """
        If declarative or interrogative, first word of verbal group
        Otherwise None
        """
        if not self.clause.verbalGroup():
            self.finite = None
            return None
        relevantLexis = [word for word in self.clause.verbalGroup().listWords() if word.label != 'RB']
        if not relevantLexis:
            self.finite = None
        elif relevantLexis[0].label not in ['TO', 'VBG', 'VBN']:
            self.assignFunction('finite', relevantLexis[0])
        else:
            self.finite = None
    
   
            
    
    
        
    
    def assignSubject(self):
        """
        Assign subject to group, add to reverse index
        """
        if not self.finite:
            self.subject = None
            return None
        # Look for groups function-labelled as subject
        subjects = self._getSubjects(self.clause)
        # In clauses like "Help them move!", 'them' is a fake subject, so check that either subject^finite or SQ/SBARQ
        if (subjects) and ((self.finite.wordID > subjects[0].getWordID(0)) or (self.clause.label in ['SQ', 'SBARQ', 'SINV'])):
            # Assign 0 so that 'I made him help me move', I gets subject, not 'him' or 'me'
            self.assignFunction('subject', subjects[0])
        else:
            self.subject = None
                
    def _getSubjects(self, clause):
        """
        Return a list of potential subjects
        """
        subjects = [group for group in clause.children() if 'SBJ' in group.functionLabels]
        if not subjects:
            #  look for WHNP's 
            subjects = [group for group in clause.children() if (group.label == 'WHNP')]
            # that were never children of a verbal group
           # (not [verbalGroup for verbalGroup in group.previousParents if verbalGroup.type == 'Verbal Group'])]
        return subjects        
            
    
    def assignResidueFunctions(self):
        """
        Predicator  = last word of VG
        Complements = NGs that arent tagged as adverbial
        Adjuncts    = Prepositional phrases, adverbial phrases
        """
        if self.clause.verbalGroup():
            self.assignFunction('predicator', self.clause.verbalGroup())
        else:
            self.predicator = None
        constituents = [g for g in self.clause.children() if g.isType('Group')]
        for group in constituents:
            if group == self.subject: continue
            if group.isType('Nominal_Group'):
                if 'VOC' in group.functionLabels:
                    self.assignFunction('vocative', group, 'Append')
                elif [adverbialLabel for adverbialLabel in group.functionLabels if adverbialLabel in ['TMP', 'DIR', 'LOC', 'MNR', 'TMP', 'PNR']]:
                    self.assignFunction('adjunct', group, 'Append')
                else:
                    self.assignFunction('complement', group, 'Append')
            else:
                for type in ['Adverbial_Group', 'Prepositional_Phrase', 'Particle']:
                    if group.isType(type):
                        self.assignFunction('adjunct', group, 'Append')
                        break
                
                
                
                
                
                
    def subtypeAdjuncts(self):
        return None
        adjunctDict = buildAdjunctDict()
        i = 0
        for adjunct in [adjunct for adjunct in self.adjunct]:
            adjunctText = ' '.join([word.text for word in adjunct.listWords()]).lower()
            if adjunctDict.get(adjunctText) == 'MoodAdjunct':
                self.functionsDict.pop(self.adjunct[i])
                self.assignFunction('moodAdjunct', self.adjunct.pop(i), 'Append')
                moodAdjuncts.append(adjunctText)
            if adjunctDict.get(adjunctText) == 'CommentAdjunct':
                self.functionsDict.pop(self.adjunct[i])
                self.assignFunction('commentAdjunct', self.adjunct.pop(i), 'Append')
                commentAdjuncts.append(adjunctText)
            if adjunctDict.get(adjunctText) == 'ConjunctiveAdjunct':
                self.functionsDict.pop(self.adjunct[i])
                self.assignFunction('conjunctiveAdjunct', self.adjunct.pop(i), 'Append')
                conjunctiveAdjuncts.append(adjunctText)
            i += 1
                
                
                

                
                


class Textual(Metafunction):
    """
    Labels and realisation index for textual metafunctional roles
    Uses Interpersonal tags
    """
    def __init__(self, clause):            
        """
        Discern properties of self and assign function labels to groups
        """
        Metafunction.__init__(self, clause)
        self.textualTheme = []
        self.interpersonalTheme = []
        self.topicalTheme = []
        self.rheme = []
        self.intpFunctionTopTheme = None
        self.checkThematicFinite()
        self.assignThematicRoles()
    
    
    
    def getXMLLines(self):
        xmlLines = ['<Textual>']
        # Get systems
        for systemName in []:
            systemValue = self.__dict__[systemName]
            # Make lists into pretty strings
            if type(systemValue) == type([]):
                systemValue = ', '.join(systemValue)
            xmlLines.append(self.makeSystemXML(systemName.lower(), str(systemValue).lower().split(': ')))
        theme = []
        rheme = []
        if theme:
            xmlLines.append('<System name="thematic structure" value="theme">')
            for system in theme:
                xmlLines.append('<System name="theme" value="' + system[0] + '" realisation="a' + str(system[1]) + '"/>')
            xmlLines.append('</System>')
        if rheme:
            xmlLines.append('<System name="thematic structure" value="rheme">')
            for system in rheme:
                xmlLines.append('<System name="rheme" value="' + system[0] + '" realisation="a' + str(system[1]) + '"/>')
            xmlLines.append('</System>')
        xmlLines.append('</Textual>')
        return xmlLines
    
    
    def checkThematicFinite(self):
        """
        Check whether the finite is an interpersonal theme
        """
        # Only applies to clauses with a finite
        if not self.clause.interpersonal.subject:
            return None
        if len(self.clause.verbalGroup().listWords()) > 1:
            predicatorID = self.clause.verbalGroup().getWordID(1)
        else:
            return None
        # Check whether the finite is before the subject, 
        # And the predicator is after the subject. index 0 used for cleft or otherwise interrupted subjects
        if (self.clause.interpersonal.finite < self.clause.interpersonal.subject) and \
        (predicatorID > self.clause.interpersonal.subject.getWordID(0)):
            self.assignFunction('interpersonalTheme', self.clause.interpersonal.finite, 'Append')
    
        
        
    def assignThematicRoles(self):
        seenTopical = 0
        for group in self.clause.children():
            if group.isType('Lexeme'): continue
            # All elements after the topical theme are rheme
            if seenTopical:
                self.assignFunction('rheme', group, 'Append')
                continue
            if group.isType('Conjunction_Group'):
                self.assignFunction('textualTheme', group, 'Append')
            elif group in getattr(self.clause.interpersonal, 'conjunctiveAdjunct', []):
                self.assignFunction('textualTheme', group, 'Append')
            # Vocatives, comment adjuncts and mood adjuncts are intp themes
            elif [role for role in ['vocative', 'moodAdjunct', 'commentAdjunct'] if group in getattr(self.clause.interpersonal, role, [])]:
                self.assignFunction('interpersonalTheme', group, 'Append')
            else:
                self.assignFunction('topicalTheme', group)
                seenTopical = 1
            
                    
                    
    def printString(self):
        printString = ''
        printString += self.printSystems(['voice'])
        functionRoles = ['textualTheme', 'interpersonalTheme', 'topicalTheme']
        for functionRole in functionRoles:
            if hasattr(self, functionRole):
                if getattr(self, functionRole) == type([]):
                    printable = str([group.printString() for group in getattr(self, group)])
                else:
                    printable = str(getattr(self, group).printString())
            else:
                printable = 'None'
            printString += functionRole + ': ' + printable + ' | '
        return printString + '\n\n'
        
        
        
                
                
def assignMetafunctions(clause):
    setattr(clause, 'interpersonal', Interpersonal(clause))
    setattr(clause, 'textual', Textual(clause))
    print clause.interpersonal.printString()
   # setattr(clause, 'systems', grammarReader.selectFromSystems(clause))
    
    
       
def outputAdjunctSubtyping():
    return None
    print '\n\n\n\nMood Adjuncts:\n\n\n\n' + '\n'.join(moodAdjuncts)
    print '\n\n\n\nComment Adjuncts:\n\n\n\n' + '\n'.join(commentAdjuncts)
    print '\n\n\n\nConjunctive Adjuncts:\n\n\n\n' + '\n'.join(conjunctiveAdjuncts)
    print '\n\n\n\nNormal Adjuncts\n\n\n\n' + '\n'.join(normalAdjuncts)

def makeCapital(targetString):
    """
    Change the first letter of a string to a capital
    """
    firstLetter = targetString[0]
    return firstLetter.upper() + targetString[1:]
    
def buildAdjunctDict():
    """
    Parse the adjuncts.txt file into a dictionary
    """
    adjuncts = open('../data/adjuncts.txt').read().split('\n')
    adjunctsDict = {}
    for adjunct in adjuncts:
        orthString, type = adjunct.split('\t')
        adjunctsDict[orthString] = type
    return adjunctsDict

moodAdjuncts = []
commentAdjuncts = []
conjunctiveAdjuncts = []
normalAdjuncts = []
verbToBe = ['be', 'been', 'being', 'is', 'are', 'was', 'were']
import xml, grammarReader
# adjunctNetwork = xml.dom.minidom.parse('../data/adjuncts.xml')