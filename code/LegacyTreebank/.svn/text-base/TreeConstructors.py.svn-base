"""
Instantiate a Node tree from a Penn Treebank parse tree string

Support different PTb formats (ATIS, SwitchBoard, WSJ, BROWN etc) and
make it easy to adapt to other, similar parse trees.
"""
import re, os
from   Nodes import *
import xml


class CompositeConstructor:
    _localID = 0
    _rootClass = None
    _internalClass = None
    _leafClass = None
    def __init__(self):
        self._childConstructors = {}

    def addChildConstructors(self, childConstructors):
        self._childConstructors.update(childConstructors)
        
    
    def startNew(self):
        self._localID = 0
        
    def make(self, rawData, nodeClass):
        """
        Instantiate a node
        """
        settings = self._getSettings(rawData)
        node = nodeClass(settings)
        if nodeClass is not self._leafClass:
            self._parseChildren(node, rawData)
        node.setup()
        return node
        
    def _parseChildren(self, node, rawData):
        """
        Iterate through immediate children, making a node from each
        In the process of making a node, this function is called, so the tree is
        parsed depth first. IDs are added later, by a Visitor, so that IDs are breadth
        first.
        """
        for child in self._getChildren(rawData):
            if self.isLeaf(child):
                leafNode = self.make(child, self._leafClass)
                node.attachChild(leafNode, len(node))
            else:
                node.attachChild(self.make(child, self._internalClass), len(node))
    
    def isLeaf(self, rawData):
        """
        Template for checking whether rawData is
        a leaf
        """
        pass
    
    def _getSettings(self, rawData):
        """
        Template for getting settings to pass to
        a Node constructor
        """
        settings = {}
        settings['_children'] = []
        settings['_parent'] = None
        settings['metadata'] = {}
        settings['_copyConstructor'] = singleton(ConstituentConstructors.CopyCreator)
        return settings


    def _getChildren(self, text):
        """
        Template for getting children from rawData
        """
        depth = 0
        start = None
        for i, char in enumerate(text):
            # Increase depth
            if char == '(':
                # Note start point of bracket if depth 0
                if not depth:
                    start = i
                depth += 1
            # Decrease depth
            elif char == ')':
                depth -= 1
                # Yield bracket when depth 0
                if depth == 0:
                    print text
                    yield text[start+1:i]
        
    


# ========================================================================================

        

class SentenceConstructor(CompositeConstructor):
    """
    Construct sentence parse trees
    """
    # What to construct
    _rootClass       = RootNode
    _internalClass   = InternalNode
    _leafClass       = LeafNode
    # Extract settings
    _labelRE = re.compile(r"^[^ ]+")
    _labelSplitRE = re.compile(r"(?<=[^-])[-=](?=[^-])")
   # _labelRE         = re.compile(r"^(-(?:[A-Z]+)-|[\^\w,\.\(\):`\$#'@]+)")
   # _functionLabelRE = re.compile(r"^(-(?:\w+)-|[\w,\.\(\):`\$#'@]+)-(\w{1,3}(?:-(?=\w))?)+")
    _textRE          = re.compile(r'(?<= )[^\s]+$')
    _hasChars        = re.compile('[^\s]')
    _sentenceID = 0
    _wordID = 0
    
    
    def make(self, rawData, nodeClass):
        """
        Instantiate a node
        """
        settings = self._getSettings(rawData)
        node = nodeClass(settings)
        if nodeClass is not self._leafClass:
            self._parseChildren(node, rawData)
        node.setup()
        return node
    
    def isLeaf(self, text):
        if '(' in text[1:]:
            return 0
        else:
            return 1    
        
    def _getSettings(self, bracket):
        settings = {'metadata': {}}
        try:
            wholeLabel = self._labelRE.search(bracket).group()
        except AttributeError:
            raise ParseError, 'Error parsing label on bracket:\n\n' + bracket
        label = self._labelSplitRE.split(wholeLabel)[0]
        # Ensure that opening brackets are trimmed
        while label.startswith('('):
            label = label[1:]
        if not label:
            print bracket
            raise ParseError
        # Reduce "uncertain" labels to the first label
        label = label.split('|')[0]
        settings['label'] = label
        settings['functionLabels'] = self._getFunctionLabels(wholeLabel)
        settings['identifier'] = self._getID(wholeLabel, '-')
        settings['identified'] = self._getID(wholeLabel, '=')
        settings['_children'] = []
        settings['_parent'] = None
        settings['constituent'] = None
        text = self._textRE.search(bracket)
        if text:
            self._wordID += 1
            settings['text'] = text.group()
            settings['wordID'] = self._wordID
        return settings
        
    def _getFunctionLabels(self, label):
        """
        Split the label, remove identifier and identified
        """
        labels = self._labelSplitRE.split(label)
        if len(labels) == 1:
            return []
        functionLabels = []
        for label in labels[1:]:
            if label.isdigit():
                continue
            # Remove identifier labels
            label = label.split('=')[0]
            functionLabels.append(label)
        return functionLabels
        
    def _getID(self, label, delimiter):
        """
        Get [=-][0-9] tags
        """
        labels = label.split(delimiter)
        if delimiter == '-':
            nonDelim = '='
        else:
            nonDelim = '-'
        for label in labels:
            label = label.split(nonDelim)[0]
            if label.isdigit():
                return label
        return ''


