"""
Classes for CCG parse tokens

Originally created as parfeat
"""
import re, sys
from CCG import Category

class ParsedDoc:
    """
    Essentially just a list of sentences, but allows the calculation of document
    features
    """
    _docID = 0
    def __init__(self, parsedText, sentClass, name = None):
        """
        Take the parser analysis and construct GRSentence objects
        """
        ParsedDoc._docID += 1
        self.ID = ParsedDoc._docID
        self.sentences = []
        if name:
            self.name = name
        for sentenceData in parsedText.split('\n\n'):
            if sentenceData.startswith('#'):
                continue
            if not sentenceData.strip():
                continue
            sentenceObj = sentClass(sentenceData)
            if name:
                sentenceObj.name = name
           # if sentenceObj.tokens:
            self.sentences.append(sentenceObj)


    def tokens(self):
        for sentence in self.sentences:
            for token in sentence.tokens:
                yield token

    def __getitem__(self, i):
        return self.sentences[i]

    def __hash__(self):
        # I don't like using hashes that are plain ints, for fear of hash collision
        return ('ParsedDoc', self.ID)

    def __cmp__(self, other):
        return cmp(self.ID, other.ID)

    def tokens(self):
        for sentence in self:
            for token in sentence:
                yield token





                

class Sentence:
    """
    Deprecated sentence class for .deps style dependencies
    """
    _sentenceCount = 0
    def __init__(self, sentenceData):
        deps, tags = self._divideData(sentenceData)
        tokens = []
        for i in xrange(len(tags)):
            try:
                form, lemma, pos, chunk, neTag, stag = self._lexInfo(tags[i].split('|'))
            except:
                print tags[i]
                raise
            ID = (Sentence._sentenceCount, i)
            tokens.append(Token(ID, form, lemma, pos, neTag, stag))
        # Organise dependency arcs so that they're keyed by the offset of their head
        depsByHead = self._arrangeDeps(deps)
        for headIdx, argNums in depsByHead.items():
            head = tokens[headIdx]
            for argIdx, argNum in argNums:
                arg = tokens[argIdx]
                if argIdx > headIdx:
                    direction = 'f'
                else:
                    direction = 'b'
                key = (argNum, direction, arg.stag)
                head.deps.setdefault(key, []).append(arg)
                headKey = (argNum, direction, head.stag)
                arg.heads.setdefault(headKey, []).append(head)
        # Set left, right and offset
        last = len(tokens) - 1
        for i, token in enumerate(tokens):
            if i == 0:
                token.left = None
            else:
                token.left = tokens[i-1]
            if i == last:
                token.right = None
            else:
                token.right = tokens[i+1]
            token.offset = i
        self.tokens = tokens
        self.ID = ('Sentence', Sentence._sentenceCount)
        Sentence._sentenceCount += 1
            
    def _divideData(self, sentenceData):
        """
        Divide the parse data into dependency arcs and token tags
        """
        deps = sentenceData.strip().split('\n')
        tags = deps.pop(-1)[4:].split()
        # Hack around the problem of splitting an empty string and arriving at a populated list
        if tags == ['']:
            tags = []
        return deps, tags

    def _lexInfo(self, fields):
        """
        Figure out what lexical info is provided from:
        
        form, lemma, pos, chunk tag, NE tag, super tag
        """
        length = len(fields)
        if length == 6:
            return fields
        elif length >= 4:
            form, lemma, pos, superTag = fields
            return form, lemma, pos, None, None, superTag
        elif length == 3:
            form, pos, superTag = fields
            return form, form, pos, None, None, superTag
        else:
            print fields
            raise StandardError, "Missing one or more required fields in lexical properties"
        
    def _arrangeDeps(self, deps):
        """
        Make a dictionary of lists, keyed by the ID of the head words.
        The value is a list of (argument ID, argument num) tuples.
        """
        # deps are dependency arcs
        depsByHead = {}
        for depString in deps:
            depFields = depString.split()
            headString, headIdx = depFields[0].split('_')
            # These nums start at 1 -- we want list indices starting at 0
            headIdx = int(headIdx) - 1
            argNum = int(depFields[2])
            argString, argIdx = depFields[3].split('_')
            argIdx = int(argIdx) - 1
            depsByHead.setdefault(headIdx, []).append( (argIdx, argNum) )
        return depsByHead


        
    def __getitem__(self, index):
        return self.tokens[index]
        
    def __len__(self):
        return len(self.tokens)

    def __hash__(self):
        return self.ID

