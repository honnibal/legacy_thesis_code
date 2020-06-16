import doctest
from __init__ import debug


def wsj_0421_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0421.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N USG)
              (N Corp.)))
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/(S[to]\NP) agreed)
              (S[to]\NP
                ((S[to]\NP)/(S[b]\NP) to)
                (S[b]\NP
                  ((S[b]\NP)/PP
                    (((S[b]\NP)/PP)/NP sell)
                    (NP
                      (NP
                        (NP[nb]/N its)
                        (N
                          (N/N headquarters)
                          (N building)))
                      (NP\NP here)))
                  (PP
                    (PP/NP to)
                    (NP
                      (NP
                        (N
                          (N/N
                            ((N/N)/(N/N) Manufacturers)
                            (N/N
                              ((N/N)/(N/N) Life)
                              (N/N Insurance)))
                          (N Co.)))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (N Toronto))))))))
            (S[dcl]\NP[conj]
              (, ,)
              (S[dcl]\NP[conj]
                (conj and)
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[b]\NP) will)
                  (S[b]\NP
                    (S[b]\NP
                      ((S[b]\NP)/NP lease)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N 19-story)
                          (N facility))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/S[dcl] until)
                      (S[dcl]
                        (NP it)
                        (S[dcl]\NP
                          (S[dcl]\NP
                            (S[dcl]\NP moves)
                            ((S\NP)\(S\NP)
                              (((S\NP)\(S\NP))/NP to)
                              (NP
                                (NP[nb]/N a)
                                (N
                                  (N/N new)
                                  (N quarters)))))
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/NP in)
                            (NP
                              (N 1992))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N USG)
              (N Corp.)))
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/(S[to]\NP) agreed)
              (S[to]\NP
                ((S[to]\NP)/(S[b]\NP) to)
                (S[b]\NP
                  ((S[b]\NP)/PP
                    (((S[b]\NP)/PP)/NP sell)
                    (NP
                      (NP[nb]/N its)
                      (N
                        (N/N headquarters)
                        (N
                          (N building)
                          (N\N here)))))
                  (PP
                    (PP/NP to)
                    (NP
                      (N
                        (N/N
                          ((N/N)/(N/N) Manufacturers)
                          (N/N
                            ((N/N)/(N/N) Life)
                            (N/N Insurance)))
                        (N
                          (N Co.)
                          (N\N
                            ((N\N)/NP of)
                            (NP
                              (N Toronto))))))))))
            (S[dcl]\NP[conj]
              (, ,)
              (S[dcl]\NP[conj]
                (conj and)
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[b]\NP) will)
                  (S[b]\NP
                    (S[b]\NP
                      ((S[b]\NP)/NP lease)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N 19-story)
                          (N facility))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/S[dcl] until)
                      (S[dcl]
                        (NP it)
                        (S[dcl]\NP
                          (S[dcl]\NP
                            ((S[dcl]\NP)/PP moves)
                            (PP
                              (PP/NP to)
                              (NP
                                (NP[nb]/N a)
                                (N
                                  (N/N new)
                                  (N quarters)))))
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/NP in)
                            (NP
                              (N 1992))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0422_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0422.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP[nb]/N The)
                (N
                  (N/N
                    ((N/N)/(N/N) recently)
                    (N/N revived))
                  (N enthusiasm)))
              (NP\NP
                ((NP\NP)/NP among)
                (NP
                  (N
                    (N/N small)
                    (N investors)))))
            (NP\NP
              ((NP\NP)/NP for)
              (NP
                (N
                  (N/N stock)
                  (N
                    (N/N mutual)
                    (N funds))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pt]\NP) has)
            (S[pt]\NP
              ((S[pt]\NP)/(S[pss]\NP) been)
              (S[pss]\NP
                (S[pss]\NP damped)
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP by)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N jittery)
                        (N
                          (N/N stock)
                          (N market))))
                    (NP[conj]
                      (conj and)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N tumult))
                        (NP\NP
                          ((NP\NP)/NP over)
                          (NP
                            (N
                              (N/N program)
                              (N trading))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N
              (N/N
                ((N/N)/(N/N) recently)
                (N/N revived))
              (N
                (N/PP
                  ((N/PP)/PP enthusiasm)
                  (PP
                    (PP/NP among)
                    (NP
                      (N
                        (N/N small)
                        (N investors)))))
                (PP
                  (PP/NP for)
                  (NP
                    (N
                      (N/N stock)
                      (N
                        (N/N mutual)
                        (N funds))))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pt]\NP) has)
            (S[pt]\NP
              ((S[pt]\NP)/(S[pss]\NP) been)
              (S[pss]\NP
                ((S[pss]\NP)/PP damped)
                (PP
                  (PP/NP by)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N jittery)
                        (N
                          (N/N stock)
                          (N market))))
                    (NP[conj]
                      (conj and)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/PP tumult)
                          (PP
                            (PP/NP over)
                            (NP
                              (N
                                (N/N program)
                                (N trading)))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0423_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0423.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N
                (N/N Secretary)
                ((N/N)\(N/N)
                  (((N/N)\(N/N))/NP of)
                  (NP
                    (N State))))
              (N Baker)))
          (S[dcl]\NP
            ((S\NP)/(S\NP)
              (, ,)
              ((S\NP)/(S\NP)
                (S[dcl]/S[dcl]
                  (S/(S\NP)
                    (NP we))
                  ((S[dcl]\NP)/S[dcl] read))
                (, ,)))
            (S[dcl]\NP
              ((S[dcl]\NP)/(S[to]\NP) decided)
              (S[to]\NP
                ((S[to]\NP)/(S[b]\NP) to)
                (S[b]\NP
                  ((S[b]\NP)/NP kill)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N speech))
                    (NP\NP
                      ((NP\NP)/(S[dcl]/NP) that)
                      (S[dcl]/NP
                        (S/(S\NP)
                          (NP
                            (NP
                              (NP
                                (N
                                  (N/N Robert)
                                  (N Gates)))
                              (NP[conj]
                                (, ,)
                                (NP
                                  (NP
                                    (N
                                      (N/N deputy)
                                      (N
                                        (N/N
                                          ((N/N)/(N/N) national)
                                          (N/N security))
                                        (N adviser))))
                                  (NP[conj]
                                    (conj and)
                                    (NP
                                      (NP[nb]/N a)
                                      (N
                                        (N/N career)
                                        (N
                                          (N/N Soviet)
                                          (N expert))))))))
                            (, ,)))
                        ((S[dcl]\NP)/NP
                          ((S[dcl]\NP)/(S[ng]\NP) was)
                          ((S[ng]\NP)/NP
                            ((S[ng]\NP)/(S[to]\NP) going)
                            ((S[to]\NP)/NP
                              ((S[to]\NP)/(S[b]\NP) to)
                              ((S[b]\NP)/NP
                                (((S[b]\NP)/PP)/NP give)
                                ((S\NP)\((S\NP)/PP)
                                  (PP
                                    (PP/NP to)
                                    (NP
                                      (NP
                                        (NP[nb]/N a)
                                        (N
                                          (N/N student)
                                          (N colloquium)))
                                      (NP[conj]
                                        (, ,)
                                        (NP
                                          (NP[nb]/N the)
                                          (N
                                            (N/N National)
                                            (N
                                              (N/N Collegiate)
                                              (N
                                                (N/N Security)
                                                (N Conference)))))))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N
                (N/N Secretary)
                ((N/N)\(N/N)
                  (((N/N)\(N/N))/NP of)
                  (NP
                    (N State))))
              (N Baker)))
          (S[dcl]\NP
            ((S\NP)/(S\NP)
              (, ,)
              ((S\NP)/(S\NP)
                (S[dcl]/S[dcl]
                  (S/(S\NP)
                    (NP we))
                  ((S[dcl]\NP)/S[dcl] read))
                (, ,)))
            (S[dcl]\NP
              ((S[dcl]\NP)/(S[to]\NP) decided)
              (S[to]\NP
                ((S[to]\NP)/(S[b]\NP) to)
                (S[b]\NP
                  ((S[b]\NP)/NP kill)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N speech)
                      (N\N
                        ((N\N)/(S[dcl]/NP) that)
                        (S[dcl]/NP
                          (S/(S\NP)
                            (NP
                              (NP
                                (NP
                                  (N
                                    (N/N Robert)
                                    (N Gates)))
                                (NP[conj]
                                  (, ,)
                                  (NP
                                    (NP
                                      (N
                                        (N/N deputy)
                                        (N
                                          (N/N
                                            ((N/N)/(N/N) national)
                                            (N/N security))
                                          (N adviser))))
                                    (NP[conj]
                                      (conj and)
                                      (NP
                                        (NP[nb]/N a)
                                        (N
                                          (N/N career)
                                          (N
                                            (N/N Soviet)
                                            (N expert))))))))
                              (, ,)))
                          ((S[dcl]\NP)/NP
                            ((S[dcl]\NP)/(S[ng]\NP) was)
                            ((S[ng]\NP)/NP
                              ((S[ng]\NP)/(S[to]\NP) going)
                              ((S[to]\NP)/NP
                                ((S[to]\NP)/(S[b]\NP) to)
                                ((S[b]\NP)/NP
                                  (((S[b]\NP)/PP)/NP give)
                                  ((S\NP)\((S\NP)/PP)
                                    (PP
                                      (PP/NP to)
                                      (NP
                                        (NP
                                          (NP[nb]/N a)
                                          (N
                                            (N/N student)
                                            (N colloquium)))
                                        (NP[conj]
                                          (, ,)
                                          (NP
                                            (NP[nb]/N the)
                                            (N
                                              (N/N National)
                                              (N
                                                (N/N Collegiate)
                                                (N
                                                  (N/N Security)
                                                  (N Conference))))))))))))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0424_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0424.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Vernon)
              (N
                (N/N E.)
                (N Jordan))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/PP elected)
              (PP
                (PP/NP to)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N board))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP[nb]/N this)
                      (N
                        (N/N
                          ((N/N)/(N/N) transportation)
                          (N/N services))
                        (N concern)))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Vernon)
              (N
                (N/N E.)
                (N Jordan))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[pss]\NP) was)
            (S[pss]\NP
              ((S[pss]\NP)/PP elected)
              (PP
                (PP/NP to)
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/PP board)
                    (PP
                      (PP/NP of)
                      (NP
                        (NP[nb]/N this)
                        (N
                          (N/N
                            ((N/N)/(N/N) transportation)
                            (N/N services))
                          (N concern))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0425_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0425.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N
              (N/N American)
              (N
                (N/N Stock)
                (N Exchange))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP
                (NP[nb]/N a)
                (N seat))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pss]\NP) was)
                (S[pss]\NP
                  ((S[pss]\NP)/PP sold)
                  (PP
                    (PP/NP for)
                    (NP
                      (NP
                        (NP
                          (N
                            (N/N[num] $)
                            (N[num] 160,000)))
                        (, ,))
                      (NP\NP
                        ((NP\NP)/PP
                          (((NP\NP)/PP)/NP down)
                          (NP
                            (N
                              (N/N[num] $)
                              (N[num] 5,000))))
                        (PP
                          (PP
                            (PP/NP from)
                            (NP
                              (NP[nb]/N the)
                              (N
                                (N/N previous)
                                (N sale))))
                          (PP\PP
                            ((PP\PP)/(PP\PP) last)
                            (PP\PP Friday)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N
              (N/N American)
              (N
                (N/N Stock)
                (N Exchange))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP
                (NP[nb]/N a)
                (N seat))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pss]\NP) was)
                (S[pss]\NP
                  ((S[pss]\NP)/PP sold)
                  (PP
                    (PP/NP for)
                    (NP
                      (NP
                        (NP
                          (N
                            (N/N[num] $)
                            (N[num] 160,000)))
                        (, ,))
                      (NP\NP
                        ((NP\NP)/PP
                          (((NP\NP)/PP)/NP down)
                          (NP
                            (N
                              (N/N[num] $)
                              (N[num] 5,000))))
                        (PP
                          (PP
                            (PP/NP from)
                            (NP
                              (NP[nb]/N the)
                              (N
                                (N/N previous)
                                (N sale))))
                          (PP\PP
                            ((PP\PP)/(PP\PP) last)
                            (PP\PP Friday)))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0426_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0426.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Two)
              (N gunmen)))
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/NP entered)
              (NP
                (NP[nb]/N a)
                (N
                  (N/N Maryland)
                  (N restaurant))))
            (S[dcl]\NP[conj]
              (, ,)
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[to]\NP)
                    (((S[dcl]\NP)/(S[to]\NP))/NP ordered)
                    (NP
                      (N
                        (N/N two)
                        (N employees))))
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      (S[b]\NP lie)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP on)
                        (NP
                          (NP[nb]/N the)
                          (N floor))))))
                (S[dcl]\NP[conj]
                  (conj and)
                  (S[dcl]\NP
                    (S[dcl]\NP
                      ((S[dcl]\NP)/NP shot)
                      (NP them))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N backs))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (NP[nb]/N their)
                            (N heads)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Two)
              (N gunmen)))
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/NP entered)
              (NP
                (NP[nb]/N a)
                (N
                  (N/N Maryland)
                  (N restaurant))))
            (S[dcl]\NP[conj]
              (, ,)
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[to]\NP)
                    (((S[dcl]\NP)/(S[to]\NP))/NP ordered)
                    (NP
                      (N
                        (N/N two)
                        (N employees))))
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/PP lie)
                      (PP
                        (PP/NP on)
                        (NP
                          (NP[nb]/N the)
                          (N floor))))))
                (S[dcl]\NP[conj]
                  (conj and)
                  (S[dcl]\NP
                    ((S[dcl]\NP)/PP
                      (((S[dcl]\NP)/PP)/NP shot)
                      (NP them))
                    (PP
                      (PP/NP in)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/PP backs)
                          (PP
                            (PP/NP of)
                            (NP
                              (NP[nb]/N their)
                              (N heads))))))))))))
        (. .)))
    True
    """
    pass
    


def wsj_0427_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0427.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N A)
            (N
              (N/N state)
              (N judge)))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP postponed)
            (NP
              (NP
                (NP[nb]/N a)
                (N decision))
              (NP\NP
                ((NP\NP)/NP on)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N move))
                    (NP\NP
                      ((NP\NP)/NP by)
                      (NP
                        (NP
                          (N holders))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N
                              (N/N Telerate)
                              (N Inc.)))))))
                  (NP\NP
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP block)
                        (NP
                          (NP
                            (NP
                              (NP[nb]/N the)
                              (N
                                (N/N tender)
                                (N offer)))
                            (NP\NP
                              ((NP\NP)/NP of)
                              (NP
                                (N
                                  (N/N
                                    ((N/N)/(N/N) Dow)
                                    (N/N Jones))
                                  (N
                                    (N/N &)
                                    (N Co.))))))
                          (NP\NP
                            ((NP\NP)/NP for)
                            (NP
                              (NP
                                (NP
                                  (NP[nb]/N the)
                                  (N
                                    (N/N 33)
                                    (N %)))
                                (NP\NP
                                  ((NP\NP)/NP of)
                                  (NP
                                    (N Telerate))))
                              (NP\NP
                                (S[dcl]/NP
                                  (S/(S\NP)
                                    (NP it))
                                  ((S[dcl]\NP)/NP
                                    ((S[dcl]\NP)/(S[b]\NP)
                                      ((S[dcl]\NP)/(S[b]\NP)
                                        ((S[dcl]\NP)/(S[b]\NP) does)
                                        ((S\NP)\(S\NP) n't))
                                      ((S\NP)\(S\NP) already))
                                    ((S[b]\NP)/NP own)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N A)
            (N
              (N/N state)
              (N judge)))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP postponed)
            (NP
              (NP[nb]/N a)
              (N
                (N/PP decision)
                (PP
                  (PP/NP on)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/(S[to]\NP)
                        ((N/(S[to]\NP))/PP move)
                        (PP
                          (PP/NP by)
                          (NP
                            (N
                              (N/PP holders)
                              (PP
                                (PP/NP of)
                                (NP
                                  (N
                                    (N/N Telerate)
                                    (N Inc.))))))))
                      (S[to]\NP
                        ((S[to]\NP)/(S[b]\NP) to)
                        (S[b]\NP
                          ((S[b]\NP)/NP block)
                          (NP
                            (NP[nb]/N the)
                            (N
                              (N/N tender)
                              (N
                                (N/PP
                                  ((N/PP)/PP offer)
                                  (PP
                                    (PP/NP of)
                                    (NP
                                      (N
                                        (N/N
                                          ((N/N)/(N/N) Dow)
                                          (N/N Jones))
                                        (N
                                          (N/N &)
                                          (N Co.))))))
                                (PP
                                  (PP/NP for)
                                  (NP
                                    (NP[nb]/N the)
                                    (N
                                      (N/N 33)
                                      (N
                                        (N
                                          (N/PP %)
                                          (PP
                                            (PP/NP of)
                                            (NP
                                              (N Telerate))))
                                        (N\N
                                          (S[dcl]/NP
                                            (S/(S\NP)
                                              (NP it))
                                            ((S[dcl]\NP)/NP
                                              ((S[dcl]\NP)/(S[b]\NP)
                                                ((S[dcl]\NP)/(S[b]\NP)
                                                  ((S[dcl]\NP)/(S[b]\NP) does)
                                                  ((S\NP)\(S\NP) n't))
                                                ((S\NP)\(S\NP) already))
                                              ((S[b]\NP)/NP own))))))))))))))))))))
        (. .)))
    Invalid: N\N --> S[dcl]/NP None
    False
    """
    pass



