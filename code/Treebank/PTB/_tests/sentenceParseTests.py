import doctest
from Treebank.PTB import PTBSentence as RootNode

def parse():
    """
    >>> node = RootNode(string=s, globalID="")
    >>> print node.label
    S
    >>> print ' '.join(['%s_%d' % (w.text, w.wordID) for w in node.listWords()])
    Pierre_0 Vinken_1 ,_2 61_3 years_4 old_5 ,_6 will_7 join_8 the_9 board_10 as_11 a_12 nonexecutive_13 director_14 Nov._15 29_16 ._17
    >>> print node.isRoot()
    True
    """
    pass

def parseAsbestos():
    """
    >>> node = RootNode(string=asbestos, globalID="")
    >>> print ' '.join(['%s_%d' % (w.text, w.wordID) for w in node.listWords()])
    A_0 form_1 of_2 asbestos_3 once_4 used_5 *_6 *_7 to_8 make_9 Kent_10 cigarette_11 filters_12 has_13 caused_14 a_15 high_16 percentage_17 of_18 cancer_19 deaths_20 among_21 a_22 group_23 of_24 workers_25 exposed_26 *_27 to_28 it_29 more_30 than_31 30_32 years_33 ago_34 ,_35 researchers_36 reported_37 0_38 *T*-1_39 ._40
    """
    pass

s = """(S 
    (NP-SBJ 
      (NP (NNP Pierre) (NNP Vinken) )
      (, ,) 
      (ADJP 
        (NP (CD 61) (NNS years) )
        (JJ old) )
      (, ,) )
    (VP (MD will) 
      (VP (VB join) 
        (NP (DT the) (NN board) )
        (PP-CLR (IN as) 
          (NP (DT a) (JJ nonexecutive) (NN director) ))
        (NP-TMP (NNP Nov.) (CD 29) )))
    (. .) )"""

asbestos = """(S 
    (S-TPC-1 
      (NP-SBJ 
        (NP 
          (NP (DT A) (NN form) )
          (PP (IN of) 
            (NP (NN asbestos) )))
        (RRC 
          (ADVP-TMP (RB once) )
          (VP (VBN used) 
            (NP (-NONE- *) )
            (S-CLR 
              (NP-SBJ (-NONE- *) )
              (VP (TO to) 
                (VP (VB make) 
                  (NP (NNP Kent) (NN cigarette) (NNS filters) )))))))
      (VP (VBZ has) 
        (VP (VBN caused) 
          (NP 
            (NP (DT a) (JJ high) (NN percentage) )
            (PP (IN of) 
              (NP (NN cancer) (NNS deaths) ))
            (PP-LOC (IN among) 
              (NP 
                (NP (DT a) (NN group) )
                (PP (IN of) 
                  (NP 
                    (NP (NNS workers) )
                    (RRC 
                      (VP (VBN exposed) 
                        (NP (-NONE- *) )
                        (PP-CLR (TO to) 
                          (NP (PRP it) ))
                        (ADVP-TMP 
                          (NP 
                            (QP (RBR more) (IN than) (CD 30) )
                            (NNS years) )
                          (IN ago) )))))))))))
    (, ,) 
    (NP-SBJ (NNS researchers) )
    (VP (VBD reported) 
      (SBAR (-NONE- 0) 
        (S (-NONE- *T*-1) )))
    (. .) )"""

if __name__ == '__main__':
    doctest.testmod()