class GRSentence(Sentence):
    """
    CCG Sentence with grammatical relation style dependencies
    """
    _sentenceCount = 0
    def __init__(self, sentenceData):
        deps, tags = self._divideData(sentenceData)
        self.rawGRs = deps
        tokens = []
        for i in xrange(len(tags)):
            bits = tags[i].split('|')
            ID = (Sentence._sentenceCount, i)
           # form, lemma, pos, chunk, neTag, stag = self._lexInfo(bits)
            try:
                form, lemma, pos, chunk, neTag, stag = self._lexInfo(bits)
            except:
                print tags[i]
                raise
            token = Token(ID, form, lemma, pos, neTag, stag)
            token.sentence = self
            tokens.append(token)
        # Organise dependency arcs so that they're keyed by the offset of their head
        depsByHead, grs = self._arrangeDeps(deps)
        for headIdx, argInfo in depsByHead.items():
            head = tokens[headIdx]
            for argIdx, relation in argInfo:
                arg = tokens[argIdx]
                head.deps.setdefault(relation, []).append(arg)
                arg.heads.setdefault(relation, []).append(head)
        # Set left, right and offset
        last = len(tokens) - 1
        for i, token in enumerate(tokens):
            if i == 0:
                token.left = None
            else:
                token.left = tokens[i-1]
            if i == last:
                token.right = None
            else:
                token.right = tokens[i+1]
            token.offset = i
        self.tokens = tokens
        self.grs = grs
        self.ID = ('GRSentence', Sentence._sentenceCount)
        Sentence._sentenceCount += 1
        
    def grFeats(self, featOpts):
        for headIdx, depIdx, relation in self.grs:
            head = self.tokens[headIdx]
            dep = self.tokens[depIdx]
            features = {relation: True}
            features.update(head.features('h', featOpts))
            features.update(dep.features('d', featOpts))
            yield features
                

        
    def _arrangeDeps(self, relationStrings):
        """
        Make a dictionary of lists, keyed by the IDs of the head words.
        The value is a list of (relation, dependent) tuples

        This is kind of broken at the moment because it doesn't handle the triples
        properly
        """
        grsByHead = {}
        # detmod(form_2, A_1)
        # head index, dependent index, relation type
        relationPieces = []
        for relationString in relationStrings:
            # Strip brackets
            relationString = relationString[1:-1]
            pieces = relationString.split()
            relation = pieces.pop(0)
            try:
                pieces = [p for p in pieces if p != '_' and '_' in p]
                if len(pieces) == 3:
                    pieces.pop(0)
                if len(pieces) < 2:
                    continue
                head, dependent = pieces
            except:
                print relationString
                raise
            
           # print head
           # print dependent
            try:
                headIdx = int(head.split('_')[-1]) - 1
                depIdx  = int(dependent.split('_')[-1]) - 1
            except:
                print relationString
                raise
            assert relation
            grsByHead.setdefault(headIdx, []).append( (depIdx, relation) )
            relationPieces.append( (headIdx, depIdx, relation) )
        return grsByHead, relationPieces

    def __str__(self):
        """
        Just print the tokens for now
        """
        tokens = []
        for t in self:
            tokens.append(t.form)
        return ' '.join(tokens)

    def printParse(self):
        relations = []
        for headIdx, depIdx, relation in self.grs:
            head = self.tokens[headIdx]
            dep = self.tokens[depIdx]
            # should be lemmas, but forms as a hack for data with no lemmas
            relation = '%s(%s_%d, %s_%d)' % (relation, head.form, headIdx + 1, dep.form, depIdx + 1)
            relations.append(relation)
        return '\n'.join(relations)

    

