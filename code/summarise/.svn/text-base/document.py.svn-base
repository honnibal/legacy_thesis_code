import collections
import os
import re

#from pyquery import PyQuery
from standardiser import standardise
from nltk.tokenize import sent_tokenize as sent_tokenise
from nltk.tokenize import word_tokenize as word_tokenise
import cgi
import urllib2
from BeautifulSoup import BeautifulSoup

class Document(list):
    def __init__(self, **kwargs):
        """
        Build a list of sentences and a bag of words
        """
        list.__init__(self)
        if 'text' in kwargs:
            text = kwargs.pop('text')
        elif 'url' in kwargs:
            text = self._urlToText(kwargs.pop('url'))
        else:
            raise StandardError, "Must initialise document with text or url"
        assert not kwargs
        bow = collections.defaultdict(int)
        for i, sentenceStr in enumerate(sent_tokenise(text)):
            sentence = Sentence(sentenceStr, i)
            self.append(sentence)
            for k, v in sentence.bagOfWords.items():
                bow[k] += v
        self.bagOfWords = bow

    whiteRE = re.compile(r'\s+')
    def _urlToText(self, url):
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        body = soup.findAll('body')
        body = body[0] if body else soup
        paragraphs = []
        for paragraph in soup.findAll('p'):
            text = paragraph.string
            if text is not None:
                text = self.whiteRE.sub(' ', text.strip())
                if text and text[-1] in ['.', '!', '?'] and \
                not text.startswith(u'\u2022'):
                    paragraphs.append(text)
        return '\n'.join(paragraphs) 
        
        
    def _urlToTextPyQuery(self, url):
        html = PyQuery(url=url)
        paragraphs = []
        entities = html('p')
        for paragraph in entities:
            text = paragraph.text_content().strip()
            if text:
                text = self.whiteRE.sub(' ', text)
                if text and text[-1] in ['.', '!', '?']:
                    paragraphs.append(text)
        return '\n'.join(paragraphs)

    urlRE = re.compile(r'^(?:http://|www)\S+$')
    @staticmethod
    def isURL(url):
        # Determine whether is url by trying to parse it
        return bool(Document.urlRE.match(url))

class Sentence(list):
    def __init__(self, sentenceStr, position):
        self.string = cgi.escape(sentenceStr)
        # Lowercase the first word
        if sentenceStr[0].isupper():
            letters = list(sentenceStr)
            letters[0] = letters[0].lower()
            sentenceStr = ''.join(letters)
        tokens = word_tokenise(sentenceStr)
        bow = collections.defaultdict(int)
        for token in tokens:
            term = standardise(token)
            if term:
                bow[term] += 1
                self.append(term)
        self.bagOfWords = bow
        self.position = position

    def __unicode__(self):
        return self.string

    def __str__(self):
        return self.string.decode('utf8', 'replace')


def test():
    """
    >>> doc = Document(u"This is a document test. Let's see the test goes.")
    >>> len(doc)
    2
    >>> print max(doc.bow.items(), key=lambda kv: kv[1])
    (u'test', 2)
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
