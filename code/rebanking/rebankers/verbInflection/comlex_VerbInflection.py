import re
from collections import defaultdict
import os
from copy import deepcopy as dcopy

import data
import CCG
import pickles
from rebanking.rebankers import Rebanker
from Treebank import CCGbank
from nltk.stem import WordNetLemmatizer
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

class ComlexPOSRelabeller(Rebanker):
    """
    Relabel part-of-speech tags for non-S verbs
    """
    verbLemmas = pickles.load('comlex_verbs')
    nounLemmas = pickles.load('comlex_nouns')
    suffixes = {'ed': 'VBD', 'en': 'VBN', 'ing': 'VBG'}
    morphs = {}
    # All words in CCGbank fed into Minnen and Carrol's morpha
    # with _V tags. i.e. their morphological analysis as though they're
    # verbs
    for line in open(os.path.dirname(__file__) + '/words_to_verb_morphs'):
        word, morph = line.strip().split()
        morphs[word] = morph.split('+')
        
    def match(self, verb):
        verb = verb.child(0)
        if not verb.isLeaf():
            return False
        if verb.pos == 'NNS' or verb.text in self.nounLemmas:
            return False
        if verb.text not in self.morphs:
            return False
        if verb.pos in self.suffixes.values():
            return False
        lemma, inflect = self.morphs[verb.text]
        # If lemma not recognised as a verb in COMLEX, don't relabel
        if lemma not in self.verbLemmas:
            return False
        if inflect not in self.suffixes:
            return False
        return True
        #if verb.pos in ['AUX', 'MD']:
        #    return False
        #if self._isVerb(verb) == (verb.pos in inflectTable):
        #    return False:0
        #return True

    def change(self, verb):
        verb = verb.child(0)
        lemma, inflect = self.morphs[verb.text]
        verb.pos = self.suffixes[inflect]
        verb.label = self.suffixes[inflect]


class POSRelabeller(Rebanker):
    # Handle false negatives for verbs
    def match(self, verb):
        verb = verb.child(0)
        if not verb.isLeaf():
            return False
        if verb.pos in ['AUX', 'MD']:
            return False
        # Hack for specific noise cases
        if verb.text.lower() == 'so':
            return False
        if not self._isVerb(verb) or (verb.pos in inflectTable):
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
        print '%s --> %s' % (str(verb), pos)
        verb.label = pos
        verb.pos = pos


class AdjunctUnariser(Rebanker):
    def match(self, adjunct):
        """
        Introduce unary rules for verbs like
        "including" that are currently tagged as
        ((S\NP)\(S\NP))/NP etc directly
        """
        if not adjunct.label.isAdjunct():
            return False
        verb = adjunct.head()
        if not verb.stag.adjunctResult():
            return False
        if not verb.pos.startswith('V'):
            return False
        return True

    def change(self, adjunct):
        verb = adjunct.head()
        if verb.label == 'VBG':
            category = CCG.Category(r'S[ng]\NP')
        elif verb.label == 'VBN':
            category = CCG.Category(r'S[pss]\NP')
        else:
            category = CCG.Category(r'S[dcl]\NP')
        node = CCGbank.CCGNode(label=adjunct.label, headIdx=0)
        adjunct.insert(node)
        adjunct.changeLabel(category)

        

class VerbInflection(Rebanker):
    def match(self, verb):
        stag = verb.label
        verb = verb.child(0)
        if not verb.isLeaf():
            return False
        if not verb.pos.startswith('V'):
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
        if verb.stag.innerResult() != 'S':
            verbCat = CCG.Category(r'S[b]\NP')
            inflectCat = CCG.addArg(verb.stag, verbCat, '\\')
            self.updateVerb(verb, CCG.Category(verbCat.morphLess()))
        else:
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
                result.innerResult().feature = '[%s]' % feature if feature else ''
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

class NounPluralInflection(VerbInflection):
    """
    Add a suffix for NNS plural nouns that adds a [pl] feature.
    Where possible, the suffix should be N\N[pl] or NP\NP[pl].
    However, all crossing composition is banned for nouns, so
    argument structures cannot be abstracted. e.g.
    fact|N/S[em] -s|(N[pl]/S)\(N/S)
    """
    def match(self, noun):
        noun = noun.child(0)
        if not noun.isLeaf():
            return False
        if noun.pos != 'NNS':
            return False
        nextWord = noun.nextWord()
        if nextWord and nextWord.pos.startswith('NI'):
            return False
        return True

    def change(self, nounParent):
        noun = nounParent.child(0)
        self.updateNoun(noun, CCG.Category(noun.stag.morphLess()))
        nounParent.label.innerResult().feature = '[pl]'
        inflectCat = CCG.addArg(nounParent.label, noun.stag.morphLess(), '\\')
        
        inflectCat.innerResult().feature = '[pl]'
        inflectNode = self._makeInflectNode('NNS', inflectCat, noun.wordID)
        nounParent.attachChild(inflectNode, 1)
        for i, word in enumerate(nounParent.root().listWords()):
            word.wordID = i

    def updateNoun(self, noun, nounCat):
        newNode = CCGbank.CCGNode(label=nounCat, headIdx=0)
        noun.insert(newNode)
        lemma = morphy(noun.text.lower(), pos='n')
        if noun.text.istitle():
            lemma = lemma.title()
        noun.text = lemma if lemma else noun.text
        noun.parg = CCG.Category(nounCat)
        #verb.pos = 'VB'
        #verb.label = 'VB'

    def _makeInflectNode(self, pos, inflectCat, wordID):
        name, pos = '-s', 'NIN'
        node = CCGbank.CCGNode(label=inflectCat, headIdx=0)
        leaf = CCGbank.CCGLeaf(text=name, label=pos, pos=pos, parg=inflectCat,
                               wordID=wordID + 0.5)
        node.attachChild(leaf)
        return node
                               
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
        if not verb.pos.startswith('V'):
            return False
        if verb.pos not in inflectTable:
            return False
        if verb.stag != 'N/N':
            return False
        nextWord = verb.nextWord()
        if nextWord and nextWord.pos.startswith('VI'):
            return 
        return True

    def change(self, verbParent):
        verb = verbParent.child(0)
        pos = verb.pos
        self.updateVerb(verb, CCG.Category(r'S[b]\NP'))
        inflectCat = CCG.Category(r'(N/N)\(S[b]\NP)')
        inflectNode = self._makeInflectNode(pos, inflectCat, verb.wordID)
        verbParent.attachChild(inflectNode, 1)
        for i, word in enumerate(verbParent.root().listWords()):
            word.wordID = i
