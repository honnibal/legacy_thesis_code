import doctest
from rebanking.rebankers.verbInflection import debug
def wsj_0201_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0201.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Rolls-Royce)
              (N
                (N/N Motor)
                (N
                  (N/N Cars)
                  (N Inc.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[to]\NP)
                  (((S[dcl]\NP)/(S[to]\NP))/NP expects)
                  (NP
                    (NP[nb]/N its)
                    (N
                      (N/N U.S.)
                      (N sales))))
                (S[to]\NP
                  ((S[to]\NP)/(S[b]\NP) to)
                  (S[b]\NP
                    (S[b]\NP
                      (S[b]\NP
                        ((S[b]\NP)/(S[adj]\NP) remain)
                        (S[adj]\NP steady))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP at)
                        (NP
                          (N
                            (N/N
                              ((N/N)/(N/N) about)
                              (N/N 1,200))
                            (N cars)))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N 1990)))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Rolls-Royce)
              (N
                (N/N Motor)
                (N
                  (N/N Cars)
                  (N Inc.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[to]\NP)
                  (((S[dcl]\NP)/(S[to]\NP))/NP
                    (((S[b]\NP)/(S[to]\NP))/NP expect)
                    ((S[dcl]\NP)\(S[b]\NP) -es))
                  (NP
                    (NP[nb]/N its)
                    (N
                      (N/N U.S.)
                      (N sales))))
                (S[to]\NP
                  ((S[to]\NP)/(S[b]\NP) to)
                  (S[b]\NP
                    (S[b]\NP
                      (S[b]\NP
                        ((S[b]\NP)/(S[adj]\NP) remain)
                        (S[adj]\NP steady))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP at)
                        (NP
                          (N
                            (N/N
                              ((N/N)/(N/N) about)
                              (N/N 1,200))
                            (N cars)))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N 1990)))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0202_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0202.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N BELL)
              (N
                (N/N INDUSTRIES)
                (N Inc.))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/NP increased)
                (NP
                  (NP[nb]/N its)
                  (N quarterly)))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP to)
                (NP
                  (N
                    (N/N 10)
                    (N cents)))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP from)
              (NP
                (NP
                  (N
                    (N/N seven)
                    (N cents)))
                (NP\NP
                  ((NP\NP)/N a)
                  (N share))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N BELL)
              (N
                (N/N INDUSTRIES)
                (N Inc.))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/NP
                  ((S[b]\NP)/NP increase)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (NP
                  (NP[nb]/N its)
                  (N quarterly)))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP to)
                (NP
                  (N
                    (N/N 10)
                    (N cents)))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP from)
              (NP
                (NP
                  (N
                    (N/N seven)
                    (N cents)))
                (NP\NP
                  ((NP\NP)/N a)
                  (N share))))))
        (. .)))
    True
    """
    pass
    


def wsj_0203_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0203.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N Investors))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[ng]\NP) are)
            (S[ng]\NP
              ((S[ng]\NP)/(S[to]\NP)
                (((S[ng]\NP)/(S[to]\NP))/PP appealing)
                (PP
                  (PP/NP to)
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N Securities)
                      (N
                        (conj and)
                        (N
                          (N/N Exchange)
                          (N Commission)))))))
              (S[to]\NP
                ((S\NP)/(S\NP) not)
                (S[to]\NP
                  ((S[to]\NP)/(S[b]\NP) to)
                  (S[b]\NP
                    ((S[b]\NP)/NP limit)
                    (NP
                      (NP
                        (NP[nb]/N their)
                        (N access))
                      (NP\NP
                        ((NP\NP)/NP to)
                        (NP
                          (NP
                            (N information))
                          (NP\NP
                            ((NP\NP)/NP about)
                            (NP
                              (NP
                                (N
                                  (N/N stock)
                                  (N
                                    (N purchases)
                                    (N[conj]
                                      (conj and)
                                      (N sales)))))
                              (NP\NP
                                ((NP\NP)/NP by)
                                (NP
                                  (N
                                    (N/N corporate)
                                    (N insiders)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N Investors))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[ng]\NP) are)
            (S[ng]\NP
              ((S[ng]\NP)/(S[to]\NP)
                (((S[ng]\NP)/(S[to]\NP))/PP
                  (((S[b]\NP)/(S[to]\NP))/PP appeal)
                  ((S[ng]\NP)\(S[b]\NP) -ing))
                (PP
                  (PP/NP to)
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N Securities)
                      (N
                        (conj and)
                        (N
                          (N/N Exchange)
                          (N Commission)))))))
              (S[to]\NP
                ((S\NP)/(S\NP) not)
                (S[to]\NP
                  ((S[to]\NP)/(S[b]\NP) to)
                  (S[b]\NP
                    ((S[b]\NP)/NP limit)
                    (NP
                      (NP
                        (NP[nb]/N their)
                        (N access))
                      (NP\NP
                        ((NP\NP)/NP to)
                        (NP
                          (NP
                            (N information))
                          (NP\NP
                            ((NP\NP)/NP about)
                            (NP
                              (NP
                                (N
                                  (N/N stock)
                                  (N
                                    (N purchases)
                                    (N[conj]
                                      (conj and)
                                      (N sales)))))
                              (NP\NP
                                ((NP\NP)/NP by)
                                (NP
                                  (N
                                    (N/N corporate)
                                    (N insiders)))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0204_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0204.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP[nb]/N
                    (NP
                      (NP[nb]/N The)
                      (N nation))
                    ((NP[nb]/N)\NP 's))
                  (N
                    (N/N largest)
                    (N
                      (N/N pension)
                      (N fund))))
                (, ,))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) which)
                (S[dcl]\NP
                  (S[dcl]\NP
                    ((S[dcl]\NP)/NP oversees)
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num]
                          (N/N 80)
                          (N[num] billion)))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP for)
                    (NP
                      (N
                        (N/N college)
                        (N employees)))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[to]\NP) plans)
            (S[to]\NP
              ((S[to]\NP)/(S[b]\NP) to)
              (S[b]\NP
                ((S[b]\NP)/PP
                  (((S[b]\NP)/PP)/NP offer)
                  (NP
                    (N
                      (N/N two)
                      (N
                        (N/N new)
                        (N
                          (N/N investment)
                          (N options))))))
                (PP
                  (PP/NP to)
                  (NP
                    (NP[nb]/N its)
                    (N
                      (N/N
                        ((N/N)/(N/N) 1.2)
                        (N/N million))
                      (N participants))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP[nb]/N
                    (NP
                      (NP[nb]/N The)
                      (N nation))
                    ((NP[nb]/N)\NP 's))
                  (N
                    (N/N largest)
                    (N
                      (N/N pension)
                      (N fund))))
                (, ,))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) which)
                (S[dcl]\NP
                  (S[dcl]\NP
                    ((S[dcl]\NP)/NP
                      ((S[b]\NP)/NP oversee)
                      ((S[dcl]\NP)\(S[b]\NP) -es))
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num]
                          (N/N 80)
                          (N[num] billion)))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP for)
                    (NP
                      (N
                        (N/N college)
                        (N employees)))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[to]\NP)
              ((S[b]\NP)/(S[to]\NP) plan)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[to]\NP
              ((S[to]\NP)/(S[b]\NP) to)
              (S[b]\NP
                ((S[b]\NP)/PP
                  (((S[b]\NP)/PP)/NP offer)
                  (NP
                    (N
                      (N/N two)
                      (N
                        (N/N new)
                        (N
                          (N/N investment)
                          (N options))))))
                (PP
                  (PP/NP to)
                  (NP
                    (NP[nb]/N its)
                    (N
                      (N/N
                        ((N/N)/(N/N) 1.2)
                        (N/N million))
                      (N participants))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0205_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0205.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N New)
                  (N
                    (N/N Brunswick)
                    (N
                      (N/N Scientific)
                      (N Co.)))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N maker))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (N
                        (N/N biotechnology)
                        (N
                          (N instrumentation)
                          (N[conj]
                            (conj and)
                            (N equipment)))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP adopted)
                (NP
                  (NP
                    (NP[nb]/N an)
                    (N
                      (N/N anti-takeover)
                      (N plan)))
                  (NP\NP
                    (S[ng]\NP
                      ((S[ng]\NP)/NP
                        (((S[ng]\NP)/NP)/NP giving)
                        (NP
                          (N shareholders)))
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N right)
                          (N\N
                            (S[to]\NP
                              ((S[to]\NP)/(S[b]\NP) to)
                              (S[b]\NP
                                (S[b]\NP
                                  (S[b]\NP
                                    ((S[b]\NP)/NP purchase)
                                    (NP
                                      (N shares)))
                                  ((S\NP)\(S\NP)
                                    (((S\NP)\(S\NP))/NP at)
                                    (NP
                                      (N
                                        (N/N half)
                                        (N price)))))
                                ((S\NP)\(S\NP)
                                  (((S\NP)\(S\NP))/NP under)
                                  (NP
                                    (N
                                      (N/N certain)
                                      (N conditions))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N New)
                  (N
                    (N/N Brunswick)
                    (N
                      (N/N Scientific)
                      (N Co.)))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N maker))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (N
                        (N/N biotechnology)
                        (N
                          (N instrumentation)
                          (N[conj]
                            (conj and)
                            (N equipment)))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP
                  ((S[b]\NP)/NP adopt)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (NP
                  (NP
                    (NP[nb]/N an)
                    (N
                      (N/N anti-takeover)
                      (N plan)))
                  (NP\NP
                    (S[ng]\NP
                      ((S[ng]\NP)/NP
                        (((S[ng]\NP)/NP)/NP
                          (((S[b]\NP)/NP)/NP give)
                          ((S[ng]\NP)\(S[b]\NP) -ing))
                        (NP
                          (N shareholders)))
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N right)
                          (N\N
                            (S[to]\NP
                              ((S[to]\NP)/(S[b]\NP) to)
                              (S[b]\NP
                                (S[b]\NP
                                  (S[b]\NP
                                    ((S[b]\NP)/NP purchase)
                                    (NP
                                      (N shares)))
                                  ((S\NP)\(S\NP)
                                    (((S\NP)\(S\NP))/NP at)
                                    (NP
                                      (N
                                        (N/N half)
                                        (N price)))))
                                ((S\NP)\(S\NP)
                                  (((S\NP)\(S\NP))/NP under)
                                  (NP
                                    (N
                                      (N/N certain)
                                      (N conditions))))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0206_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0206.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP
                    (N
                      (N/N W.)
                      (N
                        (N/N Ed)
                        (N Tyler))))
                  (, ,))
                (NP\NP
                  (S[adj]\NP
                    (NP
                      (N
                        (N/N 37)
                        (N years)))
                    ((S[adj]\NP)\NP old))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N senior)
                      (N
                        (N/N vice)
                        (N president))))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP[nb]/N this)
                      (N
                        (N/N printing)
                        (N concern)))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/NP elected)
              (NP
                (NP
                  (NP
                    (N president))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP[nb]/N its)
                      (N
                        (N/N technology)
                        (N group)))))
                (NP[conj]
                  (, ,)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N new)
                      (N position))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP
                    (N
                      (N/N W.)
                      (N
                        (N/N Ed)
                        (N Tyler))))
                  (, ,))
                (NP\NP
                  (S[adj]\NP
                    (NP
                      (N
                        (N/N 37)
                        (N years)))
                    ((S[adj]\NP)\NP old))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N senior)
                      (N
                        (N/N vice)
                        (N president))))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP[nb]/N this)
                      (N
                        (N/N printing)
                        (N concern)))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/NP
                (((S[b]\NP)/NP)/NP elect)
                ((S[pss]\NP)\((S[b]\NP)/NP) -en))
              (NP
                (NP
                  (NP
                    (N president))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP[nb]/N its)
                      (N
                        (N/N technology)
                        (N group)))))
                (NP[conj]
                  (, ,)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N new)
                      (N position))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0207_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0207.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Solo)
              (N
                (N/N woodwind)
                (N players))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[to]\NP) have)
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/(S[adj]\NP) be)
                      (S[adj]\NP creative))))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/S[dcl] if)
                  (S[dcl]
                    (NP they)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[to]\NP) want)
                      (S[to]\NP
                        ((S[to]\NP)/(S[b]\NP) to)
                        (S[b]\NP
                          (S[b]\NP work)
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/N a)
                            (N lot))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] because)
              (S[dcl]
                (NP
                  (NP[nb]/N their)
                  (N
                    (N repertoire)
                    (N[conj]
                      (conj and)
                      (N
                        (N/N audience)
                        (N appeal)))))
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[adj]\NP) are)
                  (S[adj]\NP limited))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Solo)
              (N
                (N/N woodwind)
                (N players))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[to]\NP) have)
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/(S[adj]\NP) be)
                      (S[adj]\NP creative))))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/S[dcl] if)
                  (S[dcl]
                    (NP they)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[to]\NP)
                        ((S[b]\NP)/(S[to]\NP) want)
                        ((S[dcl]\NP)\(S[b]\NP) -es))
                      (S[to]\NP
                        ((S[to]\NP)/(S[b]\NP) to)
                        (S[b]\NP
                          (S[b]\NP work)
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/N a)
                            (N lot))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] because)
              (S[dcl]
                (NP
                  (NP[nb]/N their)
                  (N
                    (N repertoire)
                    (N[conj]
                      (conj and)
                      (N
                        (N/N audience)
                        (N appeal)))))
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[adj]\NP) are)
                  (S[adj]\NP limited))))))
        (. .)))
    True

    """
    pass
    


