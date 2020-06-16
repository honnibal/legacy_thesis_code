"""
Interface for the .auto format of CCGBank derivations
"""
from Treebank.TreeConstructors import *
from CCGNodes import *
from Treebank.NodeVisitors import NodePrinter
import CCG
class AutoFileConstructor(FileConstructor):
    _leafClass = CCGRoot
    _rootClass = CCGCorpusFile
    
    def _incrementCount(self, count = [0]):
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class AutoFileConstructor instantiated"
        
    def _parseChildren(self, node, rawData, childConstructor):
        lines = rawData.strip().split('\n')
        while lines:
            line = lines.pop(0)
            if not line:
                continue
            ID = line.split()[0][3:]
            parse = lines.pop(0)
            sentence = childConstructor.make(parse, self._leafClass)
            sentence.globalID = ID
            sentence.addWordIDs()
            node.attachChild(sentence)

    def _getChildConstructor(self, location):
        return self._childConstructors['ccg']
        
    def _preprocessText(self, text):
        return text

class CCGBankNodeConstructor(SentenceConstructor):
    # What to construct
    _rootClass = CCGRoot
    _internalClass = CCGInternal
    _leafClass = CCGLeaf
    _wordID = 0
    _globalID = 0
    def _incrementCount(self, count = [0]):
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class CCGBankNodeConstructor instantiated"

    def make(self, rawData, nodeClass):
        """
        Instantiate a node
        """
        settings = self._getSettings(rawData)
        if nodeClass is self._leafClass:
            try:
                stag = settings.pop('stag')
            except:
                print rawData
                raise
            parentSettings = {}
            parentSettings.update(settings)
            parentSettings.pop('pos')
            parentSettings.pop('text')
            parentSettings['label'] = CCG.Category(stag)
            parentSettings['headIdx'] = 0
            lexNode = nodeClass(settings)
            parentNode = self._internalClass(parentSettings)
            parentNode.attachChild(lexNode)
            parentNode.setup()
            lexNode.setup()
            return parentNode
        else:
            node = nodeClass(settings)
            self._parseChildren(node, rawData)
            node.setup()
            return node
    
    def isLeaf(self, bracket):
        if bracket.startswith('<T'):
            return False
        else:
            return True        

        
    def _getSettings(self, bracket):
        settings = {'metadata': {}, '_parent': None, '_children': None}
        desc, rest = bracket.split('>', 1)
        desc = desc.split()
        if desc[0] == '<L':
            # this gets popped off, and isn't a property anymore
            settings['stag'] = desc[1]
            # Hack for incorrectly written propmod
            settings['pos'] = desc[2]
            settings['label'] = desc[3]
            settings['text'] = desc[4]
            # Predicate-argument category
            # Ignore the parg field for incorrectly written morph
            # May cause problems
            settings['parg'] = CCG.Category(settings['stag'])
            assert settings['parg']
            CCGBankNodeConstructor._wordID += 1
            settings['wordID'] = CCGBankNodeConstructor._wordID
        # In some cases, the lexical category is the only thing
        # In these cases you'll get (<L, not <L
        elif desc[0] == '(<L':
            settings['label'] = CCG.Category(desc[1])
            settings['headIdx'] = 0
        else:
            settings['label'] = CCG.Category(desc[1])
            settings['headIdx'] = int(desc[2])
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
            # Don't consider brackets within angled as children
            elif char == '<':
                depth += 1
            # Don't make the angled children either
            elif char == '>':
                depth -= 1
            # Decrease depth
            elif char == ')':
                depth -= 1
                # Yield bracket when depth 0
                if depth == 0:
                    yield self._getChild(text, start, i)
            


    def _getChild(self, text, start, end):
        return text[start+1:end]



class CCGFlatFileConstructor(FlatFileConstructor):
    _rootClass = CCGCorpusFile
    def make(self, location, nodeClass):
        settings = self._getSettings(location)
        fileNode = self._rootClass(settings)
        nodes = {fileNode.ID: fileNode}
        childConstructor = self._childConstructors['ccg']
        for nodeText in open(location):
            if not nodeText.strip(): continue
            headIdx, nodeClass, data = nodeText.split('**')
            if headIdx.isdigit():
                headIdx = int(headIdx)
            data = data.strip()
            nodeClass = eval(nodeClass)
            node = childConstructor.make(data, nodeClass)
            head = nodes[headIdx]
            head.attachChild(node)
            nodes[node.globalID] = node
        return fileNode

class CCGFlatSentenceConstructor(FlatSentenceConstructor):
    def _incrementCount(self, count = [0]):
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class FlatCCGConstructor instantiated"


    

    def _getSettings(self, data):
        pieces = data.split('\t')
        leafLabels = ['globalID', 'pos', 'label', 'text', 'parg', 'wordID', 'sentIdx']
        internalLabels = ['globalID', 'label', 'headIdx']
        settings = {'metadata': {}, '_parent': None, '_children': []}
        globalID = pieces[0]
        if globalID.isdigit():
            globalID = int(globalID)
        settings['globalID'] = globalID
        if len(pieces) == len(leafLabels):
            settings['pos'] = pieces[1]
            settings['label'] = pieces[2]
            settings['text'] = pieces[3]
            settings['parg'] = CCG.Category(pieces[4])
            settings['wordID'] = int(pieces[5])
            settings['sentIdx'] = int(pieces[6])
        elif len(pieces) == len(internalLabels):
            settings['label'] = CCG.Category(pieces[1])
            settings['headIdx'] = int(pieces[2])
        return settings
        
class CCGCorpusConstructor(CorpusConstructor):
    _leafClass = CCGCorpusFile
    def _incrementCount(self, count = [0]):
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class AutoFileConstructor instantiated"

if __name__ == '__main__':

    text = '(<T S[dcl] 0 2> (<T S[dcl] 1 2> (<L NP PRP PRP It NP>) (<T S[dcl]\NP 0 2> (<L (S[dcl]\NP)/NP VBZ VBZ has (S[dcl]\NP_82)/NP_83>) (<T NP 0 2> (<T NP 1 2> (<L NP[nb]/N DT DT no NP[nb]_90/N_90>) (<L N NN NN bearing N>) ) (<T NP\NP 0 2> (<L (NP\NP)/NP IN IN on (NP_98\NP_98)/NP_99>) (<T NP 0 2> (<T NP 1 2> (<L NP[nb]/N PRP$ PRP$ our NP[nb]_113/N_113>) (<T N 1 2> (<L N/N NN NN work N_108/N_108>) (<L N NN NN force N>) ) ) (<L NP\NP NN NN today NP_120\NP_120>) ) ) ) ) ) (<L . . . . .>))'
    sConst = CCGBankNodeConstructor()
    fConst = AutoFileConstructor()
    fConst.addChildConstructors({'ccg': sConst})
    f = fConst.make('/home/mhonn/Data/CCGBank/AUTO/00/wsj_0001.auto', CorpusFile)
    printer = NodePrinter()
    sentence = f.child(0)
    if 0:
        print printer.actOn(sentence)
        for i, w in enumerate(sentence.listWords()):
            print '%d: %s' % (i, w)
    pp = sentence.getWord(11).parent().parent()
    verb = pp.sibling()
    pp.changeLabel(CCG.Category('(S\NP)\(S\NP)'))
#    sibling.changeLabel(sibling.result, np.label, sibling.slash)
#    result, argument, slash = CCG.parseCategory(verb.result)
#    verb.changeLabel(result, argument, slash)
    print printer.actOn(sentence)
            
        
        
        
                
