"""
Align propbank with treebank 2 or 3
"""
import PTB, os
def pbVerbLocs(location):
    """
    Read in the standoff format of propbank and get a list of
    (file, sentence, token, lemma) tuples from it
    """
    verbs = []
    for line in open(location):
        pieces = line.strip().split()
        loc = '/home/mhonn/Data/Treebank3_%s' % pieces[0]
        sentence = int(pieces[1])
        token = int(pieces[2])
        lemma = pieces[4].split('.')[0]
        verbs.append((loc, sentence, token, lemma))
    return verbs

def matchToken(verbLoc, parsedFile):
    sentence = parsedFile.child(verbLoc[1])
    token = sentence.listWords()[verbLoc[2]]
    return (token, verbLoc[3])
    

os.environ['DATAPATH'] = '/home/mhonn/Data'
corpus = PTB.makeCorpus('/home/mhonn/Data/Treebank3_wsj/')
verbLocs = pbVerbLocs('/home/mhonn/Data/propbank_1/data/prop.txt')
currLoc = None
currFile = None
for verbLoc in verbLocs:
    if currLoc != verbLoc[0]:
        currLoc = verbLoc[0]
        print verbLoc
        currFile = corpus.file(verbLoc[0])
    token, lemma = matchToken(verbLoc, currFile)
    if not token.label.startswith('V'):
        print token
        print verbLoc
