import hotshot, hotshot.stats

from _Corpus import Corpus

def profile(function):
    prof = hotshot.Profile('/tmp/test.prof')
    prof.runcall(function)
    prof.close()
    stats = hotshot.stats.load('/tmp/test.prof')
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    stats.print_stats(20)

def loadFiles():
    location = '/home/matt/code/repos/data/TreeBank3/parsed/mrg/wsj/'
    corpus = Corpus(path=location)
    for child in corpus.children():
        pass

if __name__ == '__main__':
    profile(loadFiles)
    
    
