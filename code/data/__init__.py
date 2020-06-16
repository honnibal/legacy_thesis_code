from os.path import join as pjoin
import os.path

def getLoc(loc):
    if loc.startswith('data.'):
        loc = loc[5:]
        return eval(loc)
    else:
        return loc

path = os.path.dirname(__file__)
pickles = pjoin(path, 'pickles')
nombankCCG = pjoin(path, 'nombankCCG.txt')
propbankCCG = pjoin(path, 'propbankCCG.txt')
propbankHatCCG = pjoin(path, 'hat_propbank.txt')
