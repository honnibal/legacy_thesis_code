from regression import regress
from math import log, exp
import pyximport; pyximport.install()
from _distributions import smooth
import numpy

class LGTDistribution:
    def __init__(self, countCounts):
        """
        A Linear Good-Turing smoothed distribution at fixed N.
        A KatzLanguageModel will contain several distributions, because it must
        estimate probabilities for unigrams, bigrams, trigrams etc.
        """
        if not 1 in countCounts:
            countCounts[1] = 1.0
        self.nVals = countCounts
        # Calculate vocab size
        bigN = 0
        for n, n_r in countCounts.items():
            bigN += n*n_r
        self.bigN = bigN
        # Initialise r* values for simple Good-Turing smoothing.
        self._initSmoothers()
        
    def smooth(self, r):
        """
        If we're here, we assume the event has been seen before
        """
        return smooth(self.rStarArray, self.bigN, r)
        # Raw frequency
        #r = self._freqs.get(event, 0)
        if r == 0:
            # Formula here is N_1/(N_0*N)
            # However, we assume N_0 ~= N_1
            # This works out to 1/N
            rStar = 1.0/self.bigN
        else:
            # Smoothed frequency
            rStar = self.rStars[r]
        if self.rStars.get(r, 0.0) > r > 0:        
            print r
            print self.rStars[r]
            raise ConstraintError
        return rStar

    def printRStars(self):
        rVals = self.nVals.keys()
        rVals.sort()
        maxR = rVals[-1]
        for r in xrange(1, int(maxR), 1):
            rStar = self.rStars.get(r, self._smoothR(r))
            print "%s\t%s" % (r, rStar)

    def printProbs(self):
        rVals = self.nVals.keys()
        rVals.sort()
        maxR = rVals[-1]
        for r in xrange(1.0, maxR, 1.0):
            rStar = self.rStars.get(r, self._smoothR(r))
            print rStar/self.bigN
            
    def _initSmoothers(self):
        """
        Get r* estimates using Simple Good-Turing. These will be used to calculate
        discount probabilities.

        This process is complicated. Read Gale "Good-Turing Smoothing without tears"
        to really understand what's going on. Basically we apply a transform
        to the count-counts, and then smooth the logs of the resulting values with simple
        linear regression.

        This is necessary because N_r is noisy for large r.
        """
        rVals = self.nVals.keys()
        rVals.sort()
        # Apply a transform to N_r to correct the rightward tail of its distribution
        zrVals = self._getZ_rVals(rVals)
        # Get the natural logs of zr and r vals
        logR = [log(r) for r in rVals]
        logZ_r = [log(zr) for zr in zrVals]
        # Make a simple linear regression model for smoothing Z_r
        gradient, intercept = regress(logR, logZ_r)
        # See Gale for proof that we need b < -1
        if gradient >= -1:
            gradient = -1.0001
        useLGT = True
        discountR = {}
        self._m = gradient
        self._b = intercept
        for r in rVals:
            discountR[r] = self._smoothR(r)
            if discountR[r] > r > 0:
                raise ConstraintError
        vals = []
        # Make a numpy array of rStars
        for i in xrange(max(discountR.keys())+1):
            vals.append(discountR.get(i, 0.0))
        self.rStarArray = numpy.array(vals, dtype="float32")
        self.rStars = discountR
        normaliser = 0.0
        # Sum of the unnormalised values
        for rStar in discountR.values():
            normaliser += rStar/self.bigN
        if not normaliser:
            print discountR
            assert normaliser
        self._normDenom = normaliser
        self._normProd = 1 - (self.nVals[1]/self.bigN)
        assert self._normProd > 0
        assert self._normDenom > 0
        
        
    def _smoothR(self, r):
        """
        Use LGT to smooth r
        """
        gradient = self._m
        intercept = self._b
        nr  = exp(gradient*log(r)+intercept)
        nr1 = exp(gradient*(log(r+1))+intercept)
        return (r+1)*(nr1/nr)
        
            
    def _getZ_rVals(self, rVals):
        """
        Replace N_r with Z_r: N_r/0.5*(t-q), where t and q are
        the values on either side of N_r
        """
        zrVals = []
        for i in xrange(len(rVals)):
            r = rVals[i]
            # If r is the first (we can't get q) or last (we can't get t)
            # value, assume that t and q are equidistant
            if i == 0:
                tToR = rVals[i+1] - r
                q = r - tToR
            else:
                q = rVals[i-1]
            if i == len(rVals)-1:
                rToQ = r - q
                t = r + rToQ
            else:
                t = rVals[i+1]
            nr = self.nVals[r]
            zr = nr/(0.5*(t-q))
            zrVals.append(zr)
        return zrVals

class ConstraintError(StandardError):
    """
    Error for when an assumption about the data goes wrong
    """
    pass
    
class ZeroProbabilityError(ConstraintError):
    """
    Specific error for P(event) = 0
    """

def test():
    # Read count counts from Manning and Schutze test data
    raw = open('austen-cntcnt.txt').read().split('\n')
    countCounts = {}
    for line in raw:
        if not line: continue
        count, itsCount = line.split()
        countCounts[float(count)] = float(itsCount)
    distribution = LGTDistribution(countCounts)
    distribution.printRStars()

    print
    nDist = AbsDistribution(countCounts)
    nDist.printRStars()

if __name__ == "__main__":
    test()
    
