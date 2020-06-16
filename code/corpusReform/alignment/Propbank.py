"""
Because the prop.txt file references Treebank nodes, not just leaves, there are
two ways to do this. First, simply rewrite the file with the set of leaf indices
predicate or argument spans in CCGBank. Second, find the smallest set of nodes
that cover those leaves and only those leaves. For instance, if two nodes have
a common parent, use that instead of the two leaves.
"""
from os.path import join as pjoin
import os, re
import xml.dom.minidom
import Treebank

class PropBank:
    def __init__(self, propbankDir):
        """
        Doesn't use the verb lexicon atm. Each entry contains references
        to the node objects, rather than addresses
        """
        fileLoc = pjoin(propbankDir, 'data', 'prop.txt')
        linesByFile = {}
        # Index by path so that we don't have to build files multiple times
        for line in open(fileLoc):
            if not line.strip(): continue
            path = line.split()[0].split('/')[-1]
            linesByFile.setdefault(path, []).append(line)
        self.fileNames = linesByFile.keys()
        self.fileNames.sort()
        self._fileIndex = linesByFile
        self._readLexicon(propbankDir)


    def _readLexicon(self, propbankDir):
        """
        Read the lexicon
        """
        print "Reading lexicon"
        path = pjoin(propbankDir, 'data', 'frames')
        files = os.listdir(path)
        lexicon = {}
        files.sort()
        for f in files:
            if not f.endswith('.xml'): continue
            DOM = xml.dom.minidom.parse(pjoin(path, f))
            predNode = DOM.getElementsByTagName('predicate')[0]
            verbFrame = PredicateDefinition(predNode)
            lexicon[verbFrame.lemma] = verbFrame
        self.lexicon = verbFrame
    
    def fileEntries(self, corpusFile):
        lines = self._fileIndex.get(corpusFile.ID, [])
        entries = {}
        for line in lines:
            entry = PredArgStructure(line, corpusFile)
            entries.setdefault(entry.sentence, []).append(entry)
        return entries



###########################
# Classes for the lexicon #
###########################

class PredicateDefinition:
    """
    A list of possible frames for a given verb
    
    Fields:
        - roleSets (list of RoleSetDefinitions)
        - lemma (open string)
        - notes (list of open strings)
    """
    def __init__(self, predicate):
        self.roleSets = []
        self.lemma = ''
        self.note = ''
        self.lemma = predicate.getAttribute('lemma')
        noteNodes = [c for c in predicate.childNodes if c.nodeName == 'note']
        note = []
        for noteNode in noteNodes:
            # Normalise merges adjacent text nodes, ensuring that all of the text is retreived
            noteNode.normalize()
            note.append(re.sub('\s+', ' ', noteNode.firstChild.data).strip())
        self.note = ''.join(note)
        self.roleSets = []
        roleSetNodes = [c for c in predicate.childNodes if c.nodeName == 'roleset']
        for roleSetNode in roleSetNodes:
            self.roleSets.append(RoleSet(roleSetNode))              
        
    def __str__(self):
        return '\n\n\n'.join([str(rs) for rs in self.roleSets])



class RoleSet:
    """
    PropBank `Frame' -- a configuration of Participant Roles
    
    Fields:
        - ID (regular string of the form \w+\.\d+)
        - name (open string)
        - verbnetClass (regular string of the form \d+(?:\.\d+)*)
        - roles (list of RoleDefinitions)
        - examples (RoleSetExample)
    """
    def __init__(self, roleSetDOM):
        # Get ID, name and verbnetClass from attributes
        for attName, xmlName in [('ID', 'id'), ('name', 'name'), ('verbnetClass', 'vnclass')]:
            setattr(self, attName, roleSetDOM.getAttribute(xmlName))
        # Get roles
        self.roles = []
        for roleNode in roleSetDOM.getElementsByTagName('role'):
            self.roles.append(RoleDefinition(roleNode))
        examples = [c for c in roleSetDOM.childNodes if c.nodeName == 'example']
        self.examples = []
        for egNode in examples:
            self.examples.append(RoleSetExample(egNode))

        
    def __str__(self):
        lines = ['Frame: %s' % self.name]
        lines.append('')
        for rd in self.roles:
            lines.append(str(rd))
        lines.append('')
        lines.append('Examples:')
        lines.append('')
        for eg in self.examples:
            lines.append(str(eg))
            lines.append('------')
        return '\n'.join(lines)
    

