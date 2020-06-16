import doctest

import data
import flipArgumentStatus

def test_a_phrasal_verb():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0300.1')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N
                (N/N Battle-tested)
                (N
                  (N/N Japanese)
                  (N
                    (N/N industrial)
                    (N managers)))))
            (NP\NP here))
          (S[dcl]\NP
            ((S\NP)/(S\NP) always)
            (S[dcl]\NP
              ((S[dcl]\NP)/PP
                (((S[dcl]\NP)/PP)/NP
                  (((S[dcl]\NP)/PP)/NP buck)
                  ((S\NP)\(S\NP) up))
                (NP
                  (N
                    (N/N nervous)
                    (N newcomers))))
              (PP
                (PP/NP with)
                (NP
                  (NP
                    (NP[nb]/N the)
                    (N tale))
                  (NP\NP
                    ((NP\NP)/NP of)
                    (NP
                      (NP
                        (NP
                          (NP
                            (NP[nb]/N the)
                            (N first))
                          (NP\NP
                            ((NP\NP)/NP of)
                            (NP
                              (NP[nb]/N their)
                              (N countrymen))))
                        (NP\NP
                          (S[to]\NP
                            ((S[to]\NP)/(S[b]\NP) to)
                            (S[b]\NP
                              ((S[b]\NP)/NP visit)
                              (NP
                                (N Mexico))))))
                      (NP[conj]
                        (, ,)
                        (NP
                          (NP
                            (NP
                              (NP[nb]/N a)
                              (N boatload))
                            (NP\NP
                              ((NP\NP)/NP of)
                              (NP
                                (N
                                  (N/N samurai)
                                  (N warriors)))))
                          (NP\NP
                            (S[pss]\NP
                              (S[pss]\NP
                                ((S[pss]\NP)/(S[adj]\NP) blown)
                                (S[adj]\NP ashore))
                              ((S\NP)\(S\NP)
                                (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 375)
                                ((S\NP)\(S\NP)
                                  ((S\NP)\(S\NP) years)
                                  (((S\NP)\(S\NP))\((S\NP)\(S\NP)) ago))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Battle-tested)
              (N
                (N/N Japanese)
                (N
                  (N/N industrial)
                  (N
                    (N managers)
                    (N\N here))))))
          (S[dcl]\NP
            ((S\NP)/(S\NP) always)
            (S[dcl]\NP
              ((S[dcl]\NP)/PP
                (((S[dcl]\NP)/PP)/NP
                  ((((S[dcl]\NP)/PP)/NP)/PR buck)
                  (PR up))
                (NP
                  (N
                    (N/N nervous)
                    (N newcomers))))
              (PP
                (PP/NP with)
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/PP tale)
                    (PP
                      (PP/NP of)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N
                              (N first)
                              (N\N
                                ((N\N)/NP of)
                                (NP
                                  (NP[nb]/N their)
                                  (N countrymen))))
                            (N\N
                              (S[to]\NP
                                ((S[to]\NP)/(S[b]\NP) to)
                                (S[b]\NP
                                  ((S[b]\NP)/NP visit)
                                  (NP
                                    (N Mexico)))))))
                        (NP[conj]
                          (, ,)
                          (NP
                            (NP[nb]/N a)
                            (N
                              (N
                                (N/PP boatload)
                                (PP
                                  (PP/NP of)
                                  (NP
                                    (N
                                      (N/N samurai)
                                      (N warriors)))))
                              (N\N
                                (S[pss]\NP
                                  (S[pss]\NP
                                    ((S[pss]\NP)/(S[adj]\NP) blown)
                                    (S[adj]\NP ashore))
                                  ((S\NP)\(S\NP)
                                    (((S\NP)\(S\NP))/((S\NP)\(S\NP)) 375)
                                    ((S\NP)\(S\NP)
                                      ((S\NP)\(S\NP) years)
                                      (((S\NP)\(S\NP))\((S\NP)\(S\NP)) ago))))))))))))))))
        (. .)))
    True
    """
    pass

def test_b():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0300.2')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP From)
            (NP
              (NP[nb]/N the)
              (N beginning)))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP[expl] it)
              (S[dcl]\NP[expl]
                ((S[dcl]\NP[expl])/(S[to]\NP)
                  (((S[dcl]\NP[expl])/(S[to]\NP))/NP took)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N man))
                    (NP\NP
                      ((NP\NP)/NP with)
                      (NP
                        (N
                          (N/N extraordinary)
                          (N qualities))))))
                (S[to]\NP
                  ((S[to]\NP)/(S[b]\NP) to)
                  (S[b]\NP
                    (S[b]\NP succeed)
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N Mexico)))))))))
        (S[dcl]\S[dcl]
          (, ,)
          (S[dcl]\S[dcl]
            (S[dcl]\S[dcl]
              ((S[dcl]\S[dcl])/NP says)
              (NP
                (NP
                  (N
                    (N/N Kimihide)
                    (N Takimura)))
                (NP[conj]
                  (, ,)
                  (NP
                    (NP
                      (N president))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (NP[nb]/N
                          (NP
                            (N
                              (N/N Mitsui)
                              (N group)))
                          ((NP[nb]/N)\NP 's))
                        (N
                          (N/N
                            ((N/N)/(N/N)
                              (((N/N)/(N/N))/((N/N)/(N/N)) Kensetsu)
                              ((N/N)/(N/N) Engineering))
                            (N/N Inc.))
                          (N unit))))))))
            (. .)))))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP From)
            (NP
              (NP[nb]/N the)
              (N beginning)))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP[expl] it)
              (S[dcl]\NP[expl]
                ((S[dcl]\NP[expl])/(S[to]\NP)
                  (((S[dcl]\NP[expl])/(S[to]\NP))/NP took)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N man)
                      (N\N
                        ((N\N)/NP with)
                        (NP
                          (N
                            (N/N extraordinary)
                            (N qualities)))))))
                (S[to]\NP
                  ((S[to]\NP)/(S[b]\NP) to)
                  (S[b]\NP
                    (S[b]\NP succeed)
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP in)
                      (NP
                        (N Mexico)))))))))
        (S[dcl]\S[dcl]
          (, ,)
          (S[dcl]\S[dcl]
            (S[dcl]\S[dcl]
              ((S[dcl]\S[dcl])/NP says)
              (NP
                (NP
                  (N
                    (N/N Kimihide)
                    (N Takimura)))
                (NP[conj]
                  (, ,)
                  (NP
                    (N
                      (N/PP president)
                      (PP
                        (PP/NP of)
                        (NP
                          (NP[nb]/N
                            (NP
                              (N
                                (N/N Mitsui)
                                (N group)))
                            ((NP[nb]/N)\NP 's))
                          (N
                            (N/N
                              ((N/N)/(N/N)
                                (((N/N)/(N/N))/((N/N)/(N/N)) Kensetsu)
                                ((N/N)/(N/N) Engineering))
                              (N/N Inc.))
                            (N unit)))))))))
            (. .)))))
    True
    """
    pass

