"""
Errors common to multiple modules
"""
class InstanceNumberError(StandardError):
    """
    Raised when multiple instances of a _Singleton_ class are created,
    or when an abstact class is instantiated
    """
    pass
    
class ImplementationError(StandardError):
    """
    Raised when a template method is not overridden by a subclass
    """
    pass
    
class Break:
    """
    The only way a function being called in a loop can break the loop is
    by throwing an exception. This is the class to throw in such cases.
    """
    pass
    
class ConstraintError(StandardError):
    """
    Raised when a linguistic constraint on the parse tree is not met
    """
    pass
    
class InformationError(StandardError):
    pass
    
class ProtectionError(StandardError):
    """
    Raised when a change to a tree's structure is rejected
    """
    pass
    
class QueryError(StandardError):
    """
    Raised when a query illegaly returns an empty set
    """