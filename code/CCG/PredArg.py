"""
Class for what Hockenmaier refers to as "Category Objects: the data structure
that the parser operates over.

These consist of:
cat -- a Category object
heads -- A list of lexical heads. Can be empty.
Arg -- an argument object
Res -- a result object
"""
class AbstractPredArg:
    def argument(self):
        return _predArgs[self._argIdx]

    def result(self):
        return _predArgs[self._argIdx]

class AtomicPredArg(AbstractPredArg):
    def __init__(self, category):
        self.cat
        self.headIdx
        self._argIdx = None
        self._resIdx

    def argument(self):
        return None

    def result(self):
        return self




class ComplexPredArg(AbstractPredArg):
    def __init__(self, category, argIdx, resIdx, idx):
        self.headIdx
        self.cat = category
        self._argIdx = argIdx
        self._resIdx = resIdx


def PredArg(lexeme, category):
    if '/' in cat or '\\' in cat:
        argCat, resCat, idx = _parseComplex(category)
        arg = PredArg(None, argCat)
        res = PredArg(None, resCat)
        if arg.idx == res.idx:
            unify(arg, res)
        


def unify(cat1, cat2):
    cat = Category.unify(cat1, cat2)
    if not cat:
        return False
    heads = cat1.heads + cat2.heads
    deps = cat1.deps + cat2.deps
    arg = unify(cat1.arg, cat2.arg)
    if not arg:
        return False
    res = unify(cat1.res, cat2.res)
    if not res:
        return False
    return makePredArg(cat, heads, deps, arg, res)

def application(cat1, cat2):
    result = unify(cat1.arg, cat2)
    return result

# PredArgs must unify such that an object is replaced by another. In order
# to do this, predArgs should never be referenced directly, but instead retrieved
# from the dictionary. That way they can be replaced by their key
_predArgs = {}