def test_c_passive_by():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.1')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            (S[pss]\NP
              (S[pss]\NP Shaken)
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/NP by)
                (NP
                  (NP
                    (N
                      (N/N tumbling)
                      (N
                        (N/N stock)
                        (N prices))))
                  (NP[conj]
                    (conj and)
                    (NP
                      (NP
                        (N
                          (N/N pessimistic)
                          (N projections)))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (N
                            (N/N U.S.)
                            (N
                              (N/N economic)
                              (N growth)))))))))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP
                  (N
                    (N/N currency)
                    (N analysts)))
                (NP\NP
                  ((NP\NP)/NP around)
                  (NP
                    (NP[nb]/N the)
                    (N world))))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) have)
                (S[pt]\NP
                  ((S[pt]\NP)/NP
                    ((S[pt]\NP)/NP toned)
                    ((S\NP)\(S\NP) down))
                  (NP
                    (NP
                      (NP[nb]/N their)
                      (N assessments))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (NP[nb]/N
                          (NP
                            (NP[nb]/N the)
                            (N dollar))
                          ((NP[nb]/N)\NP 's))
                        (N
                          (N/N near-term)
                          (N performance))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            (S[pss]\NP
              ((S[pss]\NP)/PP Shaken)
              (PP
                (PP/NP by)
                (NP
                  (NP
                    (N
                      (N/N tumbling)
                      (N
                        (N/N stock)
                        (N prices))))
                  (NP[conj]
                    (conj and)
                    (NP
                      (N
                        (N/N pessimistic)
                        (N
                          (N/PP projections)
                          (PP
                            (PP/NP of)
                            (NP
                              (N
                                (N/N U.S.)
                                (N
                                  (N/N economic)
                                  (N growth)))))))))))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (N
                  (N/N currency)
                  (N
                    (N analysts)
                    (N\N
                      ((N\N)/NP around)
                      (NP
                        (NP[nb]/N the)
                        (N world))))))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[pt]\NP) have)
                (S[pt]\NP
                  ((S[pt]\NP)/NP
                    (((S[pt]\NP)/NP)/PR toned)
                    (PR down))
                  (NP
                    (NP[nb]/N their)
                    (N
                      (N/PP assessments)
                      (PP
                        (PP/NP of)
                        (NP
                          (NP[nb]/N
                            (NP
                              (NP[nb]/N the)
                              (N dollar))
                            ((NP[nb]/N)\NP 's))
                          (N
                            (N/N near-term)
                            (N performance)))))))))))
        (. .)))
    True
    """
    pass

def test_d():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.2')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N Most))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N 10)
                    (N analysts)))
                (NP\NP
                  (S[pss]\NP
                    (S[pss]\NP
                      (S[pss]\NP polled)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/((S\NP)\(S\NP)) last)
                        ((S\NP)\(S\NP) week)))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP by)
                      (NP
                        (NP
                          (N
                            (N/N
                              ((N/N)/(N/N) Dow)
                              (N/N Jones))
                            (N
                              (N/N
                                ((N/N)/(N/N) International)
                                (N/N News))
                              (N Service))))
                        (NP\NP
                          ((NP\NP)/NP in)
                          (NP
                            (NP
                              (N Frankfurt))
                            (NP[conj]
                              (, ,)
                              (NP
                                (NP
                                  (N Tokyo))
                                (NP[conj]
                                  (, ,)
                                  (NP
                                    (NP
                                      (N London))
                                    (NP[conj]
                                      (conj and)
                                      (NP
                                        (N
                                          (N/N New)
                                          (N York)))))))))))))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[to]\NP)
              (((S[dcl]\NP)/(S[to]\NP))/NP expect)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N U.S.)
                  (N dollar))))
            (S[to]\NP
              ((S[to]\NP)/(S[b]\NP) to)
              (S[b]\NP
                (S[b]\NP
                  (S[b]\NP ease)
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/((S\NP)\(S\NP)) only)
                    ((S\NP)\(S\NP) mildly)))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP in)
                  (NP
                    (N November)))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP/PP Most)
            (PP
              (PP/NP of)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N 10)
                  (N
                    (N analysts)
                    (N\N
                      (S[pss]\NP
                        ((S[pss]\NP)/PP
                          ((S[pss]\NP)/PP polled)
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/((S\NP)\(S\NP)) last)
                            ((S\NP)\(S\NP) week)))
                        (PP
                          (PP/NP by)
                          (NP
                            (N
                              (N/N
                                ((N/N)/(N/N) Dow)
                                (N/N Jones))
                              (N
                                (N/N
                                  ((N/N)/(N/N) International)
                                  (N/N News))
                                (N
                                  (N Service)
                                  (N\N
                                    ((N\N)/NP in)
                                    (NP
                                      (N
                                        (N Frankfurt)
                                        (N[conj]
                                          (, ,)
                                          (N
                                            (N Tokyo)
                                            (N[conj]
                                              (, ,)
                                              (N
                                                (N London)
                                                (N[conj]
                                                  (conj and)
                                                  (N
                                                    (N/N New)
                                                    (N York))))))))))))))))))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[to]\NP)
              (((S[dcl]\NP)/(S[to]\NP))/NP expect)
              (NP
                (NP[nb]/N the)
                (N
                  (N/N U.S.)
                  (N dollar))))
            (S[to]\NP
              ((S[to]\NP)/(S[b]\NP) to)
              (S[b]\NP
                (S[b]\NP
                  (S[b]\NP ease)
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/((S\NP)\(S\NP)) only)
                    ((S\NP)\(S\NP) mildly)))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/NP in)
                  (NP
                    (N November)))))))
        (. .)))
    True
    """
    pass

def test_e():
    r"""The PP here looks weird, but Propbank has nothing to say about
    'is' predicates...
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.3')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N Opinion))
          (S[dcl]\NP
            ((S[dcl]\NP)/PP
              (((S[dcl]\NP)/PP)/(S[adj]\NP) is)
              (S[adj]\NP mixed))
            (PP
              (PP/NP over)
              (NP
                (NP[nb]/N its)
                (N
                  (N/N three-month)
                  (N prospects))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N Opinion))
          (S[dcl]\NP
            ((S[dcl]\NP)/PP
              (((S[dcl]\NP)/PP)/(S[adj]\NP) is)
              (S[adj]\NP mixed))
            (PP
              (PP/NP over)
              (NP
                (NP[nb]/N its)
                (N
                  (N/N three-month)
                  (N prospects))))))
        (. .)))
    True
    """
    pass

