import math
import operator
import codecs
import collections
from math import log
import os.path
import sys

from standardiser import standardise
from document import Document


def utf8open(loc, mode='r'):
    return codecs.open(loc, mode, 'utf8')

def localPath(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

class Summariser(object):
    def __call__(self, doc, n):
        """
        Return the N most pertinent sentences of a document,
        in the order in which they occur
        """
        # The document's 'bag-of-words' -- a sparse vector of token frequencies.
        docBow = doc.bagOfWords
        print >> sys.stderr, n
        # Get N most similar.
        topN = sorted(doc,
                      key=lambda s: self.similarity(docBow, s.bagOfWords))[-n:]
        # Sort back into document order.
        return sorted(topN, key=lambda s: s.position)

    def debug(self, doc):
        docBow = doc.bagOfWords
        decorated = [(self.similarity(docBow, s.bagOfWords), s) for s in doc]
        for sim, s in decorated:
            print '%.3f: %s' % (sim, repr(s.string))
        

class FrequencySummariser(Summariser):
    """
    Score a sentence by summing the frequencies of its tokens within the
    document as a whole
    """
    def similarity(self, docBow, sentBow):
        # Sum the document frequencies for each token in the sentence.
        # We achieve this by multiplying by the frequency of the term in the
        # sentence.
        return sum([(docBow[t]-f)*f for t, f in sentBow.items()])

class TFIDFSummariser(Summariser):
    """
    Scores sentences by TF-IDF weighted token frequencies
    """
    def __init__(self):
        Summariser.__init__(self)
        # The number of documents the inverse doc frequencies were drawn from.
        n = 818741.0
        self.idfs = self._loadIDFs(n)

    def _loadIDFs(self, n):
        dfLoc = localPath('wiki_doc_freqs_trim.dat')
        # Convenience for codecs.open.
        #lines = bz2Utf8Open(dfLoc).strip().split('\n')
        # Read in the document freqs.
        # Have to do this first because we collapse some freqs through
        # standardisation.
        dfs = collections.defaultdict(int)
        for line in utf8open(dfLoc):
            token, freq = line.split('\t')
            token = standardise(token)
            if token:
                dfs[hash(token)] += int(freq)
        # Turn the frequencies into IDF weights.
        idfs = collections.defaultdict(float)
        while idfs:
            token, freq = dfs.randitem()
            idf = log(n/freq, 10)
            idfs[token] = idf
        return idfs
    
    def similarity(self, docBow, sentBow):
        idfs = self.idfs
        default = log(818741.0/100)
        # Apply the inverse document frequency weight to each term.
        return sum([f*(docBow[t]-f)*idfs.get(hash(t),default)
                    for t, f in sentBow.items()])

def main():
    text = utf8open(sys.argv[1]).read()
#    summariser = FrequencySummariser()
    print >> sys.stderr, "Setting up"
    summariser = TFIDFSummariser()
    print >> sys.stderr, "Summarising"
    for sentence in summariser(Document(text), int(sys.argv[2])):
        print sentence
        
if __name__ == '__main__':
    main()