def wsj_0208_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0208.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N One))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP
                  (NP[nb]/N
                    (NP
                      (N
                        (N/N Ronald)
                        (N Reagan)))
                    ((NP[nb]/N)\NP 's))
                  (N attributes))
                (NP\NP
                  ((NP\NP)/NP as)
                  (NP
                    (N President))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[em] was)
            (S[em]
              (S[em]/S[dcl] that)
              (S[dcl]
                (NP he)
                (S[dcl]\NP
                  ((S\NP)/(S\NP) rarely)
                  (S[dcl]\NP
                    ((S[dcl]\NP)/PP
                      (((S[dcl]\NP)/PP)/NP gave)
                      (NP
                        (NP[nb]/N his)
                        (N blessing)))
                    (PP
                      (PP/NP to)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N claptrap))
                        (NP\NP
                          ((NP\NP)/(S[dcl]\NP) that)
                          (S[dcl]\NP
                            (S[dcl]\NP
                              ((S[dcl]\NP)/PP passes)
                              (PP
                                (PP/NP for)
                                (NP
                                  (N consensus))))
                            ((S\NP)\(S\NP)
                              (((S\NP)\(S\NP))/NP in)
                              (NP
                                (N
                                  (N/N various)
                                  (N
                                    (N/N international)
                                    (N institutions)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N One))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP
                  (NP[nb]/N
                    (NP
                      (N
                        (N/N Ronald)
                        (N Reagan)))
                    ((NP[nb]/N)\NP 's))
                  (N attributes))
                (NP\NP
                  ((NP\NP)/NP as)
                  (NP
                    (N President))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[em] was)
            (S[em]
              (S[em]/S[dcl] that)
              (S[dcl]
                (NP he)
                (S[dcl]\NP
                  ((S\NP)/(S\NP) rarely)
                  (S[dcl]\NP
                    ((S[dcl]\NP)/PP
                      (((S[dcl]\NP)/PP)/NP
                        (((S[b]\NP)/PP)/NP give)
                        ((S[dcl]\NP)\(S[b]\NP) -es))
                      (NP
                        (NP[nb]/N his)
                        (N blessing)))
                    (PP
                      (PP/NP to)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N claptrap))
                        (NP\NP
                          ((NP\NP)/(S[dcl]\NP) that)
                          (S[dcl]\NP
                            (S[dcl]\NP
                              ((S[dcl]\NP)/PP
                                ((S[b]\NP)/PP pass)
                                ((S[dcl]\NP)\(S[b]\NP) -es))
                              (PP
                                (PP/NP for)
                                (NP
                                  (N consensus))))
                            ((S\NP)\(S\NP)
                              (((S\NP)\(S\NP))/NP in)
                              (NP
                                (N
                                  (N/N various)
                                  (N
                                    (N/N international)
                                    (N institutions)))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0209_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0209.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N Researchers))
            (NP\NP
              ((NP\NP)/NP at)
              (NP
                (NP
                  (N
                    (N/N Plant)
                    (N
                      (N/N Genetic)
                      (N
                        (N/N Systems)
                        (N N.V.)))))
                (NP\NP
                  ((NP\NP)/NP in)
                  (NP
                    (N Belgium))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP they)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) have)
                (S[pt]\NP
                  ((S[pt]\NP)/NP developed)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N genetic)
                        (N
                          (N/N engineering)
                          (N technique))))
                    (NP\NP
                      ((NP\NP)/(S[ng]\NP) for)
                      (S[ng]\NP
                        ((S[ng]\NP)/NP creating)
                        (NP
                          (NP
                            (N
                              (N/N hybrid)
                              (N plants)))
                          (NP\NP
                            ((NP\NP)/NP for)
                            (NP
                              (NP
                                (NP[nb]/N a)
                                (N number))
                              (NP\NP
                                ((NP\NP)/NP of)
                                (NP
                                  (N
                                    (N/N key)
                                    (N crops)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N Researchers))
            (NP\NP
              ((NP\NP)/NP at)
              (NP
                (NP
                  (N
                    (N/N Plant)
                    (N
                      (N/N Genetic)
                      (N
                        (N/N Systems)
                        (N N.V.)))))
                (NP\NP
                  ((NP\NP)/NP in)
                  (NP
                    (N Belgium))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP they)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) have)
                (S[pt]\NP
                  ((S[pt]\NP)/NP
                    ((S[b]\NP)/NP develop)
                    ((S[pt]\NP)\(S[b]\NP) -ed))
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N genetic)
                        (N
                          (N/N engineering)
                          (N technique))))
                    (NP\NP
                      ((NP\NP)/(S[ng]\NP) for)
                      (S[ng]\NP
                        ((S[ng]\NP)/NP
                          ((S[b]\NP)/NP create)
                          ((S[ng]\NP)\(S[b]\NP) -ing))
                        (NP
                          (NP
                            (N
                              (N/N hybrid)
                              (N plants)))
                          (NP\NP
                            ((NP\NP)/NP for)
                            (NP
                              (NP
                                (NP[nb]/N a)
                                (N number))
                              (NP\NP
                                ((NP\NP)/NP of)
                                (NP
                                  (N
                                    (N/N key)
                                    (N crops)))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0210_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0210.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N A)
              (N
                (N/N bitter)
                (N conflict)))
            (NP\NP
              ((NP\NP)/NP with)
              (NP
                (N
                  (N/N global)
                  (N implications)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pt]\NP) has)
            (S[pt]\NP
              (S[pt]\NP erupted)
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP between)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N Nomura)
                        (N
                          (N/N Securities)
                          (N Co.))))
                    (NP[conj]
                      (conj and)
                      (NP
                        (NP
                          (N
                            (N/N Industrial)
                            (N Bank)))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N Japan))))))
                  (NP[conj]
                    (, ,)
                    (NP
                      (NP
                        (N two))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP[nb]/N
                            (NP
                              (NP[nb]/N the)
                              (N world))
                            ((NP[nb]/N)\NP 's))
                          (N
                            (N/N
                              ((N/N)/(N/N) most)
                              (N/N powerful))
                            (N
                              (N/N financial)
                              (N companies))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N A)
              (N
                (N/N bitter)
                (N conflict)))
            (NP\NP
              ((NP\NP)/NP with)
              (NP
                (N
                  (N/N global)
                  (N implications)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pt]\NP) has)
            (S[pt]\NP
              (S[pt]\NP
                (S[b]\NP erupt)
                ((S[pt]\NP)\(S[b]\NP) -ed))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP between)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N Nomura)
                        (N
                          (N/N Securities)
                          (N Co.))))
                    (NP[conj]
                      (conj and)
                      (NP
                        (NP
                          (N
                            (N/N Industrial)
                            (N Bank)))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N Japan))))))
                  (NP[conj]
                    (, ,)
                    (NP
                      (NP
                        (N two))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP[nb]/N
                            (NP
                              (NP[nb]/N the)
                              (N world))
                            ((NP[nb]/N)\NP 's))
                          (N
                            (N/N
                              ((N/N)/(N/N) most)
                              (N/N powerful))
                            (N
                              (N/N financial)
                              (N companies))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0211_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0211.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N ITEL)
              (N CORP.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP reported)
            (NP
              (NP
                (NP
                  (N
                    (N/N third-quarter)
                    (N earnings)))
                (, ,))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) which)
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[pss]\NP) were)
                  (S[pss]\NP
                    ((S\NP)/(S\NP) mistakenly)
                    (S[pss]\NP
                      ((S[pss]\NP)/(S[to]\NP)
                        ((S[pss]\NP)/(S[to]\NP) shown)
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP in)
                          (NP
                            (NP
                              (NP[nb]/N the)
                              (N
                                (N/N Quarterly)
                                (N
                                  (N/N Earnings)
                                  (N
                                    (N/N Surprises)
                                    (N table)))))
                            (NP\NP
                              ((NP\NP)/NP in)
                              (NP
                                (NP[nb]/N
                                  (NP/NP yesterday)
                                  (NP[nb]/N 's))
                                (N edition))))))
                      (S[to]\NP
                        ((S[to]\NP)/(S[b]\NP) to)
                        (S[b]\NP
                          ((S[b]\NP)/(S[adj]\NP) be)
                          (S[adj]\NP
                            (S[adj]\NP lower)
                            ((S[adj]\NP)\(S[adj]\NP)
                              (((S[adj]\NP)\(S[adj]\NP))/NP than)
                              (NP
                                (NP
                                  (NP[nb]/N the)
                                  (N average))
                                (NP\NP
                                  ((NP\NP)/NP of)
                                  (NP
                                    (NP[nb]/N
                                      (NP
                                        (N analysts))
                                      ((NP[nb]/N)\NP '))
                                    (N estimates)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N ITEL)
              (N CORP.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP
              ((S[b]\NP)/NP report)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (NP
              (NP
                (NP
                  (N
                    (N/N third-quarter)
                    (N earnings)))
                (, ,))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) which)
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[pss]\NP) were)
                  (S[pss]\NP
                    ((S\NP)/(S\NP) mistakenly)
                    (S[pss]\NP
                      ((S[pss]\NP)/(S[to]\NP)
                        ((S[pss]\NP)/(S[to]\NP)
                          (((S[b]\NP)/NP)/(S[to]\NP) show)
                          ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP in)
                          (NP
                            (NP
                              (NP[nb]/N the)
                              (N
                                (N/N Quarterly)
                                (N
                                  (N/N Earnings)
                                  (N
                                    (N/N Surprises)
                                    (N table)))))
                            (NP\NP
                              ((NP\NP)/NP in)
                              (NP
                                (NP[nb]/N
                                  (NP/NP yesterday)
                                  (NP[nb]/N 's))
                                (N edition))))))
                      (S[to]\NP
                        ((S[to]\NP)/(S[b]\NP) to)
                        (S[b]\NP
                          ((S[b]\NP)/(S[adj]\NP) be)
                          (S[adj]\NP
                            (S[adj]\NP lower)
                            ((S[adj]\NP)\(S[adj]\NP)
                              (((S[adj]\NP)\(S[adj]\NP))/NP than)
                              (NP
                                (NP
                                  (NP[nb]/N the)
                                  (N average))
                                (NP\NP
                                  ((NP\NP)/NP of)
                                  (NP
                                    (NP[nb]/N
                                      (NP
                                        (N analysts))
                                      ((NP[nb]/N)\NP '))
                                    (N estimates)))))))))))))))
        (. .)))
    True

    """
    pass
    


def wsj_0212_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0212.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (N
                    (N/N Raymond)
                    (N
                      (N/N E.)
                      (N Ross))))
                (, ,))
              (NP\NP
                (S[adj]\NP
                  (NP
                    (N
                      (N/N 53)
                      (N years)))
                  ((S[adj]\NP)\NP old))))
            (NP[conj]
              (, ,)
              (NP
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N formerly)
                          (N
                            (N/N group)
                            (N
                              (N/N vice)
                              (N president)))))
                      (NP[conj]
                        (, ,)
                        (NP
                          (N
                            (N/N U.S.)
                            (N
                              (N/N plastics)
                              (N machinery))))))
                    (, ,))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP[nb]/N this)
                      (N
                        (N/N machine)
                        (N
                          (N/N tool)
                          (N
                            (, ,)
                            (N
                              (N/N plastics)
                              (N
                                (N/N machinery)
                                (N
                                  (conj and)
                                  (N
                                    (N/N robots)
                                    (N concern)))))))))))
                (, ,))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                ((S[pss]\NP)/NP named)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N senior)
                        (N
                          (N/N vice)
                          (N president))))
                    (NP[conj]
                      (, ,)
                      (NP
                        (N
                          (N/N industrial)
                          (N systems)))))
                  (, ,)))
              ((S\NP)\(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP succeeding)
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N David)
                          (N
                            (N/N A.)
                            (N Entrekin))))
                      (, ,))
                    (NP\NP
                      ((NP\NP)/(S[dcl]\NP) who)
                      (S[dcl]\NP
                        (S[dcl]\NP resigned)
                        ((S\NP)\(S\NP) Monday)))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (N
                    (N/N Raymond)
                    (N
                      (N/N E.)
                      (N Ross))))
                (, ,))
              (NP\NP
                (S[adj]\NP
                  (NP
                    (N
                      (N/N 53)
                      (N years)))
                  ((S[adj]\NP)\NP old))))
            (NP[conj]
              (, ,)
              (NP
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N formerly)
                          (N
                            (N/N group)
                            (N
                              (N/N vice)
                              (N president)))))
                      (NP[conj]
                        (, ,)
                        (NP
                          (N
                            (N/N U.S.)
                            (N
                              (N/N plastics)
                              (N machinery))))))
                    (, ,))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP[nb]/N this)
                      (N
                        (N/N machine)
                        (N
                          (N/N tool)
                          (N
                            (, ,)
                            (N
                              (N/N plastics)
                              (N
                                (N/N machinery)
                                (N
                                  (conj and)
                                  (N
                                    (N/N robots)
                                    (N concern)))))))))))
                (, ,))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                ((S[pss]\NP)/NP
                  (((S[b]\NP)/NP)/NP name)
                  ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                (NP
                  (NP
                    (NP
                      (N
                        (N/N senior)
                        (N
                          (N/N vice)
                          (N president))))
                    (NP[conj]
                      (, ,)
                      (NP
                        (N
                          (N/N industrial)
                          (N systems)))))
                  (, ,)))
              ((S\NP)\(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP
                    ((S[b]\NP)/NP succeed)
                    ((S[ng]\NP)\(S[b]\NP) -ing))
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N David)
                          (N
                            (N/N A.)
                            (N Entrekin))))
                      (, ,))
                    (NP\NP
                      ((NP\NP)/(S[dcl]\NP) who)
                      (S[dcl]\NP
                        (S[dcl]\NP
                          (S[b]\NP resign)
                          ((S[dcl]\NP)\(S[b]\NP) -es))
                        ((S\NP)\(S\NP) Monday)))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0213_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0213.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N John)
                  (N
                    (N/N A.)
                    (N
                      (N/N Conlon)
                      (N Jr.)))))
              (NP[conj]
                (, ,)
                (NP
                  (N 45))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                ((S[pss]\NP)/NP named)
                (NP
                  (NP[nb]/N a)
                  (N
                    (N/N managing)
                    (N director))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP at)
                (NP
                  (NP[nb]/N this)
                  (N
                    (N/N investment-banking)
                    (N company)))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N John)
                  (N
                    (N/N A.)
                    (N
                      (N/N Conlon)
                      (N Jr.)))))
              (NP[conj]
                (, ,)
                (NP
                  (N 45))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                ((S[pss]\NP)/NP
                  (((S[b]\NP)/NP)/NP name)
                  ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                (NP
                  (NP[nb]/N a)
                  (N
                    (N/N managing)
                    (N director))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP at)
                (NP
                  (NP[nb]/N this)
                  (N
                    (N/N investment-banking)
                    (N company)))))))
        (. .)))
    True
    """
    pass
    


def wsj_0214_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0214.1')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/S[dcl] As)
            (S[dcl]
              (NP
                (N
                  (N/N Yogi)
                  (N Berra)))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[b]\NP) might)
                (S[b]\NP say))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/NP 's)
                  (NP
                    (N
                      (N/N deja)
                      (N vu))))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/((S\NP)\(S\NP)) all)
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/((S\NP)\(S\NP)) over)
                    ((S\NP)\(S\NP) again)))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/S[dcl] As)
            (S[dcl]
              (NP
                (N
                  (N/N Yogi)
                  (N Berra)))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[b]\NP) might)
                (S[b]\NP say))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/NP 's)
                  (NP
                    (N
                      (N/N deja)
                      (N vu))))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/((S\NP)\(S\NP)) all)
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/((S\NP)\(S\NP)) over)
                    ((S\NP)\(S\NP) again)))))))
        (. .)))
    True
    """
    pass
    


def wsj_0215_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0215.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Alltel)
              (N Corp.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[b]\NP) will)
                (S[b]\NP
                  ((S[b]\NP)/NP acquire)
                  (NP
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N 55)
                          (N %)))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP[nb]/N
                            (NP
                              (N
                                (N/N Pond)
                                (N
                                  (N/N Branch)
                                  (N
                                    (N/N Telephone)
                                    (N
                                      (N/N Company)
                                      (N Inc.))))))
                            ((NP[nb]/N)\NP 's))
                          (N
                            (N/N cellular)
                            (N franchise)))))
                    (NP\NP
                      ((NP\NP)/(S[dcl]/NP) that)
                      (S[dcl]/NP
                        (S/(S\NP)
                          (NP it))
                        ((S[dcl]\NP)/NP
                          ((S[dcl]\NP)/(S[b]\NP)
                            ((S[dcl]\NP)/(S[b]\NP) does)
                            ((S\NP)\(S\NP) n't))
                          ((S[b]\NP)/NP
                            ((S[b]\NP)/NP own)
                            ((S\NP)\(S\NP) already)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Alltel)
              (N Corp.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[b]\NP) will)
                (S[b]\NP
                  ((S[b]\NP)/NP acquire)
                  (NP
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N 55)
                          (N %)))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP[nb]/N
                            (NP
                              (N
                                (N/N Pond)
                                (N
                                  (N/N Branch)
                                  (N
                                    (N/N Telephone)
                                    (N
                                      (N/N Company)
                                      (N Inc.))))))
                            ((NP[nb]/N)\NP 's))
                          (N
                            (N/N cellular)
                            (N franchise)))))
                    (NP\NP
                      ((NP\NP)/(S[dcl]/NP) that)
                      (S[dcl]/NP
                        (S/(S\NP)
                          (NP it))
                        ((S[dcl]\NP)/NP
                          ((S[dcl]\NP)/(S[b]\NP)
                            ((S[dcl]\NP)/(S[b]\NP) does)
                            ((S\NP)\(S\NP) n't))
                          ((S[b]\NP)/NP
                            ((S[b]\NP)/NP own)
                            ((S\NP)\(S\NP) already)))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0216_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0216.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Stewart)
              (N
                (N/N &)
                (N
                  (N/N Stevenson)
                  (N
                    (N/N Services)
                    (N Inc.))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP received)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N two)
                        (N contracts)))
                    (NP\NP
                      (S[ng]\NP
                        ((S[ng]\NP)/NP totaling)
                        (NP
                          (N
                            (N/N[num] $)
                            (N[num]
                              (N/N 19)
                              (N[num] million)))))))
                  (NP\NP
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP build)
                        (NP
                          (N
                            (N/N gas-turbine)
                            (N generators)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Stewart)
              (N
                (N/N &)
                (N
                  (N/N Stevenson)
                  (N
                    (N/N Services)
                    (N Inc.))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP
                  ((S[b]\NP)/NP receive)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (NP
                  (NP
                    (NP
                      (N
                        (N/N two)
                        (N contracts)))
                    (NP\NP
                      (S[ng]\NP
                        ((S[ng]\NP)/NP
                          ((S[b]\NP)/NP total)
                          ((S[ng]\NP)\(S[b]\NP) -ing))
                        (NP
                          (N
                            (N/N[num] $)
                            (N[num]
                              (N/N 19)
                              (N[num] million)))))))
                  (NP\NP
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP build)
                        (NP
                          (N
                            (N/N gas-turbine)
                            (N generators)))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0217_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0217.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Liberty)
              (N
                (N/N National)
                (N Bancorp))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP
                (NP
                  (NP
                    (NP
                      (NP
                        (NP[nb]/N its)
                        (N acquisition))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP
                            (NP
                              (N
                                (N/N Florence)
                                (N
                                  (N/N Deposit)
                                  (N Bank))))
                            (, ,))
                          (NP\NP
                            (NP\NP Florence)
                            (NP\NP[conj]
                              (, ,)
                              (NP\NP Ky.))))))
                    (, ,))
                  (NP\NP
                    (S[pss]\NP
                      ((S\NP)/(S\NP) first)
                      (S[pss]\NP
                        (S[pss]\NP announced)
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP in)
                          (NP
                            (N April)))))))
                (, ,))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) has)
                (S[pt]\NP
                  ((S[pt]\NP)/(S[pss]\NP) been)
                  (S[pss]\NP
                    (S[pss]\NP completed)
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (NP
                          (NP[nb]/N a)
                          (N transaction))
                        (NP\NP
                          (S[pss]\NP
                            ((S[pss]\NP)/PP valued)
                            (PP
                              (PP/NP at)
                              (NP
                                (N
                                  (N/N[num] $)
                                  (N[num]
                                    (N/N 13.1)
                                    (N[num] million)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Liberty)
              (N
                (N/N National)
                (N Bancorp))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP
                (NP
                  (NP
                    (NP
                      (NP
                        (NP[nb]/N its)
                        (N acquisition))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP
                            (NP
                              (N
                                (N/N Florence)
                                (N
                                  (N/N Deposit)
                                  (N Bank))))
                            (, ,))
                          (NP\NP
                            (NP\NP Florence)
                            (NP\NP[conj]
                              (, ,)
                              (NP\NP Ky.))))))
                    (, ,))
                  (NP\NP
                    (S[pss]\NP
                      ((S\NP)/(S\NP) first)
                      (S[pss]\NP
                        (S[pss]\NP
                          ((S[b]\NP)/NP announce)
                          ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP in)
                          (NP
                            (N April)))))))
                (, ,))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) has)
                (S[pt]\NP
                  ((S[pt]\NP)/(S[pss]\NP) been)
                  (S[pss]\NP
                    (S[pss]\NP
                      ((S[b]\NP)/NP complete)
                      ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (NP
                          (NP[nb]/N a)
                          (N transaction))
                        (NP\NP
                          (S[pss]\NP
                            ((S[pss]\NP)/PP
                              (((S[b]\NP)/NP)/PP value)
                              ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                            (PP
                              (PP/NP at)
                              (NP
                                (N
                                  (N/N[num] $)
                                  (N[num]
                                    (N/N 13.1)
                                    (N[num] million)))))))))))))))
        (. .)))
    True

    """
    pass
    


