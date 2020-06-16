"""
Load, store and cache pickled files.
Loading simply returns cPickle.load(file, 1)
Caching keeps a local reference to the file and passes the reference
if cache is called again
Storing just dumps the file
"""
import cPickle, os
import data

def load(desc):
    path = _getPath(desc)
    return cPickle.load(open(path, 'rb'))

def cache(desc):
    global _cached
    return _cached.setdefault(desc, load(desc))

def store(obj, desc):
    path = _getPath(desc)
    cPickle.dump(obj, open(path, 'wb'), -1)

def ls():
    path = _getPath('stuff').replace('stuff.pickle', '')
    dirList = os.listdir(path)
    return '\n'.join([f[:-7] for f in dirList if f.endswith('.pickle')])

def _getPath(desc):
    return os.path.join(data.pickles, desc + '.pickle')

_cached = {}