##def test_f():
##    r"""Noisy analysis hand-corrected
##    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0300.4')
##    (S
##      (S[dcl]
##        (S[dcl]
##          (S[dcl]
##            (NP
##              (N
##                (N/N Even)
##                (N after-hours)))
##            (S[dcl]\NP drag))
##          (S[dcl][conj]
##            (; ;)
##            (S[dcl]
##              (NP
##                (NP
##                  (NP
##                    (NP
##                      (N
##                        (N/N karaoke)
##                        (N bars)))
##                    (, ,))
##                  (NP\NP
##                    ((NP\NP)/S[dcl] where)
##                    (S[dcl]
##                      (NP
##                        (N
##                          (N/N Japanese)
##                          (N revelers)))
##                      (S[dcl]\NP
##                        ((S[dcl]\NP)/PP sing)
##                        (PP
##                          (PP/NP over)
##                          (NP
##                            (N
##                              (N/N recorded)
##                              (N music))))))))
##                (, ,))
##              (S[dcl]\NP
##                ((S[dcl]\NP)/(S[pss]\NP) are)
##                (S[pss]\NP
##                  (S[pss]\NP prohibited)
##                  ((S\NP)\(S\NP)
##                    (((S\NP)\(S\NP))/NP by)
##                    (NP
##                      (NP[nb]/N
##                        (NP
##                          (N Mexico))
##                        ((NP[nb]/N)\NP 's))
##                      (N
##                        (N/N powerful)
##                        (N
##                          (N/N musicians)
##                          (N union))))))))))
##        (. .)))
##    True
##    (S
##      (S[dcl]
##        (S[dcl]
##          (NP
##            (NP
##              (N
##                (N/N Even)
##                (N
##                  (N/N after-hours)
##                  (N drag)))
##            (NP[conj]
##              (; ;)
##              (NP
##                (NP
##                  (NP
##                    (NP
##                      (N
##                        (N/N karaoke)
##                        (N bars)))
##                    (, ,))
##                  (NP\NP
##                    ((NP\NP)/S[dcl] where)
##                    (S[dcl]
##                      (NP
##                        (N
##                          (N/N Japanese)
##                          (N revelers)))
##                      (S[dcl]\NP
##                        ((S[dcl]\NP)/PP sing)
##                        (PP
##                          (PP/NP over)
##                          (NP
##                            (N
##                              (N/N recorded)
##                              (N music))))))))
##                (, ,))
##          (S[dcl]\NP
##            ((S[dcl]\NP)/(S[pss]\NP) are)
##            (S[pss]\NP
##              ((S[pss]\NP)/PP prohibited)
##              (PP
##                (PP/NP by)
##                (NP
##                  (NP[nb]/N
##                    (NP
##                      (N Mexico))
##                    ((NP[nb]/N)\NP 's))
##                  (N
##                    (N/N powerful)
##                    (N
##                      (N/N musicians)
##                      (N union))))))))
##      (. .)))
##    True
##    """
##    pass

def test_h_Sadj_arg():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.4')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (N Half))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP those)
                (NP\NP
                  (S[pss]\NP polled)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[ng]\NP)
                  (((S[dcl]\NP)/(S[ng]\NP))/NP see)
                  (NP
                    (NP[nb]/N the)
                    (N currency)))
                (S[ng]\NP
                  (S[ng]\NP
                    ((S[ng]\NP)/(S[adj]\NP) trending)
                    (S[adj]\NP lower))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP over)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N next)
                        (N
                          (N/N three)
                          (N months)))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] while)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N others))
                (S[dcl]\NP
                  ((S[dcl]\NP)/NP forecast)
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N modest)
                        (N rebound)))
                    (NP\NP
                      ((NP\NP)/NP after)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N New)
                          (N Year))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP/PP Half)
            (PP
              (PP/NP of)
              (NP
                (NP those)
                (NP\NP
                  (S[pss]\NP polled)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[ng]\NP)
                  (((S[dcl]\NP)/(S[ng]\NP))/NP see)
                  (NP
                    (NP[nb]/N the)
                    (N currency)))
                (S[ng]\NP
                  (S[ng]\NP
                    ((S[ng]\NP)/(S[adj]\NP) trending)
                    (S[adj]\NP lower))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP over)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N next)
                        (N
                          (N/N three)
                          (N months)))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] while)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N others))
                (S[dcl]\NP
                  ((S[dcl]\NP)/NP forecast)
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N modest)
                      (N
                        (N rebound)
                        (N\N
                          ((N\N)/NP after)
                          (NP
                            (NP[nb]/N the)
                            (N
                              (N/N New)
                              (N Year))))))))))))
        (. .)))
    True
    """
    pass

def test_i():
    r"""Whacky stuff going on with the conjunction between an arg PP and
    adjunct PPs
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.5')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP In)
            (NP
              (N
                (N/N
                  ((N/N)/(N/N) late)
                  (N/N afternoon))
                (N
                  (N/N
                    ((N/N)/(N/N) New)
                    (N/N York))
                  (N trading)))))
          (S[dcl]
            (S/S yesterday)
            (S[dcl]
              (, ,)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N dollar))
                (S[dcl]\NP
                  ((S[dcl]\NP)/PP stood)
                  ((S\NP)\((S\NP)/PP)
                    ((S\NP)\((S\NP)/PP)
                      ((S\NP)\((S\NP)/PP)
                        (PP
                          (PP/NP at)
                          (NP
                            (N
                              (N/N 1.8415)
                              (N
                                (N/N
                                  ((N/N)/(N/N) West)
                                  (N/N German))
                                (N
                                  (N marks)
                                  (, ,)))))))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/PP up)
                        (PP
                          (PP
                            (PP/NP from)
                            (NP
                              (N
                                (N/N 1.8340)
                                (N marks))))
                          (PP\PP
                            ((PP\PP)/(PP\PP) late)
                            (PP\PP Monday)))))
                    ((S\NP)\((S\NP)/PP)[conj]
                      (, ,)
                      ((S\NP)\((S\NP)/PP)[conj]
                        (conj and)
                        ((S\NP)\((S\NP)/PP)
                          ((S\NP)\((S\NP)/PP)
                            (PP
                              (PP/NP at)
                              (NP
                                (N
                                  (N
                                    (N/N 142.85)
                                    (N yen))
                                  (, ,)))))
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/PP up)
                            (PP
                              (PP
                                (PP/NP from)
                                (NP
                                  (N
                                    (N/N 141.90)
                                    (N yen))))
                              (PP\PP
                                ((PP\PP)/(PP\PP) late)
                                (PP\PP Monday)))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP In)
            (NP
              (N
                (N/N
                  ((N/N)/(N/N) late)
                  (N/N afternoon))
                (N
                  (N/N
                    ((N/N)/(N/N) New)
                    (N/N York))
                  (N trading)))))
          (S[dcl]
            (S/S yesterday)
            (S[dcl]
              (, ,)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N dollar))
                (S[dcl]\NP
                  ((S[dcl]\NP)/PP stood)
                  ((S\NP)\((S\NP)/PP)
                    ((S\NP)\((S\NP)/PP)
                      ((S\NP)\((S\NP)/PP)
                        (PP
                          (PP/NP at)
                          (NP
                            (N
                              (N/N 1.8415)
                              (N
                                (N/N
                                  ((N/N)/(N/N) West)
                                  (N/N German))
                                (N
                                  (N marks)
                                  (, ,)))))))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/PP up)
                        (PP
                          (PP
                            (PP/NP from)
                            (NP
                              (N
                                (N/N 1.8340)
                                (N marks))))
                          (PP\PP
                            ((PP\PP)/(PP\PP) late)
                            (PP\PP Monday)))))
                    ((S\NP)\((S\NP)/PP)[conj]
                      (, ,)
                      ((S\NP)\((S\NP)/PP)[conj]
                        (conj and)
                        ((S\NP)\((S\NP)/PP)
                          ((S\NP)\((S\NP)/PP)
                            (PP
                              (PP/NP at)
                              (NP
                                (N
                                  (N
                                    (N/N 142.85)
                                    (N yen))
                                  (, ,)))))
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/PP up)
                            (PP
                              (PP
                                (PP/NP from)
                                (NP
                                  (N
                                    (N/N 141.90)
                                    (N yen))))
                              (PP\PP
                                ((PP\PP)/(PP\PP) late)
                                (PP\PP Monday)))))))))))))
        (. .)))
    True
    """
    pass

def test_j():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.6')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/N A)
            (N
              (N month)
              (N\N ago)))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N a)
                (N
                  (N/N similar)
                  (N survey)))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[dcl] predicted)
                (S[dcl]
                  (NP
                    (NP[nb]/N the)
                    (N dollar))
                  (S[dcl]\NP
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[b]\NP) would)
                      (S[b]\NP
                        ((S[b]\NP)/(S[ng]\NP) be)
                        (S[ng]\NP
                          ((S[ng]\NP)/PP trading)
                          (PP
                            (PP/NP at)
                            (NP
                              (NP
                                (N
                                  (N/N 1.8690)
                                  (N marks)))
                              (NP[conj]
                                (conj and)
                                (NP
                                  (N
                                    (N/N 139.75)
                                    (N yen)))))))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP by)
                      (NP
                        (NP
                          (NP[nb]/N the)
                          (N end))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (N October)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/N A)
            (N
              (N month)
              (N\N ago)))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N a)
                (N
                  (N/N similar)
                  (N survey)))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[dcl] predicted)
                (S[dcl]
                  (NP
                    (NP[nb]/N the)
                    (N dollar))
                  (S[dcl]\NP
                    (S[dcl]\NP
                      ((S\NP)/(S\NP) would)
                      (S[dcl]\NP
                        ((S[dcl]\NP)/(S[ng]\NP) be)
                        (S[ng]\NP
                          ((S[ng]\NP)/PP trading)
                          (PP
                            (PP/NP at)
                            (NP
                              (N
                                (N
                                  (N/N 1.8690)
                                  (N marks))
                                (N[conj]
                                  (conj and)
                                  (N
                                    (N/N 139.75)
                                    (N yen)))))))))
                    ((S\NP)\(S\NP)
                      (((S\NP)\(S\NP))/NP by)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/PP end)
                          (PP
                            (PP/NP of)
                            (NP
                              (N October))))))))))))
        (. .)))
    True
    """
    pass