def wsj_0218_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0218.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Hani)
              (N Zayadi)))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                (S[pss]\NP
                  (S[pss]\NP
                    (S[pss]\NP
                      ((S[pss]\NP)/NP appointed)
                      (NP
                        (NP
                          (NP
                            (N president))
                          (NP[conj]
                            (conj and)
                            (NP
                              (N
                                (N/N chief)
                                (N
                                  (N/N executive)
                                  (N officer))))))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (NP[nb]/N this)
                            (N
                              (N/N
                                ((N/N)/(N/N) financially)
                                (N/N troubled))
                              (N
                                (N/N department)
                                (N
                                  (N/N store)
                                  (N chain))))))))
                    (, ,))
                  ((S\NP)\(S\NP)
                    (S[adj]\NP
                      ((S[adj]\NP)/NP effective)
                      (NP
                        (N
                          (N/N[num] Nov.)
                          (N[num] 15))))))
                (, ,))
              ((S\NP)\(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP succeeding)
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N Frank)
                          (N Robertson)))
                      (, ,))
                    (NP\NP
                      ((NP\NP)/(S[dcl]\NP) who)
                      (S[dcl]\NP
                        ((S[dcl]\NP)/(S[ng]\NP) is)
                        (S[ng]\NP
                          (S[ng]\NP retiring)
                          ((S\NP)\(S\NP) early))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Hani)
              (N Zayadi)))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                (S[pss]\NP
                  (S[pss]\NP
                    (S[pss]\NP
                      ((S[pss]\NP)/NP
                        (((S[b]\NP)/NP)/NP appoint)
                        ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                      (NP
                        (NP
                          (NP
                            (N president))
                          (NP[conj]
                            (conj and)
                            (NP
                              (N
                                (N/N chief)
                                (N
                                  (N/N executive)
                                  (N officer))))))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (NP[nb]/N this)
                            (N
                              (N/N
                                ((N/N)/(N/N) financially)
                                (N/N troubled))
                              (N
                                (N/N department)
                                (N
                                  (N/N store)
                                  (N chain))))))))
                    (, ,))
                  ((S\NP)\(S\NP)
                    (S[adj]\NP
                      ((S[adj]\NP)/NP effective)
                      (NP
                        (N
                          (N/N[num] Nov.)
                          (N[num] 15))))))
                (, ,))
              ((S\NP)\(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP
                    ((S[b]\NP)/NP succeed)
                    ((S[ng]\NP)\(S[b]\NP) -ing))
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N Frank)
                          (N Robertson)))
                      (, ,))
                    (NP\NP
                      ((NP\NP)/(S[dcl]\NP) who)
                      (S[dcl]\NP
                        ((S[dcl]\NP)/(S[ng]\NP) is)
                        (S[ng]\NP
                          (S[ng]\NP
                            (S[b]\NP retire)
                            ((S[ng]\NP)\(S[b]\NP) -ing))
                          ((S\NP)\(S\NP) early))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0219_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0219.1')
    (S
      (NP
        (NP
          (N Tuesday))
        (NP[conj]
          (, ,)
          (NP
            (N
              (N
                (N
                  (N/N[num] October)
                  (N[num] 31))
                (, ,))
              (N\N 1989))))))
    True
    (S
      (NP
        (NP
          (N Tuesday))
        (NP[conj]
          (, ,)
          (NP
            (N
              (N
                (N
                  (N/N[num] October)
                  (N[num] 31))
                (, ,))
              (N\N 1989))))))
    True
    """
    pass
    


def wsj_0220_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0220.1')
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (NP[nb]/N
                (NP
                  (N Canada))
                ((NP[nb]/N)\NP 's))
              (N
                (N/N gross)
                (N
                  (N/N domestic)
                  (N product))))
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP rose)
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/N an)
                      (N
                        (N/N inflation-adjusted)
                        (N
                          (N/N 0.3)
                          (N %)))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP in)
                    (NP
                      (N August))))
                (, ,))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/((S\NP)\(S\NP)) mainly)
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP as)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N result))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N
                          (N/N service-industry)
                          (N growth)))))))))
          (S[dcl]\S[dcl]
            (, ,)
            (S[dcl]\S[dcl]
              (NP
                (NP
                  (NP
                    (N
                      (N/N Statistics)
                      (N Canada)))
                  (NP[conj]
                    (, ,)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N federal)
                        (N agency)))))
                (, ,))
              ((S[dcl]\S[dcl])\NP said))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (NP[nb]/N
                (NP
                  (N Canada))
                ((NP[nb]/N)\NP 's))
              (N
                (N/N gross)
                (N
                  (N/N domestic)
                  (N product))))
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[b]\NP rise)
                      ((S[dcl]\NP)\(S[b]\NP) -es))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/N an)
                      (N
                        (N/N inflation-adjusted)
                        (N
                          (N/N 0.3)
                          (N %)))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP in)
                    (NP
                      (N August))))
                (, ,))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/((S\NP)\(S\NP)) mainly)
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP as)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N result))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N
                          (N/N service-industry)
                          (N growth)))))))))
          (S[dcl]\S[dcl]
            (, ,)
            (S[dcl]\S[dcl]
              (NP
                (NP
                  (NP
                    (N
                      (N/N Statistics)
                      (N Canada)))
                  (NP[conj]
                    (, ,)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N federal)
                        (N agency)))))
                (, ,))
              ((S[dcl]\S[dcl])\NP
                ((S[b]\S[dcl])\NP say)
                (S[dcl]\S[b] -es)))))
        (. .)))
    True
    """
    pass
    


def wsj_0221_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0221.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Columbia)
              (N
                (N/N Pictures)
                (N
                  (N/N Entertainment)
                  (N Inc.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                (S[pss]\NP
                  (S[pss]\NP
                    (S[pss]\NP dropped)
                    (, ,))
                  ((S\NP)\(S\NP)
                    (S[adj]\NP
                      ((S[adj]\NP)/NP effective)
                      (NP
                        (N today)))))
                (, ,))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP from)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N recreational)
                      (N
                        (N/N products)
                        (N
                          (conj and)
                          (N
                            (N/N services)
                            (N
                              (N/N industry)
                              (N group)))))))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N Dow)
                        (N
                          (N/N Jones)
                          (N
                            (N/N Equity)
                            (N
                              (N/N Market)
                              (N Index))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Columbia)
              (N
                (N/N Pictures)
                (N
                  (N/N Entertainment)
                  (N Inc.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                (S[pss]\NP
                  (S[pss]\NP
                    (S[pss]\NP
                      ((S[b]\NP)/NP drop)
                      ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                    (, ,))
                  ((S\NP)\(S\NP)
                    (S[adj]\NP
                      ((S[adj]\NP)/NP effective)
                      (NP
                        (N today)))))
                (, ,))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP from)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N recreational)
                      (N
                        (N/N products)
                        (N
                          (conj and)
                          (N
                            (N/N services)
                            (N
                              (N/N industry)
                              (N group)))))))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N Dow)
                        (N
                          (N/N Jones)
                          (N
                            (N/N Equity)
                            (N
                              (N/N Market)
                              (N Index))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0222_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0222.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N
              (NP
                (N People))
              ((NP[nb]/N)\NP 's))
            (N
              (N/N Savings)
              (N
                (N/N Financial)
                (N Corp.))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[b]\NP) will)
                (S[b]\NP
                  (S[b]\NP
                    ((S[b]\NP)/NP
                      (((S[b]\NP)/NP)/(S[adj]\NP) buy)
                      (S[adj]\NP back))
                    (NP
                      (NP
                        (N
                          (N/PP
                            ((N/PP)/(S[adj]\NP) as)
                            (S[adj]\NP much))
                          (PP
                            (PP/NP as)
                            (NP
                              (N
                                (N/N 10)
                                (N %))))))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP
                            (NP[nb]/N its)
                            (N
                              (N/N
                                ((N/N)/(N/N) 2.4)
                                (N/N million))
                              (N shares)))
                          (NP\NP
                            (S[adj]\NP outstanding))))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/S[dcl] because)
                    (S[dcl]
                      (NP
                        (NP[nb]/N the)
                        (N stock))
                      (S[dcl]\NP
                        ((S[dcl]\NP)/(S[pss]\NP) is)
                        (S[pss]\NP undervalued)))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N
              (NP
                (N People))
              ((NP[nb]/N)\NP 's))
            (N
              (N/N Savings)
              (N
                (N/N Financial)
                (N Corp.))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[b]\NP) will)
                (S[b]\NP
                  (S[b]\NP
                    ((S[b]\NP)/NP
                      (((S[b]\NP)/NP)/(S[adj]\NP) buy)
                      (S[adj]\NP back))
                    (NP
                      (NP
                        (N
                          (N/PP
                            ((N/PP)/(S[adj]\NP) as)
                            (S[adj]\NP much))
                          (PP
                            (PP/NP as)
                            (NP
                              (N
                                (N/N 10)
                                (N %))))))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP
                            (NP[nb]/N its)
                            (N
                              (N/N
                                ((N/N)/(N/N) 2.4)
                                (N/N million))
                              (N shares)))
                          (NP\NP
                            (S[adj]\NP outstanding))))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/S[dcl] because)
                    (S[dcl]
                      (NP
                        (NP[nb]/N the)
                        (N stock))
                      (S[dcl]\NP
                        ((S[dcl]\NP)/(S[pss]\NP) is)
                        (S[pss]\NP
                          ((S[b]\NP)/NP undervalue)
                          ((S[pss]\NP)\((S[b]\NP)/NP) -en))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0223_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0223.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N A)
              (N seat))
            (NP\NP
              ((NP\NP)/NP on)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Chicago)
                  (N
                    (N/N Mercantile)
                    (N Exchange))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP sold)
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP for)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num] 410,000)))
                    (, ,))
                  (NP\NP
                    ((NP\NP)/PP
                      (((NP\NP)/PP)/NP down)
                      (NP
                        (N
                          (N/N[num] $)
                          (N[num] 6,000))))
                    (PP
                      (PP/NP from)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N previous)
                          (N
                            (N/N sale)
                            (N Oct)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N A)
              (N seat))
            (NP\NP
              ((NP\NP)/NP on)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Chicago)
                  (N
                    (N/N Mercantile)
                    (N Exchange))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                ((S[b]\NP)/NP sell)
                ((S[pss]\NP)\((S[b]\NP)/NP) -en))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP for)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num] 410,000)))
                    (, ,))
                  (NP\NP
                    ((NP\NP)/PP
                      (((NP\NP)/PP)/NP down)
                      (NP
                        (N
                          (N/N[num] $)
                          (N[num] 6,000))))
                    (PP
                      (PP/NP from)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N previous)
                          (N
                            (N/N sale)
                            (N Oct)))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0224_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0224.1')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP In)
            (NP
              (NP[nb]/N a)
              (N
                (N/N surprise)
                (N move))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N British)
                  (N government)))
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    ((S[dcl]\NP)/NP cleared)
                    (NP
                      (NP[nb]/N the)
                      (N way)))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP for)
                    (NP
                      (NP
                        (NP[nb]/N a)
                        (N
                          (N/N bidding)
                          (N war)))
                      (NP\NP
                        ((NP\NP)/NP for)
                        (NP
                          (N
                            (N/N Jaguar)
                            (N PLC)))))))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/(S[ng]\NP) by)
                  (S[ng]\NP
                    ((S[ng]\NP)/(S[to]\NP) agreeing)
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP remove)
                        (NP
                          (NP
                            (NP[nb]/N an)
                            (N obstacle))
                          (NP\NP
                            ((NP\NP)/NP to)
                            (NP
                              (NP
                                (NP[nb]/N a)
                                (N takeover))
                              (NP\NP
                                ((NP\NP)/NP of)
                                (NP
                                  (NP[nb]/N the)
                                  (N
                                    (N/N auto)
                                    (N maker)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP In)
            (NP
              (NP[nb]/N a)
              (N
                (N/N surprise)
                (N move))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N British)
                  (N government)))
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    ((S[dcl]\NP)/NP
                      ((S[b]\NP)/NP clear)
                      ((S[dcl]\NP)\(S[b]\NP) -es))
                    (NP
                      (NP[nb]/N the)
                      (N way)))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP for)
                    (NP
                      (NP
                        (NP[nb]/N a)
                        (N
                          (N/N bidding)
                          (N war)))
                      (NP\NP
                        ((NP\NP)/NP for)
                        (NP
                          (N
                            (N/N Jaguar)
                            (N PLC)))))))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/(S[ng]\NP) by)
                  (S[ng]\NP
                    ((S[ng]\NP)/(S[to]\NP)
                      ((S[b]\NP)/(S[to]\NP) agree)
                      ((S[ng]\NP)\(S[b]\NP) -ing))
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP remove)
                        (NP
                          (NP
                            (NP[nb]/N an)
                            (N obstacle))
                          (NP\NP
                            ((NP\NP)/NP to)
                            (NP
                              (NP
                                (NP[nb]/N a)
                                (N takeover))
                              (NP\NP
                                ((NP\NP)/NP of)
                                (NP
                                  (NP[nb]/N the)
                                  (N
                                    (N/N auto)
                                    (N maker)))))))))))))))
        (. .)))
    True

    """
    pass
    


def wsj_0225_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0225.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (N
                    (N/N Dow)
                    (N
                      (N/N Chemical)
                      (N Co.))))
                (, ,))
              (NP\NP
                (NP\NP Midland)
                (NP\NP[conj]
                  (, ,)
                  (NP\NP Mich.))))
            (NP[conj]
              (, ,)
              (NP[conj]
                (conj and)
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N Eli)
                          (N
                            (N/N Lilly)
                            (N
                              (N/N &)
                              (N Co.)))))
                      (, ,))
                    (NP\NP Indianapolis))
                  (, ,)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP they)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP completed)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N formation))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP
                        (N
                          (N/N Dow)
                          (N Elanco)))
                      (NP[conj]
                        (, ,)
                        (NP
                          (NP
                            (NP[nb]/N a)
                            (N
                              (N/N joint)
                              (N venture)))
                          (NP\NP
                            (S[ng]\NP
                              ((S[ng]\NP)/NP combining)
                              (NP
                                (NP
                                  (NP[nb]/N their)
                                  (N
                                    (N/N plant-sciences)
                                    (N businesses)))
                                (NP[conj]
                                  (conj
                                    (conj/conj as)
                                    (conj
                                      (conj/conj well)
                                      (conj as)))
                                  (NP
                                    (NP[nb]/N
                                      (NP
                                        (N Dow))
                                      ((NP[nb]/N)\NP 's))
                                    (N
                                      (N/N industrial)
                                      (N
                                        (N/N pest-control)
                                        (N business)))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (N
                    (N/N Dow)
                    (N
                      (N/N Chemical)
                      (N Co.))))
                (, ,))
              (NP\NP
                (NP\NP Midland)
                (NP\NP[conj]
                  (, ,)
                  (NP\NP Mich.))))
            (NP[conj]
              (, ,)
              (NP[conj]
                (conj and)
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N Eli)
                          (N
                            (N/N Lilly)
                            (N
                              (N/N &)
                              (N Co.)))))
                      (, ,))
                    (NP\NP Indianapolis))
                  (, ,)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP they)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP
                  ((S[b]\NP)/NP complete)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N formation))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP
                        (N
                          (N/N Dow)
                          (N Elanco)))
                      (NP[conj]
                        (, ,)
                        (NP
                          (NP
                            (NP[nb]/N a)
                            (N
                              (N/N joint)
                              (N venture)))
                          (NP\NP
                            (S[ng]\NP
                              ((S[ng]\NP)/NP
                                ((S[b]\NP)/NP combine)
                                ((S[ng]\NP)\(S[b]\NP) -ing))
                              (NP
                                (NP
                                  (NP[nb]/N their)
                                  (N
                                    (N/N plant-sciences)
                                    (N businesses)))
                                (NP[conj]
                                  (conj
                                    (conj/conj as)
                                    (conj
                                      (conj/conj well)
                                      (conj as)))
                                  (NP
                                    (NP[nb]/N
                                      (NP
                                        (N Dow))
                                      ((NP[nb]/N)\NP 's))
                                    (N
                                      (N/N industrial)
                                      (N
                                        (N/N pest-control)
                                        (N business)))))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0226_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0226.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP
                    (N
                      (N/N William)
                      (N
                        (N/N A.)
                        (N Wise))))
                  (, ,))
                (NP\NP
                  (S[adj]\NP
                    (NP
                      (N
                        (N/N 44)
                        (N years)))
                    ((S[adj]\NP)\NP old))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (N president))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N El)
                          (N
                            (N/N Paso)
                            (N
                              (N/N Natural)
                              (N
                                (N/N Gas)
                                (N
                                  (N/N Co.)
                                  (N unit)))))))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP[nb]/N this)
                          (N
                            (N/N energy)
                            (N
                              (conj and)
                              (N
                                (N/N natural-resources)
                                (N concern)))))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                (S[pss]\NP
                  ((S[pss]\NP)/PP named)
                  (PP
                    (PP/NP to)
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N additional)
                          (N post)))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (N
                            (N/N chief)
                            (N
                              (N/N executive)
                              (N officer))))))))
                (, ,))
              ((S\NP)\(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP succeeding)
                  (NP
                    (NP
                      (NP
                        (NP
                          (N
                            (N/N Travis)
                            (N
                              (N/N H.)
                              (N Petty))))
                        (NP[conj]
                          (, ,)
                          (NP
                            (N 61))))
                      (, ,))
                    (NP\NP
                      ((NP\NP)/(S[dcl]\NP) who)
                      (S[dcl]\NP
                        (S[dcl]\NP continues)
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP as)
                          (NP
                            (NP
                              (NP[nb]/N a)
                              (N
                                (N/N vice)
                                (N chairman)))
                            (NP\NP
                              ((NP\NP)/NP of)
                              (NP
                                (NP[nb]/N the)
                                (N parent)))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP
                    (N
                      (N/N William)
                      (N
                        (N/N A.)
                        (N Wise))))
                  (, ,))
                (NP\NP
                  (S[adj]\NP
                    (NP
                      (N
                        (N/N 44)
                        (N years)))
                    ((S[adj]\NP)\NP old))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (N president))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N El)
                          (N
                            (N/N Paso)
                            (N
                              (N/N Natural)
                              (N
                                (N/N Gas)
                                (N
                                  (N/N Co.)
                                  (N unit)))))))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP[nb]/N this)
                          (N
                            (N/N energy)
                            (N
                              (conj and)
                              (N
                                (N/N natural-resources)
                                (N concern)))))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              (S[pss]\NP
                (S[pss]\NP
                  ((S[pss]\NP)/PP
                    (((S[b]\NP)/NP)/PP name)
                    ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                  (PP
                    (PP/NP to)
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N additional)
                          (N post)))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (N
                            (N/N chief)
                            (N
                              (N/N executive)
                              (N officer))))))))
                (, ,))
              ((S\NP)\(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP
                    ((S[b]\NP)/NP succeed)
                    ((S[ng]\NP)\(S[b]\NP) -ing))
                  (NP
                    (NP
                      (NP
                        (NP
                          (N
                            (N/N Travis)
                            (N
                              (N/N H.)
                              (N Petty))))
                        (NP[conj]
                          (, ,)
                          (NP
                            (N 61))))
                      (, ,))
                    (NP\NP
                      ((NP\NP)/(S[dcl]\NP) who)
                      (S[dcl]\NP
                        (S[dcl]\NP
                          (S[b]\NP continue)
                          ((S[dcl]\NP)\(S[b]\NP) -es))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP as)
                          (NP
                            (NP
                              (NP[nb]/N a)
                              (N
                                (N/N vice)
                                (N chairman)))
                            (NP\NP
                              ((NP\NP)/NP of)
                              (NP
                                (NP[nb]/N the)
                                (N parent)))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0227_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0227.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N Erwin)
                  (N Tomash)))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N 67-year-old)
                        (N founder)))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (NP
                          (NP[nb]/N this)
                          (N maker))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N
                              (N/N data)
                              (N
                                (N/N communications)
                                (N products))))))))
                  (NP[conj]
                    (conj and)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N former)
                        (N
                          (N chairman)
                          (N[conj]
                            (conj and)
                            (N
                              (N/N chief)
                              (N executive))))))))))
            (, ,))
          (S[dcl]\NP
            (S[dcl]\NP resigned)
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP as)
              (NP
                (NP[nb]/N a)
                (N director)))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N Erwin)
                  (N Tomash)))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N 67-year-old)
                        (N founder)))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (NP
                          (NP[nb]/N this)
                          (N maker))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N
                              (N/N data)
                              (N
                                (N/N communications)
                                (N products))))))))
                  (NP[conj]
                    (conj and)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N former)
                        (N
                          (N chairman)
                          (N[conj]
                            (conj and)
                            (N
                              (N/N chief)
                              (N executive))))))))))
            (, ,))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[b]\NP resign)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP as)
              (NP
                (NP[nb]/N a)
                (N director)))))
        (. .)))
    True
    """
    pass
    


