import re

def escape(category):
    """
    Use a set of two character escapes for common non-alnum chars, but otherwise use
    CR# where # is the ordinal value of the character
    """
    # These characters are very common in supertags, and we dont want to unnecessarily
    # blow out the size of the feature strings. So specify short escapes for these
    commonEscapes = {
        '(': 'LP',
        ')': 'RP',
        '/': 'FS',
        '\\': 'BS',
        '{': 'LB',
        '}': 'RB',
        '[': 'LS',
        ']': 'RS',
        '-': '-'
    }
    escaped = []
    for char in category:
        if char.isalnum():
            escaped.append(char)
        elif char in commonEscapes:
                escaped.append(commonEscapes[char])
        else:
            escaped.append('CR%d' % ord(char))
    return ''.join(escaped)

def readMarkedUp(location):
    """
    Process the markedup file into a dictionary keyed by dependency relations.

    The values are dicts mapping arg numbers to grammatical relations
    """
    text = open(location).read()
    sansComments = '\n'.join([l for l in text.split('\n') if not l.startswith('#')])
    del text
    grDefs = sansComments.split('\n\n')
    directions = parseDirections(grDefs.pop(0))
    stagToGrs = {}
    del sansComments
    for grDef in grDefs:
        grDef = grDef.strip()
        lines = grDef.split('\n')
        stag = lines.pop(0)
        deps = lines.pop(0)
        if deps[0] != ' ':
            print grDef
            print deps
            
            raise StandardError
        deps = deps.split(' ')[3]
        grs = {}
        for gr in lines:
            num, relation = gr.split()
            int(num)
            grs[num] = relation
        stagToGrs[stag] = grs
    return stagToGrs, directions
    
from LegacyCategory import *
featStripRE = re.compile(r'\[\w+\]')
if __name__ == '__main__':
    pass
