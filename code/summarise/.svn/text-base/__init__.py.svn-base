import sys

import summarisers
from document import Document
from standardiser import standardise
from math import log

standardise.config(stemming='porter',
                   stopping=True,
                   lower=False)

def summarise(toSummarise, metric):
    if Document.isURL(toSummarise):
        try:
            document = Document(url=toSummarise)
        except:
            return "Unable to download or parse URL"
    else:
        document = Document(text=toSummarise)
    summariser = _getSummariser(metric)
    n = int(log(len(document), 2))
#    summariser.debug(document)
    sentences = summariser(document, n)
    return _format(sentences)



print >> sys.stderr, "Initialising TF-IDF Summariser"
_tfidfSummariser = summarisers.TFIDFSummariser()
_frequencySummariser = summarisers.FrequencySummariser()
def _getSummariser(metric):
    return _tfidfSummariser
    if metric == 'TFIDF':
        return _tfidfSummariser
    elif metric == 'Frequency':
        return _frequencySummariser

def _format(sentences):
    return '\n'.join([u'<p>%s</p>' % unicode(sentence)
                      for sentence in sentences])

if __name__ == '__main__':
    print summarise('http://www.smh.com.au/national/music-teacher-jailed-for-student-sex-20091120-ipul.html',
            'Frequency', 3)        
