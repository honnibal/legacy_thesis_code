class Rebanker(object):
    def rebank(self, sentence):
        changes = [True]
        while any(changes):
            changes = []
            for node in sentence.breadthList():
                if node.isLeaf() or node.isRoot():
                    continue
                # Get occasional ghosts from movement
                if node.length() == 0:
                    continue
                if self.match(node):
                    changes.append(True)
                    try:
                        self.change(node)
                    except:
                        print sentence.globalID
                        raise
                    
    def match(self, node):
        pass

    def change(self, node):
        pass
