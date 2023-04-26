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



# Controler
L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