class Token:
    """
    Tokens are containers of analysis properties. These ones come from CCG parses. Main fields are:
    form -- orthographic form
    lemma -- lemma
    pos -- part of speech
    neTag -- named entity tag
    stag -- supertag
    left -- token one to the left
    right -- token one to the right
    deps -- tokens dependent on this one
    heads -- tokens this one is dependent upon
    isPunc -- whether the token is punctuation (including conj tagged commas)
    """
    punc = {"$": True, "#": True, "``": True, "''": True, "(": True, ")": True, ".": True, ":": True, ",": True}
    # Tokens semcor arbitrarily (and incorrectly) tagged punc
    _arbitraryPuncTokens = {
        'msec.': True
    }
    def __init__(self, ID, form, lemma, pos, neTag, stag):
        self.ID = ID
        self.form = form
        self.lemma = lemma
        self.pos = pos
        self.wnPos = None
       # self.chunk = chunk
        self.neTag = neTag
        if stag == '_':
            self.stag = None
        else:
            self.stag = Category(stag)
        self.left = None
        self.right = None
        self.deps = {}
        self.heads = {}
        # Hack field for compliance with my SFG stuff
        self.sfg = None
        if self.form in Token._arbitraryPuncTokens:
            self.isPunc = True
        else:
            for char in self.form:
                if char.isalnum():
                    self.isPunc = False
                    break
            else:
                self.isPunc = True

    def related(self):
        """
        Generator of grammatically related tokens. Related tokens are returned in the form
        (direction, token, relation)
        """
        for key, tokens in self.deps.items():
            for token in tokens:
                yield ('d', token, key)
        for key, tokens in self.heads.items():
            for token in tokens:
                yield ('h', token, key)
        

