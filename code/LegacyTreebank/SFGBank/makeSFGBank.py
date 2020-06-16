"""
Convert parses by:

Pre-process traces
Get predicators
Get constituents
"Merge" clauses?
Filter traces
Handle gapping?
"""
import Treebank
from Treebank import Nodes
import NodeVisitors
import ConstituentConstructors, Constituency
from general.Singleton import singleton
import pickles
def preprocessTraces(parse):
    """
    Link traces to targets
    Remove traces with null reference? y
    Remove linked traces? y
    Gapping?
    """
    indexes = {}
    for node in parse.depthList():
        if node.identifier:
            assert node.identifier not in indexes
            indexes[node.identifier] = node
    for word in parse.listWords():
        if word.label == '-NONE-':
            if '-' in word.text:
                reference = word.text.split('-')[1]
                target = indexes[reference]
                tracedNode = Nodes.TracedNode(word, target)
                word.parent().attachChild(tracedNode)
                # Remove linked traces
                word.prune()
            else:
                # Remove traces with null reference
                word.prune()


def followTraces(constituents, traceIndex):
    for node in constituents.keys():
        if len(node.listWords()) > 1:
            continue
        for trace in node.listWords():
            if trace.label != '-NONE-':
                break
            constituents.pop(node)
            if '-' not in trace.text:
                break
            reference = trace.text.split('-')[1]
            target = traceIndex[reference]
            if target.constituent not in constituents:
                tracedNode = Constituency.TracedConstituent(trace, target.constituent)
                constituents[tracedNode] = True
    return constituents
            

def getPredicators(parse):
    """
    Find the first word of a VP node that does not have a VP sibling
    """
    predicators = {}
    for vp in parse.depthList():
        if vp.label == 'VP':
            predicator = getPredicator(vp)
            if predicator:
                predicators[predicator] = True
    predicators = predicators.keys()
    predicators.sort()
    return predicators

def getPredicator(vp):
    leaves = []
    for child in vp.children():
        if child.label == 'VP':
            return getPredicator(child)
        elif child.isLeaf():
            leaves.append(child)
    if leaves:
        return leaves[-1]
    else:
        return None
    

def getConstituents(predicator):
    """
    Set node as predicator
    Get sibling, unless:
        node label is VP and sibling label is VP (ellipsis)
        node label is VP and sibling label is CC and predicator < sibling (ellipsis conjunction)
    If node is a clause, only collect word siblings, and stop. If it's a nominalised clause, don't collect word siblings
    Otherwise, set node as node's parent
    Remove arguments that are referred to by traces we have collected as arguments
    """
    args = {predicator: True}
    node = predicator
    while node.parent():
        if node.isType('Clause'):
            if node.parent().label == 'SBAR':
                for sibling in node.siblings():
                    args[sibling] = True
            elif 'NOM' not in node.functionLabels and 'PRD' not in node.functionLabels:
                for sibling in node.siblings():
                    if sibling.isType('Conjunction_Group') and sibling < predicator:
                        args[sibling] = True
            break
        # For reduced relative clauses
        if node.parent().isType('Nominal_Group'):
            break
        for sibling in node.siblings():
            if node.label == 'VP':
                if sibling.label == 'VP':
                    continue
            if sibling.isType('Conjunction_Group') and predicator < sibling:
                continue
            if sibling.label == 'EDITED':
                continue
            args[sibling] = True
        node = node.parent()
    attachPoint = getAttachPoint(node, args)
    return args, attachPoint


def getAttachPoint(node, args):
    """
    Find the word whose parent we eventually want to attach the clause to
    """
    words = {}
    for arg in args:
        for word in arg.listWords():
            words[word] = True
    while node.parent():
        if not node.isType('Clause') and not node.isType('Verbal_Group'):
            return node
        for sibling in node.siblings():
            if sibling.isType('Lexis') and sibling not in words:
                return sibling
        if node.isType('Clause'):
            for vp in node.children():
                if vp.label == 'VP':
                    predicator = getPredicator(vp)
                    if predicator not in words:
                        return predicator
        elif node.isType('Verbal_Group'):
            predicator = getPredicator(node)
            if predicator not in words:
                return predicator
        node = node.parent()
    return None