class NewSentenceConstructor(object):
    # What to construct
    _rootClass       = RootNode
    _internalClass   = InternalNode
    _leafClass       = LeafNode
    # Extract settings
    _labelRE = re.compile(r"^[^ ]+")
    _labelSplitRE = re.compile(r"(?<=[^-])[-=](?=[^-])")
   # _labelRE         = re.compile(r"^(-(?:[A-Z]+)-|[\^\w,\.\(\):`\$#'@]+)")
   # _functionLabelRE = re.compile(r"^(-(?:\w+)-|[\w,\.\(\):`\$#'@]+)-(\w{1,3}(?:-(?=\w))?)+")
    _textRE          = re.compile(r'(?<= )[^\s]+$')
    _hasChars        = re.compile('[^\s]')
    _sentenceID = 0
    _wordID = 0
            
        
    def _getID(self, label, delimiter):
        """
        Get [=-][0-9] tags
        """
        labels = label.split(delimiter)
        if delimiter == '-':
            nonDelim = '='
        else:
            nonDelim = '-'
        for label in labels:
            label = label.split(nonDelim)[0]
            if label.isdigit():
                return label
        return ''
    
    def startNew(self):
        self._localID = 0
        

        
    def _parseChildren(self, node, rawData):
        """
        Iterate through immediate children, making a node from each
        In the process of making a node, this function is called, so the tree is
        parsed depth first. IDs are added later, by a Visitor, so that IDs are breadth
        first.
        """
        parseTree = self._parseTree(rawData)
        for node in parseTree:
            print node
        raise StandardError

    _start = r'(\()(\S+)'
    _end   = r'(\S+)?(\))'
    bracketsRE = re.compile(_start + '|' + _end)
    def make(self, text, rootClass):
        openBrackets = []
        parentage = {}
        nodeOffsets = {}
        # Get the nodes and record their parents
        for match in self.bracketsRE.finditer(text):
            if match.group(0) == '(':
                openBrackets.append((match.group(1), match.start()))
            else:
                label, start = openBrackets.pop()
                text = match.group(3)
                if text:
                    newNode = self._makeLeaf(label, text)
                else:
                    newNode = self._makeNode(label)
                # Store parent start position
                parentStart = openBrackets[-1][1]
                parentage[newNode] = parentStart
                # Organise nodes by start
                nodes[start] = newNode
        # Build the tree
        for node, parentOffset in parentage.items():
            parent = nodes[parentOffset]
            parent.attachChild(node)
        
                

    def _getSettings(self, label, text = None):
        settings = {'metadata': {}}
        # Reduce "uncertain" labels to the first label
        settings['label'] = label.split('|')[0]
        settings['functionLabels'] = self._getFunctionLabels(label)
        settings['identifier'] = self._getID(label, '-')
        settings['identified'] = self._getID(label, '=')
        if text:
            self._wordID += 1
            settings['text'] = text
            settings['wordID'] = self._wordID
        return settings

    def _getFunctionLabels(self, label):
        """
        Split the label, remove identifier and identified
        """
        labels = self._labelSplitRE.split(label)
        if len(labels) == 1:
            return []
        functionLabels = []
        for label in labels[1:]:
            if label.isdigit():
                continue
            # Remove identifier labels
            label = label.split('=')[0]
            functionLabels.append(label)
        return functionLabels


