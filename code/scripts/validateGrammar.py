#!/usr/bin/python2.4
"""
Apply the CCG rules to each production in a grammar, and save a dictionary
describing whether each production is valid or invalid
"""
import CCG, pickles

from general import stats
from copy import deepcopy as copy
import sys

from os.path import join as pjoin

def readGrammar(loc):
    productions = []
    for line in open(loc):
        if not line.strip():
            continue
        freq, production = line.strip().split(' # ')
        parent, children = production.split(' --> ')
        children = children.split()
        left = children[0]
        if len(children) == 2:
            right = children[1]
        else:
            right = None
        productions.append((parent, left, right, int(freq)))
    return productions

def getAnswers(productions):
    answers = {}
    CCG.setRuleFreq('a')
    for parent, left, right, freq in productions:
        left = CCG.Category(left)
        if right:
            right = CCG.Category(right)
        parent = CCG.Category(parent)
        key = (parent, left, right)
        rules = applyRules(left, right, parent)
        answers[key] = rules
    return answers

def analyse(productions, answers):
    validBinary = 0
    invalidBinary = 0
    invalidBinaryTypes = []
    validUnary = 0
    invalidUnary = 0
    invalidUnaryTypes = []
    byRule = {}
    for parent, left, right, freq in productions:
        rules = answers.get((parent, left, right), None)
        if rules == None:
#            print (parent, left, right)
            continue
        for rule in rules:
            byRule.setdefault(rule, 0)
            valid.write('%d: %s --> %s %s (%s)\n' % (freq, parent, left, right, rule))
            byRule[rule] += freq
        if rules:
            if right:
                validBinary += freq
            else:
                validUnary += freq
        else:
            if right:
                invalidBinary += freq
                invalidBinaryTypes.append((freq, parent, left, right))
            else:
                invalidUnary += freq
                invalidUnaryTypes.append((freq, parent, left))
    print 'Valid Unary: %d' % validUnary
    print 'Valid binary: %d' % validBinary
    print 'Invalid binary: %d (%d types)' % (invalidBinary, len(invalidBinaryTypes))
    print 'Invalid unary: %d (%d types)' % (invalidUnary, len(invalidUnaryTypes))
    for r, f in byRule.items():
        valid.write('%s: %d\n' % (r, f))
    invalidBinaryTypes.sort()
    invalidBinaryTypes.reverse()
    invalidUnaryTypes.sort()
    invalidUnaryTypes.reverse()
    return invalidBinaryTypes, invalidUnaryTypes

def applyRules(origLeft, origRight, label):
    def new():
        return copy(origLeft), copy(origRight)
    labelStr = str(label).replace('[nb]', '')
    left, right = new()
    if not right:
        functions = CCG.unaryFunctions
    else:
        functions = CCG.functions
    valid = []
    for function in functions:
        if right:
            guess = function(left, right)
        else:
            guess = function(left, label)
            label = copy(label)
        if str(guess).replace('[nb]', '') == labelStr:
            name = str(function).split()[1]
            valid.append(name)
        left, right = new()
    return valid

print "Reading"
if len(sys.argv) != 2:
    print "USAGE: <corpus path>"
    sys.exit(1)
corpusLoc = sys.argv[1]
grammarLoc = pjoin(corpusLoc, 'grammars', 'wsj02-21.grammar')
output = pjoin(corpusLoc, 'invalid')
valid = open(pjoin(corpusLoc, 'valid'), 'w')
productions = readGrammar(grammarLoc)
total = 0
for p, l, r, f in productions:
    total += f
print total
print "Validating productions"
answers = getAnswers(productions)
print "Analysing"
invalidBinary, invalidUnary = analyse(productions, answers)
output = open(output, 'w')
output.write("Invalid binary:\n\n")
for freq, parent, left, right in invalidBinary:
    output.write('%d: %s --> %s %s\n' % (freq, parent, left, right))
output.write("\nInvalid unary:\n\n")
for freq, parent, child in invalidUnary:
    output.write('%d: %s --> %s\n' % (freq, parent, child))
