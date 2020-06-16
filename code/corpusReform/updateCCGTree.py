#!/usr/bin/python2.4
"""
Move constituents in the ccg tree, and then update the category labels
"""
import CCG, general, pickles
from general import debug, stats, log
general.DEBUG_LEVEL = 0


class ChangeArguments:
    """
    Use Propbank entries to change the argument structure. If a propbank argument
    is attached as an adjunct, reattach it as an argument, and vice versa

    There are four change cases
    1. Argument->Adjunct
    2. Adjunct->Argument
    3. Move adjunct to the verb
    4. Move argument to the verb

    After each of these nodes, we need to update the label on the constituent
    and its subtree, and the verb and its subtree
    """
    def setEntries(self, entries):
        self.entries = entries

    def changeNodes(self, entries, sentence):
        for entry in entries:
            for parg in entry.pargs:
                stats.count('All pargs')
            pargsAndConstituents = self._getConstituents(entry)
            for parg, constituent in pargsAndConstituents:
                # Should only be for verb particles
                if parg.label == 'rel':
                    if not constituent.label.isAdjunct():
                        print constituent
                        raise StandardError
                    if self._ignoreParg(entry, constituent, parg, True):
                        continue
                    self._adjunctToArgument(constituent, 'PP')
                elif parg.label == 'ARGM' and constituent.label in ['PP', 'NP']:
               # elif parg.label == 'ARGM' and not constituent.label.adjunctResult():
                    if constituent.label == '(S\NP)\((S\NP)/PP)':
                        stats.count('(S\NP)\((S\NP)/PP) adjunct')
                        continue
