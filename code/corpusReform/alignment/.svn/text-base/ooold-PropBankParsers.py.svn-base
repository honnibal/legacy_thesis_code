"""
Constructors for PropBank FrameSets.

For now, just a DOM constructor.
"""
import re, os
import xml.dom.minidom
import PropBank

def singleton(singletonClass, argument = None, singletons = {}):
    """
    Retrieve a specified _Singleton_ instance, or instantiate it if it isn't there
    """
    if not singletons.has_key(singletonClass):
        if argument:
            singletons[singletonClass] = singletonClass(argument)
        else:
            singletons[singletonClass] = singletonClass()
    return singletons[singletonClass]

class DOMConstructor:
    def __init__(self):
        self._incrementCount()


        
        
class RoleExampleConstructor(DOMConstructor):

    def _incrementCount(self, count = [0]):
        """
        Singleton class: instantiation count should not exceed 1
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceFactory instantiated"     
    
    def __call__(self, DOM):
        settings = {}
        DOM.normalize()
        # In imperatives etc, role may be 'unrealised'
        if DOM.firstChild:
            settings['text'] = DOM.firstChild.data
        else:
            settings['text'] = ''
        settings['number'] = DOM.getAttribute('n')
        settings['function'] = DOM.getAttribute('f')
        return PropBank.RoleExample(settings)
        

class VerbExampleConstructor(DOMConstructor):
        
    def _incrementCount(self, count = [0]):
        """
        Singleton class: instantiation count should not exceed 1
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceFactory instantiated"
            
    def __call__(self, DOM):
        settings = {}
        DOM.normalize()
        settings['text'] = DOM.firstChild.data
        settings['function'] = DOM.getAttribute('f')
        return PropBank.VerbExample(settings)

class ExampleConstructor(DOMConstructor):
    _argConstructor = singleton(RoleExampleConstructor)
    _verbConstructor = singleton(VerbExampleConstructor)
        
    def _incrementCount(self, count = [0]):
        """
        Singleton class: instantiation count should not exceed 1
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceFactory instantiated"
            
    def __call__(self, exampleDOM):
        settings = {}
        settings['name'] = exampleDOM.getAttribute('name')
        settings['inflection'] = self._parseInflection(exampleDOM)
        text = exampleDOM.getElementsByTagName('text')
        assert len(text) == 1
        text[0].normalize()
        settings['text'] = text[0].firstChild.data
        settings['roles'] = []
        for child in exampleDOM.childNodes:
            if child.nodeName == 'arg':
                settings['roles'].append(self._argConstructor(child))
            elif child.nodeName == 'rel':
                settings['roles'].append(self._verbConstructor(child))
        return PropBank.RoleSetExample(settings)
        
    def _parseInflection(self, exampleDOM):
        inflection = {}
        node = [c for c in exampleDOM.childNodes if c.nodeName == 'inflection']
        if not node:
            return inflection
        else:
            for attr in ['aspect', 'form', 'person', 'tense', 'voice']:
                inflection[attr] = node[0].getAttribute(attr)
            return inflection
        
class RoleConstructor(DOMConstructor):
    """
    Construct a RoleDefinition from a DOM
    Defer construction of VerbNetRole if there is one
    """
    def _incrementCount(self, count = [0]):
        """
        Singleton class: instantiation count should not exceed 1
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceFactory instantiated"
            
    def __call__(self, roleDOM):
        settings = {}
        settings['number'] = roleDOM.getAttribute('n')
        settings['desc'] = roleDOM.getAttribute('descr')
        verbnetRole = roleDOM.getElementsByTagName('vnrole')
        if verbnetRole:
            settings['verbnetRole'] = self._parseVNRole(verbnetRole[0])
        else:
            settings['verbnetRole'] = {}
        return PropBank.RoleDefinition(settings)
        
    def _parseVNRole(self, DOM):
        VNRole = {}
        VNRole['class'] = DOM.getAttribute('vncls')
        VNRole['theta'] = DOM.getAttribute('vntheta')
        return VNRole
        
class RoleSetConstructor(DOMConstructor):
    """        
    Construct a RoleSet from a DOM.
    Defer construction of components.
    """
    _roleConstructor = singleton(RoleConstructor)
    _exampleConstructor = singleton(ExampleConstructor)
    
    def _incrementCount(self, count = [0]):
        """
        Singleton class: instantiation count should not exceed 1
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceFactory instantiated"
            
    def __call__(self, roleSetDOM):
        settings = {}
        # Get settings from attributes
        for setting, attribute in [('id', 'id'), ('name', 'name'), ('verbnetClass', 'vnclass')]:
            settings[setting] = roleSetDOM.getAttribute(attribute)
        # Get roles
        settings['roles'] = []
        for role in roleSetDOM.getElementsByTagName('role'):
            settings['roles'].append(self._roleConstructor(role))
        # Get example
        examples = [c for c in roleSetDOM.childNodes if c.nodeName == 'example']
        settings['examples'] = []
        for e in examples:
            settings['examples'].append(self._exampleConstructor(e))
        return PropBank.RoleSetDefinition(settings)

class FrameSetConstructor(DOMConstructor):
    """
    Defer construction of roleSets to another constructor
    """
    _roleSetConstructor = singleton(RoleSetConstructor)
    
    def _incrementCount(self, count = [0]):
        """
        Singleton class: instantiation count should not exceed 1
        """
        count[0] += 1
        if count[0] > 1:
            raise InstanceNumberError, "Second instance of _Singleton_ class SentenceFactory instantiated"
        
    def __call__(self, predicate):
        settings = {}
        settings['lemma'] = predicate.getAttribute('lemma')
        notes = [c for c in predicate.childNodes if c.nodeName == 'note']
        settings['note'] = []
        for note in notes:
            # Normalise merges adjacent text nodes, ensuring that all of the text is retreived
            note.normalize()
            settings['note'].append(re.sub('\s+', ' ', note.firstChild.data).strip())
        settings['roleSets'] = []
        roleSets = [c for c in predicate.childNodes if c.nodeName == 'roleset']
        for roleSet in roleSets:
            settings['roleSets'].append(self._roleSetConstructor(roleSet))
        return PropBank.FrameSet(settings)                
    

    
               
if __name__ == '__main__':
    frames = PropBank.frames()
    print len(frames.keys())
    
    
    
    
    
    