def wsj_0428_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0428.1')
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
                (N exports))
              (NP\NP
                ((NP\NP)/NP of)
                (NP
                  (N
                    (N cars)
                    (N[conj]
                      (, ,)
                      (N
                        (N trucks)
                        (N[conj]
                          (conj and)
                          (N buses))))))))
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP declined)
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 2.4)
                      ((S\NP)\(S\NP) %)))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP to)
                    (NP
                      (N
                        (N/N 535,322)
                        (N units)))))
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
          (S[dcl]\S[dcl]
            (, ,)
            (S[dcl]\S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Japan)
                  (N
                    (N/N
                      ((N/N)/(N/N) Automobile)
                      (N/N Manufacturers))
                    (N Association))))
              ((S[dcl]\S[dcl])\NP said))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (NP/(N/PP)
                (NP
                  (N Japan))
                ((NP/(N/PP))\NP 's))
              (N/PP
                ((N/PP)/PP exports)
                (PP
                  (PP/NP of)
                  (NP
                    (N
                      (N cars)
                      (N[conj]
                        (, ,)
                        (N
                          (N trucks)
                          (N[conj]
                            (conj and)
                            (N buses)))))))))
            (S[dcl]\NP
              ((S[dcl]\NP)/PP
                ((S[dcl]\NP)/PP
                  (((S[dcl]\NP)/PP)/PP
                    ((((S[dcl]\NP)/PP)/PP)/NP declined)
                    (NP
                      (N
                        (N/N 2.4)
                        (N %))))
                  (PP
                    (PP/NP to)
                    (NP
                      (N
                        (N/N 535,322)
                        (N units)))))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP in)
                  (NP
                    (N September))))
              (PP
                (PP/(S[adj]\NP) from)
                (S[adj]\NP
                  (NP
                    (NP[nb]/N a)
                    (N year))
                  ((S[adj]\NP)\NP earlier)))))
          (S[dcl]\S[dcl]
            (, ,)
            (S[dcl]\S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Japan)
                  (N
                    (N/N
                      ((N/N)/(N/N) Automobile)
                      (N/N Manufacturers))
                    (N Association))))
              ((S[dcl]\S[dcl])\NP said))))
        (. .)))
    True
    """
    pass
    


def wsj_0429_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0429.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N
                ((N/N)/(N/N)
                  (((N/N)/(N/N))/((N/N)/(N/N)) Lone)
                  ((N/N)/(N/N) Star))
                (N/N Technologies))
              (N Inc.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP
                (NP[nb]/N its)
                (N
                  (N/N
                    ((N/N)/(N/N)
                      (((N/N)/(N/N))/((N/N)/(N/N))
                        ((((N/N)/(N/N))/((N/N)/(N/N)))/(((N/N)/(N/N))/((N/N)/(N/N))) Lone)
                        (((N/N)/(N/N))/((N/N)/(N/N)) Star))
                      ((N/N)/(N/N) Steel))
                    (N/N Co.))
                  (N unit)))
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      ((S[dcl]\NP)/NP sued)
                      (NP it))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (NP
                          (N
                            (N/N federal)
                            (N court)))
                        (NP\NP here))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (S[ng]\NP
                    ((S[ng]\NP)/(S[to]\NP) seeking)
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP recover)
                        (NP
                          (NP
                            (NP[nb]/N an)
                            (N
                              (N/N intercompany)
                              (N receivable)))
                          (NP\NP
                            (S[pss]\NP
                              ((S[pss]\NP)/PP valued)
                              (PP
                                (PP/NP at)
                                (NP
                                  (NP
                                    (NP[nb]/N a)
                                    (N minimum))
                                  (NP\NP
                                    ((NP\NP)/NP of)
                                    (NP
                                      (N
                                        (N/N[num] $)
                                        (N[num]
                                          (N/N 23)
                                          (N[num] million))))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N
                ((N/N)/(N/N)
                  (((N/N)/(N/N))/((N/N)/(N/N)) Lone)
                  ((N/N)/(N/N) Star))
                (N/N Technologies))
              (N Inc.)))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP
                (NP[nb]/N its)
                (N
                  (N/N
                    ((N/N)/(N/N)
                      (((N/N)/(N/N))/((N/N)/(N/N))
                        ((((N/N)/(N/N))/((N/N)/(N/N)))/(((N/N)/(N/N))/((N/N)/(N/N))) Lone)
                        (((N/N)/(N/N))/((N/N)/(N/N)) Star))
                      ((N/N)/(N/N) Steel))
                    (N/N Co.))
                  (N unit)))
              (S[dcl]\NP
                (S[dcl]\NP
                  (S[dcl]\NP
                    (S[dcl]\NP
                      ((S[dcl]\NP)/NP sued)
                      (NP it))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N
                          (N/N federal)
                          (N
                            (N court)
                            (N\N here))))))
                  (, ,))
                ((S\NP)\(S\NP)
                  (S[ng]\NP
                    ((S[ng]\NP)/(S[to]\NP) seeking)
                    (S[to]\NP
                      ((S[to]\NP)/(S[b]\NP) to)
                      (S[b]\NP
                        ((S[b]\NP)/NP recover)
                        (NP
                          (NP[nb]/N an)
                          (N
                            (N/N intercompany)
                            (N
                              (N receivable)
                              (N\N
                                (S[pss]\NP
                                  ((S[pss]\NP)/PP valued)
                                  (PP
                                    (PP/NP at)
                                    (NP
                                      (NP[nb]/N a)
                                      (N
                                        (N/PP minimum)
                                        (PP
                                          (PP/NP of)
                                          (NP
                                            (N
                                              (N/N[num] $)
                                              (N[num]
                                                (N/N 23)
                                                (N[num] million)))))))))))))))))))))
        (. .)))
    True
    """
    pass
    