def test_k():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.7')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N Sterling))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[ng]\NP) was)
            (S[ng]\NP
              (S[ng]\NP
                (S[ng]\NP
                  ((S[ng]\NP)/PP trading)
                  (PP
                    (PP/NP at)
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num] 1.5805)))))
                (, ,))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/PP down)
                (PP
                  (PP
                    (PP/NP from)
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num] 1.5820))))
                  (PP\PP
                    ((PP\PP)/(PP\PP) late)
                    (PP\PP Monday)))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N Sterling))
          (S[dcl]\NP
            ((S[dcl]\NP)/(S[ng]\NP) was)
            (S[ng]\NP
              (S[ng]\NP
                (S[ng]\NP
                  ((S[ng]\NP)/PP trading)
                  (PP
                    (PP/NP at)
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num] 1.5805)))))
                (, ,))
              ((S\NP)\(S\NP)
                (((S\NP)\(S\NP))/PP down)
                (PP
                  (PP
                    (PP/NP from)
                    (NP
                      (N
                        (N/N[num] $)
                        (N[num] 1.5820))))
                  (PP\PP
                    ((PP\PP)/(PP\PP) late)
                    (PP\PP Monday)))))))
        (. .)))
    True
    """
    pass

def test_l():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.8')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP In)
            (NP
              (N Tokyo)))
          (S[dcl]
            (S/S Wednesday)
            (S[dcl]
              (, ,)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N U.S.)
                    (N currency)))
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[ng]\NP) was)
                  (S[ng]\NP
                    (S[ng]\NP
                      (S[ng]\NP
                        (S[ng]\NP
                          ((S[ng]\NP)/PP trading)
                          (PP
                            (PP/NP at)
                            (NP
                              (N
                                (N/N
                                  ((N/N)/(N/N) about)
                                  (N/N 142.95))
                                (N yen)))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP at)
                          (NP
                            (N midmorning))))
                      (, ,))
                    ((S\NP)\(S\NP)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/PP up)
                        (PP
                          (PP
                            (PP/NP from)
                            (NP
                              (N
                                (N/N 142.80)
                                (N yen))))
                          (PP\PP
                            ((PP\PP)/NP at)
                            (NP
                              (NP[nb]/N the)
                              (N opening)))))
                      ((S\NP)\(S\NP)[conj]
                        (conj and)
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/PP up)
                          (PP
                            (PP/NP from)
                            (NP
                              (NP
                                (NP[nb]/N
                                  (NP
                                    (N Tuesday))
                                  ((NP[nb]/N)\NP 's))
                                (N
                                  (N/N Tokyo)
                                  (N close)))
                              (NP\NP
                                ((NP\NP)/NP of)
                                (NP
                                  (N
                                    (N/N 142.15)
                                    (N yen)))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP In)
            (NP
              (N Tokyo)))
          (S[dcl]
            (S/S Wednesday)
            (S[dcl]
              (, ,)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N U.S.)
                    (N currency)))
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[ng]\NP) was)
                  (S[ng]\NP
                    (S[ng]\NP
                      (S[ng]\NP
                        (S[ng]\NP
                          ((S[ng]\NP)/PP trading)
                          (PP
                            (PP/NP at)
                            (NP
                              (N
                                (N/N
                                  ((N/N)/(N/N) about)
                                  (N/N 142.95))
                                (N yen)))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP at)
                          (NP
                            (N midmorning))))
                      (, ,))
                    ((S\NP)\(S\NP)
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/PP up)
                        (PP
                          (PP
                            (PP/NP from)
                            (NP
                              (N
                                (N/N 142.80)
                                (N yen))))
                          (PP\PP
                            ((PP\PP)/NP at)
                            (NP
                              (NP[nb]/N the)
                              (N opening)))))
                      ((S\NP)\(S\NP)[conj]
                        (conj and)
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/PP up)
                          (PP
                            (PP/NP from)
                            (NP
                              (NP[nb]/N
                                (NP
                                  (N Tuesday))
                                ((NP[nb]/N)\NP 's))
                              (N
                                (N/N Tokyo)
                                (N
                                  (N/PP close)
                                  (PP
                                    (PP/NP of)
                                    (NP
                                      (N
                                        (N/N 142.15)
                                        (N yen)))))))))))))))))
        (. .)))
    True
    """
    pass

