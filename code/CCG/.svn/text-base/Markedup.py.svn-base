"""
Interface for markedup entries
"""
import re
import CCG
import data
import math
class StringEntry(object):
    """
    Markedup entry where categories are stored as strings
    """
    categoriesSeen = {}
    def __init__(self, entryText):
        comments = []
        category = None
        annot = None
        grs = []
        lexConstraints = []
        self.entryText = entryText
        for line in entryText.split('\n'):
            if not line.strip():
                continue
            if line.startswith('#'):
                comments.append(line)
            elif not category:
                category = line
            else:
                if line.startswith('='):
                    lexConstraints.append(line)
                elif not annot:
                    numGrs, annot = line.strip().split()
                    self.numGrs = numGrs
                else:
                    grs.append(line)
        self.comments = comments
        self.cat = category
        seenCats = StringEntry.categoriesSeen
        self.catID = seenCats.setdefault(category, len(seenCats))
     #   print annot
        self.annot = annot
        self.grs = grs
        self.lexConstraints = lexConstraints

    def __str__(self):
        return self.entryText + '\n'

    argNumRE = re.compile(r'<\d+>')
    indexRE = re.compile(r'\{[A-Z*]+\}')
    def toJulia(self):
        """
        Translate markedup-style category annotation into Julia style
        annotation
        """
        cat = self.annot
        cat = self.argNumRE.sub('', cat)
        cat = cat.replace('{_}', '')
        cat = cat.replace('[X]', '')
        indexes = self.indexRE.findall(cat)
        for index in indexes:
            # Add the category's id, in case we need uniqueness
            idx = self.catID + ord(index[1])
            replacement = '_%d' % (idx)
            if '*' in index:
                # Add long-range indicated
                replacement = replacement + ':B'
            cat = cat.replace(index, replacement)
        if cat.startswith('('):
            if not cat.endswith(')'):
                print cat
                raise StandardError
            return cat[1:-1]
        else:
            return cat


class ObjectEntry(StringEntry):
    def __init__(self, entryText):
        StringEntry.__init__(self, entryText)
        self.cat = CCG.Category(self.cat)
        self.entryText = entryText

    def _annotResult(self, annot):
        """
        Strip off the last arg of the annotated category, without using
        the CCG.Category class (as we need the annotation)
        """
        depth = 0
        for i, char in enumerate(annot):
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif depth == 1 and char in ['/', '\\', '^']:
                # We must start at 1, as we don't want the first bracket -- as that matches
                # the bracket at the end
                annot = annot[1:i]
                # remove arg def
                if annot.endswith('>'):
                     annot = annot[:-3]
                break
        return annot

    
        

def indexVariables(cat):
    """
    Make a dictionary keyed by head indices, valued by the categories that
    have that index and their start and end in the markedup string
    """
    def updateVarIdx(*dicts):
        """Merg list-valued dicts into varIdx in outer scope"""
        for varDict in dicts:
            for var, cats in varDict.items():
                varIdx.setdefault(var, {}).update(cats)
    debug = False
    pieces = cat.split('^', 1)
    if len(pieces) == 2:
        pre, hat = pieces
    else:
        hat = False
    # Categories where the whole thing is hatted
    if hat and pre.count('(') == pre.count(')'):
        if '/' in pre or '\\' in pre:
            baseVars = indexVariables(pre)
        else:
            baseVars = {}
        if '/' in hat or '\\' in hat or '^':
            hatVars = indexVariables(hat)
        else:
            hatVars = {}
        x, pre = _stripOuterVar(pre)
        x, hat = _stripOuterVar(hat)
        varIdx = {'0': {cat: True, pre: True, hat: True}}
        updateVarIdx(baseVars, hatVars)
        return varIdx
    # Atomic categories
    elif '/' not in cat and '\\' not in cat:
        var, cat = _stripOuterVar(cat)
        return {var: {cat: True}}
    # Complex categories
    else:
        var, cat = _stripOuterVar(cat)
        varIdx = {'0': {cat: True}}
        result, arg = _splitArg(cat)
        argVars = indexVariables(arg)
        resVars = indexVariables(result)
        updateVarIdx(resVars, argVars)
        return varIdx
        
def _stripOuterVar(cat):
    """Remove annotation and brackets from cat, returning variable"""
    if cat.endswith('>'):
        cat = cat[:-3]
    if cat.endswith('}'):
        cat = cat[:-1]
    if cat.endswith('*'):
        cat = cat[:-1]
    var = cat[-1]
    cat = cat[:-2]
    if '^' in cat:
        pre, hat = cat.split('^', 1)
        if pre.count('(') == pre.count(')'):
            return var, cat
    if cat.endswith(')'):
        cat = cat[1:-1]
    return var, cat

def _splitArg(cat):
    """Split complex category into result and argument"""
    depth = 0
    seenHat = False
    inHat = False
    for i, char in enumerate(cat):
        if char == '(':
            depth += 1
            if seenHat:
                inHat = True
        elif char == ')':
            depth -= 1
            if depth == 0:
                inHat = False
        elif char == '^':
            seenHat = True
        elif depth == 0 and not inHat and char in ['/', '\\']:
            result = cat[:i]
            arg = cat[i+1:]
            return result, arg
    return cat, None

def deconstruct(annot):
    var, annot = _stripOuterVar(annot)
    result, arg = _splitArg(annot)
    while arg:
        yield result, arg, var
        var, result = _stripOuterVar(result)
        result, arg = _splitArg(result)
                    
                
def getEntries(fileLoc, **kwargs):
    muClass = kwargs.get('markedupClass', StringEntry)
    header, text = open(fileLoc).read().split("# now list the markedup categories")
    entryTexts = text.split('\n\n')
    entries = []
    index = {}
    for entryText in entryTexts:
        if not entryText.strip():
            continue
        try:
            entry = muClass(entryText)
        except:
            print entryText
            raise
        entries.append(entry)
        index[entry.cat] = entry.annot
    return entries, index

if __name__ == '__main__':
    entries, index = getEntries(data.origMarkedup, markedupClass=ObjectEntry)
    for entry in entries:
        print entry.toJulia()
