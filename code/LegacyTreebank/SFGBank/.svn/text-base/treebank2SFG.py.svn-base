"""
Top level for treebank conversion
All the work goes on offscreen in various modules
"""
from Treebank import Nodes
from Treebank import makeCorpus
import Constituency
from Treebank import TreeConstructors
import Converters
import FileVisiters
from general.Singleton import singleton
import sys
import copy
import cPickle


if __name__ == '__main__':
    treeText = """(S 
    (NP-SBJ 
      (NP (NNP Pierre) (NNP Vinken) )
      (, ,) 
      (ADJP 
        (NP (CD 61) (NNS years) )
        (JJ old) )
      (, ,) )
    (VP (MD will) 
      (VP (VB join) 
        (NP (DT the) (NN board) )
        (PP-CLR (IN as) 
          (NP (DT a) (JJ nonexecutive) (NN director) ))
        (NP-TMP (NNP Nov.) (CD 29) )))
    (. .) )"""
    if 1:
        printer = Converters.Printer()
        corpus = makeCorpus("/home/mhonn/Data/Treebank3_wsj/")
        converter = FileVisiters.FileController()
        controller = Converters.Controller()
        file = corpus.child(5)
       # file.performOperation(converter)
        sentence = file.child(1)
        controller.actOn(sentence)
        print sentence
        print printer.actOn(sentence.constituent)
        sys.exit(1)
    # Error analysis output
    elif 0:
        import ErrorAnalysers
        converter = FileVisiters.FileController()
        analyser = ErrorAnalysers.ConstituentHeads()
        analyser.outputDir = 'c:/workspace/grs2sfg/constituent_heads/'
        corpus = makeCorpus('c:/workspace/data/treebank/parsed/mrg/wsj/')
        for file in corpus.children():
            file.performOperation(converter)
            file.performOperation(analyser)
    else:
        # Print mode
        corpus = makeCorpus('')
        controller = NodeVisitors.Controller()
        constraintChecker = NodeVisitors.FinalConstraints()
        printer = NodeVisitors.NodePrinter()
        for i in xrange(20, corpus.length()):
            file = corpus.child(i)
            for sentence in file.children():
                print printer.actOn(sentence)
       # constraintChecker.actOn(sentence.constituent)
   # for node in sentence.constituent.depthList():
   #     print node
   # textNode = fileParser.makeNode('C:/workspace/Data/Treebank/parsed/mrg/wsj/00/wsj_0001.mrg', CorpusFile)
   # IDAdder = nodeVisitors.IDAdder()
   # textNode.performOperation(IDAdder)
   # print textNode.prettyPrint()
