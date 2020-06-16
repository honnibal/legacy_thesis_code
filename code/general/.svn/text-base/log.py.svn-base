"""
Log messages
"""
import os
def openLog(path, key = None):
    global _logFile
    directory, f = path.rsplit('/', 1)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if key:
        _logs[key] = open(path, 'w')
    else:
        _logFile = open(path, 'w')

def msg(message, key = None):
    global _logFile, _logs
    if not key:
        _logFile.write(str(message) + '\n')
    else:
        _logs[key].write(str(message) + '\n')

def close():
    global _logFile, _logs
    if _logFile:
        _logFile.close()
    for f in _logs.values():
        f.close()
    

_logs = {}
_logFile = None
