import sys

from rebanking.rebankers import verbInflection
from rebanking.rebankers import mainWrapper
from rebanking.rebankers import debugWrapper
debug = debugWrapper(verbInflection.doSentence)
if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except:
        pass
    if '-d' in sys.argv:
        debug(sys.argv[2], sys.argv[3])
    else:
        labels = verbInflection.NonSInflection.labels
        main = mainWrapper(verbInflection.doSentence)
        main()
        for l, f in reversed(sorted(labels.items(), key=lambda i: i[1])):
            print '%d: %s' % (f, l)
