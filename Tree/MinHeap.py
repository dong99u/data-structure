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
			if self.A[L] < self.A[k]:
				m = L
			else:
				m = k
			if R < n and self.A[R] < self.A[m]:
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
		while k > 0 and self.A[(k-1)//2] > self.A[k]: # parent node > child node
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