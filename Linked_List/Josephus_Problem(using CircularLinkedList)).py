class Node:
	def __init__(self, key = None):
		self.key = key
		self.next = self.prev = self
	def __str__(self):
		return str(self.key)
class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # dummy node
		self.size = 0
	def __iter__(self): # dummy node의 next node부터 return
		v = self.head.next
		while v.key != None:
			yield v
			v = v.next
	def __len__(self):
		return self.size
	def printList(self):
		print('h ->', end = ' ')
		for i in self:
			print(i.key, '->', end = ' ')
		print('h')

	def splice(self, a, b, x): # node a, b, x
		if a == None or b == None or x == None:
			return None
		ap = a.prev
		bn = b.next
		xn = x.next
		ap.next = bn
		bn.prev = ap
		x.next = a
		a.prev = x
		b.next = xn
		xn.prev = b
	def moveAfter(self, a, x):
		self.splice(a, a, x)
	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)
	def insertAfter(self, x, key):
		self.moveAfter(Node(key), x)
		self.size += 1
	def insertBefore(self, x, key):
		self.moveBefore(Node(key), x)
		self.size += 1
	def pushFront(self, key):
		self.insertAfter(self.head, key)
	def pushBack(self, key):
		self.insertBefore(self.head, key)
	def search(self, key):
		for i in self:
			if i.key == key:
				return i
		return None
	def deleteNode(self, x): # node x
		if x == None or x == self.head:
			return None
		x.prev.next = x.next
		x.next.prev = x.prev
		del x
		self.size -= 1
	def popFront(self):
		if self.size == 0:
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key
	def popBack(self):
		if self.size == 0:
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
	def first(self):
		if self.size == 0:
			return None
		else:
			return self.head.next.key
	def last(self):
		if self.size == 0:
			return None
		else:
			return self.head.prev.key
	def join(self, another_list):
		self.splice(another_list.head.next, another_list.head.prev, self.head.prev)
		self.size += another_list.size
	def split(self, x):
		another_list = DoublyLinkedList()
		self.splice(x, self.head.prev, another_list.head)
		count = 0
		for i in self:
			count += 1
		self.size = count
		count = 0
		for i in another_list:
			count += 1
		another_list.size = count

		return another_list

def Josephus(n, k):
	L = DoublyLinkedList()
	for i in range(1, n+1):
		L.pushBack(i)
	
	v = L.head
	while len(L) > 1:
		for i in range(k-1):
			if v.next == L.head:
				v = v.next
			v = v.next
			if v.next == L.head:
				v = v.next
		L.deleteNode(v.next)
	return L.head.next.key


# INPUT
n = int(input('n : '))
k = int(input('k : '))

# OUTPUT
print(Josephus(n, k))

