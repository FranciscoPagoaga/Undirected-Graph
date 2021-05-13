class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def addNeighbor(self, v, weight):
		if v not in self.neighbors:
			self.neighbors.append((v, weight))
			self.neighbors.sort()

class Graph:
	vertices = {}
	
	def addVertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def addEdge(self, u, v, weight=0):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].addNeighbor(v, weight)
			self.vertices[v].addNeighbor(u, weight)
			return True
		else:
			return False

	def lowestDegree(self):
		lowest = 0
		for key in sorted(list(self.vertices.keys())):
			
			if self.vertices[key].neighbors.len()<=lowest:
				lowest = self.vertices[key].neighbors.len()

	def printGraph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))
	   

g = Graph()
a = Vertex('A')
g.addVertex(a)
g.addVertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.addVertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.addEdge(edge[:1], edge[1:])

g.printGraph()