#                    if constituent.label.isComplex():
#                        stats.count('Complex labelled adjunct')
#                        continue
                    if self._ignoreParg(entry, constituent, parg):
                        if constituent.sibling() and constituent.sibling().label == 'NP\NP':
                            stats.count('NP\NP verb')
                        else:
                            log.msg(printer.actOn(sentence), 'rejected change')
                        stats.count('rejected arg to adj')
                        continue
                    self._argumentToAdjunct(constituent)
                # Case 1: Argument labelled as adjunct (but ignore passive 'by' arguments)
                elif parg.label != 'ARGM' and (not (entry.morph.endswith('p') and parg.feature == 'by')) and constituent.label.cat == '(S\NP)\(S\NP)':
                    if self._ignoreParg(entry, constituent, parg):
                        stats.count('rejected adj to arg')
                        log.msg(printer.actOn(sentence), 'rejected change')
                        continue
                    argLabel = 'PP'
                    argLabel = self._getArgLabel(constituent)
                    if argLabel:
                        self._adjunctToArgument(constituent, argLabel)
                    else:
                        stats.count('rejected adj to arg')
                        stats.count('No arg label found')
                        log.msg('No arg label found', 'rejected change')
                        log.msg(constituent, 'rejected change')
                        log.msg(constituent.head(), 'rejected change')
                        log.msg(printer.actOn(sentence), 'rejected change')
                else:
                    stats.setContext('unchanging')
                   # if not self._ignoreParg(entry, constituent, parg):
                    stats.count('no change')
                    stats.setContext(None)

    def _getArgLabel(self, constituent):
        # If it was a unary transformation, use the child label
        if constituent.length() == 1:
            child = constituent.child(0)
            if not child.isLeaf() and not child.label.isAdjunct():
                return child.label
        head = constituent.head()
        if head.label.startswith('N'):
            return 'NP'
        elif head.parg == 'N' or head.parg == 'NP':
            return 'NP'
        elif head.parg.adjunctResult():
            return 'PP'
        
        else:
            return None
        

    def _getConstituents(self, entry):
        pargsAndConstituents = []
        for parg in entry.pargs:
            if parg.label == 'rel':
                constituent = self._getVerbParticle(parg)
                if constituent:
                    pargsAndConstituents.append((parg, constituent))
                continue
            constituents = [c for c in parg.refChain.constituents()]
            if not constituents:
                continue
            elif len(constituents) > 1:
                stats.count('multiple constituents')
                log.msg(str(entry), 'multi constituent')
                log.msg(str(parg), 'multi constituent')
                log.msg('Constituents:', 'multi constituent')
                for c in constituents:
                    log.msg(str(c), 'multi constituent')
                continue
            constituent = constituents[0]
            if constituent.isLeaf():
                constituent = constituent.parent()
            pargsAndConstituents.append((parg, constituent))
        return pargsAndConstituents

    def _ignoreParg(self, entry, constituent, parg, isParticle = False):
        global sentence
        verb = constituent.sibling()
        # If we remove a node that's referenced by another parg, the reference is going to be deleted...
        try:
            errorMsg = '%s\n%s\n%s\n%s' % (entry, parg, constituent, verb)
        except:
            stats.count('Deleted reference node')
            return True
        if parg.label == 'ARGM' and verb.label == 'NP\NP':
            log.msg(errorMsg, 'np-np')
            log.msg(printer.actOn(sentence), 'np-np')
            return True
        if not verb:
            stats.count('verbless')
            log.msg(errorMsg, 'rejected change')
            return True
        if verb.isAdjunct():
            stats.count('invalid verb')
            log.msg(errorMsg, 'rejected change')
            return True
        if verb.label.result.isAdjunct():
            stats.count('invalid verb')
            log.msg(errorMsg, 'rejected change')
            return True
        if not verb.label.isPredicate():
            stats.count('invalid verb')
            log.msg(errorMsg, 'rejected change')
            return True            
        if constituent < verb:
            stats.count('before verb')
            log.msg(errorMsg, 'rejected change')
            return True
        if parg.label == 'rel' and not isParticle:
            return True
        elif parg.feature == 'MOD':
            stats.count('skipped aux')
            return True
        elif parg.label == 'ARG0' and parg.feature == 'by':
            stats.count('passive agent')
            return True
        if not verb.label.isComplex():
            stats.count('Atomic verb')
            return True
        head = verb.head()
        if head != entry.rel:
            log.msg(errorMsg, 'rejected change')
            stats.count('wrong verb')
            return True
        else:
            return False

    def _getVerbParticle(self, parg):
        """
        Get a particle from the verb
        """
        constituents = parg.refChain.constituents()
        possibleParticles = []
        for constituent in constituents:
            if self._isParticle(constituent):
                possibleParticles.append(constituent)
            for child in constituent.children():
                if self._isParticle(child):
                    possibleParticles.append(child)
        if len(possibleParticles) != 1:
            return None
        else:
            return possibleParticles[0]

    def _isParticle(self, constituent):
        if not constituent.isAdjunct():
            return False
        words = [w for w in constituent.listWords()]
        if len(words) > 1:
            return False
        word = words[0]
        if word.label not in ['IN', 'RP']:
            return False
        return True

        
            
    def _adjunctToArgument(self, constituent, argLabel):
        stats.count('adjunct to argument')
        debug("Adjunct to argument", 1)
        debug(constituent, 1)
        arg = CCG.Category(argLabel)
        for head in constituent.label.heads():
            arg.addHead(head)
        arg.conj = constituent.label.conj
        verb = constituent.sibling()
        if constituent.label.slash == '\\':
            verbSlash = '/'
        else:
            verbSlash = '\\'
        constituent.changeLabel(CCG.Category(arg))
        newCategory = CCG.ComplexCategory(verb.label, arg, verbSlash, False)
        debug("Changing verb to %s" % newCategory.fullPrint(), 1)
        verb.changeLabel(newCategory)
        # Change dependencies
        # Only need to change the verb, because the argument is now atomic
       # verb.parent().composeChildren()
        argNum = len(verb.label.arguments)
        verbCat = verb.head().parg
        verbCat.goldDeps.insert(argNum, [(constituent.head(), 'L')])
        

    def _argumentToAdjunct(self, constituent):
        debug("Argument to Adjunct", 1)
        debug(constituent, 1)
        stats.count('argument to adjunct')
        verb = constituent.sibling()
        if constituent < verb:
            raise StandardError
        else:
            slash = '\\'
        oldLab = constituent.label
        oldHeadLab = constituent.head().parg
        if verb.label.isComplex():
            cat = CCG.Category('(S\NP)%s(S\NP)' % slash)
        else:
            cat = CCG.Category('S%sS' % slash)
        cat.conj = oldLab.conj
        for head in oldLab.heads():
            cat.addHead(head)
        constituent.changeLabel(cat)
        if verb.label.isComplex():
            argNum = len(verb.label.arguments) - 1
            oldVerbLab = verb.label
            oldVerbHead = verb.head().parg
            verb.changeLabel(verb.label.result)
        else:
            print verb
            raise StandardError
           # verb.parent().composeChildren()
        # Add a dependency to the verb to the adjunct
        # and remove dependencies to the adjunct
        adjunctHead = constituent.head()
        try:
            verb.head().parg.goldDeps.pop(argNum)
        except:
            print verb.label
            print verb.head()
            print oldVerbLab
            print oldVerbHead
            print len(verb.head().parg.goldDeps)
            for head, depType, num in oldVerbHead.goldDependencies():
                print '%s %s %s' % (head, depType, num)
            print argNum
            verb.head().parg.goldDeps.pop(argNum)
        goldDeps = list(oldHeadLab.goldDeps)
        # Blank dependency at position 1, for the NP in S\NP
        goldDeps.insert(0, [])
        # Add the verb dependency
        goldDeps.insert(1, [(verb.head(), 'L')])
        adjunctHead.parg.goldDeps = goldDeps
