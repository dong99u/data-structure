class Heap:  # minHeap
	def __init__(self, L=[]):
		self.A = L
		self.make_heap()
	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)
	def heapify_down(self, k, n): # k = 노드의 인덱스, n = 노드의 개수
		while 2*k+1 < n:
			L, R = 2*k+1, 2*k+2
			if self.A[L][1] < self.A[k][1]:
				m = L
			else:
				m = k
			if R < n and self.A[R][1] < self.A[m][1]:
				m = R
			if m != k:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				k = m
			else:
				break
	def make_heap(self):
			n = len(self.A)
			for k in range(n-1, -1, -1):
				self.heapify_down(k, n)

	def insert(self, val):
		self.A.append(val)
		self.heapify_up(len(self.A) - 1)
	def heapify_up(self, k):
		while k > 0 and self.A[(k-1)//2][1] > self.A[k][1]: # parent node > child node
			self.A[(k-1)//2], self.A[k] = self.A[k], self.A[(k-1)//2]
			k = (k-1)//2
	def delete_min(self):
		if len(self.A) == 0:
			return None
		val = self.A[0]
		self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		self.A.pop()
		self.heapify_down(0, len(self.A))
		return val
	def heap_sort(self):
		n = len(self.A)
		for k in range(len(self.A)-1, -1, -1):
			self.A[0], self.A[k] = self.A[k], self.A[0]
			n = n - 1
			self.heapify_down(0, n)

	def decreaseKey(self, val):
		cnt = 0
		for i in range(len(self.A)):
			if self.A[i][0] == val[0]:
				if self.A[i][1] == float('inf'):
					cnt += 1
				else:
					self.A[i][1] = val[1]
					idx = self.A.index(val)
					self.heapify_up(idx)
					break
		if cnt != 0:
			self.insert(val)


def relax(dist, graph, u, v):
	if dist[v] > dist[u] + graph[u][v]:
		dist[v] = dist[u] + graph[u][v]

		
def Dijkstra(dist, graph):
	Q = Heap([[i, dist[i]] for i in range(len(dist))])
	visited = []
	while len(Q) != 0:
		u, w = Q.delete_min()
		if w == float('inf'):
			continue
		if u in graph:
			for v in graph[u]:
				relax(dist, graph, u, v)
				if [v, dist[v]] not in visited:
					Q.decreaseKey([v, dist[v]])
					visited.append([v, dist[v]])




n = int(input('Number of Nodes: '))
m = int(input('Number of Edges: '))

graph = {}

for i in range(m):
	edge_info = input('%dth edge: ' %(i+1)).split()
	n1, n2, weight = [int(j) for j in edge_info]
	if n1 not in graph:
		graph[n1] = {n2 : weight}
	else:
		graph[n1][n2] = weight


dist = [float('inf')] * n
dist[0] = 0


Dijkstra(dist, graph)
for i in dist:
	print(i, end = ' ')