def test_m():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.9')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N The)
              (N average))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP
                  (N estimates))
                (NP\NP
                  ((NP\NP)/NP of)
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N 10)
                        (N economists)))
                    (NP\NP
                      (S[pss]\NP polled)))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/PP
              (((S[dcl]\NP)/PP)/NP puts)
              (NP
                (NP[nb]/N the)
                (N dollar)))
            (PP
              (PP
                (PP
                  (PP/NP around)
                  (NP
                    (N
                      (N/N 1.8200)
                      (N marks))))
                (PP\PP
                  ((PP\PP)/NP at)
                  (NP
                    (NP
                      (NP[nb]/N the)
                      (N end))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N November))))))
              (PP[conj]
                (conj and)
                (PP
                  (PP/NP at)
                  (NP
                    (N
                      (N/N 141.33)
                      (N yen))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N
              (N/PP average)
              (PP
                (PP/NP of)
                (NP
                  (N
                    (N/PP estimates)
                    (PP
                      (PP/NP of)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N 10)
                          (N
                            (N economists)
                            (N\N
                              (S[pss]\NP polled)))))))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/PP
              (((S[dcl]\NP)/PP)/NP puts)
              (NP
                (NP[nb]/N the)
                (N dollar)))
            (PP
              (PP
                (PP
                  (PP/NP around)
                  (NP
                    (N
                      (N/N 1.8200)
                      (N marks))))
                (PP\PP
                  ((PP\PP)/NP at)
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/PP end)
                      (PP
                        (PP/NP of)
                        (NP
                          (N November)))))))
              (PP[conj]
                (conj and)
                (PP
                  (PP/NP at)
                  (NP
                    (N
                      (N/N 141.33)
                      (N yen))))))))
        (. .)))
    True
    """
    pass

def test_n():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.10')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP By)
            (NP
              (N
                (N/N late)
                (N January))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N consensus))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[for] calls)
                (S[for]
                  (S[for]/(S[to]\NP)
                    ((S[for]/(S[to]\NP))/NP for)
                    (NP
                      (NP[nb]/N the)
                      (N dollar)))
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/(S[ng]\NP) be)
                      (S[ng]\NP
                        ((S[ng]\NP)/PP trading)
                        (PP
                          (PP
                            (PP/NP around)
                            (NP
                              (N
                                (N/N 1.8200)
                                (N marks))))
                          (PP[conj]
                            (conj and)
                            (PP
                              (PP/NP near)
                              (NP
                                (N
                                  (N/N 142)
                                  (N yen))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            ((S/S)/NP By)
            (NP
              (N
                (N/N late)
                (N January))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N consensus))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[for] calls)
                (S[for]
                  (S[for]/(S[to]\NP)
                    ((S[for]/(S[to]\NP))/NP for)
                    (NP
                      (NP[nb]/N the)
                      (N dollar)))
                  (S[to]\NP
                    ((S[to]\NP)/(S[b]\NP) to)
                    (S[b]\NP
                      ((S[b]\NP)/(S[ng]\NP) be)
                      (S[ng]\NP
                        ((S[ng]\NP)/PP trading)
                        (PP
                          (PP
                            (PP/NP around)
                            (NP
                              (N
                                (N/N 1.8200)
                                (N marks))))
                          (PP[conj]
                            (conj and)
                            (PP
                              (PP/NP near)
                              (NP
                                (N
                                  (N/N 142)
                                  (N yen))))))))))))))
        (. .)))
    True
    """
    pass

def test_o():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.11')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP Those)
            (NP\NP
              ((NP\NP)/NP with)
              (NP
                (NP[nb]/N a)
                (N
                  (N/N bullish)
                  (N view)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[ng]\NP)
                  (((S[dcl]\NP)/(S[ng]\NP))/NP see)
                  (NP
                    (NP[nb]/N the)
                    (N dollar)))
                (S[ng]\NP
                  ((S[ng]\NP)/(S[adj]\NP) trading)
                  (S[adj]\NP
                    ((S[adj]\NP)/PP up)
                    (PP
                      (PP/NP near)
                      (NP
                        (NP
                          (N
                            (N/N 1.9000)
                            (N marks)))
                        (NP[conj]
                          (conj and)
                          (NP
                            (N
                              (N/N 145)
                              (N yen)))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] while)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N dollar)
                    (N bears)))
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[ng]\NP)
                    (((S[dcl]\NP)/(S[ng]\NP))/NP see)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N U.S.)
                        (N currency))))
                  (S[ng]\NP
                    ((S[ng]\NP)/PP trading)
                    (PP
                      (PP/NP around)
                      (NP
                        (NP
                          (N
                            (N/N 1.7600)
                            (N marks)))
                        (NP[conj]
                          (conj and)
                          (NP
                            (N
                              (N/N 138)
                              (N yen))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP Those)
            (NP\NP
              ((NP\NP)/NP with)
              (NP
                (NP[nb]/N a)
                (N
                  (N/N bullish)
                  (N view)))))
          (S[dcl]\NP
            (S[dcl]\NP
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[ng]\NP)
                  (((S[dcl]\NP)/(S[ng]\NP))/NP see)
                  (NP
                    (NP[nb]/N the)
                    (N dollar)))
                (S[ng]\NP
                  ((S[ng]\NP)/(S[adj]\NP) trading)
                  (S[adj]\NP
                    ((S[adj]\NP)/PP up)
                    (PP
                      (PP/NP near)
                      (NP
                        (N
                          (N
                            (N/N 1.9000)
                            (N marks))
                          (N[conj]
                            (conj and)
                            (N
                              (N/N 145)
                              (N yen)))))))))
              (, ,))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/S[dcl] while)
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N dollar)
                    (N bears)))
                (S[dcl]\NP
                  ((S[dcl]\NP)/(S[ng]\NP)
                    (((S[dcl]\NP)/(S[ng]\NP))/NP see)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N U.S.)
                        (N currency))))
                  (S[ng]\NP
                    ((S[ng]\NP)/PP trading)
                    (PP
                      (PP/NP around)
                      (NP
                        (N
                          (N
                            (N/N 1.7600)
                            (N marks))
                          (N[conj]
                            (conj and)
                            (N
                              (N/N 138)
                              (N yen))))))))))))
        (. .)))
    True
    """
    pass

def test_p():
    r"""Would really like to see 'a number' analysed as PG
    Note the interesting number agreement!
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.12')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP[nb]/N A)
              (N number))
            (NP\NP
              ((NP\NP)/NP of)
              (NP
                (NP those)
                (NP\NP
                  (S[pss]\NP polled)))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] predict)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N dollar))
              (S[dcl]\NP
                ((S[dcl]\NP)/(S[b]\NP) will)
                (S[b]\NP
                  (S[b]\NP slip)
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/S[dcl] as)
                    (S[dcl]
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N Federal)
                          (N Reserve)))
                      (S[dcl]\NP
                        ((S[dcl]\NP)/NP eases)
                        (NP
                          (N
                            (N/N interest)
                            (N rates)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N A)
            (N
              (N/PP number)
              (PP
                (PP/NP of)
                (NP
                  (NP those)
                  (NP\NP
                    (S[pss]\NP polled))))))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] predict)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N dollar))
              (S[dcl]\NP
                ((S\NP)/(S\NP) will)
                (S[dcl]\NP
                  (S[dcl]\NP slip)
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/S[dcl] as)
                    (S[dcl]
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N Federal)
                          (N Reserve)))
                      (S[dcl]\NP
                        ((S[dcl]\NP)/NP eases)
                        (NP
                          (N
                            (N/N interest)
                            (N rates)))))))))))
        (. .)))
    True
    """
    pass

def test_q_unary_rule():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.13')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N David)
                  (N Owen)))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP[nb]/N an)
                    (N economist))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP
                        (N
                          (N/N
                            ((N/N)/(N/N) Kleinwort)
                            (N/N Benson))
                          (N
                            (N/N &)
                            (N Co.))))
                      (NP\NP
                        ((NP\NP)/NP in)
                        (NP
                          (N London))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP he)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP expects)
                (NP
                  (NP
                    (NP
                      (N
                        (N/N further)
                        (N cuts)))
                    (NP\NP
                      ((NP\NP)/NP in)
                      (NP
                        (N
                          (N/N short-term)
                          (N
                            (N/N U.S.)
                            (N rates))))))
                  (NP\NP
                    ((NP\NP)/NP in)
                    (NP
                      (NP[nb]/N an)
                      (N
                        (N effort)
                        (N\N
                          (S[to]\NP
                            (S[to]\NP
                              ((S[to]\NP)/(S[b]\NP) to)
                              (S[b]\NP
                                ((S[b]\NP)/NP encourage)
                                (NP
                                  (NP
                                    (NP[nb]/N a)
                                    (N narrowing))
                                  (NP\NP
                                    ((NP\NP)/NP of)
                                    (NP
                                      (NP[nb]/N the)
                                      (N
                                        (N/N trade)
                                        (N gap)))))))
                            (S[to]\NP[conj]
                              (conj and)
                              (S[to]\NP
                                ((S[to]\NP)/(S[b]\NP) to)
                                (S[b]\NP
                                  ((S[b]\NP)/NP ensure)
                                  (NP
                                    (NP
                                      (NP[nb]/N a)
                                      (N
                                        (N/N soft)
                                        (N landing)))
                                    (NP\NP
                                      ((NP\NP)/NP in)
                                      (NP
                                        (NP[nb]/N the)
                                        (N
                                          (N/N U.S.)
                                          (N economy))))))))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N David)
                  (N Owen)))
              (NP[conj]
                (, ,)
                (NP
                  (NP[nb]/N an)
                  (N
                    (N/PP economist)
                    (PP
                      (PP/NP at)
                      (NP
                        (N
                          (N/N
                            ((N/N)/(N/N) Kleinwort)
                            (N/N Benson))
                          (N
                            (N/N &)
                            (N
                              (N Co.)
                              (N\N
                                ((N\N)/NP in)
                                (NP
                                  (N London))))))))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/S[dcl] said)
            (S[dcl]
              (NP he)
              (S[dcl]\NP
                ((S[dcl]\NP)/NP expects)
                (NP
                  (N
                    (N/N further)
                    (N
                      (N
                        (N/PP cuts)
                        (PP
                          (PP/NP in)
                          (NP
                            (N
                              (N/N short-term)
                              (N
                                (N/N U.S.)
                                (N rates))))))
                      (N\N
                        ((N\N)/NP in)
                        (NP
                          (NP[nb]/N an)
                          (N
                            (N/(S[to]\NP) effort)
                            (S[to]\NP
                              (S[to]\NP
                                ((S[to]\NP)/(S[b]\NP) to)
                                (S[b]\NP
                                  ((S[b]\NP)/NP encourage)
                                  (NP
                                    (NP[nb]/N a)
                                    (N
                                      (N/PP narrowing)
                                      (PP
                                        (PP/NP of)
                                        (NP
                                          (NP[nb]/N the)
                                          (N
                                            (N/N trade)
                                            (N gap))))))))
                              (S[to]\NP[conj]
                                (conj and)
                                (S[to]\NP
                                  ((S[to]\NP)/(S[b]\NP) to)
                                  (S[b]\NP
                                    ((S[b]\NP)/NP ensure)
                                    (NP
                                      (NP[nb]/N a)
                                      (N
                                        (N/N soft)
                                        (N
                                          (N landing)
                                          (N\N
                                            ((N\N)/NP in)
                                            (NP
                                              (NP[nb]/N the)
                                              (N
                                                (N/N U.S.)
                                                (N economy)))))))))))))))))))))
        (. .)))
    True
    """
    pass

