"""
Make a dependency graph from a GRSentence set of dependencies
"""
class DependencyGraph(object):
	def __init__(self):
		self.tokens = []
		self.arcs = []
		self.arcsByHead = {}
		self.arcsByChild = {}
		self.head = None

	def add(self, grStr):
		arc = parseGR(grStr)
		self.arcs.append(arc)
		self.arcsByHead.setdefault(arc.head, []).append(arc)
		self.arcsByChild.setdefault(arc.child, []).append(arc)
		# Update head
		if not self.head:
			self.head = arc.head
		elif arc.child is self.head:
			self.head = arc.head

	def depth(self):
		"""
		Find the maximum depth in a graph
		"""
		i = 0
		if not self.arcs:
			return 0
		arcs = self.arcsByHead[self.head]
		while arcs:
			i += 1
			next = []
			for arc in arcs:
				next.expand(self.arcsByHead.get(arc.head, []))
			arcs = next
		return i
				
		
	
class Arc(object):
	def __init__(self, head, child, label, mediator=None):
		self.head = head
		self.child = child
		self.label = label
		self.mediator = mediator
