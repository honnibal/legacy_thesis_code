#!/usr/bin/python2.4
"""
Make an LI style latex derivation figure from a specified sentence with tokens,
supertags and ordered rule applications. Handles the logic for what should go on what
lines.


Example LI derivation:

"""
import sys
class Derivation:
    def __init__(self, stringDef):
        lines = stringDef.split('\n')
        self.tokens = TokenList(lines.pop(0))
        rules = []
        for line in lines:
            rules.append(RuleApp(line, self.tokens.tokens))
        self.rules = rules
        derivLines = self.arrangeRules(rules)
        self.derivLines = derivLines
    
    def arrangeRules(self, origRules):
        """
        Arrange the rules into a list of DerivLines
        """
        lines = []
        rules = origRules[:]
        lastRule = rules.pop(0)
        currLine = [lastRule]
        while rules:
            currRule = rules.pop(0)
            # Do we continue line?
            if lastRule.end < currRule.start:
                assert currRule.start > lastRule.start
                currLine.append(currRule)
            else:
                lines.append(DerivLine(currLine))
                currLine = [currRule]
            lastRule = currRule
        if currLine:
            lines.append(DerivLine(currLine))
        return lines

    def printDeriv(self):
        lines = []
        lines.append(self.tokens.printWords())
        lines.append(self.tokens.printUlines())
        lines.append(self.tokens.printStags())
        for derivLine in self.derivLines:
            lines.append(derivLine.printNames())
            lines.append(derivLine.printResults())
        derivStr = ' \\\\\n'.join(lines)
        return '\deriv{%d}{\n%s\n}' % (len(self.tokens), derivStr)

    def printFigure(self):
        return '\\begin{figure}\n%s\\end{figure}' % self.printDeriv()

 


class TokenList:
    def __init__(self, line):
        tokenStrings = line.split()
        tokens = []
        for i, string in enumerate(tokenStrings):
            tokens.append(Token(string, i))
        self.tokens = tokens

    def __len__(self):
        return len(self.tokens)

    def printWords(self):
        words = []
        for token in self.tokens:
            words.append(r'\rm %s' % token.text)
        return ' & '.join(words)

    def printUlines(self):
        ulines = []
        for token in self.tokens:
            ulines.append(r'\uline{1}')
        return '&'.join(ulines)

    def printStags(self):
        stags = []
        for token in self.tokens:
            stags.append('%s' % token.stag)
        return ' &\n'.join(stags)

class Token:
    def __init__(self, tokenStr, offset):
        if tokenStr.count('|') != 1:
            print tokenStr
        text, stag = tokenStr.split('|')
        text = text.replace('_', ' ')
        self.text = text
        self.stag = '\cf{%s}' % stag.replace('\\', r'\bs ')
        self.offset = offset


class DerivLine:
    def __init__(self, rules):
        self.rules = rules

    def printNames(self):
        return self._printLine(True)

    def printResults(self):
        return self._printLine(False)

    def _printLine(self, isNames):
        currOffset = 0
        line = []
        for rule in self.rules:
            separators = '&'*(rule.start - currOffset)
            if line and not separators:
                line.append('&')
            else:
                line.append(separators)
#            for i in xrange(currOffset, rule.start):
#                line.append('&')
            if isNames:
                line.append(rule.printName())
            else:
                line.append(rule.printResult())
            currOffset += ((rule.start + rule.span) - 1)
        return ' '.join([i for i in line if i])
        

class RuleApp:
    def __init__(self, ruleStr, tokens):
        self.origStr = ruleStr
        rule, start, end, result = ruleStr.split()
        valid = 'fapply,bapply,fcomp,bcomp,bxcomp,ftype,btype,psg,unhat'.split(',')
        if rule not in valid:
            print "warning: unknown rule used"
        self.rule = rule
        try:
            self.start = int(start)
        except:
            self.start = self._lookup(start, tokens)
        try:
            self.end = int(end)
        except:
            self.end = self._lookup(end, tokens)
        if self.start > self.end:
		    print self.origStr
		    raise StandardError
        self.span = (self.end - self.start) + 1
        self.result = '\cf{%s}' % result.replace('\\', r'\bs ')

    def printName(self):
        """
        Do the name part, like \fapply{7}
        """
        return r'\%s{%d}' % (self.rule, self.span)
    
    def printResult(self):
        """
        Do the result part, like \mc{8}{\cf{S[dcl]\bs NP}}
        """
        return r'\mc{%d}{%s}' % (self.span, self.result)

    def __cmp__(self, other):
        return cmp(self.start, other.start)

    def _lookup(self, target, tokens):
        for i, token in enumerate(tokens):
            if token.text == target:
                return i
        else:
            raise StandardError, target




