class HashChain:
	def __init__(self, size = 10):
		self.size = size
		self.H = [SinglyLinkedList() for i in range(self.size)]

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	def __len__(self):
		return self.size
	def size(self):
		return self.size
	def __iter__(self):
		v = self.head
		while v != None:
			yield v
			v = v.next
	def printList(self):
		for i in self:
			print(i.key, '->', end = ' ')
		print("None")

	# INSERT METHODS
	def pushFront(self, key):
		newnode = Node(key)
		newnode.next = self.head
		self.head = newnode
		self.size += 1
	def pushBack(self, key):
		if self.size == 0:
			self.pushFront(key)
		else:
			newnode = Node(key)
			tail = self.head
			while tail.next != None:
				tail = tail.next
			tail.next = newnode
			self.size += 1
	def insert(self, k, key):
		if self.size <= k:
			self.pushBack(key)
		else:
			newnode = Node(key)
			prev, tail = None, self.head
			for i in range(k):
				prev = tail
				tail = tail.next
			prev.next = newnode
			newnode.next = tail
			self.size += 1


	# DELETE METHODS
	def popFront(self):
		if self.size == 0:
			return None
		else:
			v = self.head
			key = v.key
			self.head = v.next
			self.size -= 1
			del v
			return key
	def popBack(self):
		if self.size == 0:
			return None
		elif self.size == 1:
			return self.popFront()
		else:
			prev, tail = None, self.head
			while tail.next != None:
				prev = tail
				tail = tail.next
			key = tail.key
			prev.next = tail.next
			del tail
			self.size -= 1
			return key
	def remove(self, v): # Node v
		if v == None:
			return None
		else:
			if v == self.head:
				return self.popFront()
			else:
				prev, tail = None, self.head
				while tail != v:
					prev = tail
					tail = tail.next
				prev.next = tail.next
				self.size -= 1
				del tail
				return True
	def deleteMax(self):
		if self.size == 0:
			return None
		else:
			maxKey = self.findMax()
			self.remove(self.search(maxKey))
			return maxKey
	# SEARCH METHODS
	def search(self, key):
		for v in self:
			if key == v.key:
				return v
		return None
	def findMax(self):
		currentMax = self.head.key
		for i in self:
			if i.key > currentMax:
				currentMax = i.key
		return currentMax
	
	def reverse(self):
		a, b = None, self.head
		while b :
			if b :
				c = b.next
				b.next = a
			a = b
			b = c
		self.head = a

