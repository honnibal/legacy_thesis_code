"""
Get functions directly from the PTB parse
"""
class Clause:
    def __init__(self, pred, parse):
        self.predicator = pred
        constituents = self.getConstituents(pred, parse)
        self.constituents = constituents
        self.interpersonal = Interpersonal(constituents)
        self.textual = Textual(constituents)
        self.experiential = Experiential(constituents)
        self.parse = parse

    def getConstituents(self, predicator, parse):
        """
        Find the "uncles" before hitting a clause node
        """
        args = []
        node = predicator
        traceIdx = self._indexTraces(parse)
        while not node.isRoot() and not self._isClause(node):
            for sibling in node.siblings():
                argType = self._typeArg(sibling)
               # if self._isTrace(sibling):
               #     traceType, target = self._followTrace(sibling, traceIdx)
               #     if not target:
               #         continue
               #     # We may need more nuanced rules, depending on the trace type
               #     # but for now, just use the target as an argument
               #     if traceType not in ['*T*']:
               #         argType = self._typeArg(target)
               #         sibling = (sibling, target, argType)
               #     else:
               #         continue
                args.append((sibling, argType))
            node = node.parent()
        for sibling in node.siblings():
            if sibling.label in ['CC', 'CS']:
                argType = self._typeArg(sibling)
                args.append((sibling, argType))
        args.append((predicator, 'Pred'))
        args.sort()
        return args

    def _isClause(self, parent):
        if parent.label.startswith('S'):
            if parent.parent().label in ['SBAR', 'SBARQ']:
                return False
            else:
                return True
        elif parent.label == 'RRC':
            return True
        else:
            return False


    _verbTags = {'VP': True, 'AUX': True}
    _nominalTags = {'ADJP': True, 'NP': True, 'NX': True, 'QP': True, 'WHADJP': True, 'WHNP': True, 'UCP': True, 'X': True}
    _prepositionTags = {'PP': True, 'WHPP': True}
    _adverbialTags = {'ADVP': True, 'WHADVP': True, 'ADV': True}
    _particleTags = {'PRT': True}
    _conjunctionTags = {'CONJP': True, 'LST': True, 'NAC': True, 'UH': True}
    _correctionTags = {'@': True, 'EDITED': True, 'TYPO': True, 'RM': True, 'IP': True, 'RS': True}
    _intjTags = {'INTJ': True}
    _clauseTags = {'RRC': True, 'S': True, 'SBAR': True, 'SBARQ': True, 'SINV': True, 'SQ': True, 'PRN': True, 'FRAG': True, 'CODE': True}

    _tagTypes = [
        ('Verb', _verbTags),
        ('Nominal_Group', _nominalTags),
        ('Prepositional_Phrase', _prepositionTags),
        ('Adverial Group', _adverbialTags),
        ('Particle', _particleTags),
        ('Conjunction', _conjunctionTags),
        (None, _correctionTags),
        (None, _intjTags)
    ]

    def _typeArg(self, arg):
        if self._isTrace(arg):
            return 'Trace'
        elif self._isPunct(arg):
            return 'Punct'
        elif arg.isLeaf() and arg.label.startswith('V'):
            return 'Verb'
        elif arg.label in Clause._clauseTags:
            if 'NOM' in arg.functionLabels:
                return 'Nominal_Clause'
            elif 'PRD' in arg.functionLabels:
                return 'Nominal_Clause'
            elif 'TTL' in arg.functionLabels:
                return 'Nominal_Clause'
            else:
                return 'Clause'
        for argType, tags in Clause._tagTypes:
            if arg.label in tags:
                return argType
        return None


    def _indexTraces(self, parse):
        indexes = {}
        for node in parse.depthList():
            if node.identifier:
                assert node.identifier not in indexes
                indexes[node.identifier] = node
        return indexes

    def _followTrace(self, trace, index):
        for word in trace.listWords():
            if word.isTrace() and '-' in word.text:
                traceType, target = word.text.split('-')
                if target in index:
                    return (traceType, index[target])
        return (None, None)
        
        

        
    def _isTrace(self, arg):
        for word in arg.listWords():
            if not word.isTrace():
                return False
        return True

    def _isPunct(self, arg):
        for word in arg.listWords():
            if not word.isPunct():
                return False
        return True

def handleTraces(clause):
    """
    Decide whether to follow or discard traces. PTB has the following trace types:

    1. WH/relative traces   *T*   Follow
    2. 
    """
    # Probably requires reference to original parse?
    if not _isEllipsis(clause):
        pass
    for constituent in clause.constituents:
        if _isTrace(constituent):
            reference = _followTrace(constituent, clause)
            