def constructClause(constituents, predicator):
    """
    Make a Constituency.Clause object
    """
    constituentConstructor = singleton(ConstituentConstructors.ConstituentConstructor)
    functionLabels, label = getLabels(predicator)
    settings = {'type': 'Clause', 'functionLabels': functionLabels, 'label': label}
    clause = constituentConstructor.make(Constituency.Clause, settings)
    vgSettings = {'type': 'Verbal_Group', 'functionLabels': {}, 'label': 'VP'}
    cjSettings = {'type': 'Conjunction_Group', 'functionLabels': {}, 'label': 'CONJP'}
    vg = constituentConstructor.make(Constituency.VerbalGroup, vgSettings)
    clause.attachChild(vg)
    for node in constituents:
        if node.isType('Clause'):
            # Attach elements of "small clauses" directly (wsj 1.0)
            if not node.verbalGroup():
                for child in node.children():
                    if child.hasWord():
                        child.reattach(clause)
            continue
        elif node.isType('Word'):
            parent = vg
        # Attach verbal group conjunctions to the VP, for VG parataxis (wsj 11.8)
        elif node.isType('Conjunction_Group') and node.parent().isType('Verbal_Group'):
            parent = vg
        else:
            parent = clause
        if node.parent():
            node.reattach(parent)
        else:
            parent.attachChild(node)
    clause.sortChildren()
    return clause


def getClauses(parse):
    preprocess(parse)
    predicators = getPredicators(parse.constituent)
    if not predicators:
        return parse.constituent
    clauses = []
    clauses = []
    seenConstituents = {}
    for pred in predicators:
        constituents, attachPoint = getConstituents(pred)
       # constituents = followTraces(constituents, traceIndex)
        # Check that we haven't allocated a constituent twice
        for c in constituents.keys():
            if c in seenConstituents:
                constituents.pop(c)
#                raise StandardError
            else:
                seenConstituents[c] = True
        clauses.append((pred, constituents, attachPoint))
    clauseObjs = []
    for predicator, constituents, attachPoint in clauses:
        clause = constructClause(constituents, predicator)
        clauseObjs.append((clause, attachPoint))
    sentence = joinClauses(clauseObjs, parse)
    for clause, unused in clauseObjs:
        if clause.parent() and clause.verbalGroup():
            arrangeVG(clause.verbalGroup())
    return sentence


def joinClauses(clauses, parse):
    constructor = singleton(ConstituentConstructors.ConstituentConstructor)
    settings = {'type': 'Clause_Complex', 'label': parse.label, 'functionLabels': list(parse.functionLabels), 'globalID': parse.globalID}
    sentence = constructor.make(Constituency.ClauseComplex, settings)
    for clause, attachPoint in clauses:
        if not attachPoint:
            sentence.attachChild(clause)
        elif not attachPoint.isLeaf():
            attachPoint.attachChild(clause)
            attachPoint.sortChildren()
        else:
            parent = attachPoint.parent()
            if parent.isType('Verbal_Group'):
                parent.clause().attachChild(clause)
               # _attachClauseComplement(parent.clause(), clause)
                parent.clause().sortChildren()
            else:
                parent.attachChild(clause)
                parent.sortChildren()
    pruner = singleton(NodeVisitors.Pruner)
    sentence.performOperation(pruner)
    return sentence

def getLabels(predicator):
    fl = {}
    clause = predicator.clause()
    if clause.label == 'SBAR':
        fl['SBAR'] = True
        if clause.parent().isType('Clause'):            
            clause = clause.parent()
    for label in clause.functionLabels:
        fl[label] = True
    return fl, clause.label

