import sys
from os.path import join as pjoin
import random

from _Rebanker import Rebanker
from general import log
from Treebank import CCGbank
from Treebank.CCGbank import Writers

def processWrapper(processes, applications):
    def doSentence(sentence):
        for process in processes:
            # Breadthlist is important; depthlist processes nodes out of order
            # e.g. wsj_0010.auto~5
            changes = [True]
            while any(changes):
                changes = []
                for node in sentence.breadthList():
                    if node.isLeaf() or node.isRoot():
                        continue
                    # Get occasional ghosts from movement
                    if node.length() == 0:
                        continue
                    if process.match(node):
                        changes.append(True)
                        try:
                            process.change(node)
                        except:
                            print sentence.globalID
                            raise
                if any(changes):
                    applications.setdefault(
                        sentence.globalID, set()).add(str(process.__class__))
    return doSentence

def debugWrapper(doSentence):
    def debug(inLoc, key):
        log.openLog('/dev/null', 'invalid')
        ccgbank = CCGbank.CCGbank(path=inLoc)
        key = pjoin(inLoc, 'data', 'AUTO', key[4:6], key.replace('.', '.auto~'))
        s = ccgbank.sentence(key)
        print s
        #print s.validate()
        doSentence(s)
        print s
        #print s.validate()
    return debug

def reportWrapper(applications):
    def reportApplications():
        sortable = sorted(applications.items(), key=lambda a: len(a[0]))
        for sentence, processes in sortable:
            print '%s\t%s' % (sentence, '\t'.join(sorted(processes)))
    return reportApplications


def testMakerWrapper(doSentence):
    template = r"""
def %s():
    "!"
    >>> debug('%s', '%s')
    %s
    "!"
    pass
    

""".replace('"!"', '"""')
    def testMaker(start, stop, inLoc, testLoc):
        corpus = CCGbank.CCGbank(path=inLoc)
        log.openLog('/dev/null', 'invalid')
        random.seed(0)
        with open(testLoc, 'a') as testFile:
            for i in xrange(start, stop):
                file_ = corpus.child(i)
                n = file_.length()
                s = file_.child(random.randint(0, n-1))
                answer = [str(s)]
                doSentence(s)
                answer.append(str(s))
                answer = '\n'.join(answer)
                key = s.globalID
                while True:
                    response = raw_input(answer + '\n' + 'correct? y/n/q\n')
                    if response == 'y':
                        # Fix indentation
                        answer = answer.replace('\n', '\n    ')
                        slotFills = (key.replace('.', '_'), inLoc, key, answer)
                        break
                    elif response == 'n':
                        slotFills = (key.replace('.', '_'), inLoc, key, '???')
                        break
                    elif response == 'q':
                        return None
                    else:
                        response = 'correct? y/n/q'
                testCase = template % slotFills
                testFile.write(testCase)
    return testMaker

def mainWrapper(doSentence):
    inLoc, outLoc = sys.argv[1:]
    def main():
        log.openLog('/tmp/invalid.log', 'invalid')
        corpus, autoWriter, pargWriter = setup(inLoc, outLoc)
        for i in xrange(0, corpus.length()):
            file_ = corpus.child(i)
            pargLoc = file_.path.rsplit('/', 2)[0].replace('AUTO', 'PARG')
            file_.addPargDeps(pargLoc)
            #if i == 100:
            #    break
            changed = []
            pargs = []
            for sentence in file_.children():
                try:
                    doSentence(sentence)
                except:
                    print sentence.globalID
                    raise
               # if not sentence.validate():
               #     print "Invalid: %s" % sentence.globalID
                changed.append(autoWriter.getSentenceStr(sentence))
                pargs.append(pargWriter.getSentenceStr(sentence))
            autoWriter.writeFile(file_.ID, changed)
            pargWriter.writeFile(file_.ID, pargs)
    return main

def setup(inLoc, outLoc):
    outDir = pjoin(outLoc, 'data/AUTO')
    muLoc = pjoin(outLoc, 'markedup')
    autoWriter = Writers.AutoFileWriter(directory=outDir, markedup=muLoc)
    pargWriter = Writers.PargFileWriter(directory=outDir.replace('AUTO', 'PARG'),
                                        markedup=muLoc)
    ccgbank = CCGbank.CCGbank(path=inLoc)
    return ccgbank, autoWriter, pargWriter
