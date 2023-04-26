def relax(dist, graph, u, v):
	if dist[v] > dist[u] + graph[u][v]:
		dist[v] = dist[u] + graph[u][v]
def Bellman_Ford(dist, graph, n):
	for i in range(1, n):
		for u in graph:
			for v in graph[u]:
				relax(dist, graph, u, v)
				print(dist)


# INPUT

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

Bellman_Ford(dist, graph, n)

# OUTPUT

print(dist)