def _attachClauseComplement(parent, child):
    """
    Decide whether the child is a real complement, or needs to be merged
    """
    for fl in child.functionLabels:
        if fl != 'SBAR':
            parent.attachChild(child)
            break
    else:
#        # Merge if they're coindexed traces
#        childSbj = getSubject(child)
#        if childSbj:
#            trace = childSbj.child(0)
#            if trace.isType('Trace'):
#                parentSbj = getSubject(parent)
#                if '-' in trace.text:
#                    reference = trace.text.split('-')[1]
#                    if reference == parentSbj.identifier:
#                        _mergeClauses(parent, child)
#                        return None
        parent.attachChild(child)

def _mergeClauses(parent, child):
    childVG = child.verbalGroup()
    parentVG = parent.verbalGroup()
    for word in childVG.listWords():
        word.reattach(parentVG)
#    constructor = singleton(ConstituentConstructors.GroupComplexCreator)
#    vgComplex = constructor.make(parentVG)
#    parentVG.insert(vgComplex)
#    childVG.reattach(vgComplex)
    for constituent in child.children():
        constituent.reattach(parent)

def getSubject(clause):
    for node in clause.children():
        if 'SBJ' in node.functionLabels:
            return node
    return None


def _makeStr(constituent):
    words = constituent.listWords()
    words.sort()
    return ' '.join([w.text for w in words if w.label != '-NONE-'])

def _indexTraces(parse):
    indexes = {}
    for node in parse.depthList():
        if node.identifier:
            indexes[node.identifier] = node
    return indexes

def printClause(clause):
    if isinstance(clause, Nodes.Node):
        return str(clause)
    sortable = clause.keys()
    sortable.sort()
    words = []
    for node in sortable:
        words.extend(node.listWords())
    words.sort()
    return ' '.join([w.text for w in words if w.label != '-NONE-']) + '\n'

def arrangeVG(verbalGroup):
    finites = {'to': True, 'be': True, 'been': True, 'being': True, 'is': True, 'are': True, 'was': True, 'were': True, 'has': True, 'had': True, 'have': True, 'having': True, 'do': True, 'does': True, 'doing': True, 'did': True, 'will': True, 'would': True, 'shall': True, 'should': True, 'may': True, 'might': True, 'can': True, 'could': True, 'must': True, "'s": True, "'re": True, "'m": True, "'ll": True, 'going': True, "'d": True}
    currentGroup = []
    complexConstructor = singleton(ConstituentConstructors.GroupComplexCreator)
    vgComplex = complexConstructor.make(verbalGroup)
    constructor = singleton(ConstituentConstructors.ConstituentConstructor)
    settings = {'type': 'Verbal_Group', 'label': 'VP', 'functionLabels': {}}
    groups = []
    for word in verbalGroup.listWords():
        currentGroup.append(word)
        if word.text not in finites:
            groups.append(currentGroup)
            currentGroup = []
    if not len(groups) > 1:
        return None
    for group in groups:
        vg = constructor.make(Constituency.VerbalGroup, settings)
        for word in group:
            word.reattach(vg)
        vgComplex.attachChild(vg)
    clause = verbalGroup.parent()
    verbalGroup.prune()
    clause.attachChild(vgComplex)
    clause.sortChildren()


def groupNegs(parse):
    constructor = singleton(ConstituentConstructors.ConstituentConstructor)
    settings = {'type': 'Adverbial_Group', 'label': 'ADVP', 'functionLabels': {}}
    for word in parse.listWords():
        if word.text in ["n't", 'not']:
            advGroup = constructor.make(Constituency.AdverbialGroup, settings)
            word.insert(advGroup)