def wsj_0228_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0228.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N Robert)
                  (N
                    (N/N Q.)
                    (N Marston))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N president)
                          (N emeritus)))
                      (NP[conj]
                        (, ,)
                        (NP
                          (NP
                            (N University))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (N Florida))))))
                    (, ,))
                  (NP[conj]
                    (conj and)
                    (NP
                      (NP
                        (NP[nb]/N a)
                        (N director))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP
                            (NP[nb]/N this)
                            (N maker))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (N
                                (N/N medical)
                                (N devices)))))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/NP named)
              (NP
                (N chairman)))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N Robert)
                  (N
                    (N/N Q.)
                    (N Marston))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N president)
                          (N emeritus)))
                      (NP[conj]
                        (, ,)
                        (NP
                          (NP
                            (N University))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (N Florida))))))
                    (, ,))
                  (NP[conj]
                    (conj and)
                    (NP
                      (NP
                        (NP[nb]/N a)
                        (N director))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP
                            (NP[nb]/N this)
                            (N maker))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (N
                                (N/N medical)
                                (N devices)))))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/NP
                (((S[b]\NP)/NP)/NP name)
                ((S[pss]\NP)\((S[b]\NP)/NP) -en))
              (NP
                (N chairman)))))
        (. .)))
    True
    """
    pass
    


def wsj_0229_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0229.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N SFE)
              (N Technologies)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP
                (N
                  (N/N William)
                  (N
                    (N/N P.)
                    (N Kuehn))))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pss]\NP) was)
                (S[pss]\NP
                  ((S[pss]\NP)/NP elected)
                  (NP
                    (NP
                      (NP
                        (N chairman))
                      (NP[conj]
                        (conj and)
                        (NP
                          (N
                            (N/N chief)
                            (N
                              (N/N executive)
                              (N officer))))))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (NP[nb]/N this)
                        (N
                          (N/N troubled)
                          (N
                            (N/N electronics)
                            (N
                              (N/N parts)
                              (N maker))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N SFE)
              (N Technologies)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP
                (N
                  (N/N William)
                  (N
                    (N/N P.)
                    (N Kuehn))))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pss]\NP) was)
                (S[pss]\NP
                  ((S[pss]\NP)/NP
                    (((S[b]\NP)/NP)/NP elect)
                    ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                  (NP
                    (NP
                      (NP
                        (N chairman))
                      (NP[conj]
                        (conj and)
                        (NP
                          (N
                            (N/N chief)
                            (N
                              (N/N executive)
                              (N officer))))))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (NP[nb]/N this)
                        (N
                          (N/N troubled)
                          (N
                            (N/N electronics)
                            (N
                              (N/N parts)
                              (N maker))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0230_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0230.1')
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (NP
                (NP
                  (N Sales))
                (NP\NP
                  ((NP\NP)/NP of)
                  (NP
                    (N
                      (N/N new)
                      (N cars)))))
              (NP\NP
                ((NP\NP)/NP in)
                (NP
                  (N Europe))))
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP fell)
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 4.2)
                    ((S\NP)\(S\NP) %)))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP in)
                  (NP
                    (N September))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/(S[adj]\NP) from)
                (S[adj]\NP
                  (NP
                    (NP[nb]/N a)
                    (N year))
                  ((S[adj]\NP)\NP earlier)))))
          (S[dcl][conj]
            (conj and)
            (S[dcl]
              (NP
                (N analysts))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[dcl] say)
                (S[dcl]
                  (NP
                    (NP[nb]/N the)
                    (N market))
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[b]\NP) could)
                    (S[b]\NP
                      (S[b]\NP
                        ((S[b]\NP)/(S[to]\NP) continue)
                        (S[to]\NP
                          ((S[to]\NP)/(S[b]\NP) to)
                          (S[b]\NP soften)))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP in)
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N months)
                            (N\N ahead)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (NP
                (NP
                  (N Sales))
                (NP\NP
                  ((NP\NP)/NP of)
                  (NP
                    (N
                      (N/N new)
                      (N cars)))))
              (NP\NP
                ((NP\NP)/NP in)
                (NP
                  (N Europe))))
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[b]\NP fall)
                    ((S[dcl]\NP)\(S[b]\NP) -es))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 4.2)
                    ((S\NP)\(S\NP) %)))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP in)
                  (NP
                    (N September))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/(S[adj]\NP) from)
                (S[adj]\NP
                  (NP
                    (NP[nb]/N a)
                    (N year))
                  ((S[adj]\NP)\NP earlier)))))
          (S[dcl][conj]
            (conj and)
            (S[dcl]
              (NP
                (N analysts))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[dcl]
                  ((S[b]\NP)/S[dcl] say)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (S[dcl]
                  (NP
                    (NP[nb]/N the)
                    (N market))
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[b]\NP) could)
                    (S[b]\NP
                      (S[b]\NP
                        ((S[b]\NP)/(S[to]\NP) continue)
                        (S[to]\NP
                          ((S[to]\NP)/(S[b]\NP) to)
                          (S[b]\NP soften)))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP in)
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N months)
                            (N\N ahead)))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0231_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0231.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Tokyo)
              (N stocks)))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP rebounded)
                ((S\NP)\(S\NP) Tuesday))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP from)
                (NP
                  (N
                    (N/N two)
                    (N
                      (N/N consecutive)
                      (N
                        (N/N daily)
                        (N losses)))))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP in)
              (NP
                (N
                  (N/N
                    ((N/N)/(N/N) relatively)
                    (N/N active))
                  (N dealings))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Tokyo)
              (N stocks)))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[b]\NP rebound)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                ((S\NP)\(S\NP) Tuesday))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP from)
                (NP
                  (N
                    (N/N two)
                    (N
                      (N/N consecutive)
                      (N
                        (N/N daily)
                        (N losses)))))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP in)
              (NP
                (N
                  (N/N
                    ((N/N)/(N/N) relatively)
                    (N/N active))
                  (N dealings))))))
        (. .)))
    True
    """
    pass
    


