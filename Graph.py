# BFS and DFS On a Graph
# Build Graph

# When would you use a graph?

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)


	def add_edge(self, u, v):
		self.graph[u].append(v)

	### TRAVERSALS ###

	## When to use BFS vs DFS?

	# Breadth First Search
	## Graphs that have numbers in ascending order
	def bfs(self, source_node):

		visited = [False] * (max(self.graph) + 1)


	# Depth First Search
	def dfs(self, source_node, visited):
		pass



	### SPANNING TREE ALGOS ###
