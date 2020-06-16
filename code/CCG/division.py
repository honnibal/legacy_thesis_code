"""
Explore the category reduction from division
"""
import Category, re
from Category import catDict
def replaceAdj(adjunct):
    innerRes = cat.result
    while innerRes.isComplex():
        innerRes = innerRes.result
    newCat = '%s$%s%s$' % (str(innerRes), cat.slash, str(innerRes))
    return newCat

def replaceCat(cat):
    if not cat.isComplex():
        return str(cat)
    elif cat.isAdjunct():
        newCat = replaceAdj(cat)
    else:
        argument = replaceCat(cat.argument)
        if cat.argument.isComplex():
            argument = '(%s)' % argument
        result = replaceCat(cat.result)
        if cat.result.isComplex():
            result = '(%s)' % result
        newCat = result + cat.slash + argument
    return newCat

newCatDict = {}
for catStr in catDict:
    cat = Category.Category(catStr)
    newCat = replaceCat(cat)
    newCatDict[newCat] = True
print len(catDict)
print len(newCatDict)
#for cat in newCatDict:
#    print cat