class SWBDSentenceConstructor(SentenceConstructor):
    """
    The Switchboard section of the Treebank is rather different, as it supports
    features documenting the 'noise' in the data -- dysfluencies and transcription
    errors.
    """
    _typoRE = re.compile(r'\^[A-Z]+')
    
    
    def _parseChildren(self, node, rawData):
        """
        Overrides CompositeConstructor's method, adding special handling for 'doubled' tokens:
        tokens with two parts of speech because a transcriber fused two words.
        """
        for child in self._getChildren(rawData):
            if self.isLeaf(child):
                if self._isTypo(child):
                    parts = self._handleTypo(child)
                    for part in parts:
                        node.attachChild(part)
                else:
                    node.attachChild(self.make(child, self._leafClass), -1)
            else:
                node.attachChild(self.make(child, self._internalClass), -1)
    
    def _isTypo(self, child):
        """
        Typos are marked by ^ in the label
        """
        if self._typoRE.search(child):
            return True
        else:
            return False
            
    def _handleTypo(self, bracket):
        """
        Determine whether the typo is a fusion of two words.
        If one word, make the child and add typo metadata
        If two words, make the first child as normal, and then make a second with special text.
        """
        settings = {}
        try:
            label = self._labelRE.search(bracket).group()[1:]
        except:
            raise ParseError, 'Error parsing label on bracket:\n\n' + bracket
        parts = []
        labels = label.split('^')
        for POS in labels:
            settings['label'] = POS
            settings.update(self._getLeafSettings(bracket))
            parts.append(self._leafClass(settings))
        return parts
    
    
    
    def _getLeafSettings(self, bracket):
        settings = {'metadata': {'typo': 1}}
        settings['_children'] = []
        settings['_parent'] = None
        settings['constituent'] = None
        settings['functionLabels'] = []
        self._wordID += 1
        settings['text'] = self._textRE.search(bracket).group()
        settings['wordID'] = self._wordID
        return settings



        
    


# ========================================================================================

    
class FileConstructor(CompositeConstructor):
    """
    Construct a corpus file
    """
    _startBracket    = '('
    _endBracket      = ')'
    _whitespaceRE = re.compile(r'\s+')
    _commentRE = re.compile(r'\*x.+')
    _rootClass = CorpusFile
    _leafClass = RootNode
    
    def make(self, location, nodeClass):
        """
        Instantiate a file
        """
        text = open(location).read()
        text = self._preprocessText(text)
        settings = self._getSettings(location)
        node = nodeClass(settings)
        if nodeClass is not self._leafClass:
            self._parseChildren(node, text, self._getChildConstructor(location))
        return node
        
    def _parseChildren(self, node, rawData, childConstructor):
        """
        Iterate through immediate children, making a node from each
        In the process of making a node, this function is called, so the tree is
        parsed depth first. IDs are added later, by a Visitor, so that IDs are breadth
        first.
        """
        sentenceID = 0
        for child in self._getChildren(rawData):
            ID = node.ID + '~' + self._padInt(sentenceID, 4)
            try:
                sentence = childConstructor.make(child, self._leafClass)
            except ParseError:
                raise
                print >> sys.stderr, "Parse error"
                continue
            sentence.globalID = ID
            # Each word ID is sentIdx. Offset within sentence
            node.attachChild(sentence)
            sentenceID += 1
    
    
    def isLeaf(self, text):
        """
        Not implemented
        """
        raise AttributeError, 'FileConstructors do not implement isLeaf'
        
    def _getSettings(self, location):
        settings = {'path': location}
        filename = location.split('/')[-1]
        settings['filename'] = filename
        settings['ID'] = filename
        settings['_children'] = []
        settings['_parent'] = None
        return settings
        
    def _getChild(self, text, start, end):
        return text[start+2:end]


        
        
    def _getMetadata(self, text):
        """
        WSJ and ATIS have no metadata
        """
        return {}
    
    def _preprocessText(self, text):
        """
        Remove whitespace
        """
        text = self._whitespaceRE.sub(' ', self._commentRE.sub('', text))
        # Sometimes sentences start (( instead of ( (. This is an error, correct it
        text = text.replace('((', '( (')
        return text
        
    def _getChildConstructor(self, location):
        if location.find('sw') != -1:
            return self._childConstructors['swbd']
        else:
            return self._childConstructors['standard']
            
    def _padInt(self, number, length):
        """
        Pad an int string with 0s
        """
        numberString = str(number)
        while len(numberString) < length:
            numberString = '0' + numberString
        return numberString

    def _getChildren(self, text):
        """
        Template for getting children from rawData
        """
        depth = 0
        start = None
        for i, char in enumerate(text):
            # Increase depth
            if char == '(':
                # Note start point of bracket if depth 0
                if not depth:
                    start = i
                depth += 1
            # Decrease depth
            elif char == ')':
                depth -= 1
                # Yield bracket when depth 0
                if depth == 0:
                    yield text[start+2:i]




class FlatFileConstructor(FileConstructor):
    
    def make(self, location, nodeConstructor):
        settings = self._getSettings(location)
        fileNode = self._rootClass(settings)
        nodes = {fileNode.ID: fileNode}
        for nodeText in open(location):
            headIdx, nodeClass, data = nodeText.split('**')
            headIdx = headIdx
            nodeClass = eval(nodeClass)
            node = nodeConstructor.make(data, nodeClass)
            head = nodes[headIdx]
            head.attachChild(node)
            nodes[node.globalID] = node


class FlatSentenceConstructor:
    def make(self, data, nodeClass):
        settings = self._getSettings(data)
        return nodeClass(settings)
    

    
# ========================================================================================    

