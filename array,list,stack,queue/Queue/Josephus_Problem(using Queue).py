class Queue:
	def __init__(self):
		self.items = []
		self.front_index = 0
	def enqueue(self, val):
		self.items.append(val)
	def dequeue(self):
		if len(self.items) == 0 or self.front_index == len(self.items):
			print('Queue is empty')
		else:
			x = self.items[self.front_index]
			self.front_index += 1
			return x
	def front(self):
		if len(self.items) == 0 or self.front_index == len(self.items):
			print("Queue is empty")
		else:
			return self.items[self.front_index]
	def __len__(self):
		return len(self.items) - self.front_index
	def isEmpty(self):
		if len(self) == 0:
			return True
		return False
		
def Josephus(n, k):
	Q = Queue()
	for i in range(1, n+1):
		Q.enqueue(i)
	while len(Q) != 1:
		for i in range(k-1):
			Q.enqueue(Q.dequeue())
		Q.dequeue()
	
	return Q.front()

# INPUT
n = int(input('n : '))
k = int(input('k : '))

# OUTPUT
print(Josephus(n, k))