def handleVGHTaxis(parse):
    """
    Delete clause node parenting infinitive clause complements where the subject
    of the embedded clause is coindexed with the subject of the matrix clause
    """
    global matthiessen, ourVGH
    for vg in parse.depthList():
        if vg.isType('Verbal_Group'):
            for compl in vg.children():
                if compl.label == 'S' and not [fl for fl in compl.functionLabels if fl != 'SBAR']:
                    for sibling in vg.siblings():
                        if 'SBJ' in sibling.functionLabels:
                            vgSubj = sibling
                            break
                    else:
                        break
                    matthiessen += 1
                    for embSubj in compl.children():
                        if 'SBJ' in embSubj.functionLabels:
                            if embSubj.length() == 1:
                                trace = embSubj.child(0)
                                if trace.isType('Trace'):
                                    if '-' in trace.text:
                                        reference = trace.text.split('-')[1]
                                        if reference == vgSubj.identifier:
                                            _fixVGH(vg, compl)
                                            ourVGH += 1
                            break
                    else:
                        break

def _fixVGH(vg, compl):
    for child in compl.children():
        child.reattach(vg)
    compl.prune()
    vg.sortChildren()
    

ellipsisHandler = singleton(NodeVisitors.EllipsisHandler)
gapHandler = singleton(NodeVisitors.GappedClauseHandler)
def preprocess(parse):
    typer = singleton(NodeVisitors.ConstituentTyper)
    connector = singleton(NodeVisitors.ConstituentConnector)
    idAdder = singleton(NodeVisitors.IDAdder)
    retyper = singleton(NodeVisitors.RetypeConstituents)
    cjGrouper = singleton(NodeVisitors.ConjunctionGrouper)
    mwCjHandler = singleton(NodeVisitors.MWConjunctionGrouper)
    
    minorClInserter = singleton(NodeVisitors.MinorClauseInserter)
    relativeClInserter = singleton(NodeVisitors.RelativeClauseInserter)
    
    traceMover = singleton(NodeVisitors.TraceMover)
    childSorter = singleton(NodeVisitors.ChildSorter)
    nominaliser = singleton(NodeVisitors.ClauseNominaliser)
    advClauseDeleter = singleton(NodeVisitors.VerblessADVClauseRemover)
    groupComplexer = singleton(NodeVisitors.GroupComplexer)
    corrItemMover = singleton(NodeVisitors.CorrectedItemMover)
    etcMover = singleton(NodeVisitors.ETCConjunctionReassigner)
    parse.performOperation(typer)
    parse.performOperation(connector)
    parse.constituent.performOperation(corrItemMover)
    parse.performOperation(idAdder)
    dflRemover(parse.constituent)
    parse.constituent.performOperation(gapHandler)
    parse.constituent.performOperation(etcMover)
    parse.constituent.performOperation(minorClInserter)
    parse.constituent.performOperation(nominaliser)
    parse.constituent.performOperation(retyper)
    parse.constituent.performOperation(relativeClInserter)
    parse.constituent.performOperation(mwCjHandler)
    parse.constituent.performOperation(cjGrouper)
    groupNegs(parse.constituent)
    handleVGHTaxis(parse.constituent)
    parse.constituent.performOperation(groupComplexer)
    parse.constituent.performOperation(advClauseDeleter)
    parse.constituent.performOperation(childSorter)
   # parse.constituent.performOperation(traceMover)
    parse.constituent.performOperation(ellipsisHandler)
   # print cPrinter.actOn(parse.constituent)

def dflRemover(parse):
    for node in parse.depthList():
        if node.label == 'EDITED' or node.isType('Dysfluency'):
            node.prune()

def postprocess(sentence):
    quoteChecker = singleton(NodeVisitors.QuotationChecker)
    punctLower = singleton(NodeVisitors.PunctuationLowerer)
    punctRaiser = singleton(NodeVisitors.PunctuationRaiser)
    tracePruner = singleton(NodeVisitors.TracePruner)
    pruner = singleton(NodeVisitors.Pruner)
    truncater = singleton(NodeVisitors.Truncater)
    finaliser = singleton(NodeVisitors.Finaliser)
    sentence.performOperation(quoteChecker)
    sentence.performOperation(punctLower)
    sentence.performOperation(punctRaiser)
    sentence.performOperation(tracePruner)
    sentence.performOperation(pruner)
    sentence.performOperation(truncater)
    sentence.performOperation(finaliser)


