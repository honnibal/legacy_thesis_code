from _AdjunctToArgument import AdjunctToArgument

class PhrasalVerbChanger(AdjunctToArgument):
    def rebank(self, entries):
        for entry in entries:
            particle = self.match(entry.predicate)
            if particle:
                self.doParg(particle, particle.sibling())
                    
    def match(self, pred):        
        for particle in pred.words:
            if particle.label in ['IN', 'RP']:
                particle = particle.parent()
                while particle.label.conj or not particle.sibling() or \
                      particle.sibling().label.conj:
                    particle = particle.parent()
                return particle
        return None

    def argLabeller(self, constituent):
        return 'PR'
