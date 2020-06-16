"""
Corpus construction functions
"""
from TreeConstructors import *
import Nodes

def makeCorpus(location):
    """
    Instantiate a Corpus class
    """
    sentenceConstructor = SentenceConstructor()
    SWBDConstructor     = SWBDSentenceConstructor()
    fileConstructor     = FileConstructor()
    fileConstructor.addChildConstructors({'standard': sentenceConstructor, 'swbd': SWBDConstructor})
    corpusConstructor   = CorpusConstructor()
    corpusConstructor.addChildConstructors({'standard': fileConstructor})
    return corpusConstructor.make('standard', location, Nodes.Corpus)
    
def makeDBCorpus(section):
    sentenceConstructor = SentenceConstructor
    SWBDConstructor     = SWBDSentenceConstructor
    fileConstructor     = DBFileConstructor, {'standard': sentenceConstructor, 'swbd': SWBDConstructor}
    corpusConstructor   = DBCorpusConstructor, {'database': fileConstructor}
    return corpusConstructor.make('database', section, Nodes.Corpus)
    
def makeXMLCorpus(location):
    fileConstructor     = XMLFileConstructor
    corpusConstructor   = CorpusConstructor, {'standard': fileConstructor}
    fileConstructor.setPath(location)
    return corpusConstructor.make('standard', location, Nodes.Corpus)

def fileList(location):
    """
    Get all files below location
    """
    paths = []
    for path in [os.path.join(location, fileName) for fileName in os.listdir(location)]:
        if path.endswith('CVS') or path.endswith('.SVN'): continue
        if os.path.isdir(path):
            paths.extend(fileList(path))
        elif path.endswith('.mrg') or path.endswith('.auto'):
            paths.append(path)
    paths.sort()
    return paths
