"""
Class for storing the metafunctional analyses of clauses --
both system selections and function structures
"""
class Metafunction:
    """
    Interface:
    
    systems
    function
    label
    """
    def __init__(self):
        self._initialiseData()

    def _initialiseData(self):
        self.label = ''
        self.function = ''
        self.systems = {}
        self.childFunctions = {}
        
    def __getattr__(self, functionName):
        if self.childFunctions.has_key(functionName):
            if (functionName in ['finite', 'subject', 'topicalTheme', 'process']) and (self.childFunctions[functionName]):
                return self.childFunctions[functionName][0]
            else:
                return self.childFunctions[functionName]
        else:
            return []
            
    def __eq__(self, other):
        raise StandardError