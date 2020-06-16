import re
from collections import defaultdict
import data
import CCG
from rebanking.rebankers import Rebanker
from Treebank import CCGbank
from nltk.stem import WordNetLemmatizer
from copy import deepcopy as dcopy
from _stagToPos import stagToPos

morphy = WordNetLemmatizer().lemmatize    
inflectTable = {
            'VBD': ('-ed', 'VID'),
            'VBP': ('-es', 'VIP'),
            'VBZ': ('-es', 'VIZ'),
            'VBG': ('-ing', 'VIG'),
            'VBN': ('-ed', 'VIN')
        }
features = set(['[dcl]', '[ng]', '[pss]', '[pt]'])
featTable = {'pss': 'VBN', 'ng': 'VBG', 'pt': 'VBD'}
#catMap = [
#            (r'S[b]\NP', r'(S[%s]\NP)\(S[b]\NP)'),
#            (r'S[b]/NP', r'(S[%s]/NP)\(S[b]/NP)')]

class POSRelabeller(Rebanker):
    """
    Relabel part-of-speech tags for non-S verbs
    """
    def match(self, verb):
        verb = verb.child(0)
        if not verb.isLeaf():
            return False
        if verb.pos in ['AUX', 'MD']:
            return False
        if self._isVerb(verb) == (verb.pos in inflectTable):
            return False
        return True

    def _isVerb(self, verb):
        # Allow N/N as a verb for publishing|VBG|N/N case
        if verb.stag == 'N/N' and verb.pos.startswith('V'):
            return True
        elif verb.stag.innerResult().feature in features:
            return True
        else:
            return False

    def change(self, verb):
        verb = verb.child(0)
        if self._isVerb(verb):
            feat = verb.stag.innerResult().feature
            if feat in featTable:
                pos = featTable[feat]
            # Dispatch dcl via pos and text
            elif verb.pos == 'VB':
                pos = 'VBP'
            elif verb.text.lower().endswith('ed'):
                pos = 'VBD'
            elif verb.text.lower().endswith('s'):
                pos = 'VBZ'
            else:
                pos = 'VBD'
        else:
            # Use the most common non-verb pos tag for the stag
            pos = stagToPos.get(str(verb.stag), 'NN')
        verb.label = pos
        verb.pos = pos


        

class VerbInflection(Rebanker):
    def match(self, verb):
        stag = verb.label
        verb = verb.child(0)
        if not verb.isLeaf():
            return False
        if verb.pos not in inflectTable:
            return False
        if verb.pos.startswith('VI'):
            return False
        nextWord = verb.nextWord()
        if nextWord and nextWord.pos.startswith('VI'):
            return False
        return True
        

    def change(self, verbParent):
        feature = verbParent.label.innerResult().feature[1:-1]
        verb = verbParent.child(0)
        pos = verb.pos
        verbCat = self._getVerbCat(verbParent.label, feature)
        self.updateVerb(verb, CCG.Category(verbCat.morphLess()))
        inflectCat = self._getInflectCat(verbCat, feature)
        inflectNode = self._makeInflectNode(pos, inflectCat, verb.wordID)
        verbParent.attachChild(inflectNode, 1)
        for i, word in enumerate(verbParent.root().listWords()):
            word.wordID = i

    def updateVerb(self, verb, verbCat):
        newNode = CCGbank.CCGNode(label=verbCat, headIdx=0)
        verb.insert(newNode)
        lemma = morphy(verb.text.lower(), pos='v')
        if verb.text.istitle():
            lemma = lemma.title()
        verb.text = lemma if lemma else verb.text
        verb.parg = verbCat
        #verb.pos = 'VB'
        #verb.label = 'VB'

    def _getVerbCat(self, oldCat, feature):
        newCat = CCG.Category(oldCat)
        newCat.innerResult().feature = '[b]'
        return newCat
        
    def _getInflectCat(self, verbCat, feature):
        cats = list(verbCat.deconstruct())
        cats.insert(0, (verbCat, None, None, None))
        slashDir = None
        for result, argument, slash, hat in cats:
            #for before, after in catMap:
            #    if CCG.isIdentical(result, before):
            #        return CCG.Category(after % feature)
            if result == 'S' and argument == 'NP' and slash == '\\':
                slashDir = '/'
            if hat or (slashDir and slash and slash != slashDir):
                result = CCG.addArg(result, argument, slash)
                result.morph = hat
                result.innerResult().feature = '[%s]' % feature
                # Eliminate [expr] etc feats from the inflect cat
                if not result.argument.isComplex():
                    result.argument.feature = ''
                arg = CCG.Category(result.morphLess())
                arg.innerResult().feature = '[b]'
                return CCG.addArg(result, arg, '\\')
            slashDir = slash
        else:
            if result == 'S':
                result.feature = '[%s]' % feature
            category = CCG.addArg(result, 'S[b]', '\\')
            category.morph = hat
            return category
        
    
    def _makeInflectNode(self, pos, inflectCat, wordID):
        name, pos = inflectTable[pos]
        node = CCGbank.CCGNode(label=inflectCat, headIdx=0)
        leaf = CCGbank.CCGLeaf(text=name, label=pos, pos=pos, parg=inflectCat,
                               wordID=wordID + 0.5)
        node.attachChild(leaf)
        return node