#        if adjunctHead.parg == '((S\NP)%s(S\NP))/NP' % slash or adjunctHead.parg == '(S\NP)%s(S\NP)' % slash:
#            adjunctHead.parg.goldDeps.append([])
#            adjunctHead.parg.goldDeps.append([(verb.head(), 'L')])
#            if oldHeadLab == 'PP/NP' and oldHeadLab.goldDeps and adjunctHead.parg == '((S\NP)%s(S\NP))/NP' % slash:
#                adjunctHead.parg.goldDeps.append(oldHeadLab.goldDeps[0])



if __name__ == '__main__':
    from Propbank.Propbank import Propbank
    from Treebank import CCGBank, NodeVisitors
    from Treebank.CCGBank import CCGNodeVisitors
    import psyco
    general.DEBUG_LEVEL = 0
    import CCG.Category
    
    psyco.full()
    printer = NodeVisitors.NodePrinter()
    changer = ChangeArguments()
    propbank = Propbank('./alignment/ccgPropbank.txt')
    corpus = CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/AUTO/')
    sentenceCount = -1
    autoWriter = CCGNodeVisitors.AutoFileWriter()
    autoWriter.setDir('/home/mhonn/Data/CCGBank/PropModTest')
    pargWriter = CCGNodeVisitors.PargFileWriter()
    pargWriter.setDir('/home/mhonn/Data/CCGBank/PropModTestParg')
    log.openLog('/home/mhonn/code/mhonn/CCG/corpusReform/logs/invalid.txt', 'invalid')
    log.openLog('/home/mhonn/code/mhonn/CCG/corpusReform/logs/rejected_change.txt', 'rejected change')
    log.openLog('/home/mhonn/code/mhonn/CCG/corpusReform/logs/multi_constituent.txt', 'multi constituent')
    log.openLog('/home/mhonn/code/mhonn/CCG/corpusReform/logs/np-np.txt', 'np-np')
    # 2170
    for j in xrange(21, 70):
        f = corpus.child(j)
        f.finalise()
        f.addPargDeps()
        f.finalise()
        i = -1
        autoStrings = []
        pargStrings = []
        for sentence, entries in propbank.fileEntries(f):
            i += 1
            sentenceCount += 1
            before = printer.actOn(sentence)
            sentenceStr = autoWriter.getSentenceStr(sentence)
            pargStr = pargWriter.getSentenceStr(sentence)
            stats.count('sentences')
            stats.setContext('original')
            for ruleFreq in xrange(0, 1):
                CCG.setRuleFreq(ruleFreq)
                if not sentence.validate():
                    stats.setContext(None)
                    stats.count('invalid before at %d' % ruleFreq)
                    debug("Invalid before changes", 0)
                    debug(i, 0.1)
                    debug(before, 0.1)
                   # raise StandardError
            stats.setContext(None)
            changer.changeNodes(entries, sentence)
            for ruleFreq in xrange(0, 1):
                CCG.setRuleFreq(ruleFreq)
                if not sentence.validate():
                    stats.count('invalid after at %d' % ruleFreq)
                    debug("Invalid after changes", 0)
                    debug(printer.actOn(sentence), 0.5)
                    debug(before, 0.5)
                    log.msg(f.ID, 'invalid')
                    log.msg(i, 'invalid')
                    log.msg(before, 'invalid')
                    log.msg(printer.actOn(sentence), 'invalid')
                    continue
                    after = printer.actOn(sentence)
                    debug(before, 0)
                    debug(after, 0)
                    debug(i, 0)
                    raise StandardError
            else:
                sentenceStr = autoWriter.getSentenceStr(sentence)
                pargStr = pargWriter.getSentenceStr(sentence)
            after = printer.actOn(sentence)
            if before != after:
                debug(before, 0.9)
                debug(after, 0.8)
                stats.count('Sentences changed')
            autoStrings.append(sentenceStr)
            pargStrings.append(pargStr)
#        autoWriter.writeFile(f.ID, autoStrings)
#        pargWriter.writeFile(f.ID, pargStrings)
    stats.report()
    log.close()
    

