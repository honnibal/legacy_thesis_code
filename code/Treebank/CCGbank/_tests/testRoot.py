import doctest
from _Root import CCGRoot

pierre = """(<T S[dcl] 0 2> (<T S[dcl] 1 2> (<T NP 0 2> (<T NP 0 2> (<T NP 0 2>
(<T NP 0 1> (<T N 1 2> (<L N/N NNP NNP Pierre N_73/N_73>) (<L N NNP NNP Vinken
N>) ) ) (<L , , , , ,>) ) (<T NP\NP 0 1> (<T S[adj]\NP 1 2> (<T NP 0 1> (<T N 1
2> (<L N/N CD CD 61 N_93/N_93>) (<L N NNS NNS years N>) ) ) (<L (S[adj]\NP)\NP
JJ JJ old (S[adj]\NP_83)\NP_84>) ) ) ) (<L , , , , ,>) ) (<T S[dcl]\NP 0 2> (<L
(S[dcl]\NP)/(S[b]\NP) MD MD will (S[dcl]\NP_10)/(S[b]_11\NP_10:B)_11>) (<T
S[b]\NP 0 2> (<T S[b]\NP 0 2> (<T (S[b]\NP)/PP 0 2> (<L ((S[b]\NP)/PP)/NP VB VB
join ((S[b]\NP_20)/PP_21)/NP_22>) (<T NP 1 2> (<L NP[nb]/N DT DT the
NP[nb]_29/N_29>) (<L N NN NN board N>) ) ) (<T PP 0 2> (<L PP/NP IN IN as
PP/NP_34>) (<T NP 1 2> (<L NP[nb]/N DT DT a NP[nb]_48/N_48>) (<T N 1 2> (<L N/N
JJ JJ nonexecutive N_43/N_43>) (<L N NN NN director N>) ) ) ) ) (<T
(S\NP)\(S\NP) 0 2> (<L ((S\NP)\(S\NP))/N[num] NNP NNP Nov.
((S_61\NP_56)_61\(S_61\NP_56)_61)/N[num]_62>) (<L N[num] CD CD 29 N[num]>) ) ) )
) (<L . . . . .>) )"""

def testBracketParse():
    """
    >>> parser = CCGRoot.bracketsRE
    >>> parser.search(r'(<T S[dcl] 1 2> ').groups()
    ('(', 'T S[dcl] 1 2', None, None)
    >>> parser.findall(r'(<L N NN NN director N>)')
    [('(', 'L N NN NN director N', '', ''), ('', '', '', ')')]
    """
    pass

def testRoot():
    """
    >>> root = CCGRoot(globalID="test", string=pierre)
    >>> print ' '.join([word.text for word in root.listWords()])
    Pierre Vinken , 61 years old , will join the board as a nonexecutive director Nov. 29 .
    >>> print root.isRoot()
    True
    """
    pass

def testRoot2():
    """
    
    """
    pass

def testRoot3():
    """
    
    """
    pass

def testRoot3():
    pass

if __name__ == '__main__':
    doctest.testmod()
