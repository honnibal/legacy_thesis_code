"""
Use the treebank to find the IDs of quotation marks, and then remove those lines
from the conll data
"""
import Treebank, os
def getPartitions(corpus):
    files = {}
    for i, fileName in enumerate(corpus._children):
        key = fileName.split('/')[-1][4:6]
        files.setdefault(key, []).append(i)
    partitions = []
    keys = files.keys()
    keys.sort()
    for partition in keys:
        indexes = files[partition]
        start = min(indexes)
        end = max(indexes)
        partitions.append(xrange(start, end+1))
    return partitions

def rewrite(quotes, dataFile, newLoc):
    lines = []
    wordID = 0
    for line in dataFile:
        if line.strip():
            if wordID not in quotes:
                lines.append(line)
            wordID += 1
        else:
            lines.append(line)
    open(newLoc, 'w').write('\n'.join(lines))

corpus = Treebank.makeCorpus('/home/mhonn/Data/Treebank3_wsj/')
partitions = getPartitions(corpus)
path = '/home/mhonn/Data/conll05st-release/train/props/'
conllFiles = os.listdir(path)
conllFiles.sort()
for conllFile, partition in zip(conllFiles, partitions)[2:3]:
    wordID = 0
    quotes = {}
    for i in partition:
        f = corpus.child(i)
        for sentence in f.children():
            for w in sentence.listWords():
                if w.text in ["``", "''"]:
                    quotes[wordID] = True
                wordID += 1
    rewrite(quotes, os.path.join(path, conllFile), 'new_02.txt')
    break

    