class RoleDefinition:
    """
    PropBank Role
    
    Fields:
        - desc (open string)
        - number (semi-open string)
        - verbnetRole (Dictionary)
          Dictionary may be empty, or may have both:
            - class (regular string of the form: \d+(?:\.\d+)*)
            - theta (ennumerable string:
              Actor1 | Actor2 | Agent | Asset | Attribute| Beneficiary| Cause |
              Destination | Experiencer | Extent| Instrument | Location | Material |
              Patient | Patient1 | Patient2 | Predicate | Product | Recipient |
              Source | Stimulus | Theme | Theme1 | Theme2 | Time | Topic)
    """
    def __init__(self, roleDOM):
        self.number = roleDOM.getAttribute('n')
        self.desc = roleDOM.getAttribute('descr')
        verbnetRole = roleDOM.getElementsByTagName('vnrole')
        VNRole = {}
        if verbnetRole:
            VNRole['class'] = verbnetRole[0].getAttribute('vncls')
            VNRole['theta'] = verbnetRole[0].getAttribute('vntheta')
        self.verbnetRole = VNRole

        
    def __str__(self):
        return self.number + ': ' + self.desc


    
class RoleSetExample:
    """
    An annotated text example of a verb frame -- a configuration of Participant Roles.
    
    Fields:
        - name (open string)
        - inflection (Dictionary:
            Key     Value
            person  ennumerable string: (third | other | ns)
            tense   ennumerable string: (present | past | future | ns)
            aspect  ennumerable string: (perfect | progressive | both | ns)
            voice   ennumerable string: (active | passive | ns)
            form    ennumerable string: (infinitive | gerund | participle | full | ns)
        - roles (list of RoleExamples)
    """
    def __init__(self, exampleDOM):
        self.name = exampleDOM.getAttribute('name')
        self.inflection = self._parseInflection(exampleDOM)
        textNodes = exampleDOM.getElementsByTagName('text')
        assert len(textNodes) == 1
        textNodes[0].normalize()
        self.text = textNodes[0].firstChild.data
        self.roles = []
        for child in exampleDOM.childNodes:
            if child.nodeName == 'arg':
                self.roles.append(RoleExample(child))
            elif child.nodeName == 'rel':
                self.roles.append(RoleExample(child))

    def _parseInflection(self, exampleDOM):
        inflection = {}
        node = [c for c in exampleDOM.childNodes if c.nodeName == 'inflection']
        if not node:
            return inflection
        else:
            for attr in ['aspect', 'form', 'person', 'tense', 'voice']:
                inflection[attr] = node[0].getAttribute(attr)
            return inflection
        
    def __str__(self):
        return '\n'.join([str(r) for r in self.roles])
    

    
class RoleExample:
    """
    An argument or predicate in a RoleSetExample
    
    Fields:
        - text (open string)
        - function (frames.dtd says: ``a rel can have an "f" attribute for a single reason, so that
         auxilliary uses of the verb "have" can be marked as such.
         There should be no other "f" attributes.''
    """
    def __init__(self, DOM):
        DOM.normalize()
        # In imperatives etc, role may be 'unrealised'
        if DOM.firstChild:
            self.text = DOM.firstChild.data
        else:
            self.text = ''
        self.number = DOM.getAttribute('n')
        self.function = DOM.getAttribute('f')
        if DOM.nodeName == 'rel':
            self.isPred = True
        else:
            self.isPred = False

        
    def __str__(self):
        return self.text

######################################
# Classes for the Predicate-Argument #
# structure annotated data           #
######################################

