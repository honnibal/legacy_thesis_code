"""
Use N-Gram language modelling to compute the probabilities of different
analyses
"""
import os, sys, codecs
from math import log, exp
from Distributions import LGTDistribution
import pyximport; pyximport.install()
from _cython import getCountCounts, getFreqs, evaluateFreqs

class KatzLanguageModel:
    def __init__(self, name, vocab):
        self.name = name
        self.vocab = vocab
        
    
        
    def evaluate(self, sentence):
        global N
        logProb = 0.0
        for i in xrange(N, len(sentence)):
            gram = sentence[i-N:i]
            logProb += log(self.prob(gram))
        return logProb

    def evaluateFreqs(self, freqs):
        global N
        return evaluateFreqs(freqs, N, self.prob)
        logProb = 0.0
        for ngram, freq in freqs.items():
            if len(ngram) == N:
                itsProb = self.prob(ngram)
                itsProb ** freq
                logProb += log(itsProb)
        assert logProb != 0.0
        return logProb
            

    def prob(self, gram):
        """
        Check to see whether gram has been seen before. If not,
        reduce its context by 1 and apply a normalisation constant
        """
        assert gram
        freqs = self.freqs
        length = len(gram)
        distribution = self.distributions[length]
        
        if gram not in freqs:
            fullGramFreq = 0.0
        else:
            fullGramFreq = freqs[gram]
            if fullGramFreq < K:
                fullGramFreq = 0.0
                
        if length == 1:
            discountFreq = distribution.smooth(fullGramFreq)
            return discountFreq/distribution.bigN
        elif fullGramFreq:
            discountFreq = distribution.smooth(fullGramFreq)
            contextFreq = freqs[gram[:-1]]
            return discountFreq/contextFreq
        # Backoff by shortening ngram
        else:
            if length == 2:
                # For bigrams we know that the denominator is 1
                shorter = self.normalisers.get(gram[:-1], 1.0)
                contextOfShorter = 1.0
            else:
                # We've stored 1-sum(...). If we don't have a value,
                # the sum(...)=0, so result is 1
                shorter = self.normalisers.get(gram[:-1], 1.0)
                contextOfShorter = self.normalisers.get(gram[1:-1], 1.0)
           # assert numerator < denominator
            backoffProb = (shorter/contextOfShorter)*self.prob(gram[1:])
            assert backoffProb > 0
            return backoffProb

    def printDist(self, n):
        """
        Output a table of r vs r* for the distribution at n
        """
        self.distributions[n].printRStars()


    def train(self, **kwargs):
        global N
        if 'text' in kwargs:
            text = kwargs.pop('text')
            freqs = self.getFreqs(text)
        elif 'freqs' in kwargs:
            freqs = kwargs.pop('freqs')
        else:
            raise StandardError
        countCountsAtN = getCountCounts(freqs)
        self.freqs = freqs
        distributions = {}
        for n, countCounts in countCountsAtN.items():
            distributions[n] = LGTDistribution(countCounts)
        self.distributions = distributions
        self._initNormConstants()

    def getFreqs(self, text):
        global N
        return getFreqs(text, self.vocab, N)

    def _countCounts(self):
        return _countCounts(self.freqs)
        # Count up the frequencies at various N
        countCounts = {}
        for gram, count in self.freqs.items():
            n = len(gram)
            # Avoid setdefault/get as this part is speed critical
            if n in countCounts:
                countDict = countCounts[n]
            else:
                countDict = {}
                countCounts[n] = countDict
            # Round the counts so that we do not get
            # an unusually sparse distribution
            rounded = round(count)
            if rounded in countDict:
                countDict[rounded] += 1.0
            else:
                countDict[rounded] = 1.0
        return countCounts

    def _initNormConstants(self):
        """
        Katz normalisation constants for each event type seen.

        The normalisation constants ensure that even after smoothing
        sum = 0
        for word in language:
            sum += P(word|context)
        assert sum == 1

        We do this by figuring out how much probability is assigned for unseen
        events by the discounting and the complement of the probability that
        would be assigned to backed off events. We then use the ratio between
        these two as a normalisation constant.
        """
        global K
        freqs = self.freqs
        prob = self.prob
        # First, key events by their context
        byContext = {}
        for gram in freqs:
            if len(gram) > 1 and freqs.get(gram) > K:
                byContext.setdefault(gram[:-1], []).append(gram)
        normalisers = {}
        # Now get 1-(sum(p(gram), grams)) for each gram that starts
        # with a given context
        for context, grams in byContext.items():
            discountTotal = sum([prob(gram) for gram in grams])
            normalisers[context] = 1 - discountTotal
            # Debugging, disabled for speed
#            if discountTotal > 1:
#                print discountTotal
#                print context
#                print self.freqs[context]
#                raise StandardError
        self.normalisers = normalisers
        

def main(modelClass, basePath, toClassify):
    """
    Test suite for simple language modelling problem: language
    recognition
    """
    languages = os.listdir(basePath)
    languages.sort()
    models = {}
    for lang in languages:
        path = os.path.join(basePath, lang)
        # Collect language text as a single list of letters
        if not path.endswith('.txt'): continue
        # Split text into sentences on newlines, making each sentence a list of letters
        text = [tuple(sentence) for sentence in open(path, 'r').read().split('\n')]
        print "Modelling: %s" % lang
        model = modelClass(lang)
        model.train(text)
#        model.startTrain()
#        for sentence in text:
#            model.count(sentence)
#        model.endTrain()
        models[lang] = model
   # english = list("This is a very simple test sentence of English.")
    modelList = models.values()
    best = ()
    for model in modelList:
        score = model.evaluate(toClassify)
#        print "%s: %s" % (model.name, score)
        if not best or (best[0] < score):
            best = (score, model.name)
    print 'Best model: %s (%s)' % (best[1], best[0])
        
def profile():
    import hotshot, hotshot.stats
    prof = hotshot.Profile('test.prof')
    prof.runcall(test)
    prof.close()
    stats = hotshot.stats.load('test.prof')
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    stats.print_stats(20)   

def test():
    main(KatzLanguageModel, sys.argv[1], tuple("This is a test"))

N = 2
K = 10
if __name__ == '__main__':
    test()
    
