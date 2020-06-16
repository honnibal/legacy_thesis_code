"""
Classes for PropBankFrameSets and their components:
RoleDefinition, VNRoleDefinition, RoleSetDefinition, RoleExample, VerbExample, RoleSetExample

These classes are just interfaces for the data, they have no methods
"""
class FrameSet:
    """
    A list of possible frames for a given verb
    
    Fields:
        - roleSets (list of RoleSetDefinitions)
        - lemma (open string)
        - notes (list of open strings)
    """
    def __init__(self, settings):
        self._initialiseData()
        for key, value in settings.items():
            setattr(self, key, value)
            
    def _initialiseData(self):
        self.roleSets = []
        self.lemma = ''
        self.note = ''
        
    def __str__(self):
        return '\n\n\n'.join([str(rs) for rs in self.roleSets])
    

class RoleSetDefinition:
    """
    PropBank `Frame' -- a configuration of Participant Roles
    
    Fields:
        - ID (regular string of the form \w+\.\d+)
        - name (open string)
        - verbnetClass (regular string of the form \d+(?:\.\d+)*)
        - roles (list of RoleDefinitions)
        - examples (RoleSetExample)
    """
    def __init__(self, settings):
        self._initialiseData()
        for key, value in settings.items():
            setattr(self, key, value)
            
    def _initialiseData(self):
        pass
        
    def __str__(self):
        lines = ['Frame: %s' % self.name]
        lines.append('')
        for rd in self.roles:
            lines.append(str(rd))
        lines.append('')
        lines.append('Examples:')
        lines.append('')
        for eg in self.examples:
            lines.append(str(eg))
            lines.append('------')
        return '\n'.join(lines)
    
class RoleDefinition:
    """
    PropBank Role
    
    Fields:
        - desc (open string)
        - number (semi-open string)
        - verbnetRole (Dictionary)
          Dictionary may be empty, or may have both:
            - class (regular string of the form: \d+(?:\.\d+)*)
            - theta (ennumerable string:
              Actor1 | Actor2 | Agent | Asset | Attribute| Beneficiary| Cause |
              Destination | Experiencer | Extent| Instrument | Location | Material |
              Patient | Patient1 | Patient2 | Predicate | Product | Recipient |
              Source | Stimulus | Theme | Theme1 | Theme2 | Time | Topic)
    """
    def __init__(self, settings):
        self._initialiseData()
        for key, value in settings.items():
            setattr(self, key, value)
            
    def _initialiseData(self):
        pass
        
    def __str__(self):
        return self.number + ': ' + self.desc


    
class RoleSetExample:
    """
    An annotated text example of a verb frame -- a configuration of Participant Roles.
    
    Fields:
        - name (open string)
        - inflection (Dictionary:
            Key     Value
            person  ennumerable string: (third | other | ns)
            tense   ennumerable string: (present | past | future | ns)
            aspect  ennumerable string: (perfect | progressive | both | ns)
            voice   ennumerable string: (active | passive | ns)
            form    ennumerable string: (infinitive | gerund | participle | full | ns)
        - roles (list of RoleExamples)
    """
    def __init__(self, settings):
        self._initialiseData()
        for key, value in settings.items():
            setattr(self, key, value)
            
    def _initialiseData(self):
        pass
        
    def __str__(self):
        return '\n'.join([str(r) for r in self.roles])
    
class RoleExample:
    """
    A slice of text annotated with Role information
    
    Fields:
        - text (open string)
        - number (semi-open string)
        - function (quasi-ennumerated string. Usually a function tag from the following set:
            EXT  extent
            LOC  location
            DIR  direction
            NEG  negation  (not in PREDITOR)
            MOD  general modification
            ADV  adverbial modification
            MNR  manner
            PRD  secondary predication
            REC  recipricol (eg herself, etc)
            TMP  temporal
            PNC  purpose no cause
            CAU  cause
        But can also be a preposition (possibly crucial for verbs Neale considers phrasal?)
    """
    def __init__(self, settings):
        self._initialiseData()
        for key, value in settings.items():
            setattr(self, key, value)
            
    def _initialiseData(self):
        pass
        
    def __str__(self):
        if self.function:
            tag = '(%s-%s)' % (self.number, self.function)
        else:
            tag = '(%s)' % self.number
        return '%s %s' % (tag, self.text)
    
class VerbExample:
    """
    The verb in a RoleSetExample
    
    Fields:
        - text (open string)
        - function (frames.dtd says: ``a rel can have an "f" attribute for a single reason, so that
         auxilliary uses of the verb "have" can be marked as such.
         There should be no other "f" attributes.''
    """
    def __init__(self, settings):
        self._initialiseData()
        for key, value in settings.items():
            setattr(self, key, value)
            
    def _initialiseData(self):
        pass
        
    def __str__(self):
        return self.text
        
def index():
    global PATH
    locations = [PATH + f for f in os.listdir(PATH) if f.endswith('.xml')]
    FSConstructor = PropBankParsers.FrameSetConstructor()
    frames = {}
    print 'Reading PropBank'
    for l in locations:
        DOM = xml.dom.minidom.parse(l)
        for predicateDOM in DOM.getElementsByTagName('predicate'):
            frameSet = FSConstructor(predicateDOM)
            frames[str(frameSet.lemma)] = frameSet
    print 'Done'
    return frames

import PropBankParsers
import os, xml
PATH = 'C:/workspace/Data/pb-frames/pb-frames/'
if __name__ == '__main__':
    frames = index()
    think = frames['hold']         
    print think