def makeDocument(derivations, location):
    """
    Add a header so that the derivations compile, for easy debugging
    """
    header = r"""\documentclass[11pt]{article}
\usepackage{LI}

\newcommand{\cf}[1]{\mbox{$\it{#1}$}}   % category font"""
    figures = []
    for derivation in derivations:
        figures.append(derivation.printFigure())                           
    document = '%s\n\\begin{document}\n%s\end{document}' % (header, '\n\n'.join(figures))
    open(location, 'w').write(document)



def debug(testInput, goldOutput):
    deriv = Derivation(testInput)
    testOutput = deriv.printDeriv()
    for i, c in enumerate(testOutput):
        if c != goldOutput[i]:
            print 'Mismatch at char %d (%s, %s)' % (i, repr(c), repr(goldOutput[i]))
            print testOutput
            print goldOutput
            print testOutput[i-10:i+10]
            print goldOutput[i-10:i+10]
            raise StandardError
    print "Outputs match!"

# Example input sentence
testInput = """Pierre|NP will|(S[dcl]\NP)/(S[b]\NP) join|((S[b]\NP)/PP)/NP the|NP/N board|N as|PP/NP a|NP/N nonexecutive|N/N director|N
fapply 3 4 N
fapply 7 8 N
fapply 2 4 (S[b]\NP)/PP
fapply 6 8 NP
fapply 5 8 PP
fapply 2 8 S[b]\NP
fapply 1 8 S[dcl]\NP
bapply 0 8 S[dcl]"""

# Example LI derivation
testDeriv = r"""\deriv{9}{
\rm Pierre & \rm will & \rm join & \rm the & \rm board & \rm as & \rm a & \rm nonexecutive & \rm director \\
\uline{1}&\uline{1}&\uline{1}&\uline{1}&\uline{1}&\uline{1}&\uline{1}&\uline{1}&\uline{1} \\
\cf{NP} &
\cf{(S[dcl]\bs NP)/(S[b]\bs NP)} &
\cf{((S[b]\bs NP)/PP)/NP} &
\cf{NP/N} &
\cf{N} &
\cf{PP/NP} &
\cf{NP/N} &
\cf{N/N} &
\cf{N} \\
&&& \fapply{2} &&& \fapply{2} \\
&&& \mc{2}{\cf{N}} &&& \mc{2}{\cf{N}} \\
&& \fapply{3} && \fapply{3} \\
&& \mc{3}{\cf{(S[b]\bs NP)/PP}} && \mc{3}{\cf{NP}} \\
&&&&& \fapply{4} \\
&&&&& \mc{4}{\cf{PP}} \\
&& \fapply{7} \\
&& \mc{7}{\cf{S[b]\bs NP}} \\
& \fapply{8} \\
& \mc{8}{\cf{S[dcl]\bs NP}} \\
\bapply{9} \\
\mc{9}{\cf{S[dcl]}}
}"""


if __name__ == '__main__':

    
#    deriv = Derivation(stringDeriv)
#    print deriv.printFigure()
#    deriv = Derivation(stringDeriv2)
#    print deriv.printFigure()
#    deriv = Derivation(stringDeriv3)
#    print deriv.printFigure()
#    deriv = Derivation(stringDeriv4)
#    deriv.makeDocument('/home/mhonn/papers/formfunction/derivations/noun_raising1.tex')
#    deriv = Derivation(stringDeriv5)
#    deriv.makeDocument('/home/mhonn/papers/formfunction/derivations/noun_raising2.tex')
    
    if len(sys.argv) != 3:
        print """USAGE: latexDerivation.py <input file> <output file>"""
        sys.exit(1)
    inputLoc = sys.argv[1]
    outputLoc = sys.argv[2]
    # Try the locations, just to check immediately whether they're valid
    try:
        open(inputLoc)
        open(outputLoc, 'a')
    except:
        print "Unable to open one or more of the locations specified."
        print """USAGE: latexDerivation.py <input file> <output file>"""
        sys.exit(1)
    derivDescs = open(sys.argv[1]).read().strip().split('\n\n')
    derivations = []
    for derivDesc in derivDescs:
        deriv = Derivation(derivDesc)
        derivations.append(deriv)
    makeDocument(derivations, outputLoc)
