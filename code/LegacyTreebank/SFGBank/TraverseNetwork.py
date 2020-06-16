"""
Process the grammar file
"""
import xml.dom.minidom, SelectionFunctions
import copy
import os.path
class System:
    """
    if entryCondition -> (term 1 v term 2 v...term n)
    """
    def __init__(self, xmlSystemNode):
        """
        Call XMLParse
        """
        self.parseXML(xmlSystemNode)
        # Fetch the rules function for the system
        SelectionFunctions.clauseClass
        self.calculationFunction = getattr(SelectionFunctions, toStudlyCaps(self.name))
    
    
    def parseXML(self, xmlSystemNode):
        """
        Assign entry conditions and terms
        """
        self.name = str(xmlSystemNode.getAttribute('name'))
        entryCondition = str(xmlSystemNode.getAttribute('entrycondition'))
        # Check whether disjunctive
        if '|' in entryCondition:
            self.disjunctive = bool(1)
            # Save conditions as list
            self.entryCondition = entryCondition.split(' | ')
        else:
            self.disjunctive = bool(0)
            self.entryCondition = entryCondition.split(', ')
        self.terms = {}
        for term in xmlSystemNode.getElementsByTagName('Selection'):
            # Store terms as dict key: name, value: id
            self.terms[term.getAttribute('name')] = term.getAttribute('id')
        self.oTerms = self.terms.keys()
        self.oTerms.sort()
            
    
    def checkEntryCondition(self, selectedTerms):
        """
        Can handle entry conditions like:
            Clause (token type)
            status.free & voice.active (conjunctive)
            status.free or voice.active (disjunctive)
            status.free (normal)
        Cannot handle entry conditions like:
            Clause, status.free
            (status.free, polarity.negative) or voice.active
        """
        # Handle token type entry conditions
        # Broken. Must fix for non-clause systems
        # if self.entryCondition[0] in ['Clause', 'Group/Phrase', 'Lexeme']:
        #     return tokenChecker(entryCondition)
        # Handle disjunctive entry conditions
        if self.disjunctive:
            for entryCondition in self.entryCondition:
                if entryCondition in selectedTerms:
                    return 1
            else:
                return 0
        # Handle normal/conjunctive entry conditions
        else:
            for entryCondition in self.entryCondition:
                if entryCondition not in selectedTerms:
                    return 0
            return 1
                
                
                    
    def selectFrom(self, token, selectedTerms):
        if self.checkEntryCondition(selectedTerms):
            selection = self.calculationFunction(token)
            return self.name.replace(' ', '_') + '.' + selection
        else:
            return None


def toStudlyCaps(nameString):
    words = nameString.split(' ')
    return words[0] + ''.join([word.capitalize() for word in words[1:]])

    

def parseGrammarFile(tokenType):
    """
    Initialise globals
    """
    global GRAMMAR_PATH
    grammarDOM = xml.dom.minidom.parse(os.path.join(GRAMMAR_PATH, '%s_systems.xml' % tokenType))
    systemDOMs = grammarDOM.getElementsByTagName('System')
    systemObjects = []
    terms = []
    namesList = []
    for systemDOM in systemDOMs:
        systemObjects.append(System(systemDOM))
        terms = terms + systemObjects[-1].terms.keys()
        namesList.append(systemObjects[-1].name)
    systemsIndex = indexSystems(systemObjects)
    return systemsIndex, namesList
    
def indexSystems(systems):
    """
    Build dictionary - condition: system set
    """
    systemsIndex = {}
    for system in systems:
        for term in system.terms.values():
            systemsIndex.setdefault(term, [])
        for entryCondition in system.entryCondition:
            systemsIndex.setdefault(entryCondition, []).append(system)
    return systemsIndex
    


def selectFromSystems(token):
    """
    Add systemic information to a token from a given metafunction
    """
    systemsIndex, namesList = getSystemsNames(token)
    selectionsDictionary = {}
    for name in namesList:
        selectionsDictionary[name] = None
    selectionsDictionary['namesList'] = namesList
    tokenTypes = _initialiseStack(token)
    selectedTerms = [t for t in tokenTypes]
    entryConditionsStack = [t for t in tokenTypes]
    while entryConditionsStack:
        entryCondition = entryConditionsStack.pop(0)
        if not systemsIndex.has_key(entryCondition):
            raise StandardError, 'Entry condition not found: %s' % entryCondition
        for system in systemsIndex.get(entryCondition, []):
            selection = system.selectFrom(token, selectedTerms)
            if selection:
                selectedTerms.append(selection)
                entryConditionsStack.insert(0, selection)
                nameAndValue = selection.replace('_', ' ').split('.')
                selectionsDictionary[nameAndValue[0]] = nameAndValue[1]
    return selectionsDictionary
    
