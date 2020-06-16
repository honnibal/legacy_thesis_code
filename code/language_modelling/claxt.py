"""
Classify text with a language model class that supports an evaluate(text)
function that returns a log probability of the text.
"""
import os, sys, re

import nltk.tokenize
import LM

def localPath(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))


class TextClassifier:
    def __init__(self, lmClass, vocab):
        """
        Set the language model class that allows the evaluation
        """
        self.vocab = vocab
        self.lmClass = lmClass
        self.models = {}
        
    def trainLang(self, language, instances):
        """
        Train the model on some set of language instances. Start and stop
        words should be inserted into the tokenised text. Text can be tokenised
        as word or letter objects. Instances should be hashable sequences.
        """
        model = self.lmClass(language, self.vocab)
        model.train(text=instances)
        self.models[language] = model

    def classify(self, text):
        """
        Classify some appropriately pre-processed text
        """
        scores = {}
        for name, model in self.models.items():
            score = model.evaluate(text)
            scores[name] = score
        return self.argmax(scores)

    def quickClassify(self, text):
        """
        Find the ngram frequencies of some appropriately preprocessed text once
        and use those to classify
        """
        aModel = self.models.values()[0]
        freqs = aModel.getFreqs(text)
        scores = {}
        for name, model in self.models.items():
            score = model.evaluateFreqs(freqs)
            scores[name] = score
        return self.argmax(scores)

    def argmax(self, scores):
        scoreList = [(s, m) for m, s in scores.items()]
        scoreList.sort()
        scoreBest, nameBest = scoreList[-1]
        return nameBest, scoreBest

##################
# Pre-processing #
##################

class Preprocessor:
    def splitSentences(self, text):
        raise StandardError

    def tokenise(self, sentence):
        raise StandardError
    
    def __call__(self, text):
        """
        Preprocess a string into a list of tokenised sentences, inserting start and
        end words
        """
        sentences = self.splitSentences(text)
        instances = []
        for sentence in sentences:
            tokens = self.tokenise(sentence)
            tokens.insert(0, '_START_')
            tokens.append('_END')
            instances.append(tuple(tokens))
        return instances

class DumbPreprocessor(Preprocessor):
    def splitSentences(self, text):
        text = text.replace('\n', ' ')
        text = re.sub(' +', ' ', text)
        return [s for s in text.split('. ') if s]

    def tokenise(self, sentence):
        return sentence.strip().split()

class NLTKPreprocessor(Preprocessor):
    def splitSentences(selt, text):
        text = text.replace('\n', ' ')
        text = re.sub(' +', ' ', text)
        return nltk.tokenize.sent_tokenize(text)

    def tokenise(self, sentence):
        return nltk.tokenize.word_tokenize(sentence)

class LetterPreprocessor(DumbPreprocessor):
    def tokeniser(sentence):
        return list(sentence)

######################
# Running experiment #
######################

def experiment(testDir, trainDir, modelClass, preprocessor):
    print "Loading vocab"
    vocab = loadVocab()
    classifier = TextClassifier(modelClass, vocab)
    languages = os.listdir(trainDir)
    languages.sort()
    print "TRAINING"
    for aLang in languages:
        print aLang
        trainSet = makeTrainSet(os.path.join(trainDir, aLang), preprocessor)
        classifier.trainLang(aLang, trainSet)
    answers = os.listdir(testDir)
    results = {}
    correct = 0.0
    total = 0
    print "TESTING"
    for answer in answers:
        texts = os.listdir(os.path.join(testDir, answer))
        for textName in texts:
            text = open(os.path.join(testDir, answer, textName)).read()
            guess, score = classifier.quickClassify(preprocessor(text))
            results.setdefault(answer, {}).setdefault(guess, 0)
            results[answer][guess] += 1
            if answer == guess:
                correct += 1.0
            total += 1
    print correct/total
    print correct
    print total
    return results, correct/total

def makeTrainSet(trainLoc, preprocessor):
    """
    Make a set of training instances from multiple texts
    """
    allInstances = []
    texts = os.listdir(trainLoc)
    for i, textName in enumerate(texts):
        text = open(os.path.join(trainLoc, textName)).read()
        instances = preprocessor(text)
        allInstances.extend(instances)
    return allInstances

def loadVocab():
    dfLoc = localPath('wiki_doc_freqs.dat')
    freqs = []
    for line in open(dfLoc):
        term, freq = line.split('\t')
        freqs.append((int(freq), term))
    vocab = {}
    for i, (freq, term) in enumerate(sorted(freqs)):
        vocab[term] = i+1
    return vocab
    

def main():
    
    path = sys.argv[1]
    train = os.path.join(path, '20news-bydate-train')
    test = os.path.join(path, '20news-bydate-test')
    preprocessor = NLTKPreprocessor()
    LM.N = 2
    LM.K = 10
    results = experiment(train, test, LM.KatzLanguageModel, preprocessor)

if __name__ == '__main__':
    main()

    
