"""
Simple wrapper for nltk sentenciser and ptb tokeniser
"""
import re
import nltk.data
import nltk.tokenize


def sentenceAndTokenise(text):
    """
    Detect sentence boundaries using the Punkt module, and split sentences
    into tokens using the PunktWordTokenizer, after splitting off final period
    """
    global _sentenciser, _tokeniser, _periodFixRE
    sentences = []
    # Split into sentences using the Punkt unsupervised model described by
    # Kiss, Tibor and Strunk, Jan (2006): Unsupervised Multilingual Sentence
    # Boundary Detection.  Computational Linguistics 32: 485-525.
    for sentence in _sentenciser.tokenize(text.strip()):
        tokens = _tokeniser.tokenize(sentence)
        sentences.append(tokens)
    return sentences

def tokenise(text):
    return _tokeniser.tokenize(text)

whiteRE = re.compile(r'\s+')
def sentencise(text):
    text = whiteRE.sub(' ', text)
    return _sentenciser.tokenize(text.strip())
    

def _test():
    r"""
    >>> text = 'Punkt knows that the periods in Mr. Smith and Johann S. Bach do not mark sentence boundaries. And sometimes sentences can start with non-capitalized words.  i is a good variable name.'
    >>> sentenceAndTokenise(text)
    [['Punkt', 'knows', 'that', 'the', 'periods', 'in', 'Mr', 'Smith', 'and', 'Johann', 'S', 'Bach', 'do', 'not', 'mark', 'sentence', 'boundaries'], ['And', 'sometimes', 'sentences', 'can', 'start', 'with', 'non', 'capitalized', 'words'], ['i', 'is', 'a', 'good', 'variable', 'name']]
    """
    pass

_sentenciser = nltk.data.load('tokenizers/punkt/english.pickle')
_tokeniser = nltk.tokenize.WordTokenizer() # Note that this discards punctuation
if __name__ == '__main__':
    import doctest
    doctest.testmod()