def test_r():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.14')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (N
                  (N/N Robert)
                  (N White)))
              (NP[conj]
                (, ,)
                (NP
                  (NP
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N
                          (N/N vice)
                          (N president))
                        (N[conj]
                          (conj and)
                          (N manager))))
                    (NP\NP
                      ((NP\NP)/NP of)
                      (NP
                        (N
                          (N/N corporate)
                          (N trade)))))
                  (NP\NP
                    ((NP\NP)/NP at)
                    (NP
                      (NP
                        (N
                          (N/N First)
                          (N Interstate)))
                      (NP\NP
                        ((NP\NP)/NP of)
                        (NP
                          (N California))))))))
            (, ,))
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/PP agreed)
              (PP
                (PP/NP with)
                (NP
                  (NP[nb]/N that)
                  (N view))))
            (S[dcl]\NP[conj]
              (conj and)
              (S[dcl]\NP
                ((S[dcl]\NP)/S[dcl] predicted)
                (S[dcl]
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N U.S.)
                      (N
                        (N/N federal)
                        (N
                          (N/N funds)
                          (N rate)))))
                  (S[dcl]\NP
                    ((S[dcl]\NP)/(S[b]\NP) will)
                    (S[b]\NP
                      (S[b]\NP
                        (S[b]\NP
                          (S[b]\NP drop)
                          ((S\NP)\(S\NP)
                            (((S\NP)\(S\NP))/NP to)
                            (NP
                              (N
                                (N/N between)
                                (N
                                  (N
                                    (N/N 7)
                                    (N
                                      (N/N 3\/4)
                                      (N %)))
                                  (N[conj]
                                    (conj and)
                                    (N
                                      (N/N 8)
                                      (N %))))))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP within)
                          (NP
                            (N
                              (N/N 60)
                              (N days)))))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP from)
                        (NP
                          (NP
                            (NP[nb]/N its)
                            (N
                              (N/N current)
                              (N level)))
                          (NP\NP
                            ((NP\NP)/NP at)
                            (NP
                              (N
                                (N/N
                                  (N/N 8)
                                  ((N/N)\(N/N) 13\/16))
                                (N %)))))))))))))
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
                  (N White)))
              (NP[conj]
                (, ,)
                (NP
                  (NP[nb]/N a)
                  (N
                    (N/PP
                      ((N/PP)/PP
                        ((N/PP)/PP
                          (N/N vice)
                          ((N/PP)/PP president))
                        ((N/PP)/PP[conj]
                          (conj and)
                          ((N/PP)/PP manager)))
                      (PP
                        (PP/NP of)
                        (NP
                          (N
                            (N/N corporate)
                            (N trade)))))
                    (PP
                      (PP/NP at)
                      (NP
                        (N
                          (N/N First)
                          (N
                            (N Interstate)
                            (N\N
                              ((N\N)/NP of)
                              (NP
                                (N California)))))))))))
            (, ,))
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/PP agreed)
              (PP
                (PP/NP with)
                (NP
                  (NP[nb]/N that)
                  (N view))))
            (S[dcl]\NP[conj]
              (conj and)
              (S[dcl]\NP
                ((S[dcl]\NP)/S[dcl] predicted)
                (S[dcl]
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N U.S.)
                      (N
                        (N/N federal)
                        (N
                          (N/N funds)
                          (N rate)))))
                  (S[dcl]\NP
                    ((S\NP)/(S\NP) will)
                    (S[dcl]\NP
                      ((S[dcl]\NP)/PP
                        ((S[dcl]\NP)/PP
                          (((S[dcl]\NP)/PP)/PP drop)
                          (PP
                            (PP/NP to)
                            (NP
                              (N
                                (N/N between)
                                (N
                                  (N
                                    (N/N 7)
                                    (N
                                      (N/N 3\/4)
                                      (N %)))
                                  (N[conj]
                                    (conj and)
                                    (N
                                      (N/N 8)
                                      (N %))))))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP within)
                          (NP
                            (N
                              (N/N 60)
                              (N days)))))
                      (PP
                        (PP/NP from)
                        (NP
                          (NP[nb]/N its)
                          (N
                            (N/N current)
                            (N
                              (N/PP level)
                              (PP
                                (PP/NP at)
                                (NP
                                  (N
                                    (N/N
                                      (N/N 8)
                                      ((N/N)\(N/N) 13\/16))
                                    (N %)))))))))))))))
        (. .)))
    True
    """
    pass

def test_s():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.15')
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (N
                (N/N Fed)
                (N funds)))
            (S[dcl]\NP
              ((S[dcl]\NP)/NP is)
              (NP
                (NP
                  (NP[nb]/N the)
                  (N rate))
                (NP\NP
                  (S[dcl]/NP
                    (S/(S\NP)
                      (NP
                        (N banks)))
                    ((S[dcl]\NP)/NP
                      ((S[dcl]\NP)/NP
                        (((S[dcl]\NP)/NP)/NP charge)
                        (NP
                          (NP[nb]/N each)
                          (N other)))
                      ((S\NP)\(S\NP)
                        (((S\NP)\(S\NP))/NP on)
                        (NP
                          (N
                            (N/N overnight)
                            (N loans))))))))))
          (S[dcl][conj]
            (; ;)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N Fed))
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/NP influences)
                  (NP
                    (NP[nb]/N the)
                    (N rate)))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/(S[ng]\NP) by)
                  (S[ng]\NP
                    ((S[ng]\NP)/PP
                      (((S[ng]\NP)/PP)/NP
                        (((S[ng]\NP)/PP)/NP adding)
                        (((S[ng]\NP)/PP)/NP[conj]
                          (conj or)
                          (((S[ng]\NP)/PP)/NP draining)))
                      (NP
                        (N reserves)))
                    (PP
                      (PP/NP from)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N banking)
                          (N system))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S[dcl]
            (NP
              (N
                (N/N Fed)
                (N funds)))
            (S[dcl]\NP
              ((S[dcl]\NP)/NP is)
              (NP
                (NP[nb]/N the)
                (N
                  (N rate)
                  (N\N
                    (S[dcl]/NP
                      (S/(S\NP)
                        (NP
                          (N banks)))
                      ((S[dcl]\NP)/NP
                        (((S[dcl]\NP)/NP)/PP
                          ((((S[dcl]\NP)/NP)/PP)/NP charge)
                          (NP
                            (NP[nb]/N each)
                            (N other)))
                        (PP
                          (PP/NP on)
                          (NP
                            (N
                              (N/N overnight)
                              (N loans)))))))))))
          (S[dcl][conj]
            (; ;)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N Fed))
              (S[dcl]\NP
                (S[dcl]\NP
                  ((S[dcl]\NP)/NP influences)
                  (NP
                    (NP[nb]/N the)
                    (N rate)))
                ((S\NP)\(S\NP)
                  (((S\NP)\(S\NP))/(S[ng]\NP) by)
                  (S[ng]\NP
                    ((S[ng]\NP)/PP
                      (((S[ng]\NP)/PP)/NP
                        (((S[ng]\NP)/PP)/NP adding)
                        (((S[ng]\NP)/PP)/NP[conj]
                          (conj or)
                          (((S[ng]\NP)/PP)/NP draining)))
                      (NP
                        (N reserves)))
                    (PP
                      (PP/NP from)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N banking)
                          (N system))))))))))
        (. .)))
    Invalid: N\N --> S[dcl]/NP None
    False
    """
    pass

