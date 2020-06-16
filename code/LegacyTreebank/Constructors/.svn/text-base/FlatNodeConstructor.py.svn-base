"""
Flat node constructor for the PTB
"""
def make(pieces):
    nodeClass = determineClass(pieces.pop(0))
    settings = getSettings(pieces)
    node = nodeClass(settings)
    return node

def getSettings(pieces):
    """
    For treebank data:
    ID, label, function label, identifier, identified, [text], [word id]
    """
    global _labels, _baseSettings
    settings = {}
    settings.update(baseSettings)
    assert len(pieces) == len(labels)
    for piece, label in zip(pieces, labels):
        if piece and label:
            settings[label] = eval(piece)
    return piece

_labels = ['globalID', 'label', 'functionLabel', 'identifier', 'identified', 'text', 'wordID']
_baseSettings = {'metadata': {}, '_children': [], '_parent': None, 'constituent': None}