def wsj_0232_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0232.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N French)
              (N
                (N/N consumer)
                (N prices))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP rose)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 0.2)
                        ((S\NP)\(S\NP) %)))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N September))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP from)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N previous)
                        (N month)))))
                (S[dcl]\NP[conj]
                  (conj and)
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[adj]\NP) were)
                    (S[adj]\NP
                      ((S[adj]\NP)/PP
                        (((S[adj]\NP)/PP)/NP up)
                        (NP
                          (N
                            (N/N 3.4)
                            (N %))))
                      (PP
                        (PP/(S[adj]\NP) from)
                        (S[adj]\NP
                          (NP
                            (NP[nb]/N a)
                            (N year))
                          ((S[adj]\NP)\NP earlier)))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/PP according)
              (PP
                (PP/NP to)
                (NP
                  (NP
                    (N
                      (N/N definitive)
                      (N figures)))
                  (NP\NP
                    ((NP\NP)/NP from)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N National)
                        (N
                          (N/N Statistics)
                          (N Institute))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N French)
              (N
                (N/N consumer)
                (N prices))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP
                        (S[b]\NP rise)
                        ((S[dcl]\NP)\(S[b]\NP) -es))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 0.2)
                        ((S\NP)\(S\NP) %)))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N September))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP from)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N previous)
                        (N month)))))
                (S[dcl]\NP[conj]
                  (conj and)
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[adj]\NP) were)
                    (S[adj]\NP
                      ((S[adj]\NP)/PP
                        (((S[adj]\NP)/PP)/NP up)
                        (NP
                          (N
                            (N/N 3.4)
                            (N %))))
                      (PP
                        (PP/(S[adj]\NP) from)
                        (S[adj]\NP
                          (NP
                            (NP[nb]/N a)
                            (N year))
                          ((S[adj]\NP)\NP earlier)))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/PP according)
              (PP
                (PP/NP to)
                (NP
                  (NP
                    (N
                      (N/N definitive)
                      (N figures)))
                  (NP\NP
                    ((NP\NP)/NP from)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N National)
                        (N
                          (N/N Statistics)
                          (N Institute))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0233_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0233.1')
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (NP
                (NP[nb]/N
                  (NP
                    (N Japan))
                  ((NP[nb]/N)\NP 's))
                (N index))
              (NP\NP
                ((NP\NP)/NP of)
                (NP
                  (N
                    (N/N leading)
                    (N indicators)))))
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP rose)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP to)
                        (NP
                          (N 63.6))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N August))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP above)
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N so-called)
                        (N
                          (N/N boom-or-bust)
                          (N line))))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N 50))))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP for)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N first)
                      (N time)))
                  (NP\NP
                    ((NP\NP)/NP since)
                    (NP
                      (N May)))))))
          (S[dcl]\S[dcl]
            (, ,)
            (S[dcl]\S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Economic)
                  (N
                    (N/N Planning)
                    (N Agency))))
              ((S[dcl]\S[dcl])\NP said))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (NP
                (NP[nb]/N
                  (NP
                    (N Japan))
                  ((NP[nb]/N)\NP 's))
                (N index))
              (NP\NP
                ((NP\NP)/NP of)
                (NP
                  (N
                    (N/N leading)
                    (N indicators)))))
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP
                        (S[b]\NP rise)
                        ((S[dcl]\NP)\(S[b]\NP) -es))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP to)
                        (NP
                          (N 63.6))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N August))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP above)
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N so-called)
                        (N
                          (N/N boom-or-bust)
                          (N line))))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N 50))))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP for)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N first)
                      (N time)))
                  (NP\NP
                    ((NP\NP)/NP since)
                    (NP
                      (N May)))))))
          (S[dcl]\S[dcl]
            (, ,)
            (S[dcl]\S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Economic)
                  (N
                    (N/N Planning)
                    (N Agency))))
              ((S[dcl]\S[dcl])\NP
                ((S[b]\S[dcl])\NP say)
                (S[dcl]\S[b] -es)))))
        (. .)))
    True
    """
    pass
    


def wsj_0234_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0234.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Metromedia)
              (N Co.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP
                (NP[nb]/N its)
                (N
                  (N/N Metromedia)
                  (N
                    (N/N Long)
                    (N
                      (N/N Distance)
                      (N unit)))))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) has)
                (S[pt]\NP
                  ((S[pt]\NP)/(S[pss]\NP) been)
                  (S[pss]\NP
                    (S[pss]\NP
                      (S[pss]\NP
                        ((S[pss]\NP)/NP renamed)
                        (NP
                          (N
                            (N/N Metromedia-ITT)
                            (N
                              (N/N Long)
                              (N Distance)))))
                      (, ,))
                    ((S\NP)\(S\NP)
                      (S[ng]\NP
                        ((S[ng]\NP)/NP reflecting)
                        (NP
                          (NP
                            (N acquisitions))
                          (NP\NP
                            ((NP\NP)/NP from)
                            (NP
                              (NP
                                (NP
                                  (N
                                    (N/N ITT)
                                    (N Corp.)))
                                (, ,))
                              (NP\NP
                                ((NP\NP)/(S[dcl]\NP) which)
                                (S[dcl]\NP
                                  ((S[dcl]\NP)/PP
                                    (((S[dcl]\NP)/PP)/NP licenses)
                                    (NP
                                      (NP[nb]/N its)
                                      (N name)))
                                  (PP
                                    (PP/NP to)
                                    (NP
                                      (N
                                        (N/N
                                          ((N/N)/(N/N) closely)
                                          (N/N held))
                                        (N Metromedia)))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Metromedia)
              (N Co.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP
                (NP[nb]/N its)
                (N
                  (N/N Metromedia)
                  (N
                    (N/N Long)
                    (N
                      (N/N Distance)
                      (N unit)))))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) has)
                (S[pt]\NP
                  ((S[pt]\NP)/(S[pss]\NP) been)
                  (S[pss]\NP
                    (S[pss]\NP
                      (S[pss]\NP
                        ((S[pss]\NP)/NP
                          (((S[b]\NP)/NP)/NP rename)
                          ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                        (NP
                          (N
                            (N/N Metromedia-ITT)
                            (N
                              (N/N Long)
                              (N Distance)))))
                      (, ,))
                    ((S\NP)\(S\NP)
                      (S[ng]\NP
                        ((S[ng]\NP)/NP
                          ((S[b]\NP)/NP reflect)
                          ((S[ng]\NP)\(S[b]\NP) -ing))
                        (NP
                          (NP
                            (N acquisitions))
                          (NP\NP
                            ((NP\NP)/NP from)
                            (NP
                              (NP
                                (NP
                                  (N
                                    (N/N ITT)
                                    (N Corp.)))
                                (, ,))
                              (NP\NP
                                ((NP\NP)/(S[dcl]\NP) which)
                                (S[dcl]\NP
                                  ((S[dcl]\NP)/PP
                                    (((S[dcl]\NP)/PP)/NP
                                      (((S[b]\NP)/PP)/NP license)
                                      ((S[dcl]\NP)\(S[b]\NP) -es))
                                    (NP
                                      (NP[nb]/N its)
                                      (N name)))
                                  (PP
                                    (PP/NP to)
                                    (NP
                                      (N
                                        (N/N
                                          ((N/N)/(N/N) closely)
                                          (N/N held))
                                        (N Metromedia)))))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0235_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0235.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N South)
              (N
                (N/N Korean)
                (N
                  (N/N consumer)
                  (N prices)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP rose)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 5)
                        ((S\NP)\(S\NP) %)))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N/N first)
                            (N
                              (N/N 10)
                              (N months))))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (NP[nb]/N this)
                            (N year))))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (S[ng]\NP
                    ((S[ng]\NP)/NP matching)
                    (NP
                      (NP
                        (NP[nb]/N
                          (NP
                            (NP[nb]/N the)
                            (N government))
                          ((NP[nb]/N)\NP 's))
                        (N target))
                      (NP\NP
                        ((NP\NP)/NP for)
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N/N entire)
                            (N year))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/PP according)
              (PP
                (PP/NP to)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N Bank))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N Korea))))
                  (NP[conj]
                    (conj and)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N Economic)
                        (N
                          (N/N Planning)
                          (N Board))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N South)
              (N
                (N/N Korean)
                (N
                  (N/N consumer)
                  (N prices)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP
                        (S[b]\NP rise)
                        ((S[dcl]\NP)\(S[b]\NP) -es))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 5)
                        ((S\NP)\(S\NP) %)))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N/N first)
                            (N
                              (N/N 10)
                              (N months))))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (NP[nb]/N this)
                            (N year))))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (S[ng]\NP
                    ((S[ng]\NP)/NP
                      ((S[b]\NP)/NP match)
                      ((S[ng]\NP)\(S[b]\NP) -ing))
                    (NP
                      (NP
                        (NP[nb]/N
                          (NP
                            (NP[nb]/N the)
                            (N government))
                          ((NP[nb]/N)\NP 's))
                        (N target))
                      (NP\NP
                        ((NP\NP)/NP for)
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N/N entire)
                            (N year))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/PP according)
              (PP
                (PP/NP to)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N Bank))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N Korea))))
                  (NP[conj]
                    (conj and)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N Economic)
                        (N
                          (N/N Planning)
                          (N Board))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0236_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0236.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Martin)
              (N
                (N/N Marietta)
                (N Corp.))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/PP
                    (((S[dcl]\NP)/PP)/NP won)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N
                          ((N/N)/N[num] $)
                          (N[num]
                            (N/N 38.2)
                            (N[num] million)))
                        (N contract))))
                  (PP
                    (PP/NP from)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N U.S.)
                        (N
                          (N/N Postal)
                          (N Service))))))
                ((S\NP)\(S\NP)
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/NP
                        ((S[b]\NP)/NP manufacture)
                        ((S[b]\NP)/NP[conj]
                          (conj and)
                          ((S[b]\NP)/NP install)))
                      (NP
                        (N
                          (N/N automated)
                          (N
                            (N/N mail-sorting)
                            (N machines)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Martin)
              (N
                (N/N Marietta)
                (N Corp.))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/PP
                    (((S[dcl]\NP)/PP)/NP
                      (((S[b]\NP)/PP)/NP win)
                      ((S[dcl]\NP)\(S[b]\NP) -es))
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N
                          ((N/N)/N[num] $)
                          (N[num]
                            (N/N 38.2)
                            (N[num] million)))
                        (N contract))))
                  (PP
                    (PP/NP from)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N U.S.)
                        (N
                          (N/N Postal)
                          (N Service))))))
                ((S\NP)\(S\NP)
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/NP
                        ((S[b]\NP)/NP manufacture)
                        ((S[b]\NP)/NP[conj]
                          (conj and)
                          ((S[b]\NP)/NP install)))
                      (NP
                        (N
                          (N/N automated)
                          (N
                            (N/N mail-sorting)
                            (N machines)))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0237_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0237.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP
                    (N
                      (N/N Thomas)
                      (N
                        (N/N A.)
                        (N Donovan))))
                  (, ,))
                (NP\NP
                  (S[adj]\NP
                    (NP
                      (N
                        (N/N 37)
                        (N years)))
                    ((S[adj]\NP)\NP old))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N formerly)
                          (N
                            (N/N vice)
                            (N president))))
                      (NP[conj]
                        (, ,)
                        (NP
                          (N
                            (N/N West)
                            (N
                              (N/N Coast)
                              (N operations))))))
                    (, ,))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP[nb]/N this)
                      (N
                        (N/N hazardous-waste-site)
                        (N
                          (N/N remediation)
                          (N concern))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/NP named)
              (NP
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N executive)
                          (N
                            (N/N vice)
                            (N president))))
                      (NP[conj]
                        (conj and)
                        (NP
                          (N
                            (N/N chief)
                            (N
                              (N/N operating)
                              (N officer))))))
                    (NP[conj]
                      (, ,)
                      (NP
                        (NP[nb]/N both)
                        (N
                          (N/N
                            ((N/N)/(N/N) newly)
                            (N/N created))
                          (N posts)))))
                  (, ,))
                (NP[conj]
                  (conj and)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N director))
                    (NP\NP
                      (, ,)
                      (S[ng]\NP
                        ((S[ng]\NP)/NP filling)
                        (NP
                          (NP[nb]/N a)
                          (N vacancy))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP
                    (N
                      (N/N Thomas)
                      (N
                        (N/N A.)
                        (N Donovan))))
                  (, ,))
                (NP\NP
                  (S[adj]\NP
                    (NP
                      (N
                        (N/N 37)
                        (N years)))
                    ((S[adj]\NP)\NP old))))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N formerly)
                          (N
                            (N/N vice)
                            (N president))))
                      (NP[conj]
                        (, ,)
                        (NP
                          (N
                            (N/N West)
                            (N
                              (N/N Coast)
                              (N operations))))))
                    (, ,))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP[nb]/N this)
                      (N
                        (N/N hazardous-waste-site)
                        (N
                          (N/N remediation)
                          (N concern))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/NP
                (((S[b]\NP)/NP)/NP name)
                ((S[pss]\NP)\((S[b]\NP)/NP) -en))
              (NP
                (NP
                  (NP
                    (NP
                      (NP
                        (N
                          (N/N executive)
                          (N
                            (N/N vice)
                            (N president))))
                      (NP[conj]
                        (conj and)
                        (NP
                          (N
                            (N/N chief)
                            (N
                              (N/N operating)
                              (N officer))))))
                    (NP[conj]
                      (, ,)
                      (NP
                        (NP[nb]/N both)
                        (N
                          (N/N
                            ((N/N)/(N/N) newly)
                            (N/N created))
                          (N posts)))))
                  (, ,))
                (NP[conj]
                  (conj and)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N director))
                    (NP\NP
                      (, ,)
                      (S[ng]\NP
                        ((S[ng]\NP)/NP
                          ((S[b]\NP)/NP fill)
                          ((S[ng]\NP)\(S[b]\NP) -ing))
                        (NP
                          (NP[nb]/N a)
                          (N vacancy))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0238_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0238.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N Yields))
            (NP\NP
              ((NP\NP)/NP on)
              (NP
                (NP
                  (N
                    (N/N savings-type)
                    (N certificates)))
                (NP\NP
                  ((NP\NP)/NP of)
                  (NP
                    (N deposit))))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP dropped)
              ((S\NP)\(S\NP) slightly))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP in)
              (NP
                (NP
                  (NP[nb]/N the)
                  (N week))
                (NP\NP
                  (S[pss]\NP
                    (S[pss]\NP ended)
                    ((S\NP)\(S\NP) yesterday)))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N Yields))
            (NP\NP
              ((NP\NP)/NP on)
              (NP
                (NP
                  (N
                    (N/N savings-type)
                    (N certificates)))
                (NP\NP
                  ((NP\NP)/NP of)
                  (NP
                    (N deposit))))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                (S[b]\NP drop)
                ((S[dcl]\NP)\(S[b]\NP) -es))
              ((S\NP)\(S\NP) slightly))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/NP in)
              (NP
                (NP
                  (NP[nb]/N the)
                  (N week))
                (NP\NP
                  (S[pss]\NP
                    (S[pss]\NP
                      ((S[b]\NP)/NP end)
                      ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                    ((S\NP)\(S\NP) yesterday)))))))
        (. .)))
    True
    """
    pass
    


