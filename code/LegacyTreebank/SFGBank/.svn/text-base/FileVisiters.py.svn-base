"""
Operations between sentences.
"""
from Treebank import Nodes
import Converters
from general.Errors import *
#import Semcor
import cPickle
#import FrameNet
import os

class FileVisiter(Converters.TreeOperation):
    """
    Abstract
    """
    _leaf     = Nodes.RootNode
    _file     = Nodes.CorpusFile
    _corpus   = Nodes.Corpus
    listType  = 'depthList'
    moreChanges = False
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
    
    def actOn(self, node):
        if self._functionMap.has_key(node.__class__):
            self._functionMap[node.__class__](node)
        else:
            pass
    
    def _makeFunctionMap(self):
        """
        Map classes to the methods that should be called on them
        """
        return {self._leaf: self._visitSentence,
            self._file: self._visitFile,
            self._corpus: self._visitCorpus
        }
    
    def _visitCorpus(self, corpus):
        """
        Must be overridden in subclasses
        """
        raise ImplementationError, "Subclasses must override this function"  
      
    def _visitFile(self):
        """
        Must be overridden in subclasses
        """
        raise ImplementationError, "Subclasses must override this function"  

    def _visitSentence(self, node):
        """
        Must be overridden in subclasses
        """
        raise ImplementationError, "Subclasses must override this function"
        
    def wordGenerator(self, file):
        """
        Generator function for iterating through the words in a file
        """
        for sentence in file.children():
            for word in sentence.listWords():
                yield word



class SpeakerCodeMover(FileVisiter):
    """
    Move the speaker code metadata to the next Sentence in
    SWBD files and remove @ junk in ATIS file.
    """
    def actOn(self, node):
        self._functionMap[node.__class__](node)
    
    def newStructure(self):
        """
        Reset counter
        """
        self._counter = 0
    
    def _visitFile(self, file):
        """
        Iterate through sentences, checking whether each is a Speaker Code.
        If it is, add the metadata to the next sentence and continue
        """
        sentences = file.listNodes()
        for i in xrange(len(sentences[:-1])):
            code = sentences[i]
            if code.label != 'CODE':
                if code.label == '@':
                    file.detachChild(code)
                continue
            speaker, turn = self._getData(code)
            sentence = sentences[i+1]
            sentence.metadata['Speaker'] = speaker
            sentence.metadata['Turn'] = turn
            file.detachChild(code)
            
    def _getData(self, code):
        """
        Extract the speaker and turn number from the CODE line
        """
        sym = code.child(0).child(0)
        assert sym.label == 'SYM'
        assert sym.text.startswith('Speaker')
        speaker = sym.text[7]
        turn = int(sym.text[8:])
        return speaker, turn
            
    def _visitSentence(self, node):
        """
        Break
        """
        raise Break




        
class ClauseVectorBuilder(FileVisiter):
    """
    Iterate through sentences and then clauses, building a tuple to be committed
    to the database
    """
    sentenceCount = 0
    
    def vectors(self):
        """
        Return the vectors that have been built
        """
        return self._tuples
        
    def newStructure(self):
        self._tuples = []
        self._columnNames = []
    
    def columnNames(self):
        return self._columnNames
     
    
    def _visitFile(self, file):
        self._filename = file.filename
        
    def _visitSentence(self, sentence):
        """
        Iterate through clauses and build a tuple that consists of the words, the sentence
        ID and each system value
        """
        self._sentenceID = sentence.globalID
        self._clauseID = 0
        for clause in sentence.constituent.rankingClauses():
            try:
                self._tuples.append(self._systemsVector(clause))
            except:
                print clause
                print sentence
                print sentence.globalID
                self._tuples.append(self._systemsVector(clause))
            self._clauseID += 1
            if not self._columnNames:
                self._columnNames = ['CBKey', 'Sentence', 'Section', 'Verified', 'TextString'] + [sn.replace(' ', '_') for sn in clause.systems['namesList']]
        self.sentenceCount += 1
           
    def _systemsVector(self, clause):
        """
        Just a tuple of system values, prepended by the PrimaryKey and String entries
        """
        vector = [self._buildKey(), self._sentenceID, self._sentenceID[:2], 'False', ' '.join([l.text for l in clause.listLexis()]).replace("'", '_SQT_')]
        for systemName in clause.systems['namesList']:
            vector.append(str(clause.systems[systemName]))
        return vector
        
    def _buildKey(self):
        return '%s~%s' % (self._sentenceID, str(self._clauseID))
        
