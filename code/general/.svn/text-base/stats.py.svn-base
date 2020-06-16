"""
Store counters in a dictionary so that they're globally accessible,
so that we can have arbitrary statistics without a flood of global variables
"""
def count(key):
    global theCounts, _context
    theCounts.setdefault((key, _context), 0)
    theCounts[(key, _context)] += 1

def report(order = None):
    if not order:
        order = sorted(theCounts.keys())
    for k in order:
        if len(k) == 1:
            key = k
            context = None
        else:
            key, context = k
        if not context:
            print "%s: %d" % (key, theCounts.get(k, 0))
        else:
            print "%s (%s): %d" % (key, context, theCounts.get(k, 0))

def setContext(context):
    global _context
    _context = context

theCounts = {}
_context = None
