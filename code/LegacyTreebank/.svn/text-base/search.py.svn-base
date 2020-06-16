#!/usr/bin/python2.4
"""
Find sentences or examples, by specifying a particular word, tag, or location.

Interface:
-tb <path> -- Specify a particular treebank

-s <file> -- Start search at a particular file (either file name or number)
-e <file> -- Don't seek past a particular file (either name or number)
--sent <location> -- Look for a particular sentence. This can be of the form wsj_0003.1, or just list index like 2.0

--cat Search for a particular category
--word Search for a particular word
-p --pipe: Pipe mode -- do not prompt user to display next file
"""
from optparse import OptionParser
import Treebank
from Treebank.NodeVisitors import NodePrinter
import sys, os
TB_LOC = '/home/mhonn/Data/Treebank3_wsj/'


def getOptions(tbLoc):
    op = OptionParser()
    op.add_option('--tb', action='store', type='string', dest='tbLoc', default=tbLoc, help='Treebank location')
    op.add_option('-s', '--start', action='store', type='string', dest='start', default='0', help='Start search at a particular file (either file name or number)')
    op.add_option('-e', '--end', action='store', type='string', dest='end', default='2312', help="Don't seek past a particular file (either name or number)")
    op.add_option('--sent', action='store', type='string', dest='sent', help="Look for a particular sentence. This can be of the form wsj_0003.1, or just list index like 2.0")
    op.add_option('-c', '--cat', action='store', type='string', dest='cat', help='Search for a particular category')
    op.add_option('-w', '--word', action='store', type='string', dest='word', help='Search for a particular word')
    op.add_option('-p', '--pipe', action='store_true', dest='pipe', default=False, help='Pipe mode -- do not prompt user to continue')
    options, args = op.parse_args()
    return options

def getRange(options):
    """
    Get the start and end points to search through
    """
    # If sent specified, we know the file
    if options.sent:
        value = options.sent
        if '.' in value:
            fileString, sentString = value.split('.')
            sentIdx = int(sentString)
            start = parseFile(fileString, options)
            return start, start, sentIdx
        else:
            print "Haven't implemented search by absolute sentence index yet."
            sys.exit(1)
    else:
        start = parseFile(options.start)
        end = parseFile(options.end)
        return start, end, None

def parseFile(fileString, options):
    if fileString.startswith('wsj_'):
        section = fileString[4:6]
        filePath = os.path.join(options.tbLoc, section, fileString + EXT)
        return filePath
    elif fileString.isdigit():
        return int(fileString)
    else:
        print "Could not parse file specifier: %s" % fileString
        sys.exit(1)
        

def getExamples(corpus, start, end, sentIdx, word, cat):
    if sentIdx:
        tbFile = getFile(corpus, start)
        print sentIdx
        yield tbFile.child(sentIdx)
    else:
        print "Search by word or category not supported yet"
        sys.exit(1)

def getFile(corpus, start):
    if type(start) == str:
        return corpus.file(start)
    else:
        return corpus.child(start)

def getCorpus(location):
    return Treebank.makeCorpus(location)

def main(corpus, options):
    printer = NodePrinter()

    start, end, sentIdx = getRange(options)
    for example in getExamples(corpus, start, end, sentIdx, options.word, options.cat):
        print printer.actOn(example)
        if not options.pipe:
            raw_input('Press any key for next sentence.')

EXT = '.mrg'
if __name__ == '__main__':
    options = getOptions(TB_LOC)
    corpus = getCorpus(options.tbLoc)
    main()