def test_t():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.16')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Mr.)
              (N White)))
          (S[dcl]\NP
            ((S\NP)/(S\NP) also)
            (S[dcl]\NP
              ((S[dcl]\NP)/NP predicted)
              (NP
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N half-point)
                      (N cut)))
                  (NP\NP
                    ((NP\NP)/NP in)
                    (NP
                      (NP[nb]/N the)
                      (N
                        (N/N U.S.)
                        (N
                          (N/N discount)
                          (N rate))))))
                (NP\NP
                  ((NP\NP)/NP in)
                  (NP
                    (NP[nb]/N the)
                    (N
                      (N/N near)
                      (N future))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (N
              (N/N Mr.)
              (N White)))
          (S[dcl]\NP
            ((S\NP)/(S\NP) also)
            (S[dcl]\NP
              ((S[dcl]\NP)/NP predicted)
              (NP
                (NP[nb]/N a)
                (N
                  (N/N half-point)
                  (N
                    (N
                      (N/PP cut)
                      (PP
                        (PP/NP in)
                        (NP
                          (NP[nb]/N the)
                          (N
                            (N/N U.S.)
                            (N
                              (N/N discount)
                              (N rate))))))
                    (N\N
                      ((N\N)/NP in)
                      (NP
                        (NP[nb]/N the)
                        (N
                          (N/N near)
                          (N future))))))))))
        (. .)))
    True
    """
    pass

def test_u():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.17')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP[nb]/N The)
                (N
                  (N/N discount)
                  (N rate)))
              (NP[conj]
                (, ,)
                (NP
                  (N
                    (N/N currently)
                    (N
                      (N/N 7)
                      (N %))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP is)
            (NP
              (NP
                (NP[nb]/N the)
                (N rate))
              (NP\NP
                (S[dcl]/NP
                  (S/(S\NP)
                    (NP
                      (NP[nb]/N the)
                      (N Fed)))
                  ((S[dcl]\NP)/NP
                    ((S[dcl]\NP)/NP
                      ((S[dcl]\NP)/NP
                        ((S[dcl]\NP)/NP
                          (((S[dcl]\NP)/NP)/NP charges)
                          (NP
                            (N
                              (N/N member)
                              (N banks))))
                        ((S\NP)\(S\NP)
                          (((S\NP)\(S\NP))/NP for)
                          (NP
                            (N loans))))
                      (, ,))
                    ((S\NP)\(S\NP)
                      (S[ng]\NP
                        ((S[ng]\NP)/PP
                          (((S[ng]\NP)/PP)/NP using)
                          (NP
                            (N
                              (N/N government)
                              (N securities))))
                        (PP
                          (PP/NP as)
                          (NP
                            (N collateral)))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP
              (NP
                (NP[nb]/N The)
                (N
                  (N/N discount)
                  (N rate)))
              (NP[conj]
                (, ,)
                (NP
                  (N
                    (N/N currently)
                    (N
                      (N/N 7)
                      (N %))))))
            (, ,))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP is)
            (NP
              (NP[nb]/N the)
              (N
                (N rate)
                (N\N
                  (S[dcl]/NP
                    (S/(S\NP)
                      (NP
                        (NP[nb]/N the)
                        (N Fed)))
                    ((S[dcl]\NP)/NP
                      ((S[dcl]\NP)/NP
                        ((S[dcl]\NP)/NP
                          (((S[dcl]\NP)/NP)/PP
                            ((((S[dcl]\NP)/NP)/PP)/NP charges)
                            (NP
                              (N
                                (N/N member)
                                (N banks))))
                          (PP
                            (PP/NP for)
                            (NP
                              (N loans))))
                        (, ,))
                      ((S\NP)\(S\NP)
                        (S[ng]\NP
                          ((S[ng]\NP)/PP
                            (((S[ng]\NP)/PP)/NP using)
                            (NP
                              (N
                                (N/N government)
                                (N securities))))
                          (PP
                            (PP/NP as)
                            (NP
                              (N collateral))))))))))))
        (. .)))
    Invalid: N\N --> S[dcl]/NP None
    False
    """
    pass