class WordVectorBuilder(ClauseVectorBuilder):
    """
    Iterate through words, building a tuple to be commited to the database
    """
        
    def _visitSentence(self, sentence):
        """
        Iterate through clauses and build a tuple that consists of the words, the sentence
        ID and each system value
        """
        self._sentenceID = sentence.ID
        self._wordID = 0
        for word in sentence.constituent.listWords():
            if not word.isType('Word'):
                continue
            try:
                self._tuples.append(self._systemsVector(word))
            except:
                print word
                print sentence
                print sentence.ID
                self._tuples.append(self._systemsVector(word))
            self._wordID += 1
            if not self._columnNames:
                self._columnNames = ['ID', 'Section', 'Lemma', 'TextString', 'PossessedLemma'] + [sn.replace(' ', '_') for sn in word.systems['namesList']]
        self.sentenceCount += 1
    
    def _systemsVector(self, word):
        """
        Just a tuple of system values, prepended by the PrimaryKey and String entries
        """
        vector = self._initialiseVector(word)
        for systemName in word.systems['namesList']:
            vector.append(str(word.systems[systemName]))
        return vector
        
    def _initialiseVector(self, word):
        """
        Initial values: ID, corpus section, lemma, textstring, possessed lemma, possessed textstring
        """
        ID = '%s~%s' % (self._sentenceID, str(self._wordID))
        section = self._sentenceID[:2]
        lemma = word.lemma().replace("'", '_SQT_')
        string = word.text.replace("'", '_SQT_')
        possessed = word.possession.possessed
        if not possessed:
            pLemma = 'None'
            pText = 'None'
        else:
            pLemma = possessed.lemma().replace("'", '_SQT_')
            pText = possessed.text.replace("'", '_SQT_')
        return [ID, section, lemma, string, pLemma]


    