class DBFileConstructor(FileConstructor):
    """
    Retrieve a corpus file from a database
    """        
    def make(self, fileKey, nodeClass):
        """
        Instantiate a file
        """
        records = self._getFileSentences(fileKey)
        settings = self._getSettings(fileKey)
        node = nodeClass(settings)
        childConstructor =  self._getChildConstructor(fileKey)
        if nodeClass is not self._leafClass:
            for sentenceID, tree in records:
                sentence = childConstructor.make(tree.replace('_SQT_', "'"), self._leafClass)
                sentence.globalID = sentenceID
                node.attachChild(sentence)
        return node
        
    def _getFileSentences(self, fileKey):
        """
        Use the database cursor to get a set of sentence records
        """
        global DSN_PATH
        databaseConnection = mx.ODBC.Windows.DriverConnect('FILEDSN=%s' % DSN_PATH)
        cursor = databaseConnection.cursor()
        query = """SELECT PKey,TreeString
        FROM PTB_Sentences
        WHERE FileName='%s'
        ORDER BY ParseNumber;""" % fileKey
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        if not records:
            raise QueryError
        return [r for r in records]



class XMLFileConstructor(FileConstructor):
    """
    Create a 'File' for an XML corpus
    """
    
    def __init__(self):
        self._XMLParser = xml.sax.make_parser()
        self._XMLParser.setContentHandler(SFG_XML.SFGContentHandler())
    
    def make(self, location, nodeClass):
        """
        Attributes: id
        """
        self._XMLParser.parse(location)
        return self._XMLParser.getContentHandler().file()
        
    def setPath(self, path):
        self._path = path


# ========================================================================================  


class CorpusConstructor(FileConstructor):
    """
    Read in a corpus, initiating corpus files
    """
    _leafClass = CorpusFile
    def make(self, type, location, nodeClass):
        """
        Instantiate a Corpus
        """
        settings = {'path': location}
        node = nodeClass(settings)
        node.settings(self._getChildConstructor(type), self._leafClass)
        self._parseChildren(node, self._getFileList(location))
        return node
    
    
    def _getChildren(self, filenames):
        """
        Generator function
        
        Iterates through a directory listing and yields text
        """
        raise AttributeError, '_getChildren function not implemented for CorpusConstructor'
    
    def _parseChildren(self, node, rawData):
        """
        Iterate through immediate children, making a node from each
        In the process of making a node, this function is called, so the tree is
        parsed depth first. IDs are added later, by a Visitor, so that IDs are breadth
        first.
        """
        for child in rawData:
            node.attachChild(child)
            
    
    def _getFileList(self, location):
        """
        Get all files below location
        """
        if not location.endswith('/'): location = location + '/'
        paths = []
        for path in [location + file for file in os.listdir(location)]:
            if path.endswith('CVS'): continue
            if os.path.isdir(path):
                paths.extend(self._getFileList(path))
             
            elif path.endswith('.mrg') or path.endswith('.auto'):
                paths.append(path)
        paths.sort()
        return paths
        
    def _getChildConstructor(self, type):
        return self._childConstructors[type]
        
class DBCorpusConstructor(CorpusConstructor):
    """
    Read in a corpus by connecting to a database
    """
    
    def _getFileList(self, section):
        """
        Get all files below location
        """
        global DSN_PATH
        # Hack for semcor
        if section == 'SEMCOR':
            return open(DATA_PATH + 'semcor/pickled/ptb_intersection.txt').read().split()
        databaseConnection = mx.ODBC.Windows.DriverConnect('FILEDSN=%s' % DSN_PATH)
        cursor = databaseConnection.cursor()
        if not section:
            query = """SELECT PKey
            FROM PTB_Files
            WHERE PKey
            ORDER BY PKey;"""
        else:
            query = """SELECT PKey
            FROM PTB_Files
            WHERE Section='%s'
            ORDER BY PKey;""" % section
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return [r[0] for r in records]
        
        
# ========================================================================================

class ParseError(StandardError):
    pass

def profile():
    import hotshot, hotshot.stats
    prof = hotshot.Profile('/tmp/test.prof')
    prof.runcall(test)
    prof.close()
    stats = hotshot.stats.load('/tmp/test.prof')
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    stats.print_stats(20)

def test():
    import Treebank
    corpus = Treebank.makeCorpus('/home/mhonn/26-0/Data/Treebank3/wsj/')
    s1 = corpus.child(0).child(0)
    print ' '.join([w.text for w in s1.listWords()])
    print type(s1)
    print dir(s1)
    print s1._children
    print s1.label
    print s1._children[0].label
#    for i in xrange(100):
#        c = corpus.child(i)
            
#whitespaceStripRE = re.compile(r'\s+')

if __name__ == '__main__':
#    profile()
    test()