class TokenFeatureMaker:
    """
    Class controlling how token features look as strings. Suitable when tokens are instances
    NOT suitable when larger spans are instances -- use DocumentFeatureReprsenter for that!

    This allows customisation of what information is included in the feature from a dependency
    arc, as well as how readably (or searchably) it is displayed as a string. Multiple strings
    may be returned so that multiple levels of generality can be represented, allowing the learner
    some "back off" from specific, sparse features. For instance, a feature type might omit lemmas.
    """
    def __init__(self, template, argumentMakers, pathDelimiter, pathLength, conjDelimiter):
        """
        A template defines the string representation, the argumentMaker fills in that representation
        with pieces from the string. The template should include spaces for the most specific features,
        and the argument makers should supply cadigans (like a Kleane star *) for details it is skipping.
        
        An argument maker must always take the arguments: token, related, relation, direction
        and return a tuple of strings with length equal to the number of slots in the template.
        
        An example template and two example arg makers ar included below        

        Finally, the delimiter controls how multiple arcs will be joined together to make single features.
        """
        self.template = template
        self.argumentMakers = argumentMakers
        self.pathDelim = pathDelimiter
        self.pathLength = pathLength
       # self.conjSize = conjSize
       # self.conjPrefixes = conjPrefixes
        self.conjDelim = conjDelimiter
            
    def __call__(self, token):
        """
        Interface method returning a dictionary of strings.
        """
        self._visited = {}
        initPaths = self.emptyPaths()
        for generalityLevel in initPaths:
            generalityLevel.append([])
        paths = self._addLink(initPaths, token, self.pathLength)
        features = {}
        shortPaths = {}
        for generalityPaths in paths:
            for path in generalityPaths:
                assert path
                # Extract smaller paths as features
                shortPaths[tuple(path[:1])] = True
                for i in xrange(1, self.pathLength + 1):
                    feature = self.pathDelim.join(path[:i])
                    features[feature] = True
        features.update(self._conjFeatures(shortPaths))
        return features
        
    def _conjFeatures(self, allFeatures):
        """
        Augment features with conjunctions of short paths of certain feature classes.
        For instance, if there are three features: (pos-VBD, lemma-hid, subj-boy)
        on a token, conj((pos, lemma), 2) will add pos-VBD_pos
        """
        conjSet = {}
        conjuncted = {}
        for f1 in allFeatures:
            for f2 in conjSet:
                if f1 != f2:
                    conjuncted['%s%s%s' % (f1, self.conjDelim, f2)] = True
        return conjuncted
            
            

    def emptyPaths(self):
        """
        Return a list of empty lists the same length as the argumentMakers
        """
        paths = []
        for argMaker in self.argumentMakers:
            paths.append([])
        return paths


    def _addLink(self, paths, token, maxLength):
        """
        Take all current paths, make a new one with each new link appended,
        and return the new paths. Do this for each generality level
        """
        newPaths = self.emptyPaths()
        for direction, related, relation in token.related():
            if not self._useLink(token, related, relation, direction, maxLength):
                continue
            relationPaths = self.emptyPaths()
            for i, generalityLevel in enumerate(paths):
                argumentMaker = self.argumentMakers[i]
                feature = self.template % argumentMaker(token, related, relation, direction)
                for path in generalityLevel:
                    pathCopy = path[:]
                    pathCopy.append(feature)
                    relationPaths[i].append(pathCopy)
            if maxLength > 1:
                relationPaths = self._addLink(relationPaths, related, maxLength - 1)
            for i, generalityLevel in enumerate(newPaths):
                generalityLevel.extend(relationPaths[i])
                
        return newPaths


    def _useLink(self, token, related, relation, direction, maxLength):
        if direction == 'h':
            key = (related, token, relation)
        else:
            key = (token, related, relation)
        # This stops us from travelling in circles
        if key in self._visited:
            return False
        self._visited[key] = True
        # Allow other constraints to be encoded without copying the visited code
        return self._otherChecks(token, related, relation, direction, maxLength)

    def _otherChecks(self, token, related, relation, direction, maxLength):
        """
        Use no other checks
        """
        return True

class TokenFeaturesForDoc(TokenFeatureMaker):
    def _otherChecks(self, token, related, relation, direction, maxLength):
        """
        Use no other checks
        """
        if maxLength == self.pathLength and relation == 'h':
            return False
        else:
            return True

class DocumentFeatureMaker:
    def __init__(self, template, argumentMakers, delimiter, pathLength):
        self._tokenFeatureMaker = TokenFeaturesForDoc(template, argumentMakers, delimiter, pathLength)
        
    def __call__(self, document):
        features = {}
        tokenFeatureMaker = self._tokenFeatureMaker
        for sentence in document:
            for token in sentence:
                tokenFeatures = tokenFeatureMaker(token)
                for feat in tokenFeatures:
                    features.setdefault(feat, 0)
                    features[feat] += 1
        return features
           
def escape(feature):
    """
    Use a set of two character escapes for common non-alnum chars, but otherwise use
    CR# where # is the ordinal value of the character
    """
    # These characters are very common in supertags, and we dont want to unnecessarily
    # blow out the size of the feature strings. So specify short escapes for these
    commonEscapes = {
        '(': 'LP',
        ')': 'RP',
        '/': 'FS',
        '\\': 'BS',
        '{': 'LB',
        '}': 'RB',
        '[': 'LS',
        ']': 'RS',
        '-': '-'
    }
    escaped = []
    for char in feature:
        if char.isalnum():
            escaped.append(char)
        elif char in commonEscapes:
                escaped.append(commonEscapes[char])
        else:
            escaped.append('CR%d' % ord(char))
    return ''.join(escaped)

def defaultScheme(token, related, relation, direction):
    """
    This is an example scheme that presents maximum information in a semi-structured way

    All schemes must have this function's argument structure, and should return a string. How that
    string is calculated is entirely up for grabs.
    """
    return  (token.pos, token.lemma, relation, direction, related.pos, related.lemma)