def wsj_0239_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0239.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP I)
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/(S[to]\NP) had)
              (S[to]\NP
                ((S[to]\NP)/(S[b]\NP) to)
                (S[b]\NP
                  (S[b]\NP
                    (S[b]\NP reach)
                    ((S\NP)\(S\NP) back))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP to)
                    (NP
                      (N
                        (N French)
                        (N\N 101)))))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] when)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N
                      (N/N monsieur)
                      ((N/N)\(N/N) avec))
                    (N clipboard)))
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP leaned)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP over)
                        (NP
                          (NP[nb]/N my)
                          (N shoulder))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP during)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N/N coffee)
                            (N phase)))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N dinner))))))
                  (S[dcl]\NP[conj]
                    (conj and)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/S[qem] asked)
                      (S[qem]
                        (S[qem]/S[dcl] whether)
                        (S[dcl]
                          (NP I)
                          (S[dcl]\NP
                            ((S[dcl]\NP)/(S[to]\NP) wanted)
                            (S[to]\NP
                              ((S[to]\NP)/(S[b]\NP) to)
                              (S[b]\NP
                                (S[b]\NP ride)
                                ((S\NP)\(S\NP)
                                  (((S\NP)\(S\NP))/NP in)
                                  (NP
                                    (NP[nb]/N a)
                                    (N montgolfiere)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP I)
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/(S[to]\NP) had)
              (S[to]\NP
                ((S[to]\NP)/(S[b]\NP) to)
                (S[b]\NP
                  (S[b]\NP
                    (S[b]\NP reach)
                    ((S\NP)\(S\NP) back))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP to)
                    (NP
                      (N
                        (N French)
                        (N\N 101)))))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] when)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N
                      (N/N monsieur)
                      ((N/N)\(N/N) avec))
                    (N clipboard)))
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP
                        (S[b]\NP lean)
                        ((S[dcl]\NP)\(S[b]\NP) -es))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP over)
                        (NP
                          (NP[nb]/N my)
                          (N shoulder))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP during)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N/N coffee)
                            (N phase)))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N dinner))))))
                  (S[dcl]\NP[conj]
                    (conj and)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/S[qem]
                        ((S[b]\NP)/S[qem] ask)
                        ((S[dcl]\NP)\(S[b]\NP) -es))
                      (S[qem]
                        (S[qem]/S[dcl] whether)
                        (S[dcl]
                          (NP I)
                          (S[dcl]\NP
                            ((S[dcl]\NP)/(S[to]\NP)
                              ((S[b]\NP)/(S[to]\NP) want)
                              ((S[dcl]\NP)\(S[b]\NP) -es))
                            (S[to]\NP
                              ((S[to]\NP)/(S[b]\NP) to)
                              (S[b]\NP
                                (S[b]\NP ride)
                                ((S\NP)\(S\NP)
                                  (((S\NP)\(S\NP))/NP in)
                                  (NP
                                    (NP[nb]/N a)
                                    (N montgolfiere)))))))))))))))
        (. .)))
    True

    """
    pass
    


def wsj_0240_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0240.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Treasury)
              (N
                (N/N Undersecretary)
                (N
                  (N/N David)
                  (N Mulford)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/NP defended)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N
                        (NP
                          (NP[nb]/N the)
                          (N Treasury))
                        ((NP[nb]/N)\NP 's))
                      (N efforts))
                    (NP\NP
                      ((NP\NP)/N this)
                      (N fall)))
                  (NP\NP
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP
                          ((S[b]\NP)/NP drive)
                          ((S\NP)\(S\NP) down))
                        (NP
                          (NP
                            (NP[nb]/N the)
                            (N value))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (NP[nb]/N the)
                              (N dollar)))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (S[ng]\NP
                ((S[ng]\NP)/S[dcl] saying)
                (S[dcl]
                  (NP it)
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[b]\NP) helped)
                    (S[b]\NP
                      ((S[b]\NP)/NP minimize)
                      (NP
                        (NP
                          (N damage))
                        (NP\NP
                          ((NP\NP)/NP from)
                          (NP
                            (NP
                              (NP
                                (NP[nb]/N the)
                                (N
                                  (N/N 190-point)
                                  (N drop)))
                              (NP\NP
                                ((NP\NP)/NP in)
                                (NP
                                  (NP[nb]/N the)
                                  (N
                                    (N/N stock)
                                    (N market)))))
                            (NP\NP
                              ((NP\NP)/N[num] Oct.)
                              (N[num] 13))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Treasury)
              (N
                (N/N Undersecretary)
                (N
                  (N/N David)
                  (N Mulford)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/NP
                  ((S[b]\NP)/NP defend)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (NP
                  (NP
                    (NP
                      (NP[nb]/N
                        (NP
                          (NP[nb]/N the)
                          (N Treasury))
                        ((NP[nb]/N)\NP 's))
                      (N efforts))
                    (NP\NP
                      ((NP\NP)/N this)
                      (N fall)))
                  (NP\NP
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP
                          ((S[b]\NP)/NP drive)
                          ((S\NP)\(S\NP) down))
                        (NP
                          (NP
                            (NP[nb]/N the)
                            (N value))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (NP[nb]/N the)
                              (N dollar)))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (S[ng]\NP
                ((S[ng]\NP)/S[dcl]
                  ((S[b]\NP)/S[dcl] say)
                  ((S[ng]\NP)\(S[b]\NP) -ing))
                (S[dcl]
                  (NP it)
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[b]\NP) helped)
                    (S[b]\NP
                      ((S[b]\NP)/NP minimize)
                      (NP
                        (NP
                          (N damage))
                        (NP\NP
                          ((NP\NP)/NP from)
                          (NP
                            (NP
                              (NP
                                (NP[nb]/N the)
                                (N
                                  (N/N 190-point)
                                  (N drop)))
                              (NP\NP
                                ((NP\NP)/NP in)
                                (NP
                                  (NP[nb]/N the)
                                  (N
                                    (N/N stock)
                                    (N market)))))
                            (NP\NP
                              ((NP\NP)/N[num] Oct.)
                              (N[num] 13))))))))))))
        (. .)))
    True

    """
    pass
    


