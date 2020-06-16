"""
Functions to reverse complement/adjunct distinctions
"""

def adjunctToAppliedArgument(constituent, argLabel):
    """
    Convert an adjunct into an argument to be applied
    """
    pred = constituent.sibling()
    newPredLabel = CCG.addArgs(pred.label, [argLabel, predSlash, None]))
    pred.changeLabel(newPredLabel)
    constituent.changeLabel(CCG.Category(argLabel))
    ##################
    # DO PARG UPDATE #
    ##################

def adjunctToTypeRaiseArgument(constituent, argLabel, slot):
    """
    Convert an adjunct into an argument that is acquired via
    type-raising and composition. e.g.
    (S[dcl]\NP)/NP (S\NP)\(S\NP) --> ((S[dcl]\NP)/PP)/NP (S\NP)\((S\NP)/PP)
    """
    pass

def adjunctToDisplacedArgument(constituent, argLabel):
    """
    Convert an adjunct into an argument that has been displaced. This involves
    making the next argument back type-raise and compose.
    e.g.
    ( S[dcl]\NP
      ( S[dcl]\NP
        ( (S[dcl]\NP)/NP )
        ( NP )
      )
      ( VP\VP )
      )
    )
    -->
    ( S[dcl]\NP
      ( (S[dcl]\NP)/ARG
        ( ((S[dcl]\NP)/NP)/ARG )
        ( ((S\NP)\((S\NP)/NP)
          ( NP )
        )
      )
      ( ARG )
      )
    )
    """
    pred = constituent.sibling()
    # Get the child on the same side of the predicate as the constituent
    if constituent < pred:
        displaced, pChild = pred.children()
        slash1 = '/'
        slash2 = '\\'
    else:
        pChild, displaced = pred.children()
        slash1 = '\\'
        slash2 = '/'
    # Do the type raise production
    t = CCG.Category(pred.label.featLess())
    result = CCG.ComplexCategory(t, displaced, slash2, False)
    typeRaised = CCG.ComplexCategory(t, result, slash1, False)
    newNode = CCGBank.newNode(typeRaised)
    displaced.insert(newNode)
    # Change the node's category
    constituent.changeLabel(argLabel)
    # Add the argument. This should propagate down to the predicate below,
    # where we type-raised
    newPredLabel = CCG.addArgs(pred.label, [argLabel, slash2])
    pred.changeLabel(newPredLabel)
    ##################
    # DO PARG UPDATE #
    ##################


def argumentToAdjunct(constituent):
    pred = constituent.sibling()
    if pred < constituent:
        slash = '\\'
    else:
        slash = '/'
    pred.changeLabel(pred.parent().label)
    # Handle type-raised arguments by trimming the production
    if constituent.label.isTypeRaise() and constituent.isUnary():
        constituent = constituent.child()
        constituent.parent().delete()
    adjunctLabel = CCG.makeAdjunct(pred.label, slash, True)
    constituent.changeLabel(adjunctLabel)
    

    
    
    
    
