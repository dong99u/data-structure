class Stack:
	def __init__(self):
		self.items = []
	def push(self, val):
		self.items.append(val)
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is Empty")
	def top(self):
		try:
			return self.itmes[-1]
		except IndexError:
			print("Stack is Empty")
	def __len__(self):
		return len(self.items)
class Queue:
	def __init__(self):
		self.items = []
		self.front_index = 0
	def __len__(self):
		return len(self.items) - self.front_index
	def enqueue(self, val):
		self.items.append(val)
	def dequeue(self):
		if self.front_index == len(self.items):
			print('Queue is Empty')
		else:
			x = self.items[self.front_index]
			self.front_index += 1
			return x

def DFS(graph, s): # v를 방문중
	stack = Stack()
	visited = []
	stack.push(s)
	while len(stack) != 0:
		v = stack.pop()
		if v not in visited:
			visited.append(v)
			for w in reversed(list(graph[v])):
				if w not in visited:
					stack.push(w)

	return visited
def DFS_ALL(graph):
	visited = DFS(graph, 0)
	for vertex in graph:
		if vertex not in visited:
			visited += DFS(graph, vertex)
	return visited

def BFS(graph, s):
	queue = Queue()
	visited = []
	queue.enqueue(s)
	while len(queue) != 0:
		v = queue.dequeue()
		if v not in visited:
			visited.append(v)
			for w in graph[v]:
				if w not in visited:
					queue.enqueue(w)
	return visited
def BFS_ALL(graph):
	visited = BFS(graph, 0)
	for vertex in graph:
		if vertex not in visited:
			visited += BFS(graph, vertex)
	return visited


# INPUT

n = int(input('Number of Nodes: ')) # number of Nodes (n <= 10000)
m = int(input('Number of Edges: ')) # number of Edges (m <= 100000)

graph = {}
for i in range(m):
	edge_info = input('%dth edge: ' %(i+1)).split()
	n1, n2 = [int(j) for j in edge_info]
	if n1 not in graph:
		graph[n1] = {n2}
	elif n2 not in graph[n1]:
		graph[n1].add(n2)

	if n2 not in graph:
		graph[n2] = {n1}
	elif n1 not in graph[n2]:
		graph[n2].add(n1)


# OUTPUT

print('DFS:', DFS_ALL(graph))
print('BFS:', BFS_ALL(graph))