def specificArgMaker(token, related, relation, direction):
    """
    an example of a specific arg maker to go with exampleTemplate
    """
    return (token.pos, token.lemma, relation, direction, related.pos, related.lemma)

def vagueArgMaker(token, related, relation, direction):
    """
    An example of an inspecific arg maker
    """
    return (token.pos, '*', relation, direction, related.pos, '*')

def conciseArgMaker(token, related, relation, direction):
    return (token.lemma, related.lemma)

def conciseArgMaker2(token, related, relation, direction):
    return ('*', related.lemma)
    
def verbToBeFeature(token, related, relation, direction):
    """
    Features for whether a verb-to-be is attached
    """
    if related.pos.startswith('V'):
        relatedPos = related.pos
        if related.lemma == 'be':
            relatedVtb = 't'
        else:
            relatedVtb = 'f'
    else:
        relatedPos = 'NA'
        relatedVtb = 'NA'
        relation = 'NA'
        direction = 'NA'
    return ('vtb', direction, relation, '*', token.pos, relatedPos, relatedVtb)
    
    
def negativeFeatures(token, related, relation, direction):
    """
    Features for whether a negative marker is attached
    """
    if related.form in ["n't", 'not']:
        return (related.form.replace("'", ''), direction, '*', '*', '*', '*', '*')
    else:
        return ('pos', direction, '*', '*', '*', '*', '*')

def lemmalessGRFeatures(token, related, relation, direction):
    """
    GR features with lemma abstraction
    """
    return ('llgr', direction, relation, '*', '*', related.pos, '*')
    
def stagFeatures(token, related, relation, direction):
    return ('stag', '*', '*', escape(token.stag), '*', '*', '*')
    
def lemmaFeatures(token, related, relation, direction):
    return ('lem', direction, relation, '*', '*', escape(token.lemma), '*')

# The template here is feature name, direction, relation, specific token field, vaguer token field, specific related field, vaguer related field
sfgTemplate = '%s-%s_%s--%s_%s--%s_%s'
verboseTemplate = "start_pos: %s\nstart_lemma: %s\nrelation: %s\ndirection %s\nrelated_pos: %s\nrelated_lemma: %s\n"
conciseTemplate = "%s-%s"

if __name__ == '__main__':
    path = '/home/mhonn/Data/wsj00.stagged.ready.gold'
    doc = ParsedDoc(open(path).read(), GRSentence)
    for t in doc[0]:
        print t.form
    sys.exit(1)
#    path = 'C:/workspace/Data/wsjGR/wsj_0003.mrg.grs'
    # Test sfg features
    if 1:
        document = ParsedDoc(open(path).read())
        argMakers = [defaultScheme]
#        argMakers = [verbToBeFeature, negativeFeatures, lemmalessGRFeatures, stagFeatures]
        featureMaker = TokenFeatureMaker(verboseTemplate, argMakers, '__', 1, '')
        token = document[0][8]
        features = featureMaker(token)
        for f in features:
            print f
        sys.exit(1)
    else:
        document = ParsedDoc(open(path).read())
        argMakers = [verbToBeFeature, negativeFeatures, lemmalessGRFeatures, stagFeatures]
        argMakers.append(specificArgMaker)
        argMakers.append(vagueArgMaker)
        argMakers.append(conciseArgMaker)
        argMakers.append(conciseArgMaker2)
        template = conciseTemplate
        featureMaker = DocumentFeatureMaker(conciseTemplate, argMakers, '_', 5)
        features = featureMaker(document)
    sortable = [(n, f) for f, n in features.items()]
    sortable.sort()
    sortable.reverse()
    for i in xrange(len(sortable)):
        print "%s: %d" % (sortable[i][1], sortable[i][0])
        print '---------------------------------------------'
    print '===%s features found===\n' % len(features)