def enumeratePaths(tokenType):
    """
    List the possible ways to traverse a system network
    """
    systemsIndex, namesList = parseGrammarFile(tokenType)
    # Features, seen systems
    paths = [([tokenType.upper()], {})]
    for selectedTerms, seenSystems in paths:
        entryConditionStack = [t for t in selectedTerms]
        while entryConditionStack:
            entryCondition = entryConditionStack.pop(0)
            for system in systemsIndex.get(entryCondition, []):
                if seenSystems.has_key(system.name):
                    continue
                else:
                    seenSystems[system.name] = 1
                if system.checkEntryCondition(selectedTerms):
                    terms = system.terms.values()
                    for selection in terms[1:]:
                        newPath = [ec for ec in selectedTerms]
                        newPath.append(selection)
                        paths.append( (newPath, copy.copy(seenSystems)) )
                    selectedTerms.append(terms[0])
                    entryConditionStack.append(terms[0])
    return [p[0] for p in paths]
    
def pathsFollowed(tokenType):
    """
    Count the number of corpus instances at each feature combination.
    Do not follow branches once a combination has reached 0 instances
    """
    counts = []
    systemsIndex, namesList = parseGrammarFile(tokenType)
    # Features, seen systems 
    paths = [( [tokenType.upper()], {} )]
    # Iterate through paths (more will be added)
    for selectedTerms, seenSystems in paths:
        entryConditionStack = [t for t in selectedTerms]
        while entryConditionStack:
            entryCondition = entryConditionStack.pop(0)
            # Iterate through systems that this feature is an entry condition for
            for system in systemsIndex.get(entryCondition, []):
                # Check that the system hasnt been entered before on this path
                if not seenSystems.has_key(system.name):
                    seenSystems[system.name] = 1
                    # Check entry condition is met
                    if not system.checkEntryCondition(selectedTerms): continue
                    terms = system.terms.values()
                    for selection in terms[1:]:
                        newPath = [ec for ec in selectedTerms]
                        newPath.append(selection)
                        count = countInstances(newPath)
                        counts.append( (newPath, selectedTerms) )
                        if count:
                            paths.append( (newPath, copy.copy(seenSystems)) )
                    selectedTerms.append(terms[0])
                    print ', '.join(selectedTerms[1:])
                    count = countInstances(selectedTerms)
                    print count
                    if count:
                        entryConditionStack.append(terms[0])
                    counts.append( (selectedTerms, count) )
    return counts
    
def countInstances(selectedTerms):
    global cursor
    constraint = []
    for feature in selectedTerms:
        if feature == 'CLAUSE': continue
        name, value = feature.split('.')
        value = value.replace('_', ' ')
        constraint.append("%s='%s'" % (name, value))
    query = str('SELECT COUNT(*)\nFROM RankingClauses\nWHERE\n%s' % (' AND '.join(constraint)))
    cursor.execute(query)
    return cursor.fetchall()[0][0]
    
def getSystemsNames(token, cache = [{}]):
    if token.isType('Clause'):
        return cache[0].setdefault('Clause', parseGrammarFile('clause'))
    elif token.isType('Word'):
        return cache[0].setdefault('Word', parseGrammarFile('word'))
    else:
        return ({}, [])
    
def _initialiseStack(token):
    """
    Get the token's type for the stack
    """
    entryConditions = []
    if token.isType('Clause'):
        entryConditions.append('CLAUSE')
   # if token.isType('Word'):
   #     entryConditions.append('WORD')
   # if token.isType('Group'):
   #     entryConditions.append('GROUP')
   # if token.isType('COMPLEX'):
   #     entryConditions.append('COMPLEX')
    return entryConditions
    

GRAMMAR_PATH = ''
# Get the total number of possible paths from a grammar
if __name__ == '__main__':
    import cPickle
    dbc = mx.ODBC.Windows.DriverConnect("FILEDSN=c:\\Program Files\\Common Files\\ODBC\\Data Sources\\ClauseBank.dsn")
    cursor = dbc.cursor()
    paths = pathsFollowed('clause')
   # for path in paths:
   #    print path
    """
    seenPaths = {}
    for path in paths:
        path.sort()
        string = ''.join(path)
        if seenPaths.has_key(string):
            raise StandardError, string
        else:
            seenPaths[string] = 1
    """
    cPickle.dump(paths, open('./scraps/counts.dat', 'w'))
    
