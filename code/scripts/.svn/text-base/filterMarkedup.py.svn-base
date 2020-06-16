"""
Remove markedup entries for categories that occur fewer than 10 times
"""
import sys
from os.path import join as pjoin

from CCG import Markedup, Lexicon


class Options:
    def __init__(self, args):
        try:
            corpus = args[0]
            self.lexLoc = pjoin(corpus, 'lexicons', '02-21.lex')
            self.muLoc = pjoin(corpus, 'full_markedup')
        except:
            print "Usage: filterMarkedup.py <corpus loc>"
            sys.exit(1)
            
def main():
    options = Options(sys.argv[1:])
    lexicon = Lexicon.Lexicon(options.lexLoc)
    entries, index = Markedup.getEntries(options.muLoc)
    header, text = open(options.muLoc).read().split("# now list the markedup categories")
    print header.strip()
    print '# now list the markedup categories'
    markedup = {}
    for entry in entries:
        markedup[entry.cat] = entry
    cats = [(sum(f.values()), c) for c, f in lexicon.cats.items()]
    for f, cat in reversed(sorted(cats)):
        if f < 10:
            break
        entry = markedup[cat]
        print entry
    if r'NP/(NP\NP)' in markedup:
        print markedup[r'NP/(NP\NP)']
            
if __name__ == '__main__':
    main()
    
    