def test_v():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.18')
    (S
      (S[dcl]
        (S[dcl]
          (NP He)
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/NP expects)
              (NP
                (NP/NP such)
                (NP
                  (NP[nb]/N a)
                  (N cut))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/PP because)
              (PP
                (PP/NP of)
                (NP
                  (NP
                    (N problems))
                  (NP\NP
                    ((NP\NP)/NP in)
                    (NP
                      (NP
                        (NP
                          (N
                            (N/N several)
                            (N sectors)))
                        (NP\NP
                          ((NP\NP)/NP of)
                          (NP
                            (NP[nb]/N the)
                            (N economy))))
                      (NP[conj]
                        (, ,)
                        (NP
                          (NP
                            (NP/NP particularly)
                            (NP
                              (N
                                (N/N real)
                                (N estate))))
                          (NP[conj]
                            (conj and)
                            (NP
                              (N automobiles))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP He)
          (S[dcl]\NP
            (S[dcl]\NP
              ((S[dcl]\NP)/NP expects)
              (NP
                (NP/NP such)
                (NP
                  (NP[nb]/N a)
                  (N cut))))
            ((S\NP)\(S\NP)
              (((S\NP)\(S\NP))/PP because)
              (PP
                (PP/NP of)
                (NP
                  (N
                    (N/PP problems)
                    (PP
                      (PP/NP in)
                      (NP
                        (NP
                          (N
                            (N/N several)
                            (N
                              (N/PP sectors)
                              (PP
                                (PP/NP of)
                                (NP
                                  (NP[nb]/N the)
                                  (N economy))))))
                        (NP[conj]
                          (, ,)
                          (NP
                            (NP
                              (NP/NP particularly)
                              (NP
                                (N
                                  (N/N real)
                                  (N estate))))
                            (NP[conj]
                              (conj and)
                              (NP
                                (N automobiles)))))))))))))
        (. .)))
    True
    """
    pass

def test_w():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.19')
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            (S[ng]\NP
              ((S[ng]\NP)/NP Bolstering)
              (NP
                (NP[nb]/N his)
                (N argument))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Commerce)
                  (N Department)))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[em]
                  ((S[dcl]\NP)/S[em] reported)
                  ((S\NP)\(S\NP) yesterday))
                (S[em]
                  (S[em]/S[dcl] that)
                  (S[dcl]
                    (NP
                      (NP
                        (N
                          (N/N
                            ((N/N)/(N/N) new)
                            (N/N home))
                          (N sales)))
                      (NP\NP
                        ((NP\NP)/NP for)
                        (NP
                          (N September))))
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[adj]\NP) were)
                      (S[adj]\NP
                        ((S[adj]\NP)/PP
                          (((S[adj]\NP)/PP)/NP down)
                          (NP
                            (N
                              (N/N 14)
                              (N %))))
                        (PP
                          (PP/NP from)
                          (NP
                            (NP[nb]/N
                              (NP
                                (N August))
                              ((NP[nb]/N)\NP 's))
                            (N
                              (N/N revised)
                              (N
                                (N/N
                                  ((N/N)/(N/N) 3.1)
                                  (N/N %))
                                (N fall)))))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S
            (S[ng]\NP
              ((S[ng]\NP)/NP Bolstering)
              (NP
                (NP[nb]/N his)
                (N argument))))
          (S[dcl]
            (, ,)
            (S[dcl]
              (NP
                (NP[nb]/N the)
                (N
                  (N/N Commerce)
                  (N Department)))
              (S[dcl]\NP
                ((S[dcl]\NP)/S[em]
                  ((S[dcl]\NP)/S[em] reported)
                  ((S\NP)\(S\NP) yesterday))
                (S[em]
                  (S[em]/S[dcl] that)
                  (S[dcl]
                    (NP
                      (N
                        (N/N
                          ((N/N)/(N/N) new)
                          (N/N home))
                        (N
                          (N sales)
                          (N\N
                            ((N\N)/NP for)
                            (NP
                              (N September))))))
                    (S[dcl]\NP
                      ((S[dcl]\NP)/(S[adj]\NP) were)
                      (S[adj]\NP
                        ((S[adj]\NP)/PP
                          (((S[adj]\NP)/PP)/NP down)
                          (NP
                            (N
                              (N/N 14)
                              (N %))))
                        (PP
                          (PP/NP from)
                          (NP
                            (NP[nb]/N
                              (NP
                                (N August))
                              ((NP[nb]/N)\NP 's))
                            (N
                              (N/N revised)
                              (N
                                (N/N
                                  ((N/N)/(N/N) 3.1)
                                  (N/N %))
                                (N fall)))))))))))))
        (. .)))
    True
    """
    pass

def test_x():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.20')
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N drop))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP marked)
            (NP
              (NP
                (NP[nb]/N the)
                (N
                  (N/N largest)
                  (N
                    (N/N monthly)
                    (N tumble))))
              (NP\NP
                ((NP\NP)/NP since)
                (NP
                  (NP
                    (NP[nb]/N a)
                    (N
                      (N/N
                        ((N/N)/(N/N) 19)
                        (N/N %))
                      (N slide)))
                  (NP\NP
                    ((NP\NP)/NP in)
                    (NP
                      (N
                        (N January)
                        (N\N 1982)))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (NP
            (NP[nb]/N The)
            (N drop))
          (S[dcl]\NP
            ((S[dcl]\NP)/NP marked)
            (NP
              (NP[nb]/N the)
              (N
                (N/N largest)
                (N
                  (N/N monthly)
                  (N
                    (N tumble)
                    (N\N
                      ((N\N)/NP since)
                      (NP
                        (NP[nb]/N a)
                        (N
                          (N/N
                            ((N/N)/(N/N) 19)
                            (N/N %))
                          (N
                            (N slide)
                            (N\N
                              ((N\N)/NP in)
                              (NP
                                (N
                                  (N January)
                                  (N\N 1982))))))))))))))
        (. .)))
    True
    """
    pass

def test_y():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.21')
    """
    pass

def test_z():
    r"""
    >>> flipArgumentStatus.debug(data.ccgbankNP, 'wsj_0301.22')
    (S
      (S[dcl]
        (S[dcl]
          (S/S Indeed)
          (S[dcl]
            (, ,)
            (S[dcl]
              (S/S
                ((S/S)/NP in)
                (NP
                  (N
                    (N/N early)
                    (N October))))
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N
                      ((N/N)/(N/N) West)
                      (N/N German))
                    (N
                      (N/N central)
                      (N bank))))
                (S[dcl]\NP
                  (S[dcl]\NP
                    ((S[dcl]\NP)/NP raised)
                    (NP
                      (NP[nb]/N its)
                      (N
                        (N/N
                          (N/N discount)
                          (N/N[conj]
                            (conj and)
                            (N/N Lombard)))
                        (N rates))))
                  ((S\NP)\(S\NP)
                    (((S\NP)\(S\NP))/NP by)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N full)
                        (N
                          (N/N percentage)
                          (N point))))))))))
        (. .)))
    True
    (S
      (S[dcl]
        (S[dcl]
          (S/S Indeed)
          (S[dcl]
            (, ,)
            (S[dcl]
              (S/S
                ((S/S)/NP in)
                (NP
                  (N
                    (N/N early)
                    (N October))))
              (S[dcl]
                (NP
                  (NP[nb]/N the)
                  (N
                    (N/N
                      ((N/N)/(N/N) West)
                      (N/N German))
                    (N
                      (N/N central)
                      (N bank))))
                (S[dcl]\NP
                  ((S[dcl]\NP)/PP
                    (((S[dcl]\NP)/PP)/NP raised)
                    (NP
                      (NP[nb]/N its)
                      (N
                        (N/N
                          (N/N discount)
                          (N/N[conj]
                            (conj and)
                            (N/N Lombard)))
                        (N rates))))
                  (PP
                    (PP/NP by)
                    (NP
                      (NP[nb]/N a)
                      (N
                        (N/N full)
                        (N
                          (N/N percentage)
                          (N point))))))))))
        (. .)))
    True
    """
    pass

if __name__ == '__main__':
    doctest.testmod()
