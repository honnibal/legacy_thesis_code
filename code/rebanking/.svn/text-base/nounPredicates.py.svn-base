"""
Transform e.g.:
destruction|N of|NP\NP property|N
-->
destruction|N/PP of|PP/NP property|NP
"""
def attachAtN(npnp):
    np = npnp.sibling()
    rightChild = np.children(-1)
    while rightChild.label != CCG.N:
        rightChild = rightChild(-1)
    npnp.reattach(rightChild)
    npnp.changeLabel(CCG.Category(r'N\N'))

def adjunctToArgument(adjunct):
    head = adjunct.sibling()
    preposition, np = adjunct.children()
    assert np.label == CCG.NP
    preposition.prune()
    adjunct.delete()
    newParentLabel = CCG.addArgs(head.label, [('NP', r'/', False)])
    newParent = CCGBank.newNode(newParentLabel)
    newParent.attachChild(preposition)
    newLabel = CCG.addArgs(newParentLabel, [('PP/NP', r'/', False)])
    head.changeLabel(newLabel)
    preposition.changeLabel(CCG.Category('PP/NP'))
    
def possessiveToArgument(clitic):
    """
    (NP/N)\NP
    -->
    (NP/((N/NP)/(PP/NP)))\NP
    """
    # Romans (possessor) ' (clitic) destruction (head)
    head = clitic.sibling()
    headCat = CCG.addArguments(head.label, [('NP', '/'), ('PP/NP', '/')])
    head.changeLabel(headCat)
    cliticLabel = CCG.ComplexCategory(clitic.result, headCat, '/', clitic.conj)
    clitic.changeLabel(cliticLabel)
    
    
    
    
    
    
        