class XMLPrinter(FileVisiter):
    """
    Print an XML representation of the file
    """
    location = 'c:/workspace/data/clauseBank/xml/'
    schemaLocation = 'c:/workspace/schemas/sfg_instantial.xsd'
    
    def newStructure(self):
        """
        Reset expression, create text node
        """
        self._expressionIndex = {}
        self._words = []
        self._length = 0
    
    def _visitFile(self, file):
        textNode = XMLNode('Text', 0)
        textNode.addAttr('id', file.ID)
        textNode.addAttr('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        textNode.addAttr('xsi:noNamespaceSchemaLocation', self.schemaLocation)
        grammar = XMLNode('Grammar', 1)
        for sentence in file.children():
            self._addWords(sentence.constituent)
            constituentXML = self._makeConstituent(sentence.constituent, 2)
            grammar.addNode(constituentXML)
        expressionPlane = XMLNode('ExpressionPlane', 1)
        expressionPlane.addText(' '.join(self._words))
        textNode.addNode(expressionPlane)
        textNode.addNode(grammar)
        open(self.location + file.ID[:-4] + '.xml', 'w').write(textNode.prettyPrint())
    
    def _visitSentence(self, file):
        pass
    
    def _addWords(self, clauseComplex):
        """
        Make the expression plane string that words will index into
        """
        words = clauseComplex.listLexis()
        for word in words:
            start = self._length
            self._length += len(word.text)
            end = self._length
            self._expressionIndex[word.globalID] = (start, end)
            self._words.append(word.text)
            # Increment length for whitespace
            self._length += 1
            
        
    def _makeConstituent(self, constituent, depth):
        xml = XMLNode('Constituent', depth)
        xml.addAttr('id', self._getID(constituent))
        xml.addAttr('type', self._getType(constituent))
        text = ' '.join([w.text for w in constituent.listWords()])
        xml.addComment(text)
        # Three ways to deal with realisation:
        # A Constituents element, a ConstituentRef, a StringRef
        # Constituents
        if not constituent.isType('Lexeme'):
            realisation = XMLNode('Constituents', depth + 1)
            for child in constituent.children():
                realisation.addNode(self._makeConstituent(child, depth + 2))
        # ConstituentRef
        elif constituent.isType('Ellipsis'):
            realisation = XMLNode('ConstituentRef', depth + 1)
            realisation.addAttr('idref', self._getID(constituent.ref()))
        # StringRef
        else:
            realisation = constituentRef = XMLNode('StringRef', depth + 1)
            start, end = self._expressionIndex[constituent.globalID]
            realisation.addAttr('start', str(start))
            realisation.addAttr('end', str(end))
        assert realisation.hasContent()
        xml.addNode(realisation)
        features = self._makeFeatures(constituent, depth + 1)
        if features.hasContent():
            xml.addNode(features)
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
        # Add system selection features
        for system in node.systems['namesList']:
            if not node.systems[system]:
                continue
            selection = XMLNode('Feature', depth + 1)
            selection.addAttr('type', 'system selection')
            selection.addAttr('value', '%s.%s' % (system, node.systems[system]))
            xml.addNode(selection)
        extraFeatures = self._getMiscFeatures(node, depth)
        for feature in extraFeatures:
            xml.addNode(feature)
        for metafunctionName in ['interpersonal', 'textual', 'experiential']:
            metafunction = getattr(node, metafunctionName, None)
            try:
                functions = metafunction.childFunctions.keys()
            except:
                continue
            functions.sort()
            for functionName in functions:
                if not metafunction.childFunctions[functionName]:
                    continue
                functionXML = XMLNode('Function', depth + 1)
                functionXML.addAttr('metafunction', metafunctionName)
                functionXML.addAttr('name', functionName)
                for constituent in metafunction.childFunctions[functionName]:
                    constituentRef = XMLNode('ConstituentRef', depth + 2)
                    constituentRef.addAttr('idref', self._getID(constituent))
                    functionXML.addNode(constituentRef)
                xml.addNode(functionXML)
        return xml
        
    def _getMiscFeatures(self, node, depth):
        """
        Get sundry hackish features specific to the workings of this system
        """
        extraFeatures = []
        # Add Penn Treebank label
        label = XMLNode('Feature', depth + 1)
        label.addAttr('type', 'PTB data')
        label.addAttr('value', 'label.%s' % (node.label))
        extraFeatures.append(label)
        # Add Penn Treebank function labels
        if node.functionLabels:
            functionLabel = XMLNode('Feature', depth + 1)
            functionLabel.addAttr('type', 'PTB data')
            functionLabel.addAttr('value', 'functionLabels.%s' % (', '.join(node.functionLabels)))
            extraFeatures.append(functionLabel)
        # Add special "quoted" feature
        if getattr(node, 'quoted', False):
            quoted = XMLNode('Feature', depth + 1)
            quoted.addAttr('type', 'misc')
            quoted.addAttr('value', 'quoted')
            extraFeatures.append(quoted)
        # Add metadata features
        for name, value in node.metadata.items():
           # print '%s: %s' % (str(name), str(value))
            metadata = XMLNode('Feature', depth + 1)
            metadata.addAttr('type', 'metadata')
            metadata.addAttr('value', '%s.%s' % (name, value))
            extraFeatures.append(metadata)
        return extraFeatures
        
        
    def _getID(self, constituent):
        """
        Different IDs for words and constituents
        """
        if constituent.isType('Lexeme'):
            return 'w%s' % constituent.wordID
        else:
            return 'c%s' % constituent.globalID
    
    
class FileController(FileVisiter):
    """
    Perform tasks on files
    """
    _speakerCodeMover = SpeakerCodeMover()
    _SFGConverter = Converters.Controller()
    
    def _visitFile(self, file):
        
        file.performOperation(self._speakerCodeMover)
    
    def _visitSentence(self, sentence):
        self._SFGConverter.actOn(sentence)
        """
        try:
            self._SFGConverter.actOn(sentence)
        except StandardError, e:
            print sentence.globalID
            raise e
        """
        
class ClauseTableCreater(FileVisiter):
    """
    Create a DB table for the ClauseBank
    """
    _clauseVectorBuilder = ClauseVectorBuilder()
    _fileOperator = FileController()
    fileCount = 0
    
    def _visitCorpus(self, corpus):
        self._databaseConnection = mx.ODBC.Windows.DriverConnect("""FILEDSN=c:\\Program Files\\Common Files\\ODBC\\Data Sources\\ClauseBank.dsn""")
        self._dropTables()
        self._columnNames = []
    
    def _visitFile(self, file):
        file.performOperation(self._fileOperator)
        file.performOperation(self._clauseVectorBuilder)
        self._commitClauses()
        
    def _commitClauses(self):
        """
        Insert clause vectors into a DB table
        """
        cursor = self._databaseConnection.cursor()
        if not self._columnNames:
            self._columnNames = self._clauseVectorBuilder.columnNames()
            self._createRankingClauses()
        for dbEntry in self._clauseVectorBuilder.vectors():
            query = """INSERT INTO RankingClauses (%s) VALUES (%s);""" % (', '.join(self._columnNames), ', '.join(["'%s'" % t for t in dbEntry]))
            cursor.execute(query)
        cursor.close()
        self._databaseConnection.commit()
        
    def _dropTables(self):
        """
        Check the existance of various tables in the database, and set flags
        to create them later if they do not exist
        """
        cursor = self._databaseConnection.cursor()
        try:
            query = """DROP TABLE RankingClauses"""
            cursor.execute(query)
        except:
            pass
        cursor.close()
            
    def _createRankingClauses(self):
        """
        Create a table for RankingClauses
        """
        tableName = 'RankingClauses'
        # Build create string
        createString = 'CREATE TABLE %s (\n' % tableName
        for columnName in self._columnNames:
            if columnName.lower() == 'textstring':
                createString += columnName + ' MEMO,\n'
            elif columnName.lower() == 'verified':
                createString += columnName + ' TEXT(5),\n'
            else:
                createString += columnName + ' TEXT(50),\n'
        # Trim final comma
        createString = createString[:-2]
        createString += '\n);'
        # Execute the SQL command
        cursor = self._databaseConnection.cursor()
        cursor.execute(createString)
        cursor.close()

class WordTableCreater(ClauseTableCreater):
    _tableName = 'Words'
    _vectorBuilder = WordVectorBuilder()
    _clauseVectorBuilder = None
    _fileOperator = FileController()
    fileCount = 0
    
    def _visitCorpus(self, corpus):
        self._databaseConnection = mx.ODBC.Windows.DriverConnect("""FILEDSN=c:\\Program Files\\Common Files\\ODBC\\Data Sources\\ClauseBank.dsn""")
        self._dropTable()
        self._columnNames = []
    
    def _visitFile(self, file):
        file.performOperation(self._fileOperator)
        file.performOperation(self._vectorBuilder)
        self._commit()
        
    def _commit(self):
        """
        Insert clause vectors into a DB table
        """
        cursor = self._databaseConnection.cursor()
        if not self._columnNames:
            self._columnNames = self._vectorBuilder.columnNames()
            self._createTable()
        for dbEntry in self._vectorBuilder.vectors():
            query = """INSERT INTO %s (%s) VALUES (%s);""" % (self._tableName, ', '.join(self._columnNames), ', '.join(["'%s'" % t for t in dbEntry]))
            cursor.execute(query)
        cursor.close()
        self._databaseConnection.commit()
        
    def _dropTable(self):
        """
        Check the existance of various tables in the database, and set flags
        to create them later if they do not exist
        """
        cursor = self._databaseConnection.cursor()
        try:
            query = """DROP TABLE %s""" % self._tableName
            cursor.execute(query)
        except:
            pass
        cursor.close()
            
    def _createTable(self):
        """
        Create a table for RankingClauses
        """
        # Build create string
        createString = 'CREATE TABLE %s (\n' % self._tableName
        for columnName in self._columnNames:
            if columnName.lower() == 'textstring':
                createString += columnName + ' MEMO,\n'
            elif columnName.lower() == 'verified':
                raise StandardError
            else:
                createString += columnName + ' TEXT(50),\n'
        # Trim final comma
        createString = createString[:-2]
        createString += '\n);'
        # Execute the SQL command
        cursor = self._databaseConnection.cursor()
        cursor.execute(createString)
        cursor.close()
        
        
class COMLEXAssociator(FileVisiter):
    """
    Associate the first COMLEX entry with each word
    This allows lematisation for WN sense association later
    """
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
        print "Building COMLEX Dict"
        self._COMLEX = COMLEX.buildLexicon()
    
    def _visitSentence(self, sentence):
        pass
    
    def _visitFile(self, file):
        """
        Forward words for sense attachment, reject other nodes
        """
        for word in self.wordGenerator(file):
            self._addSyntax(word)
        
    def _addSyntax(self, word):
        entries = self._COMLEX.get(word.lemma(), [])
        word.metadata['COMLEX'] = []
        for entry in entries:
            if self._POSMatch(word.label, entry.label):
                word.metadata['COMLEX'].append(entry)
                
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

        
class SenseAssociator(FileVisiter):
    """
    Add sense to data to text that overlaps with some WSD corpus
    """
    _count = 0
    try: _alignmentMap = cPickle.load(open('c:/workspace/data/semcor/pickled/ptb_map.dat'))
    except: alignmentMap = {}
#    _posDict = {
#        'verb': wordnet.V,
#        'noun': wordnet.N,
#        'adjective': wordnet.ADJ,
#        'adverb': wordnet.ADV
#    }
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
        self._readSenseIDX()
        self._sensevalFiles = cPickle.load(open('C:/workspace/Data/SENSEVAL_2/senseval_wsj.dat'))
    
    def _readSenseIDX(self):
        """
        Read in the sense.IDX into a dict
        """
        lines = [entry.split() for entry in open('C:/Program Files/WordNet/2.0/dict/sense.IDX').read().split('\n') if entry]
        senseIDX = {}
        for sKey, ssOffset, sNum, sCnt in lines:
            senseIDX[sKey] = (int(ssOffset), int(sNum))
        self._senseIDX = senseIDX
    
    def _visitSentence(self, sentence):
        raise Break
    
    def _visitFile(self, file):
        """
        Load mappings produced elsewhere, because mapping is a non-trivial once-off task that
        depends on the source of the sense keys: senseval lexical set data, semcor corpus, etc
        """
        self._initSenses(file)
        # Hack to generate semcor set with no extra wsd
       # return None
        if Semcor.hasFile(file.ID):
            self._doSemcorDisamb(file)
        if file.ID in self._sensevalFiles:
            self._doSensevalDisamb(file)
        
    def _doSensevalDisamb(self, file):
        """
        Add senses to the few words disambiguated in the SENSEVAL set
        """
        words = [w for w in self.wordGenerator(file)]
        for offset, senseKeys in self._sensevalFiles[file.ID]:
            senses = [self._getSense(senseKey) for senseKey in senseKeys]
            word = words[offset]
            setattr(word, 'senses', senses)
        
    def _doSemcorDisamb(self, file):
        """
        Wordnet sense disambiguate a file that has been manually annotated in the
        SemCor corpus
        """
        filename = 'br-' + file.ID[1:-4]
        parseSentences = [p for p in file.children()]
        # Get list of ptb words
        parseWords = []
        for s in parseSentences:
            parseWords.extend(s.listWords())
        senseSentences = Semcor.parse(filename)
        # Get list of semcor words
        senseWords = []
        for s in senseSentences:
            senseWords.extend(s['words'])
        aligned = self._alignmentMap[file.ID]
        for senseOffset, parseOffset in aligned:
            try:
                senseWord = senseWords[senseOffset]
            except:
                print senseOffset
            parseWord = parseWords[parseOffset]
            sense = self._getSense(senseWord['lexsn'])
            if senses:
                setattr(parseWord, 'senses', [sense])

    
    _pos = ('noun', 'verb', 'adjective', 'adverb')
    def _getSense(self, senseKey):
        senseKey = senseKey.replace("-", "'")
        offset, sNum = self._senseIDX[senseKey]
        lemma, nums = senseKey.split('%')
        nums = nums.split(':')
        posNum = int(nums[0]) - 1
        if posNum == 4:
            posNum = 2
        dictionary = wordnet.Dictionaries[posNum]
        word = dictionary[str(lemma.replace('_', ' '))]
        senseOffset = int(nums[2])
        sense = word[sNum - 1]
        return sense

    def _initSenses(self, file):
        """
        Get a WordNet POS and a WordNet polysemy. If polysemy is 1, return the synset
        offset too. Otherwise just return 'null'
        
        return: WN_POS, WNSynsetOffset, WNPolysemy
        """
        for word in self.wordGenerator(file):
            WN_POS = self._getWNPOS(word.label)
            if not WN_POS:
                word.senses = []
                continue
            else:
                index = self._posDict[WN_POS]
            if index.has_key(word.lemma()):
                word.senses = [s for s in index[word.lemma()]]
            else:
                word.senses = []
               # print word.lemma()
            
            
    def _getWNPOS(self, tbPOS):
        """
        Choose between N, V, ADJ, ADV based on the TB pos
        """
        if tbPOS.startswith('N'):
            return 'noun'
        elif tbPOS.startswith('V'):
            return 'verb'
        elif tbPOS.startswith('R'):
            return 'adverb'
        elif tbPOS.startswith('J'):
            return 'adjective'
        else:
            return ''
            
            

class FrameNetAssociator(FileVisiter):
    """
    Add a list of frames and a list of "predicted frames" to a word.
    Use wn-sense if possible, via the Shi et al. mapping.
    """
    
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
        self._getWordnetFramenetMap()
        self._getGoldText()
        luSet = FrameNet.LUSet(FrameNet.frameNet.lexis)
        self.fnWords = luSet.divide('name')
        frames = FrameNet.frameNet.frames
        self.frameNames = frames.keys()
        self.frames = frames
        self.frameNames.sort()
            
    
    def _visitSentence(self, sentence):
        pass
        
    def _visitFile(self, file):
        for word in self.wordGenerator(file):
            # form.pos, e.g. brick.n
            fnKey = '%s.%s' % (word.lemma(), self._getPOS(word))
            # fnWords' values are LUSets. Get the members' frames.
            word.metadata['fn_frames'] = [w.frame for w in self.fnWords.get(fnKey, [])]
            if len(word.senses) == 1:
                sense = word.senses[0]
                # If there are 'shi_frames', filter by them
               # if self._wordnetFrameMap.has_key(sense.synsetOffset):
               #     shiFrames = self._wordnetFrameMap[sense.synsetOffset]
               #     word.metadata['fn_frames'] = [f for f in word.metadata['fn_frames'] if f.name in shiFrames]
        goldWords = self._goldText.get(file.ID[:-4], [])
        if not goldWords:
            return None
        i = 0
        for word in self.wordGenerator(file):
            goldWord = goldWords[i]
            assert goldWord[1] == word.text
            if len(goldWord) == 3:
                word.metadata['fn_frames'] = [self.frames[goldWord[2]]]
            i += 1
            
            
    def _getPOS(self, word):
        if word.label.startswith('N'):
            return 'n'
        elif word.label.startswith('V'):
            return 'v'
        elif word.label.startswith('R'):
            return 'adv'
        elif word.label.startswith('J'):
            return 'adj'
        elif word.label == 'IN':
            return 'prep'
        else:
            return ''
            
            
    def _getWordnetFramenetMap(self):
        senseIDX = self._getSenseIDX()
        path = 'C:/workspace/Data/FrameNet/FnWnVerbMap.1.0/FnWnVerbMap.1.0.txt'
        data = open(path).read()
        self._wordnetFrameMap = {}
        for line in data.split('\n'):
            try:
                frame, verb, senses = line.split(' ', 2)
            except ValueError:
                continue
            frame = frame.capitalize()
            if senses == '0':
                continue
            senses = senses.split()
            for senseKey in senses:
                synsetOffset = senseIDX[senseKey]
                if frame not in self._wordnetFrameMap.setdefault(synsetOffset, []):
                    self._wordnetFrameMap[synsetOffset].append(frame)
                    
    
    def _getGoldText(self):
        """
        Read in the gold standard texts. Each will be a table. They will be indexed
        by file name
        """
        path = 'c:/workspace/frame_prediction/gold_standard/'
        names = os.listdir(path)
        self._goldText = {}
        for n in names:
            table = [l.split('\t') for l in open(path + n).read().split('\n')]
            self._goldText[n] = table
            
    
                
    def _getSenseIDX(self):
        """
        Build a dict from the sense idx file
        """
        wnHome = os.environ['WNHOME']
        data = open(wnHome + '/dict/sense.idx').read()
        senseIDX = {}
        for l in data.split('\n'):
            if not l: continue
            key, value = l.split()[:2]
            senseIDX[key] = int(value)
        return senseIDX
                
        
class FrameFeatureExtractor(FileVisiter):
    """
    There are 7 main `slots' that participate in frames:
        0. The head verb (SFG Predicator)
        1. The logical subject (the agent in passives, the subject in actives)
        2. Direct object
        3. Indirect object (SFG Benificiary)
        4. NP child of PP (Cardiff SFG 'completive')
        5. ADVP
        6. Other
    These correspond to the following WN networks:
        0. Verb --  13,650
        1. Noun --  81,426
        2. Noun --  81,426
        3. Noun --  81,426
        4. Noun --  81,426
        5. Advb --   3,644
        6. All  -- 117,597
        
        Total:     460,595
    """
    def __init__(self):
        self._functionMap = self._makeFunctionMap()
        print "Getting vectors"
        # A list dictionaries mapping synset ID's to offsets in a sparse vector 
        self._getSparseVectorMap()
        self.vectors = []
        self.output = None
        self._specialPOS = {'NNP': 1, 'WP': 1, 'WDT': 1, 'PRP': 1}
    
    def _visitFile(self, file):
        pass
        
    def _visitSentence(self, sentence):
        for clause in [c for c in sentence.constituent.depthList() if c.isType('Clause')]:
            # Ignore clause criteria...
            # 1. Minor clauses
            if clause.systems['clause class'] == 'minor':
                continue
            # 2. Non-Finite
            elif not clause.interpersonal.subject:
                continue
            # Nominalised clause constituents (head finding gets messed up)
            elif [g for g in clause.groups() if 'NOM' in g.functionLabels]:
                continue 
           # self._visitClause(clause)
            self._makeTable(clause)
                        
    #############
    # Main loop #
    #############
    
    def _makeTable(self, clause):
        # Get the words that can fill the 7 slots
        slots = self._getSlotWords(clause)
        functionLabels = slots.pop()
        row = [clause.verbalGroup().head().lemma()]
        specialPOS = self._specialPOS
#        i = 0
#        print "SLOTS FOR CLAUSE:"
#        print clause
        for slot in slots:
            cell = []
            for word in slot:
                # Use special synsets for pro and proper nouns
                if word.label in specialPOS:
                    # Assume proper nouns are people or companies etc
                    if word.label == 'NNP':
                        # person 1, company 1, organisation 2, corporation 1
                        offsets = [6026, 7670529, 7569639]
                    # 'it' -- use object 1, event 2
                    elif word.lemma() == 'it':
                        offsets = [16236, 25950]
                    # non-it pronoun: use person 1
                    elif word.label == 'PRP':
                        offsets = [6026]
                    # Who -- use person 1
                    elif word.lemma() == 'who':
                        offsets = [6026]
                    # Which: use object 1, event 2
                    elif word.lemma() == 'which':
                        offsets = [16236, 25950]
                    # Union of who and which
                    else:
                        offsets = [16236, 25950, 6026]
                    # They're all nouns.
                    cell.append('.'.join(['noun!%d' % offset for offset in offsets]))
                else:
                    cell.append('.'.join(['%s!%d' % (sense.pos, sense.synsetOffset) for sense in word.senses]))
#            print "Slot %d" % i
#            i += 1
#            if i < 6:
#                for w in cell:
#                    if not w: continue
#                    senses = w.split('.')
#                    print "Synset:"
#                    for ssKey in senses:
#                        if not ssKey:
#                            continue
#                        pos, offset = ssKey.split('!')
#                        s = wordnet.getSynset(pos, int(offset))
#                        print s
            row.append(':'.join(cell))
        row.append(':'.join(functionLabels))
        predicator = clause.verbalGroup().head()
        frames = [f.name for f in predicator.metadata['fn_frames']]
        row.append(':'.join(frames))
        self.output.write(','.join(row) + '\n')
        
    def setClass(self, classFrame):
        self.classFrame = classFrame
        self.vectors = []

    
    
                    
    ######################################
    # Divide the clause into the `slots' #
    ######################################
                
    def _getSlotWords(self, clause):
        """
        Get the words which can occupy each of the seven slots.
        """
        # Item 0
        vg = [clause.verbalGroup().head()]
        # Item 1
        if clause.systems['effective voice'] == 'receptive': # Passive in LexCart SFG jargon
            logicalSubj = self._getByAgent(clause)
            directObj = [clause.interpersonal.subject.head()]
            indirectObj = []
            for complement in clause.interpersonal.complement:
                if 'BNF' in complement.functionLabels:
                    indirectObj.append(complement.head())
        else:
            logicalSubj = [clause.interpersonal.subject.head()]
            # Items 2 and 3
            directObj = []
            indirectObj = []
            for complement in clause.interpersonal.complement:
                if 'BNF' in complement.functionLabels:
                    indirectObj.append(complement.head())
                else:
                    directObj.append(complement.head())
        
        # Item 4
        completives = []
        for pp in [g for g in clause.groups() if g.isType('Prepositional_Phrase')]:
            for ng in pp.groups():
                if (ng.isType('Nominal_Group')) and ('LGS' not in ng.functionLabels):
                    completives.append(ng.head())
        # Item 5
        advp = []
        for g in clause.groups():
            if g.isType('Adverbial_Group'):
                advp.append(g.head())
        # Item 6
        all = []
        for constituent in clause.children():
            if not constituent.isType('Clause'):
                all.extend(constituent.listWords())
        # Item 7: function labels
        functionLabels = []
        for constituent in clause.children():
            functionLabels.extend(constituent.functionLabels)
        slots = [vg, logicalSubj, directObj, indirectObj, completives, advp, all, functionLabels]
       # for i in xrange(len(slots)):
       #     s = slots[i]
       #     print "Slot %d: %s" % (i, [str(w) for w in s])
        return [vg, logicalSubj, directObj, indirectObj, completives, advp, all, functionLabels]
       # return [vg, logicalSubj, directObj, indirectObj, completives, advp]


    def _getByAgent(self, clause):
        # Iterate through surface constituents
        for const in clause.groups():
            if not const.isType('Prepositional_Phrase'):
                continue
            # Iterate through PP children...
            for group in const.groups():
                if 'LGS' in group.functionLabels:
                    return [group.head()]
        return []
    
    
    #######################################
    # Initialising global data structures #
    #######################################
                
    def _getSparseVectorMap(self):
        """
        Each of the six slots is associated with its own subset of the feature space.
        A synset offset can occur in multiple spaces, e.g. a noun synset will be in 1, 2, 3, 4, 6.
        In order to build sparse vectors, we must map the synset offsets to indexes into a global array
        that can be constructed later.
        """
        synsetLists = self._getSynsetLists()
        globalIndex = 0
        synsetSpaces = [
            synsetLists['verb'], # 0 
            synsetLists['noun'], # 1
            synsetLists['noun'], # 2
            synsetLists['noun'], # 3
            synsetLists['noun'], # 4
            synsetLists['advb'], # 5
           # synsetLists['all']   # 6
        ]
        self._sparseVectorMap = []
        self.header = {'Class': 'Class'}
        slot = 0
        for synsets in synsetSpaces:
            singleMap = {}
            for synsetID in synsets:
                globalIndex += 1
                singleMap[synsetID] = globalIndex
                self.header[globalIndex] = '%d_%d' % (slot, synsetID)
            slot += 1
            self._sparseVectorMap.append(singleMap)
        
    def _getSynsetLists(self):
        """
        Get lists of synset offsets for different parts of speech
        """
        wnHome = os.environ['WNHOME']
        senseIDX = open(wnHome + '/dict/sense.idx').read().split('\n')
        synsets = {'verb': [], 'noun': [], 'advb': [], 'all': []}
        for line in senseIDX:
            if not line: continue
            # Example line: acculturation%1:09:01:: 05424093 3 0
            senseKey, synsetOffset = line.split()[:2]
            synsetOffset = int(synsetOffset)
            synsets['all'].append(synsetOffset)
            # Get the '1' from acculturation%1:09:01::
            synsetType = senseKey.split('%')[1].split(':')[0]
            if synsetType == '1':
                synsets['noun'].append(synsetOffset)
            elif synsetType == '2':
                synsets['verb'].append(synsetOffset)
            elif synsetType == '3':
                synsets['advb'].append(synsetOffset)
        return synsets

        
    
    ##########
    # Output #
    ##########
    
    def writeCSV(self, classFrame, location):
        location = location + classFrame + '.csv'
        seenKeys = {}
        for vector in self.vectors:
            for k in vector.keys():
                seenKeys[k] = True
        seenKeys = seenKeys.keys()
        seenKeys.remove('Class')
        header = []
        for k in seenKeys:
            header.append(self.header[k])
        header.append('Class')
        csv = open(location, 'w')
        csv.write(','.join([str(cell) for cell in header]) + '\n')
        while self.vectors:
            vector = self.vectors.pop(0)
            # Hack for training data: use only 1 or 0 class valued vectors
            if vector['Class'] not in [1, 0]:
                continue
            v = []
            for k in seenKeys:
                v.append(vector.get(k, 0))
            # Hack for training data: discretise the class value
            v.append(bool(vector['Class']))
            csv.write(','.join([str(cell) for cell in v]) + '\n')
        csv.close()






        
class IOBSensePrinter(FileVisiter):
#    _posDict = {
#        'verb': wordnet.V,
#        'noun': wordnet.N,
#        'adjective': wordnet.ADJ,
#        'adverb': wordnet.ADV
#    }
    
    def _visitSentence(self, sentence):
        pass
    
    def _visitFile(self, file):
        """
        text, lemma, WN_Polysemy, WN-POS, WN-Synset Offset, TB-POS, SyntaxIOB, Framenet_Polysemy
        """
        global DATA_PATH
        words = [('text', 'lemma', 'WN_Form', 'WN_Polysemy', 'WN-POS', 'WN-Synset Offset', 'TB-POS', 'SyntaxIOB', 'FN_Polysemy', 'All_Frames', 'Shi_Polysemy', 'Shi_Frames')]
        for word in self.wordGenerator(file):
            text  = word.text
            lemma = word.lemma()
            POS = word.label
            syntaxIOB = self._getSyntaxIOB(word)
            frames = word.metadata['fn_frames']
            shiFrames = word.metadata['shi_frames']
            if word.wordnetSense:
                WN_POS = word.wordnetSense.pos
                WNSynsetOffset = word.wordnetSense.synsetOffset
                WNForm = word.wordnetSense.form
                index = self._posDict[word.wordnetSense.pos]
                WNPolysemy = len(index[WNForm])
            else:
                WN_POS = 'null'
                WNSynsetOffset = 'null'
                WNForm = 'null'
                WNPolysemy = 0
            words.append( (text, lemma, WNForm, str(WNPolysemy), WN_POS, str(WNSynsetOffset), POS, syntaxIOB, str(len(frames)), ', '.join(frames), str(len(shiFrames)), ', '.join(shiFrames)) )
        string = '\n'.join(['\t'.join(w) for w in words])
        open(DATA_PATH + 'semcor/TB_IOB/' + file.ID[:-4] + '.tab', 'w').write(string)
                
                
    
    def _getSyntaxIOB(self, word):
        indent = []
        parent = word.parent()
        while word == parent.listWords()[0]:
            indent.append(parent.label)
            try:
                parent = parent.parent()
            except AttributeError:
                break
        dedent = []
        parent = word.parent()
        while word == parent.listWords()[-1]:
            dedent.append(parent.label)
            try:
                parent = parent.parent()
            except AttributeError:
                break
        indent.reverse()
        indentString = ''.join(['(' + label for label in indent])
        dedentString = ''.join([')' for label in dedent])
        return indentString + '*' + dedentString
        
    

class TokenPrinter(FileVisiter):
    """
    Print tokenised sentences ready for parsing
    """
    def _visitFile(self, theFile):
        sentences = []
        for sentence in theFile.children():
            textSent = []
            for word in sentence.constituent.listWords():
                if not word.isType('Ellipsed') and not word.isType('Trace'):
                    textSent.append(word.text)
            sentences.append(' '.join(textSent))
        open(TEXT_PATH + theFile.filename, 'w').write('\n'.join(sentences) + '\n')
    
    def _makeFunctionMap(self):
        """
        Map classes to the methods that should be called on them
        """
        return {self._file: self._visitFile}
    
    
DATA_PATH = "c:/workspace/data/"
TEXT_PATH = "c:/workspace/data/textTB/"
