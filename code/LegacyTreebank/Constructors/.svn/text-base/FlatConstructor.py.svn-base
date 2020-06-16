"""
Make a file from a flat representation that lists each node by its head index,
so that we can avoid the recursive string parsing
"""
import FileConstructor

def make(location, fileClass, nodeConstructor):
    settings = FileConstructor.getSettings(location)
    fileNode = fileClass(settings)
    nodes = {fileNode.ID: fileNode}
    for nodeText in open(location):
        pieces = nodeText.split('\t')
        headIdx = eval(pieces.pop(0))
        node = nodeConstructor.make(pieces)
        head = nodes[headIdx]
        head.attachChild(node)
        nodes[node.globalID] = node
