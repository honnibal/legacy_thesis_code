#!/usr/bin/python2.4
"""
Validate a corpus, printing log files with the invalid sentences
"""
import sys
from Treebank import CCGBank
from general import log
import psyco
import CCG
psyco.full()
corpusLoc = sys.argv[1]
output = sys.argv[2]
log.openLog(output, 'invalid')
ccgbank = CCGBank.makeCCGBank(corpusLoc)
lastSent = None
CCG.setRuleFreq(0)
CCG.debug()
for i in xrange(0, ccgbank.length()):
    try:
        f = ccgbank.child(i)
        for sNum, s in enumerate(f.children()):
            lastSent = s.globalID
            if not s.validate():
                log.msg(s.globalID, 'invalid')
    except:
        log.msg("Epic fail!! Last valid: %s" % lastSent, 'invalid')
