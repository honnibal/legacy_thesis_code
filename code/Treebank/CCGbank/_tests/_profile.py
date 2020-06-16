import hotshot, hotshot.stats
import sys

from Treebank.CCGbank import CCGbank as Corpus

def profile(function):
    prof = hotshot.Profile('/tmp/test.prof')
    prof.runcall(function)
    prof.close()
    stats = hotshot.stats.load('/tmp/test.prof')
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    stats.print_stats(20)

def loadFiles():
    location = '/home/mhonn/repos/code/data/CCGbank1.2_np_v0.7'
    corpus = Corpus(path=location)
    for i, child in enumerate(corpus.children()):
        if i >= 20: break
        pass

if __name__ == '__main__':
    profile(loadFiles)
    
    