##def wsj_0430_1():
##    """Broken CCGbank analysis where the is head
##    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0430.1')
##    ???
##    """
##    pass
    

##
##def wsj_0431_1():
##    """
##    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0431.1')
##    ???
##    """
##    pass


##def wsj_0299_9():
##    """Example where the CCGbank bracketing doesn't allow a span over the
##    nodes for a nombank argument, and rebracketing is possible
##    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_0299.9')
##    ???
##    """
##    pass

def wsj_1006_17():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_1006.17')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N
                (NP
                  (N Provigo))
                ((NP[nb]/N)\NP 's))
              (N
                (N/N profit)
                (N record)))
            (NP\NP
              ((NP\NP)/NP over)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N past)
                  (N
                    (N/N two)
                    (N years))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP tarnished)
            (NP
              (NP[nb]/N
                (NP[nb]/N
                  (NP
                    (NP[nb]/N the)
                    (N company))
                  ((NP[nb]/N)\NP 's))
                (NP[nb]/N[conj]
                  (conj and)
                  (NP[nb]/N
                    (NP
                      (N
                        (N/N Mr.)
                        (N Lortie)))
                    ((NP[nb]/N)\NP 's))))
              (N reputations))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP/(N/PP)
              (NP
                (N Provigo))
              ((NP/(N/PP))\NP 's))
            (N/PP
              (N/N profit)
              (N/PP
                (N/PP record)
                ((N/PP)\(N/PP)
                  (((N/PP)\(N/PP))/NP over)
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N past)
                      (N
                        (N/N two)
                        (N years))))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP tarnished)
            (NP
              (NP/(N/PP)
                (NP/(N/PP)
                  (NP
                    (NP[nb]/N the)
                    (N company))
                  ((NP/(N/PP))\NP 's))
                (NP/(N/PP)[conj]
                  (conj and)
                  (NP/(N/PP)
                    (NP
                      (N
                        (N/N Mr.)
                        (N Lortie)))
                    ((NP/(N/PP))\NP 's))))
              (N/PP reputations))))
        (. .)))
    True
    """
    pass

def wsj_1550_32():
    """
    >>> debug('data/CCGbank1.2_np_v0.7/', 'wsj_1550.32')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N bursts))
          (S[dcl]\NP
            ((S\NP)/(S\NP) often)
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP occur)
                ((S\NP)\(S\NP)
                  (, ,)
                  ((S\NP)\(S\NP)
                    (S[dcl]/S[dcl]
                      (S/(S\NP)
                        (NP they))
                      ((S[dcl]\NP)/S[dcl] said))
                    (, ,))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/S[dcl] after)
                (S[dcl]
                  (NP they)
                  (S[dcl]\NP
                    (S[dcl]\NP
                      ((S[dcl]\NP)/NP perturbed)
                      (NP
                        (NP[nb]/N the)
                        (N experiments)))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/(S[ng]\NP) by)
                      (S[ng]\NP
                        (S[ng]\NP
                          ((S[ng]\NP)/NP
                            ((S[ng]\NP)/NP raising)
                            ((S[ng]\NP)/NP[conj]
                              (conj or)
                              ((S[ng]\NP)/NP lowering)))
                          (NP
                            (NP
                              (NP
                                (NP[nb]/N the)
                                (N amount))
                              (NP\NP
                                ((NP\NP)/NP of)
                                (NP
                                  (N
                                    (N/N electric)
                                    (N current)))))
                            (NP\NP
                              (S[ng]\NP
                                ((S[ng]\NP)/(S[pss]\NP) being)
                                (S[pss]\NP applied)))))
                        (S[ng]\NP[conj]
                          (, ,)
                          (S[ng]\NP[conj]
                            (conj or)
                            (S[ng]\NP
                              (S[ng]\NP
                                ((S[ng]\NP)/NP switching)
                                (NP
                                  (NP[nb]/N the)
                                  (N current)))
                              ((S\NP)\(S\NP)
                                ((S\NP)\(S\NP) off)
                                ((S\NP)\(S\NP)[conj]
                                  (conj and)
                                  ((S\NP)\(S\NP) on))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N bursts))
          (S[dcl]\NP
            ((S\NP)/(S\NP) often)
            (S[dcl]\NP
              (S[dcl]\NP
                (S[dcl]\NP occur)
                ((S\NP)\(S\NP)
                  (, ,)
                  ((S\NP)\(S\NP)
                    (S[dcl]/S[dcl]
                      (S/(S\NP)
                        (NP they))
                      ((S[dcl]\NP)/S[dcl] said))
                    (, ,))))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/S[dcl] after)
                (S[dcl]
                  (NP they)
                  (S[dcl]\NP
                    (S[dcl]\NP
                      ((S[dcl]\NP)/NP perturbed)
                      (NP
                        (NP[nb]/N the)
                        (N experiments)))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/(S[ng]\NP) by)
                      (S[ng]\NP
                        (S[ng]\NP
                          ((S[ng]\NP)/NP
                            ((S[ng]\NP)/NP raising)
                            ((S[ng]\NP)/NP[conj]
                              (conj or)
                              ((S[ng]\NP)/NP lowering)))
                          (NP
                            (NP[nb]/N the)
                            (N
                              (N
                                (N/PP amount)
                                (PP
                                  (PP/NP of)
                                  (NP
                                    (N
                                      (N/N electric)
                                      (N current)))))
                              (N\N
                                (S[ng]\NP
                                  ((S[ng]\NP)/(S[pss]\NP) being)
                                  (S[pss]\NP applied))))))
                        (S[ng]\NP[conj]
                          (, ,)
                          (S[ng]\NP[conj]
                            (conj or)
                            (S[ng]\NP
                              ((S[ng]\NP)/PR
                                (((S[ng]\NP)/PR)/NP switching)
                                (NP
                                  (NP[nb]/N the)
                                  (N current)))
                              (PR
                                (PR off)
                                (PR[conj]
                                  (conj and)
                                  (PR on))))))))))))))
        (. .)))
    Invalid: N\N --> S[ng]\NP None
    False
    """
    pass

def wsj_0020_1():
    """
    >>> debug('data/CCGbank1.2_np_v0.7', 'wsj_0020.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N U.S.))
          (S[dcl]\NP
            (, ,)
            (S[dcl]\NP
              ((S\NP)/(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP claiming)
                  (NP
                    (NP
                      (NP[nb]/N some)
                      (N success))
                    (NP\NP
                      ((NP\NP)/NP in)
                      (NP
                        (NP[nb]/N its)
                        (N
                          (N/N trade)
                          (N diplomacy)))))))
              (S[dcl]\NP
                (, ,)
                (S[dcl]\NP
                  ((S[dcl]\NP)/PP
                    (((S[dcl]\NP)/PP)/NP removed)
                    (NP
                      (NP
                        (N
                          (N/N South)
                          (N Korea)))
                      (NP[conj]
                        (, ,)
                        (NP
                          (NP
                            (N Taiwan))
                          (NP[conj]
                            (conj and)
                            (NP
                              (N
                                (N/N Saudi)
                                (N Arabia))))))))
                  (PP
                    (PP/NP from)
                    (NP
                      (NP
                        (NP[nb]/N a)
                        (N list))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (NP
                            (N countries))
                          (NP\NP
                            (S[dcl]/NP
                              (S/(S\NP)
                                (NP it))
                              ((S[dcl]\NP)/NP
                                ((S[dcl]\NP)/(S[ng]\NP) is)
                                ((S[ng]\NP)/NP
                                  ((S\NP)/(S\NP) closely)
                                  ((S[ng]\NP)/NP
                                    (((S[ng]\NP)/PP)/NP watching)
                                    ((S\NP)\((S\NP)/PP)
                                      (PP
                                        (PP/(S[ng]\NP) for)
                                        (S[ng]\NP
                                          ((S\NP)/(S\NP) allegedly)
                                          (S[ng]\NP
                                            ((S[ng]\NP)/(S[to]\NP) failing)
                                            (S[to]\NP
                                              ((S[to]\NP)/(S[b]\NP) to)
                                              (S[b]\NP
                                                ((S[b]\NP)/NP honor)
                                                (NP
                                                  (N
                                                    (N/N U.S.)
                                                    (N
                                                      (N patents)
                                                      (N[conj]
                                                        (, ,)
                                                        (N
                                                          (N copyrights)
                                                          (N[conj]
                                                            (conj and)
                                                            (N
                                                              (N/N other)
                                                              (N
                                                                (N/N intellectual-property)
                                                                (N rights)))))))))))))))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N U.S.))
          (S[dcl]\NP
            (, ,)
            (S[dcl]\NP
              ((S\NP)/(S\NP)
                (S[ng]\NP
                  ((S[ng]\NP)/NP claiming)
                  (NP
                    (NP[nb]/N some)
                    (N
                      (N/PP success)
                      (PP
                        (PP/NP in)
                        (NP
                          (NP[nb]/N its)
                          (N
                            (N/N trade)
                            (N diplomacy))))))))
              (S[dcl]\NP
                (, ,)
                (S[dcl]\NP
                  ((S[dcl]\NP)/PP
                    (((S[dcl]\NP)/PP)/NP removed)
                    (NP
                      (N
                        (N
                          (N/N South)
                          (N Korea))
                        (N[conj]
                          (, ,)
                          (N
                            (N Taiwan)
                            (N[conj]
                              (conj and)
                              (N
                                (N/N Saudi)
                                (N Arabia))))))))
                  (PP
                    (PP/NP from)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/PP list)
                        (PP
                          (PP/NP of)
                          (NP
                            (N
                              (N countries)
                              (N\N
                                (S[dcl]/NP
                                  (S/(S\NP)
                                    (NP it))
                                  ((S[dcl]\NP)/NP
                                    ((S[dcl]\NP)/(S[ng]\NP) is)
                                    ((S[ng]\NP)/NP
                                      ((S\NP)/(S\NP) closely)
                                      ((S[ng]\NP)/NP
                                        ((S[ng]\NP)/NP watching)
                                        ((S\NP)\(S\NP)
                                          (((S\NP)\(S\NP))/(S[ng]\NP) for)
                                          (S[ng]\NP
                                            ((S\NP)/(S\NP) allegedly)
                                            (S[ng]\NP
                                              ((S[ng]\NP)/(S[to]\NP) failing)
                                              (S[to]\NP
                                                ((S[to]\NP)/(S[b]\NP) to)
                                                (S[b]\NP
                                                  ((S[b]\NP)/NP honor)
                                                  (NP
                                                    (N
                                                      (N/N U.S.)
                                                      (N
                                                        (N patents)
                                                        (N[conj]
                                                          (, ,)
                                                          (N
                                                            (N copyrights)
                                                            (N[conj]
                                                              (conj and)
                                                              (N
                                                                (N/N other)
                                                                (N
                                                                  (N/N intellectual-property)
                                                                  (N rights))))))))))))))))))))))))))))))
        (. .)))
    Invalid: N\N --> S[dcl]/NP None
    False
    """
    pass

    
if __name__ == '__main__':
    doctest.testmod()
