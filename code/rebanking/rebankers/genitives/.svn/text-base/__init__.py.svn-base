from _Genitives import PPGenitives, GenitiveSuperlatives
from rebanking import rebankers
import sys

_processes = [PPGenitives()]
_applications = {}

# Use closures to supply a persistent argument
doSentence = rebankers.processWrapper(_processes, _applications)
debug = rebankers.debugWrapper(doSentence)
reportApplications = rebankers.reportWrapper(_applications)
testMaker = rebankers.testMakerWrapper(doSentence)

if __name__ == '__main__':
    testMaker(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])    
