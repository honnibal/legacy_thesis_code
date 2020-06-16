import sys

import CCG

class PARGRebanker(object):
    def rebank(self, entries, resource):
        self.resource = resource
        for entry in entries:
            rel = entry.rel
            #print entry.rel
            for arg in entry.args:
                const = arg.getConstituent()
                if const and self.match(arg, const):
                    head = const.sibling()
                    if head and rel in head.listWords():
                        self.doParg(const, head)

    def canChange(self, parg, argument):
        if CCG.isIdentical(argument.label, 'conj'):
            return False
        return True

#    def doParg(self, parg, constituent):
#        head = constituent.sibling()
#        return self.flipArgAdjunct(constituent, head)

    def getArgSlash(self, arg, head):
        if arg > head:
            return '/'
        else:
            return '\\'

    def getAdjSlash(self, arg, head):
        if arg > head:
            return '\\'
        else:
            return '/'