class AgentivePassive(VerbInflection):
    def match(self, verb):
        if not VerbInflection.match(self, verb.head().parent()):
            return False
        if verb.label.innerResult().feature != '[pss]':
            return False
        sibling = verb.sibling()
        if not sibling:
            return False
        if sibling.head().text.lower() != 'by':
            return False
        return True

    def change(self, passive):
        # Ensure agent is a complement, not an adjunct
        agent = passive.sibling()
        if agent.label.isAdjunct():
            agent.changeLabel(CCG.Category('PP'))
            passive.changeLabel(CCG.addArg(passive.label, 'PP', '/'))
        elif agent.label != 'PP':
            agent.changeLabel(CCG.Category('PP'))
            passive.changeLabel(CCG.addArg(passive.label.result, 'PP', '/'))
        else:
            print passive
        verb = passive.head().parent()
        verbCat = self._makePassiveVerb(verb.label, passive.label)
        # Do standard inflect change
        VerbInflection.change(self, passive.head().parent())
        # Now change the verb's PP to an NP (for canonical active category)
        verb = passive.head().parent()
        inflect = verb.sibling()
        verb.changeLabel(verbCat)
        inflectCat = self._makePassiveInflect(verbCat, True)
        inflect.changeLabel(inflectCat)

    def _makePassiveInflect(self, verbCat, agentive):
        hasTVb = any(r for r, a, s, h in verbCat.deconstruct() if r == r'(S[b]\NP)/NP')
        if not hasTVb and verbCat != r'(S[b]\NP)/NP':
            if agentive:
                inflectResult = CCG.addArg(verbCat.result, 'PP', '/')
            else:
                inflectResult = CCG.Category(str(verbCat.result))
            inflectResult.innerResult().feature = '[pss]'
            inflectArg = CCG.Category(str(verbCat))
            inflectArg.innerResult().feature = '[b]'
            return CCG.addArg(inflectResult, inflectArg, '\\')
        elif agentive:
            return CCG.Category(r'((S[pss]\NP)/PP)\((S[b]\NP)/NP)')
        else:
            return CCG.Category(r'(S[pss]\NP)\((S[b]\NP)/NP)')
            
    def _makePassiveVerb(self, verbLabel, parentLabel):
        args = []
        if verbLabel != parentLabel:
            for result, argument, slash, hat in verbLabel.deconstruct():
                args.append((argument, slash, None))
                if result == parentLabel:
                    break
            else:
                raise StandardError
        args.insert(0, (CCG.NP, '/', None))
        cat = CCG.addArgs(parentLabel.result, args)
        cat.innerResult().feature = '[b]'
        return cat

##    def _addVerbArgument(self, verbBase, removePP):
##        if verbBase == 'S[b]\NP':
##            return CCG.addArg(verbBase, CCG.NP, '/')
##        elif verbBase == 'S[b]':
##            # wsj_1003.14. No good solution
##            return CCG.Category(r'S[b]/NP')
##        outerArgs = []
##        # Insert the NP next to the S[b]\NP
##        for result, arg, slash, hat in verbBase.deconstruct():
##            outerArgs.insert(0, (arg, slash, hat))
##            if result == r'S[b]\NP' or result.slash == '\\':
##                break
##        # If agentive, remove the PP argument for the by agent
##        if removePP:
##            outerArgs.pop(0)
##        outerArgs.insert(0, (CCG.NP, '/', None))
##        return CCG.addArgs(result, outerArgs)

class AgentlessPassive(AgentivePassive):
    def match(self, verb):
        if not VerbInflection.match(self, verb):
            return False
        if verb.label.innerResult().feature != '[pss]':
            return False
        return True

    def change(self, verb):
        # Do standard inflect change
        word = verb.child(0)
        VerbInflection.change(self, verb)
        verb = word.parent()
        # Now add the NP argument to match canonical active
        verbCat = CCG.addArg(verb.label, 'NP', '/')
        verb.changeLabel(verbCat)
        # And make the agent perform the NP-->null coercion
        inflect = verb.sibling()
        inflectCat = self._makePassiveInflect(verbCat, False)
        inflect.changeLabel(inflectCat)
        #inflectResult = inflect.label.result
        #inflectArg = CCG.addArg(inflect.label.argument, 'NP', '/')
        #inflect.changeLabel(CCG.addArg(inflectResult, inflectArg, '\\'))
        
        
                               
class NonSInflection(VerbInflection):
    """
    Handle inflection for words that don't have supertags starting in
    S[dcl|ng|pt|b]
    """
    labels = defaultdict(int)
    def match(self, verb):
        verb = verb.child(0)
        if not verb.isLeaf():
            return False
        if verb.pos not in inflectTable:
            return False
        if verb.stag.innerResult() == 'S' and \
            verb.stag.innerResult().feature in features:
            return False
        #if verb.stag != 'N/N':
        #    return False
        nextWord = verb.nextWord()
        if nextWord and nextWord.pos.startswith('VI'):
            return 
        return True

    def change(self, verbParent):
        verb = verbParent.child(0)
        pos = verb.pos
        self.updateVerb(verb, verb.stag)
        inflectNode = self._makeInflectNode(pos, CCG.Category(r','), verb.wordID)
        verbParent.attachChild(inflectNode, 1)
        for i, word in enumerate(verbParent.root().listWords()):
            word.wordID = i
        #if verbParent.label.argument == 'NP' and verbParent.label.slash == '/':
        #    self.updateVerb(verb, CCG.Category(r'(S[b]\NP)/NP'))
        #    inflectCat = CCG.addArg(verbParent.label.result, CCG.Category(r'S[b]\NP'), '\\')
        #else:
        #    self.updateVerb(verb, CCG.Category(r'S[b]\NP'))
        #    inflectCat = CCG.addArg(verbParent.label, CCG.Category(r'S[b]\NP'), '\\')
        #inflectNode = self._makeInflectNode(pos, inflectCat, verb.wordID)
        #verbParent.attachChild(inflectNode, 1)
        #for i, word in enumerate(verbParent.root().listWords()):
        #    word.wordID = i
