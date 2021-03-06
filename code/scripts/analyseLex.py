#!/usr/bin/python
"""
Gather several descriptive systems about a CCGbank instance:

- Number of categories vs n, where n is a frequency threshold
- Avg. category ambiguiy vs n
- Expected category entropy
"""
from os.path import join as pjoin
import CCG, pickles
import math, re, sys
from CCG.Lexicon import Lexicon

def merge(d1, d2):
    rows = []
    for row in zip(d1, d2):
        cols = [row[0][0]]
        for col in row:
            cols.append(col[1])
        print cols
        rows.append(cols)
    return rows



def printMissing(expLex, control):
    expMissing = expLex.getMissing(control, 1)
    print "Missing from CCGbank"
    for f, c, words in expMissing:
        print "%d: %s (%s)" % (f, c, ', '.join(sorted(['%s|%s' % (w[0], w[1]) for w in words.keys()])[:5]))
    print "Missing from New Version"
    controlMissing = control.getMissing(expLex, 1)
    for f, c, words in controlMissing:
        print "%d: %s (%s)" % (f, c, ', '.join(sorted([w[0] for w in words.keys()[:5]])))


def plotAvgEntropy(expLex, control, maxThresh, dataName = ''):
    expRows = expLex.avgEntropyAtN(maxThresh)
    controlRows = control.avgEntropyAtN(maxThresh)
    if dataName:
        fileName = 'entropy_%s' % dataName
    else:
        fileName = 'entropy'
    plot(controlRows, expRows, "Avg. Entropy with Categories more Frequent than N", "N", "Entropy", fileName)
#    plotSingle(expLex, "Avg. Entropy with Categories more Frequent than N", "N", "Avg. Entropy", fileName)


def printEntropyChanges(expLex, control):
    changes = expLex.entropyChanges(control)
    for change, word, expEnt, controlEnt in changes:
        word = '|'.join(word)
        if change != 0:
            print "%.3f: %s %.3f %.3f" % (change, word, expEnt, controlEnt)



        
def plotLines(lines, title, xLabel, yLabel, fName):
    g = Gnuplot.Gnuplot(debug=1)
    g('set data style lines')
    g.title(title)
    data = []
    for line, lineTitle in lines:
        data.append(Gnuplot.PlotItems.Data(line, title=lineTitle))
    g.plot(*data)
    g.xlabel(xLabel)
    g.ylabel(yLabel)
    g.hardcopy('/home/mhonn/code/thesis/analysis/%s.eps' % fName, enhanced = 1, color = 1)
    raw_input("Press any key to continue.")

def main():
    verbose = bool(sys.argv[1] == '-v')
    if verbose: sys.argv.pop(1)
    expLex = Lexicon(pjoin(sys.argv[1], 'lexicons', '02-21.lex'))
    expUns = Lexicon(pjoin(sys.argv[1], 'lexicons', '00.lex'))
    conLex = Lexicon(pjoin(sys.argv[2], 'lexicons', '02-21.lex'))
    conUns = Lexicon(pjoin(sys.argv[2], 'lexicons', '00.lex'))
    if verbose: printMissing(expLex, conLex)
    print "# Cats in experiment lexicon: %d" % (len(expLex.cats))
    print "# Cats in control lexicon:    %d" % (len(conLex.cats))
    print "Delta: %.3f" % (len(expLex.cats)/float(len(conLex.cats)))
    expCats = len([c for (c, occ) in expLex.cats.iteritems()
                   if sum(occ.values()) > 9])
    conCats = len([c for (c, occ) in conLex.cats.iteritems()
                   if sum(occ.values()) > 9])
    print "# Cats in experiment lexicon >=10: %d" % (expCats)
    print "# Cats in control lexicon >=10:    %d" % (conCats)
    print "Delta: %.3f" % (expCats/float(conCats))
    expCov, expAvgSize = expLex.coverageOnUnseen(expUns)
    conCov, conAvgSize = conLex.coverageOnUnseen(conUns)
    print "Coverage with experiment lexicon: %.6f" % (expCov)
    print "Coverage with control lexicon:    %.6f" % (conCov)
    print "Delta: %.3f" % (expCov/conCov)
    print "Avg. Tag dict size with experiment lexicon: %.3f" % (expAvgSize)
    print "Avg. Tag dict size with control lexicon:    %.3f" % (conAvgSize)
    print "Delta: %.3f" % (expAvgSize/conAvgSize)
    
try:
    import psyco
    psyco.full()
except:
    pass
if __name__ == '__main__':
    import pickles
    if len(sys.argv) not in [3, 4]:
        print "USAGE: <experiment lex> <control lex>"
        sys.exit(1)
    main()
    

    
                             
    