class Metafunction:
    pass

class Interpersonal(Metafunction):
    def __init__(self, constituents):
        subj = None
        finite = None
        complements = []
        adjuncts = []
        for constituent, cType in constituents:
            if cType == 'Trace':
                continue
                trace, constituent, cType = constituent
            if cType == 'Punct':
                continue
            if cType == 'Pred':
                predicator = constituent
            elif 'SBJ' in constituent.functionLabels:
                assert not subj
                subj = constituent
            elif cType == 'Verb' and not finite:
                finite = constituent
            elif cType == 'Nominal_Group':
                if not constituent.functionLabels:
                    complements.append(constituent)
                elif 'PRD' in constituent.functionLabels:
                    complements.append(constituent)
                else:
                    adjuncts.append(constituent)
            elif cType in {'Adverbial_Group': True, 'Prepositional_Phrase': True, 'Particle': True}:
                adjuncts.append(constituent)
            elif cType in {'Nominal_Group': True, 'Nominal_Clause': True, 'Clause': True}:
                complements.append(constituent)
        self.subject = subj
        self.finite = finite
        self.predicator = predicator
        self.complements = complements
        self.adjuncts = adjuncts

class Textual(Metafunction):
    def __init__(self, constituents):
        topTheme = None
        rheme = []
        intThemes = []
        txtThemes = []
        for constituent, cType in constituents:
            if topTheme:
                rheme.append(constituent)
                continue
            if cType == 'Pred':
                topTheme = constituent
            elif cType == 'Conjunction':
                txtThemes.append(constituent)
            elif cType == 'Adverbial_Group':
                adjType = _typeAdjunct(constituent)
                if adjType == 'Interpersonal':
                    intThemes.append(constituent)
                elif adjType == 'Textual':
                    txtThemes.append(constituent)
                else:
                    topTheme = constituent
                    break
            elif cType == 'Verb':
                intThemes.append(constituent)
            else:
                topTheme = constituent
        self.topicalTheme = topTheme
        self.intpThemes = intThemes
        self.txtThemes = txtThemes


class Experiential(Metafunction):
    def __init__(self, constituents):
        process = None
        particles = []
        participants = []
        circumstances = []
        for constituent, cType in constituents:
            if cType == 'Process':
                process = constituent
            elif cType == 'Particle':
                particles.append(constituent)
            elif cType in {'Nominal_Group': True, 'Clause': True, 'Nominal_Clause': True}:
                if 'PRD' in constituent.functionLabels:
                    participants.append(constituent)
                elif 'CLR' in constituent.functionLabels:
                    participants.append(constituent)
                elif constituent.functionLabels:
                    circumstances.append(constituent)
                else:
                    participants.append(constituent)
            elif cType in {'Adverbial_Group': True, 'Prepositional_Phrase': True}:
                circumstances.append(constituent)
        self.process = process
        self.particles = particles
        self.participants = participants
        self.circumstances = circumstances
            


    
            
        

def getPredicators(parse):
    predicators = []
    for node in parse.depthList():
        if node.label == 'VP':
            predicator = _getPredicator(node)
            if predicator:
                predicators.append(predicator)
    return predicators


def _getPredicator(vp):
    for child in vp.children():
        if child.label == 'VP':
            break
    else:
        words = [w for w in vp.children() if _isVerb(w)]
        if words:
            return words[-1]
        
def _isVerb(word):
    if not word.isLeaf():
        return False
    elif word.label.startswith('V'):
        return True
    else:
        return False





import Treebank, Treebank.NodeVisitors
ptb = Treebank.makeCorpus('/home/mhonn/Data/Treebank3_wsj/')
printer = Treebank.NodeVisitors.NodePrinter()
f = ptb.child(2)
s = f.child(17)
preds = getPredicators(s)
print printer.actOn(s)
for p in preds:
    clause = Clause(p, s)
    print 'Subj: %s' % clause.interpersonal.subject
    print 'Finite: %s' % clause.interpersonal.finite
    print 'Pred: %s' % clause.interpersonal.predicator
    for constituent in clause.interpersonal.adjuncts:
        print 'Adj: %s' % constituent
    for constituent in clause.interpersonal.complements:
        print 'Comp: %s' % constituent
    print 'Theme: %s' % clause.textual.topicalTheme
