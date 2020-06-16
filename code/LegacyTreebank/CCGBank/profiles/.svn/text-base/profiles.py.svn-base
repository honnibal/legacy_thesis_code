"""
Profile various corpus tasks for optimisation
"""
from Treebank import CCGBank
import hotshot, hotshot.stats
def makeFiles(corpus, n):
    for i in xrange(n):
        f = corpus.child(i)


corpus = CCGBank.makeCCGBank('/home/mhonn/Data/CCGBank/orig')
prof = hotshot.Profile('test.prof')
prof.runcall(makeFiles, corpus, 10)
prof.close()
stats = hotshot.stats.load('test.prof')
stats.strip_dirs()
stats.sort_stats('time', 'calls')
stats.print_stats(20)
