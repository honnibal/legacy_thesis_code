import Treebank.PTB
import Treebank.CCGbank
from pb import Propbank, Nombank
from general import stats
import data
import sys

def getStats(entry):
    pred = entry.rel
    numArgs = 0
    numCore = 0
    for parg in entry.pargs:
        for constituent in parg.refChain.constituents():
            if constituent != pred:
                numArgs += 1
                if parg.label not in ['ARGM', 'rel', 'Support', 'support']:
                    numCore += 1
                    stats.count('core args')
                    stats.count(parg.label)
                    if constituent.label == 'PP':
                        stats.count('PP args')
                stats.count('tot args')
                break
    stats.count('%d args' % numArgs)
    stats.count('%d core args' % numCore)
    stats.count('entries')


def getAgreement(entry):
    predicate = entry.rel
    for parg in entry.pargs:
        stats.setContext(None)
        if parg.label == 'rel': continue
        if parg.constituent is entry.rel.parent(): continue
        if parg.label.lower() == 'support':
            break
        if parg.label == 'ARGM':
            label = 'adjunct'
        elif parg.label.startswith('ARG'):
            label = 'argument'
        else:
            continue
        constituents = list(parg.refChain.constituents())
        if not constituents:
            stats.count('no args')
        elif len(constituents) > 1:
            stats.count('multi args')
        else:
            stats.count('one arg')
            constituent = constituents[0]
            if constituent.label == 'N/N':
                continue
            sibling = constituent.sibling()
            if sibling and predicate in sibling.listWords():
           # if sibling and (predicate is sibling.head() or
           #                 sibling.head().stag == 'conj'):
                stats.count('attached')
                stats.setContext(label)
                if constituent.label.isAdjunct():
                    stats.count('adjunct')
                else:
                    stats.count('argument')
            else:
                #print entry.rel
                #                print constituent
                stats.count('detached')

def reportStats(counts):
    total = 0.0
    totalRight = 0.0
    for true in ['argument', 'adjunct']:
        opposite = 'adjunct' if true == 'argument' else 'argument'
        right = counts[(true, true)]
        wrong = counts[(opposite, true)]
        total += right + wrong
        totalRight += right
        accuracy = right/float(right+wrong)
        print "%s: %.2f" % (true, accuracy*100)
    detached = counts[('detached', None)]
    multiArgs = counts[('multi args', None)]
    noArgs = counts[('no args', None)]
    total += detached
    total += multiArgs
    total += noArgs
    accuracy = totalRight/total
    print "detached: %.2f" % ((detached/total)*100)
    print "multi args: %.2f" % ((multiArgs/total)*100)
    print "no args: %.2f" % ((noArgs/total)*100)
    print "accuracy: %.2f" % ((accuracy*100))
        
    

def main():
    corpus = Treebank.CCGbank.CCGbank(path=sys.argv[1])
    pb = Propbank(sys.argv[2])
    for i in xrange(corpus.length()):
        try:
            f = corpus.child(i)
        except:
            print "Parsing failed!"
            raise
        for s, entries in pb.fileEntries(f):
            for entry in entries:
                getAgreement(entry)
        if i == 200:
            break
    reportStats(stats.theCounts)


if __name__ == '__main__':
    main()
