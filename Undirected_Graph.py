class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def addNeighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append((v))
			self.neighbors.sort()

class Graph:
	vertices = {}
	
	def addVertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def addEdge(self, u, v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].addNeighbor(v)
			self.vertices[v].addNeighbor(u)
			return True
		else:
			return False

	def lowestDegree(self):
		lowest = 0
		cont = 0
		vertex = "" 
		for key in sorted(list(self.vertices.keys())):
			if(cont == 0):
				lowest = len(self.vertices[key].neighbors)
				vertex=key
			elif(len(self.vertices[key].neighbors) <= lowest):
				lowest = len(self.vertices[key].neighbors)
				vertex=key

			cont+=1
		return (lowest, vertex)

	def graphDegree(self):
		lowest = 0
		cont = 0 
		for key in sorted(list(self.vertices.keys())):
			if(cont == 0):
				lowest = len(self.vertices[key].neighbors)
			elif(len(self.vertices[key].neighbors) > lowest):
				lowest = len(self.vertices[key].neighbors)
			cont+=1
		return (lowest)

	def sumDegree(self):
		sum = 0
		for key in sorted(list(self.vertices.keys())):
			sum+= len(self.vertices[key].neighbors)
		return sum

	def printGraph(self):
		print(self.vertices)
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))
	
	def shortestPath(self,x,y):
		explored = []
		queue = [[x]]
		if x == y:
			return 
		
		while queue:
			path = queue.pop(0)
			node = path[-1]
			if node not in explored:
				neighbours = self.vertices[node].neighbors
				print(neighbours)
				for neighbour in neighbours:
					new_path = list(path)
					new_path.append(neighbour)
					queue.append(new_path)					
					if neighbour == y:
						return new_path
				explored.append(node)
		return

# g = Graph()
# a = Vertex('A')
# g.addVertex(a)
# g.addVertex(Vertex('B'))
# for i in range(ord('A'), ord('K')):
# 	g.addVertex(Vertex(chr(i)))

# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
# for edge in edges:
# 	g.addEdge(edge[:1], edge[1:])

# g.printGraph()