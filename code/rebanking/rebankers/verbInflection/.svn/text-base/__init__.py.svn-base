import sys

from rebanking import rebankers
from _VerbInflection import VerbInflection
from _VerbInflection import NonSInflection
from _VerbInflection import POSRelabeller
from _VerbInflection import AgentivePassive
from _VerbInflection import AgentlessPassive
#from _VerbInflection import ComlexPOSRelabeller
#from _VerbInflection import NounPluralInflection
#from _VerbInflection import AdjunctUnariser

# by-Passives have to be done first, so that the other case can catch agentless
# passives
_processes = [
    POSRelabeller(),
#    ComlexPOSRelabeller(),
    NonSInflection(),
#    AgentivePassive(),
#    AgentlessPassive(),
#    AdjunctUnariser(),
    #NounPluralInflection(),
    VerbInflection()
    ]
_applications = {}

# Use closures to supply a persistent argument
doSentence = rebankers.processWrapper(_processes, _applications)
debug = rebankers.debugWrapper(doSentence)
reportApplications = rebankers.reportWrapper(_applications)
testMaker = rebankers.testMakerWrapper(doSentence)
if __name__ == '__main__':
    debug(sys.argv[1], sys.argv[2])    