def wsj_0241_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0241.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N
                (N/N Five)
                (N officials)))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP[nb]/N this)
                (N
                  (N/N investment)
                  (N
                    (N/N banking)
                    (N firm))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) were)
            (S[pss]\NP
              (S[pss]\NP
                ((S[pss]\NP)/NP elected)
                (NP
                  (N directors)))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP :)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N E.)
                        (N
                          (N/N Garrett)
                          (N
                            (N/N Bewkes)
                            (N III)))))
                    (NP[conj]
                      (, ,)
                      (NP
                        (NP
                          (NP[nb]/N a)
                          (N
                            (N/N 38-year-old)
                            (N
                              (N/N managing)
                              (N director))))
                        (NP\NP
                          ((NP\NP)/NP in)
                          (NP
                            (NP[nb]/N the)
                            (N
                              (N/N mergers)
                              (N
                                (conj and)
                                (N
                                  (N/N acquisitions)
                                  (N department)))))))))
                  (NP[conj]
                    (; ;)
                    (NP
                      (NP
                        (NP
                          (N
                            (N/N Michael)
                            (N
                              (N/N R.)
                              (N Dabney))))
                        (NP[conj]
                          (, ,)
                          (NP
                            (NP
                              (N 44))
                            (NP[conj]
                              (, ,)
                              (NP
                                (NP
                                  (NP[nb]/N a)
                                  (N
                                    (N/N managing)
                                    (N director)))
                                (NP\NP
                                  ((NP\NP)/(S[dcl]\NP) who)
                                  (S[dcl]\NP
                                    ((S[dcl]\NP)/NP directs)
                                    (NP
                                      (NP
                                        (NP[nb]/N the)
                                        (N
                                          (N/N principal)
                                          (N
                                            (N/N activities)
                                            (N group))))
                                      (NP\NP
                                        ((NP\NP)/(S[dcl]\NP) which)
                                        (S[dcl]\NP
                                          ((S[dcl]\NP)/NP provides)
                                          (NP
                                            (NP
                                              (N funding))
                                            (NP\NP
                                              ((NP\NP)/NP for)
                                              (NP
                                                (N
                                                  (N/N leveraged)
                                                  (N acquisitions)))))))))))))))
                      (NP[conj]
                        (; ;)
                        (NP
                          (NP
                            (NP
                              (N
                                (N/N Richard)
                                (N Harriton)))
                            (NP[conj]
                              (, ,)
                              (NP
                                (NP
                                  (N 53))
                                (NP[conj]
                                  (, ,)
                                  (NP
                                    (NP
                                      (NP[nb]/N a)
                                      (N
                                        (N/N general)
                                        (N partner)))
                                    (NP\NP
                                      ((NP\NP)/(S[dcl]\NP) who)
                                      (S[dcl]\NP
                                        ((S[dcl]\NP)/NP heads)
                                        (NP
                                          (NP[nb]/N the)
                                          (N
                                            (N/N correspondent)
                                            (N
                                              (N/N clearing)
                                              (N services)))))))))))
                          (NP[conj]
                            (; ;)
                            (NP
                              (NP
                                (NP
                                  (N
                                    (N/N Michael)
                                    (N Minikes)))
                                (NP[conj]
                                  (, ,)
                                  (NP
                                    (NP
                                      (N 46))
                                    (NP[conj]
                                      (, ,)
                                      (NP
                                        (NP
                                          (NP[nb]/N a)
                                          (N
                                            (N/N general)
                                            (N partner)))
                                        (NP\NP
                                          ((NP\NP)/(S[dcl]\NP) who)
                                          (S[dcl]\NP
                                            ((S[dcl]\NP)/NP is)
                                            (NP
                                              (N treasurer)))))))))
                              (NP[conj]
                                (; ;)
                                (NP[conj]
                                  (conj and)
                                  (NP
                                    (NP
                                      (N
                                        (N/N William)
                                        (N
                                          (N/N J.)
                                          (N Montgoris))))
                                    (NP[conj]
                                      (, ,)
                                      (NP
                                        (NP
                                          (N 42))
                                        (NP[conj]
                                          (, ,)
                                          (NP
                                            (NP
                                              (NP[nb]/N a)
                                              (N
                                                (N/N general)
                                                (N partner)))
                                            (NP\NP
                                              ((NP\NP)/(S[dcl]\NP) who)
                                              (S[dcl]\NP
                                                ((S[dcl]\NP)/NP
                                                  ((S[dcl]\NP)/NP is)
                                                  ((S\NP)\(S\NP) also))
                                                (NP
                                                  (NP
                                                    (NP
                                                      (N
                                                        (N/N senior)
                                                        (N
                                                          (N/N vice)
                                                          (N president))))
                                                    (NP\NP
                                                      ((NP\NP)/NP of)
                                                      (NP
                                                        (N finance))))
                                                  (NP[conj]
                                                    (conj and)
                                                    (NP
                                                      (N
                                                        (N/N chief)
                                                        (N
                                                          (N/N financial)
                                                          (N officer))))))))))))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N
                (N/N Five)
                (N officials)))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP[nb]/N this)
                (N
                  (N/N investment)
                  (N
                    (N/N banking)
                    (N firm))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) were)
            (S[pss]\NP
              (S[pss]\NP
                ((S[pss]\NP)/NP
                  (((S[b]\NP)/NP)/NP elect)
                  ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                (NP
                  (N directors)))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP :)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N E.)
                        (N
                          (N/N Garrett)
                          (N
                            (N/N Bewkes)
                            (N III)))))
                    (NP[conj]
                      (, ,)
                      (NP
                        (NP
                          (NP[nb]/N a)
                          (N
                            (N/N 38-year-old)
                            (N
                              (N/N managing)
                              (N director))))
                        (NP\NP
                          ((NP\NP)/NP in)
                          (NP
                            (NP[nb]/N the)
                            (N
                              (N/N mergers)
                              (N
                                (conj and)
                                (N
                                  (N/N acquisitions)
                                  (N department)))))))))
                  (NP[conj]
                    (; ;)
                    (NP
                      (NP
                        (NP
                          (N
                            (N/N Michael)
                            (N
                              (N/N R.)
                              (N Dabney))))
                        (NP[conj]
                          (, ,)
                          (NP
                            (NP
                              (N 44))
                            (NP[conj]
                              (, ,)
                              (NP
                                (NP
                                  (NP[nb]/N a)
                                  (N
                                    (N/N managing)
                                    (N director)))
                                (NP\NP
                                  ((NP\NP)/(S[dcl]\NP) who)
                                  (S[dcl]\NP
                                    ((S[dcl]\NP)/NP
                                      ((S[b]\NP)/NP direct)
                                      ((S[dcl]\NP)\(S[b]\NP) -es))
                                    (NP
                                      (NP
                                        (NP[nb]/N the)
                                        (N
                                          (N/N principal)
                                          (N
                                            (N/N activities)
                                            (N group))))
                                      (NP\NP
                                        ((NP\NP)/(S[dcl]\NP) which)
                                        (S[dcl]\NP
                                          ((S[dcl]\NP)/NP
                                            ((S[b]\NP)/NP provide)
                                            ((S[dcl]\NP)\(S[b]\NP) -es))
                                          (NP
                                            (NP
                                              (N funding))
                                            (NP\NP
                                              ((NP\NP)/NP for)
                                              (NP
                                                (N
                                                  (N/N leveraged)
                                                  (N acquisitions)))))))))))))))
                      (NP[conj]
                        (; ;)
                        (NP
                          (NP
                            (NP
                              (N
                                (N/N Richard)
                                (N Harriton)))
                            (NP[conj]
                              (, ,)
                              (NP
                                (NP
                                  (N 53))
                                (NP[conj]
                                  (, ,)
                                  (NP
                                    (NP
                                      (NP[nb]/N a)
                                      (N
                                        (N/N general)
                                        (N partner)))
                                    (NP\NP
                                      ((NP\NP)/(S[dcl]\NP) who)
                                      (S[dcl]\NP
                                        ((S[dcl]\NP)/NP
                                          ((S[b]\NP)/NP head)
                                          ((S[dcl]\NP)\(S[b]\NP) -es))
                                        (NP
                                          (NP[nb]/N the)
                                          (N
                                            (N/N correspondent)
                                            (N
                                              (N/N clearing)
                                              (N services)))))))))))
                          (NP[conj]
                            (; ;)
                            (NP
                              (NP
                                (NP
                                  (N
                                    (N/N Michael)
                                    (N Minikes)))
                                (NP[conj]
                                  (, ,)
                                  (NP
                                    (NP
                                      (N 46))
                                    (NP[conj]
                                      (, ,)
                                      (NP
                                        (NP
                                          (NP[nb]/N a)
                                          (N
                                            (N/N general)
                                            (N partner)))
                                        (NP\NP
                                          ((NP\NP)/(S[dcl]\NP) who)
                                          (S[dcl]\NP
                                            ((S[dcl]\NP)/NP is)
                                            (NP
                                              (N treasurer)))))))))
                              (NP[conj]
                                (; ;)
                                (NP[conj]
                                  (conj and)
                                  (NP
                                    (NP
                                      (N
                                        (N/N William)
                                        (N
                                          (N/N J.)
                                          (N Montgoris))))
                                    (NP[conj]
                                      (, ,)
                                      (NP
                                        (NP
                                          (N 42))
                                        (NP[conj]
                                          (, ,)
                                          (NP
                                            (NP
                                              (NP[nb]/N a)
                                              (N
                                                (N/N general)
                                                (N partner)))
                                            (NP\NP
                                              ((NP\NP)/(S[dcl]\NP) who)
                                              (S[dcl]\NP
                                                ((S[dcl]\NP)/NP
                                                  ((S[dcl]\NP)/NP is)
                                                  ((S\NP)\(S\NP) also))
                                                (NP
                                                  (NP
                                                    (NP
                                                      (N
                                                        (N/N senior)
                                                        (N
                                                          (N/N vice)
                                                          (N president))))
                                                    (NP\NP
                                                      ((NP\NP)/NP of)
                                                      (NP
                                                        (N finance))))
                                                  (NP[conj]
                                                    (conj and)
                                                    (NP
                                                      (N
                                                        (N/N chief)
                                                        (N
                                                          (N/N financial)
                                                          (N officer))))))))))))))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0242_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0242.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N Some)
            (N
              (N/N U.S.)
              (N allies)))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[ng]\NP) are)
            (S[ng]\NP
              ((S[ng]\NP)/S[em] complaining)
              (S[em]
                (S[em]/S[dcl] that)
                (S[dcl]
                  (NP
                    (N
                      (N/N President)
                      (N Bush)))
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[ng]\NP) is)
                    (S[ng]\NP
                      (S[ng]\NP
                        (S[ng]\NP
                          (S[ng]\NP
                            ((S[ng]\NP)/NP pushing)
                            (NP
                              (N
                                (N/N conventional-arms)
                                (N talks))))
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/((S\NP)\(S\NP)) too)
                            ((S\NP)\(S\NP) quickly)))
                        (, ,))
                      ((S\NP)\(S\NP)
                        (S[ng]\NP
                          ((S[ng]\NP)/NP creating)
                          (NP
                            (NP[nb]/N a)
                            (N
                              (N/S[em] risk)
                              (S[em]
                                (S[em]/S[dcl] that)
                                (S[dcl]
                                  (NP
                                    (N negotiators))
                                  (S[dcl]\NP
                                    ((S[dcl]\NP)/(S[b]\NP) will)
                                    (S[b]\NP
                                      ((S[b]\NP)/NP make)
                                      (NP
                                        (NP
                                          (N errors))
                                        (NP\NP
                                          ((NP\NP)/(S[dcl]\NP) that)
                                          (S[dcl]\NP
                                            ((S[dcl]\NP)/(S[b]\NP) could)
                                            (S[b]\NP
                                              (S[b]\NP
                                                ((S[b]\NP)/NP affect)
                                                (NP
                                                  (NP
                                                    (NP[nb]/N the)
                                                    (N security))
                                                  (NP\NP
                                                    ((NP\NP)/NP of)
                                                    (NP
                                                      (N
                                                        (N/N Western)
                                                        (N Europe))))))
                                              ((S\NP)\(S\NP)
                                                (((S\NP)\(S\NP))/NP for)
                                                (NP
                                                  (N years))))))))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N Some)
            (N
              (N/N U.S.)
              (N allies)))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[ng]\NP) are)
            (S[ng]\NP
              ((S[ng]\NP)/S[em]
                ((S[b]\NP)/S[em] complain)
                ((S[ng]\NP)\(S[b]\NP) -ing))
              (S[em]
                (S[em]/S[dcl] that)
                (S[dcl]
                  (NP
                    (N
                      (N/N President)
                      (N Bush)))
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[ng]\NP) is)
                    (S[ng]\NP
                      (S[ng]\NP
                        (S[ng]\NP
                          (S[ng]\NP
                            ((S[ng]\NP)/NP
                              ((S[b]\NP)/NP push)
                              ((S[ng]\NP)\(S[b]\NP) -ing))
                            (NP
                              (N
                                (N/N conventional-arms)
                                (N talks))))
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/((S\NP)\(S\NP)) too)
                            ((S\NP)\(S\NP) quickly)))
                        (, ,))
                      ((S\NP)\(S\NP)
                        (S[ng]\NP
                          ((S[ng]\NP)/NP
                            ((S[b]\NP)/NP create)
                            ((S[ng]\NP)\(S[b]\NP) -ing))
                          (NP
                            (NP[nb]/N a)
                            (N
                              (N/S[em] risk)
                              (S[em]
                                (S[em]/S[dcl] that)
                                (S[dcl]
                                  (NP
                                    (N negotiators))
                                  (S[dcl]\NP
                                    ((S[dcl]\NP)/(S[b]\NP) will)
                                    (S[b]\NP
                                      ((S[b]\NP)/NP make)
                                      (NP
                                        (NP
                                          (N errors))
                                        (NP\NP
                                          ((NP\NP)/(S[dcl]\NP) that)
                                          (S[dcl]\NP
                                            ((S[dcl]\NP)/(S[b]\NP) could)
                                            (S[b]\NP
                                              (S[b]\NP
                                                ((S[b]\NP)/NP affect)
                                                (NP
                                                  (NP
                                                    (NP[nb]/N the)
                                                    (N security))
                                                  (NP\NP
                                                    ((NP\NP)/NP of)
                                                    (NP
                                                      (N
                                                        (N/N Western)
                                                        (N Europe))))))
                                              ((S\NP)\(S\NP)
                                                (((S\NP)\(S\NP))/NP for)
                                                (NP
                                                  (N years))))))))))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0243_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0243.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N International)
              (N
                (N/N Lease)
                (N
                  (N/N Finance)
                  (N Corp.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP announced)
            (NP
              (NP
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N leasing)
                      (N contract)))
                  (NP\NP
                    ((NP\NP)/NP with)
                    (NP
                      (N
                        (N/N charter)
                        (N
                          (N/N carrier)
                          (N
                            (N/N American)
                            (N
                              (N/N Trans)
                              (N
                                (N/N Air)
                                (N Inc.)))))))))
                (, ,))
              (NP\NP
                ((NP\NP)/NP in)
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N transaction))
                  (NP\NP
                    (S[ng]\NP
                      ((S[ng]\NP)/NP involving)
                      (NP
                        (N
                          (N/N six)
                          (N
                            (N/N Boeing)
                            (N
                              (N/N Co.)
                              (N 757-200s))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N International)
              (N
                (N/N Lease)
                (N
                  (N/N Finance)
                  (N Corp.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP
              ((S[b]\NP)/NP announce)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (NP
              (NP
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N leasing)
                      (N contract)))
                  (NP\NP
                    ((NP\NP)/NP with)
                    (NP
                      (N
                        (N/N charter)
                        (N
                          (N/N carrier)
                          (N
                            (N/N American)
                            (N
                              (N/N Trans)
                              (N
                                (N/N Air)
                                (N Inc.)))))))))
                (, ,))
              (NP\NP
                ((NP\NP)/NP in)
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N transaction))
                  (NP\NP
                    (S[ng]\NP
                      ((S[ng]\NP)/NP
                        ((S[b]\NP)/NP involve)
                        ((S[ng]\NP)\(S[b]\NP) -ing))
                      (NP
                        (N
                          (N/N six)
                          (N
                            (N/N Boeing)
                            (N
                              (N/N Co.)
                              (N 757-200s))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0244_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0244.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N
                (NP
                  (N Norway))
                ((NP[nb]/N)\NP 's))
              (N
                (N/N unemployment)
                (N rate)))
            (NP\NP
              ((NP\NP)/NP for)
              (NP
                (N October))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP was)
            (NP
              (NP
                (NP
                  (N
                    (N/N 3.6)
                    (N %)))
                (, ,))
              (NP\NP
                (S[adj]\NP
                  (S[adj]\NP
                    ((S[adj]\NP)/PP unchanged)
                    (PP
                      (PP/NP from)
                      (NP
                        (N September))))
                  (S[adj]\NP[conj]
                    (conj but)
                    (S[adj]\NP
                      ((S[adj]\NP)/PP up)
                      (PP
                        (PP/NP from)
                        (NP
                          (NP
                            (N
                              (N/N 2.6)
                              (N %)))
                          (NP\NP
                            ((NP\NP)/NP in)
                            (NP
                              (NP
                                (NP[nb]/N the)
                                (N
                                  (N/N same)
                                  (N month)))
                              (NP\NP
                                ((NP\NP)/(NP\NP) last)
                                (NP\NP year)))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N
                (NP
                  (N Norway))
                ((NP[nb]/N)\NP 's))
              (N
                (N/N unemployment)
                (N rate)))
            (NP\NP
              ((NP\NP)/NP for)
              (NP
                (N October))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP was)
            (NP
              (NP
                (NP
                  (N
                    (N/N 3.6)
                    (N %)))
                (, ,))
              (NP\NP
                (S[adj]\NP
                  (S[adj]\NP
                    ((S[adj]\NP)/PP unchanged)
                    (PP
                      (PP/NP from)
                      (NP
                        (N September))))
                  (S[adj]\NP[conj]
                    (conj but)
                    (S[adj]\NP
                      ((S[adj]\NP)/PP up)
                      (PP
                        (PP/NP from)
                        (NP
                          (NP
                            (N
                              (N/N 2.6)
                              (N %)))
                          (NP\NP
                            ((NP\NP)/NP in)
                            (NP
                              (NP
                                (NP[nb]/N the)
                                (N
                                  (N/N same)
                                  (N month)))
                              (NP\NP
                                ((NP\NP)/(NP\NP) last)
                                (NP\NP year)))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0245_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0245.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Coca-Cola)
              (N Co.)))
          (S[dcl]\NP
            (, ,)
            (S[dcl]\NP
              ((S\NP)/(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/(S[to]\NP) aiming)
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/NP boost)
                      (NP
                        (NP
                          (N
                            (N/N soft-drink)
                            (N volume)))
                        (NP\NP
                          ((NP\NP)/NP in)
                          (NP
                            (N Singapore))))))))
              (S[dcl]\NP
                (, ,)
                (S[dcl]\NP
                  ((S[dcl]\NP)/S[dcl] said)
                  (S[dcl]
                    (NP it)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[ng]\NP) is)
                      (S[ng]\NP
                        (S[ng]\NP
                          ((S[ng]\NP)/NP discussing)
                          (NP
                            (NP[nb]/N a)
                            (N
                              (N/N joint)
                              (N venture))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP with)
                          (NP
                            (NP
                              (N
                                (N/N Fraser)
                                (N
                                  (N/N &)
                                  (N
                                    (N/N Neave)
                                    (N Ltd.)))))
                            (NP[conj]
                              (, ,)
                              (NP
                                (NP
                                  (NP[nb]/N its)
                                  (N
                                    (N/N bottling)
                                    (N franchisee)))
                                (NP\NP
                                  ((NP\NP)/NP in)
                                  (NP
                                    (NP[nb]/N that)
                                    (N country)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Coca-Cola)
              (N Co.)))
          (S[dcl]\NP
            (, ,)
            (S[dcl]\NP
              ((S\NP)/(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/(S[to]\NP)
                    ((S[b]\NP)/(S[to]\NP) aim)
                    ((S[ng]\NP)\(S[b]\NP) -ing))
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/NP boost)
                      (NP
                        (NP
                          (N
                            (N/N soft-drink)
                            (N volume)))
                        (NP\NP
                          ((NP\NP)/NP in)
                          (NP
                            (N Singapore))))))))
              (S[dcl]\NP
                (, ,)
                (S[dcl]\NP
                  ((S[dcl]\NP)/S[dcl]
                    ((S[b]\NP)/S[dcl] say)
                    ((S[dcl]\NP)\(S[b]\NP) -es))
                  (S[dcl]
                    (NP it)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[ng]\NP) is)
                      (S[ng]\NP
                        (S[ng]\NP
                          ((S[ng]\NP)/NP
                            ((S[b]\NP)/NP discuss)
                            ((S[ng]\NP)\(S[b]\NP) -ing))
                          (NP
                            (NP[nb]/N a)
                            (N
                              (N/N joint)
                              (N venture))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP with)
                          (NP
                            (NP
                              (N
                                (N/N Fraser)
                                (N
                                  (N/N &)
                                  (N
                                    (N/N Neave)
                                    (N Ltd.)))))
                            (NP[conj]
                              (, ,)
                              (NP
                                (NP
                                  (NP[nb]/N its)
                                  (N
                                    (N/N bottling)
                                    (N franchisee)))
                                (NP\NP
                                  ((NP\NP)/NP in)
                                  (NP
                                    (NP[nb]/N that)
                                    (N country)))))))))))))))
        (. .)))
    True

    """
    pass
    


def wsj_0246_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0246.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (N
                    (N/N AMERICAN)
                    (N
                      (N/N BRANDS)
                      (N Inc.))))
                (, ,))
              (NP\NP
                (NP\NP
                  ((NP\NP)/(NP\NP) Old)
                  (NP\NP Greenwich))
                (NP\NP[conj]
                  (, ,)
                  (NP\NP Conn.))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP
                        ((S[dcl]\NP)/NP increased)
                        (NP
                          (NP[nb]/N its)
                          (N
                            (N/N quarterly)
                            (N
                              (N/N 11)
                              (N %)))))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP to)
                        (NP
                          (NP
                            (N
                              (N/N 68)
                              (N cents)))
                          (NP\NP
                            ((NP\NP)/N a)
                            (N share)))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP from)
                      (NP
                        (N
                          (N/N 61)
                          (N cents)))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (S[adj]\NP
                    ((S[adj]\NP)/PP
                      (((S[adj]\NP)/PP)/NP payable)
                      (NP
                        (N
                          (N/N[num] Dec.)
                          (N[num] 1))))
                    (PP
                      (PP/NP to)
                      (NP
                        (NP
                          (NP
                            (N stock))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (N record))))
                        (NP\NP
                          ((NP\NP)/N[num] Nov.)
                          (N[num] 10))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (N
                    (N/N AMERICAN)
                    (N
                      (N/N BRANDS)
                      (N Inc.))))
                (, ,))
              (NP\NP
                (NP\NP
                  ((NP\NP)/(NP\NP) Old)
                  (NP\NP Greenwich))
                (NP\NP[conj]
                  (, ,)
                  (NP\NP Conn.))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      (S[dcl]\NP
                        ((S[dcl]\NP)/NP
                          ((S[b]\NP)/NP increase)
                          ((S[dcl]\NP)\(S[b]\NP) -es))
                        (NP
                          (NP[nb]/N its)
                          (N
                            (N/N quarterly)
                            (N
                              (N/N 11)
                              (N %)))))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP to)
                        (NP
                          (NP
                            (N
                              (N/N 68)
                              (N cents)))
                          (NP\NP
                            ((NP\NP)/N a)
                            (N share)))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP from)
                      (NP
                        (N
                          (N/N 61)
                          (N cents)))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (S[adj]\NP
                    ((S[adj]\NP)/PP
                      (((S[adj]\NP)/PP)/NP payable)
                      (NP
                        (N
                          (N/N[num] Dec.)
                          (N[num] 1))))
                    (PP
                      (PP/NP to)
                      (NP
                        (NP
                          (NP
                            (N stock))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (N record))))
                        (NP\NP
                          ((NP\NP)/N[num] Nov.)
                          (N[num] 10))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0247_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0247.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Giovanni)
              (N
                (N/N Agnelli)
                (N
                  (N/N &)
                  (N Co.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP announced)
            (NP
              (NP
                (NP[nb]/N a)
                (N transaction))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) that)
                (S[dcl]\NP
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[b]\NP) will)
                    (S[b]\NP
                      ((S[b]\NP)/NP strengthen)
                      (NP
                        (NP
                          (NP[nb]/N its)
                          (N
                            (N/N indirect)
                            (N control)))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N
                              (N/N Fiat)
                              (N
                                (N/N S.p)
                                (N
                                  (. .)
                                  (N A.)))))))))
                  (S[dcl]\NP[conj]
                    (conj and)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[b]\NP) will)
                      (S[b]\NP
                        (S[b]\NP
                          ((S[b]\NP)/NP admit)
                          (NP
                            (N
                              (N/N Prince)
                              (N
                                (N/N Karim)
                                (N
                                  (N/N Aga)
                                  (N Khan))))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP as)
                          (NP
                            (NP[nb]/N its)
                            (N
                              (N/N first)
                              (N
                                (N/N non-family)
                                (N shareholder)))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Giovanni)
              (N
                (N/N Agnelli)
                (N
                  (N/N &)
                  (N Co.)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP
              ((S[b]\NP)/NP announce)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (NP
              (NP
                (NP[nb]/N a)
                (N transaction))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) that)
                (S[dcl]\NP
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[b]\NP) will)
                    (S[b]\NP
                      ((S[b]\NP)/NP strengthen)
                      (NP
                        (NP
                          (NP[nb]/N its)
                          (N
                            (N/N indirect)
                            (N control)))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N
                              (N/N Fiat)
                              (N
                                (N/N S.p)
                                (N
                                  (. .)
                                  (N A.)))))))))
                  (S[dcl]\NP[conj]
                    (conj and)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[b]\NP) will)
                      (S[b]\NP
                        (S[b]\NP
                          ((S[b]\NP)/NP admit)
                          (NP
                            (N
                              (N/N Prince)
                              (N
                                (N/N Karim)
                                (N
                                  (N/N Aga)
                                  (N Khan))))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP as)
                          (NP
                            (NP[nb]/N its)
                            (N
                              (N/N first)
                              (N
                                (N/N non-family)
                                (N shareholder)))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0248_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0248.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N Your)
              (N
                (N/N Oct.)
                (N
                  (N/N 2)
                  (N
                    (N/N page-one)
                    (N article)))))
            (NP\NP
              ((NP\NP)/NP on)
              (NP
                (NP
                  (N people))
                (NP\NP
                  (S[ng]\NP
                    (S[ng]\NP
                      ((S[ng]\NP)/NP riding)
                      (NP
                        (N
                          (N/N so-called)
                          (N railbikes))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP on)
                      (NP
                        (N
                          (N/N railroad)
                          (N tracks)))))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP was)
            (NP
              (NP
                (NP[nb]/N a)
                (N disservice))
              (NP\NP
                ((NP\NP)/NP to)
                (NP
                  (NP[nb]/N your)
                  (N readers))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N Your)
              (N
                (N/N Oct.)
                (N
                  (N/N 2)
                  (N
                    (N/N page-one)
                    (N article)))))
            (NP\NP
              ((NP\NP)/NP on)
              (NP
                (NP
                  (N people))
                (NP\NP
                  (S[ng]\NP
                    (S[ng]\NP
                      ((S[ng]\NP)/NP
                        ((S[b]\NP)/NP ride)
                        ((S[ng]\NP)\(S[b]\NP) -ing))
                      (NP
                        (N
                          (N/N so-called)
                          (N railbikes))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP on)
                      (NP
                        (N
                          (N/N railroad)
                          (N tracks)))))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP was)
            (NP
              (NP
                (NP[nb]/N a)
                (N disservice))
              (NP\NP
                ((NP\NP)/NP to)
                (NP
                  (NP[nb]/N your)
                  (N readers))))))
        (. .)))
    True
    """
    pass
    


def wsj_0249_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0249.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N MCI)
              (N
                (N/N Communications)
                (N Corp.))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP received)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N three-year)
                        (N contract)))
                    (NP\NP
                      (S[pss]\NP
                        ((S[pss]\NP)/PP valued)
                        (PP
                          (PP/NP at)
                          (NP
                            (N
                              (N/N
                                (S[adj]\NP more)
                                ((N/N)\(S[adj]\NP) than))
                              (N
                                (N/N[num] $)
                                (N[num]
                                  (N/N 15)
                                  (N[num] million)))))))))
                  (NP\NP
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/PP
                          (((S[b]\NP)/PP)/NP provide)
                          (NP
                            (N
                              (N/N network)
                              (N
                                (, ,)
                                (N
                                  (N/N credit-card)
                                  (N
                                    (conj and)
                                    (N
                                      (N/N other)
                                      (N
                                        (N/N telecommunications)
                                        (N services)))))))))
                        (PP
                          (PP/NP to)
                          (NP
                            (N
                              (N/N Drexel)
                              (N
                                (N/N Burnham)
                                (N
                                  (N/N Lambert)
                                  (N Inc))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N MCI)
              (N
                (N/N Communications)
                (N Corp.))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl]
              ((S[b]\NP)/S[dcl] say)
              ((S[dcl]\NP)\(S[b]\NP) -es))
            (S[dcl]
              (NP it)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP
                  ((S[b]\NP)/NP receive)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (NP
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N three-year)
                        (N contract)))
                    (NP\NP
                      (S[pss]\NP
                        ((S[pss]\NP)/PP
                          (((S[b]\NP)/NP)/PP value)
                          ((S[pss]\NP)\((S[b]\NP)/NP) -en))
                        (PP
                          (PP/NP at)
                          (NP
                            (N
                              (N/N
                                (S[adj]\NP more)
                                ((N/N)\(S[adj]\NP) than))
                              (N
                                (N/N[num] $)
                                (N[num]
                                  (N/N 15)
                                  (N[num] million)))))))))
                  (NP\NP
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/PP
                          (((S[b]\NP)/PP)/NP provide)
                          (NP
                            (N
                              (N/N network)
                              (N
                                (, ,)
                                (N
                                  (N/N credit-card)
                                  (N
                                    (conj and)
                                    (N
                                      (N/N other)
                                      (N
                                        (N/N telecommunications)
                                        (N services)))))))))
                        (PP
                          (PP/NP to)
                          (NP
                            (N
                              (N/N Drexel)
                              (N
                                (N/N Burnham)
                                (N
                                  (N/N Lambert)
                                  (N Inc))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0250_1():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0250.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N
                (N/N Congressional)
                (N Democrats)))
            (NP[conj]
              (conj and)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Bush)
                  (N administration)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/PP agreed)
                (PP
                  (PP/NP on)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N compromise)
                      (N
                        (N/N minimum-wage)
                        (N bill))))))
              (, ,))
            ((S\NP)\(S\NP)
              (S[ng]\NP
                ((S[ng]\NP)/NP opening)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N way))
                  (NP\NP
                    ((NP\NP)/NP for)
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N first)
                          (N
                            (N/N wage-floor)
                            (N boost))))
                      (NP\NP
                        ((NP\NP)/NP in)
                        (NP
                          (N
                            (N/N
                              ((N/N)/(N/N)
                                (S[adj]\NP more)
                                (((N/N)/(N/N))\(S[adj]\NP) than))
                              (N/N nine))
                            (N years)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N
                (N/N Congressional)
                (N Democrats)))
            (NP[conj]
              (conj and)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Bush)
                  (N administration)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/PP
                  ((S[b]\NP)/PP agree)
                  ((S[dcl]\NP)\(S[b]\NP) -es))
                (PP
                  (PP/NP on)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N compromise)
                      (N
                        (N/N minimum-wage)
                        (N bill))))))
              (, ,))
            ((S\NP)\(S\NP)
              (S[ng]\NP
                ((S[ng]\NP)/NP
                  ((S[b]\NP)/NP open)
                  ((S[ng]\NP)\(S[b]\NP) -ing))
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N way))
                  (NP\NP
                    ((NP\NP)/NP for)
                    (NP
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N first)
                          (N
                            (N/N wage-floor)
                            (N boost))))
                      (NP\NP
                        ((NP\NP)/NP in)
                        (NP
                          (N
                            (N/N
                              ((N/N)/(N/N)
                                (S[adj]\NP more)
                                (((N/N)/(N/N))\(S[adj]\NP) than))
                              (N/N nine))
                            (N years)))))))))))
        (. .)))
    True
    """
    pass

def wsj_0003_18_agent_passive():
    """
    >>> debug('data/CCGbank1.2/', 'wsj_0003.18')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP[nb]/N The)
                  (N plant))
                (, ,))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) which)
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[pss]\NP) is)
                  (S[pss]\NP
                    (S[pss]\NP owned)
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP by)
                      (NP
                        (N
                          (N/N Hollingsworth)
                          (N
                            (N/N &)
                            (N
                              (N/N Vose)
                              (N Co.))))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/PP was)
            (PP
              (PP/NP under)
              (NP
                (NP
                  (NP
                    (N contract))
                  (NP\NP
                    ((NP\NP)/NP with)
                    (NP
                      (N Lorillard))))
                (NP\NP
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/NP make)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N cigarette)
                          (N filters))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP
                  (NP[nb]/N The)
                  (N plant))
                (, ,))
              (NP\NP
                ((NP\NP)/(S[dcl]\NP) which)
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[pss]\NP) is)
                  (S[pss]\NP
                    ((S[pss]\NP)/PP
                      ((S[b]\NP)/NP own)
                      (((S[pss]\NP)/PP)\((S[b]\NP)/NP) -en))
                    (PP
                      (PP/NP by)
                      (NP
                        (N
                          (N/N Hollingsworth)
                          (N
                            (N/N &)
                            (N
                              (N/N Vose)
                              (N Co.))))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/PP was)
            (PP
              (PP/NP under)
              (NP
                (NP
                  (NP
                    (N contract))
                  (NP\NP
                    ((NP\NP)/NP with)
                    (NP
                      (N Lorillard))))
                (NP\NP
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/NP make)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N cigarette)
                          (N filters))))))))))
        (. .)))
    True

    """
    
if __name__ == '__main__':
    doctest.testmod()