def addMetafunctions(sentence):
    sentence.finalise()
    metafunctionAdder = singleton(NodeVisitors.MetafunctionAdder)
    selector = singleton(NodeVisitors.SystemSelector)
    sentence.performOperation(metafunctionAdder)
    sentence.performOperation(selector)

def getSelections(sentence):
    global clauseCount, selectionsDict
    for clause in sentence.depthList():
        if clause.isType('Clause'):
            for system, selection in clause.systems.items():
                if system == 'namesList':
                    continue
                selectionsDict.setdefault(system, {}).setdefault(selection, 0)
                selectionsDict[system][selection] += 1
            clauseCount += 1

def saveSelections(clauseCount, selectionsDict):
    lines = []
    for system, counts in selectionsDict.items():
        noneCount = counts.get(None, 0)
        line = [system]
        for selection, count in counts.items():
            line.append('%s: %d' % (selection, count))
        lines.append((noneCount, '\t'.join(line)))
    lines.sort()
    lines.reverse()
    lines = [l[1] for l in lines]
    open('/home/mhonn/code/mhonn/Treebank/SFGBank/system_selections.txt', 'w').write('\n'.join(lines))


def selectionsTable(clauseCount, selectionsDict):
    lines = []
    for system, counts in selectionsDict.items():
        noneCount = counts.get(None, 0)
        selections = [(c, s) for s, c in counts.items()]
        selections.sort()
        selections.reverse()
        line = [system]
        for count, selection in selections:
            if selection == None:
                continue
            pc = int((float(count)/clauseCount)*100)
            line.append('%s (%d' % (selection, pc) + '\\%)')
        pc = int((float(noneCount)/clauseCount)*100)
        line.insert(1, '%d' % (pc) + '\\%')
        lines.append((noneCount, ' & '.join(line)))
    lines.sort()
    lines = [l[1] for l in lines]
    open('/home/mhonn/papers/sfgbank/selectionsTable.tex', 'w').write('\\\\ \n'.join(lines))
        
            

#import psyco
#psyco.full()
ptb = Treebank.makeCorpus('/home/mhonn/Data/tbSample/')
nPrinter = NodeVisitors.NodePrinter()
cPrinter = NodeVisitors.Printer()
mPrinter = NodeVisitors.MetafunctionPrinter()
clauseCount = 0
selectionsDict = {}
matthiessen = 0
ourVGH = 0
if 1:
    f = ptb.child(2)
    s = f.child(1)
    print nPrinter.actOn(s)
    sentence = getClauses(s)
    postprocess(sentence)
    print cPrinter.actOn(sentence)
    addMetafunctions(sentence)
    getSelections(sentence)
    print mPrinter.actOn(sentence)
else:
    errors = 0
    for j in xrange(ptb.length()):
       # if j % 5:
       #     continue
        f = ptb.child(j)
        for i, s in enumerate(f.children()):
            s = f.child(i)
            try:
                sentence = getClauses(s)
                postprocess(sentence)
                addMetafunctions(sentence)
                getSelections(sentence)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except:
                print "Error on file %d sentence %d" % (j, i)
                errors += 1
               # sentence = getClauses(s)
    selectionsTable(clauseCount, selectionsDict)
    print "Ellipsis percentage: %s" % (float(ellipsisHandler.counter)/clauseCount)
    print "Gap percentage: %s" % (float(gapHandler.counter)/clauseCount)
    print "Percent reduction using Matthiessen VGH def: %s" % (float(matthiessen)/(matthiessen + clauseCount))
    print "Percent reduction using our VGH def: %s" % (float(ourVGH)/(ourVGH + clauseCount))
    print ellipsisHandler.counter
    print gapHandler.counter
    print matthiessen
    print ourVGH
    print clauseCount
