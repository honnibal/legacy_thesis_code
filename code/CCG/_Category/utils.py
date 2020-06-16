def makeAdjunct(category, catSlash, forceDep = False):
    global VP
    new = copy(category)
    if not new.isComplex():
        x = new
    if forceDep and new.isAdjunct():
        x = new
    elif new == r'S\NP':
        x = new
    elif new.innerResult() != 'S':
        x = new
    else:
        lastCat = new
        #Select either: an adjunct, S\NP, or an atom
        for result, argument, slash, morph in new.deconstruct():
            # Ensure the slash directions work
            # If the functor's to the left, cannot cross-compose into a backslash -- unless not complexAdj!s
            if catSlash == '/' and slash == '\\':
                continue
            # Don't back-cross compose into non-S
            if catSlash == '\\' and slash == '/' and result.innerResult() != 'S':
                continue
            if result == r'S\NP':
                x = result
                break
            elif not result.isComplex():
                x = result
                break
            elif result.isAdjunct():
                x = result
                break
            # In case the slashes don't work out for a while (ie cross composition), store the last valid
            # place to compose into, and its arg set
            lastCat = result
        else:
            x = lastCat
    # Don't remove features if it's a "fake" adjunct like S[dcl]/S[ng]
    if not (x.result == x.argument) and not x.isAdjunct():
        x = copy(x)
        _removeFeatures(x)
    newFunctor = ComplexCategory(x, x, catSlash, False)
    return newFunctor

def _removeFeatures(cat):
    if cat.isComplex():
        cat.morph = None
        for result, argument, slash, morph in cat.deconstruct():
            _removeFeatures(result)
            _removeFeatures(argument)
    else:
        cat.feature = ''
        cat.morph = None



                


def testAdjunct(forceDep):
    cats, index = Markedup.getEntries('~/Data/markedupFiles/markedup_v4.2')
    for category in index.keys():
        category = Category(category)
        for slash in ['/', '\\']:
            adjunct = makeAdjunct(category, slash, forceDep)
            print "Category: %s" % category
            print slash
            print "Adjunct: %s" % adjunct
            if slash == '/':
                combined = validate(adjunct, category, category, True)
            else:
                combined = validate(category, adjunct, category, True)
            if not combined:
                print 'Fail'
            else:
                print 'Pass'



def validate(origLeft, origRight, label):
    """
    See which (if any) rules can generate the label from the two
    other categories
    """
    global functions, unaryFunctions, unaryRules, binaryRules, ruleFreq
    def new():
        return copy(origLeft), copy(origRight)
    if origRight == None:
        if unaryRules.get(str(origLeft), {}).get(str(label), 0):
            stats.count('Valid unary look-up')
            return True
        elif label == 'TOP':
            return True
        else:
            for function in unaryFunctions:
                guess = function(origLeft, label)
                # Unary rules are 'open ended', so compare against the parent within the rule
                if guess:
                    return True
                left, right = new()
            stats.count('Invalid unary look-up')
            return False
   # bKey = (origLeft.morphLess(), origRight.morphLess())
    bKey = (str(origLeft), str(origRight))
    if binaryRules.get(bKey, {}).get(str(label), 0) > ruleFreq:
        stats.count('Valid binary look-up')
        return True
    labelStr = str(label)
    left, right = new()
    for function in functions:
        guess = function(left, right)
        # Hack to never produce nb feat
        guessStr = str(guess).replace('[nb]', '')
        if guessStr == labelStr.replace('[nb]', ''):
            return True
        if guess != None:
            left, right = new()
    stats.count('Uncombinable production')
    return False

def combine(origLeft, origRight):
    """
    Get the set of labels that could be applied to the two cats
    """
    global unaryRules
    if not origRight:
        return unaryRules.get(str(origLeft), {})
    cats = {}
    def new():
        return copy(origLeft), copy(origRight)
    left, right = new()
    for function in functions:
        newCat = function(left, right)
        if newCat:
            cats[newCat] = True
            left, right = new()
    return cats

def getRule(origLeft, origRight, answer = None):
    def new():
        return copy(origLeft), copy(origRight)
    answers = {}
    seenRight = False
    for function in functions:
        left, right = new()
        combined = function(left, right)
        general.debug(function, 5)
        general.debug(combined, 5)
        if combined:
            if answer and isIdentical(combined, answer):
                seenRight = True
            answers[function] = combined
    return seenRight, answers

def combineChildren(parent, origLeft, origRight):
    if not origRight:
        newCat = parent.unify(origLeft)
        if newCat:
            return newCat
        typeRaised = parent
        while typeRaised != origLeft:
            if typeRaised.isComplex():
                typeRaised = typeRaised.argument
            else:
                break
        # If we can't unify, we at least need to head share.
        newCat = typeRaised.unify(origLeft)
        if not newCat:
            origLeft.headShare(parent)
            return parent
        else:
            return newCat
    def new():
        return copy(origLeft), copy(origRight)
    left, right = new()
    assert parent
    for function in functions:
        newCat = function(left, right)
        if str(newCat) == str(parent):
            newerCat = function(origLeft, origRight)
            newerCat.unify(parent)
            return newerCat
        elif newCat:
            left, right = new()
    return False

def setRuleFreq(newFreq):
    global ruleFreq
    ruleFreq = newFreq


def isIdentical(cat1, cat2):
    """
    Do a string based comparison of the categories
    """
    if str(cat1) == str(cat2):
        return True
    else:
        return False


def addArgs(result, args):
    """
    Build the category that results from progressively adding the
    given arguments
    """
    if isinstance(result, str):
        result = Category(result)
    else:
        result = copy(result)
    for arg, slash, morph in args:
        result = ComplexCategory(result, copy(arg), slash, False)
        result.morph = copy(morph)
    return result

def addArg(result, arg, slash, morph=False):
    """
    Add a single argument to the result
    """
    if isinstance(arg, str):
        arg = Category(arg)
    return addArgs(result, [(arg, slash, morph)])

def debug():
    print ruleFreq