class PredArgStructure:
    def __init__(self, line, ptbFile):
        pieces = line.strip().split()
        self.path = pieces[0]
        sentIdx = int(pieces[1])
        sentence = ptbFile.child(sentIdx)
        self.sentence = sentence
        self.sentIdx = sentIdx
        relIdx = int(pieces[2])
        rel = sentence.getWord(relIdx)
        self.relIdx = relIdx
        assert rel.label[0] == 'V'
        self.gold = pieces[3]
        self.frame = pieces[4]
        self.morph = pieces[5]
        pargs = []
        for parg in pieces[6:]:
            pargs.append(PredOrArg(line, parg, sentence))
        self.pargs = pargs



        

    def __str__(self):
        pieces = [self.path, self.sentIdx, self.relIdx, self.gold, self.frame, self.morph] + self.pargs
        return ' '.join([str(p) for p in pieces])

class PredOrArg:
    def __init__(self, line, text, sentence):
        self.line = line
        columns = text.split('-')
        if len(columns) == 3:
            relation, label, feature = columns
        else:
            relation, label = columns
            feature = None
        self.refChain = ReferenceChain(relation, sentence)
        self.label = label
        self.feature = feature


    def __str__(self):
        if self.feature:
            return '%s-%s-%s' % (self.refChain, self.label, self.feature)
        else:
            return '%s-%s' % (self.refChain, self.label)

        
        

class ReferenceChain(list):
    """
    Set of nodes that together constitute an argument for a PredArg structure
    """
    def __init__(self, relationStr, sentence):
        refChain = relationStr.split('*')
        nodeSets = []
        for ref in refChain:
            self.append(NodeSet(ref, sentence))
            

    def __str__(self):
        """
        Print addresses in identical format to propbank
        """
        return '*'.join([str(nodeSet) for nodeSet in self])

    def contentNodes(self):
        # First look for content nodes
        contentNodes = [n for n in self if n.type() == 'Content']
        if not contentNodes:
            return [n for n in self if n.type() == 'WH']
        else:
            return contentNodes
                



class NodeSet(list):
    """
    Set of nodes that together reference an argument within a reference chain
    """
    def __init__(self, addressStr, sentence):
        addresses = addressStr.split(',')
        for address in addresses:
            constituent = self._getConstituent(address, sentence)
            self.append(constituent)


    def _getConstituent(self, address, sentence):
        tokIdx, height = address.split(':')
        constituent = sentence.getWord(int(tokIdx))
        height = int(height)
        while height:
            constituent = constituent.parent()
            height -= 1
        return constituent

    def __str__(self):
        return ','.join([self._nodeAddress(node) for node in self])
    

    def _nodeAddress(self, node):
        """
        Find the ID of the first word in the node, and the height of the node
        from that word
        """
        height = 0
        while not node.isLeaf():
            height += 1
            node = node.child(0)
        lexNum = node.sentIdx
        return '%d:%d' % (lexNum, height)

    def type(self):
        if len(self) > 1:
            return 'Content'
        seenWH = False
        for word in self[0].listWords():
            if word.label.startswith('W'):
                seenWH = True
            elif word.label != '-NONE-':
                return 'Content'
        if seenWH:
            return 'WH'
        else:
            return 'Trace'

    def words(self):
        for node in self:
            for word in node.listWords():
                yield word
        
        
        
PTB_PATH = '/home/mhonn/Data/Treebank3_wsj'
if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    ptb = Treebank.makeCorpus(PTB_PATH)
    propbankLoc = '/home/mhonn/Data/propbank_1'
    propbank = PropBank(propbankLoc)
    propbankLines = open(pjoin(propbankLoc, 'data', 'prop.txt')).read().strip().split('\n')
    i = 0
    for ptbFile in ptb.children():
        entries = propbank.fileEntries(ptbFile)
        sentences = entries.keys()
        sentences.sort()
        for sentence in sentences:
            for entry in entries[sentence]:
                propbankLine = propbankLines[i]
                i += 1
                if str(entry) != propbankLine:
                    print entry
                    print propbankLine
                    print sentence
                    raise StandardError
   # propbank = []
   # for line in open('/home/mhonn/Data/propbank_1/data/prop.txt'):
   #     propbank.append(PropBankEntry(line))
    
        
