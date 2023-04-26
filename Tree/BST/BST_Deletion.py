class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None

	def __str__(self):
		return str(self.key)


class Tree:
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def preorder(self, v):
		if v != None:
			print(v.key, end=' ')
			self.preorder(v.left)
			self.preorder(v.right)

	def inorder(self, v):
		if v != None:
			self.inorder(v.left)
			print(v.key, end=' ')
			self.inorder(v.right)
			
	def postorder(self, v):
		if v != None:
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end=' ')

	def find_loc(self, key):
		if self.size == 0: return None
		p = None
		v = self.root
		while v:
			if v.key == key: return v # key가 일치하면 해당노드 return
			elif v.key < key:
				p = v
				v = v.right
			else: # v.key > key:
				p = v
				v = v.left
		return p

	def search(self, key):
		p = self.find_loc(key)
		if p and p.key == key: return p
		else: return None # not found

	def insert(self, key):
		p = self.find_loc(key)
		if p == None or p.key != key:
			v = Node(key)
			if p == None:
				self.root = v
			else: # p.key != key
				v.parent = p
				if p.key >= key:
					p.left = v
				else:
					p.right = v
			self.size += 1

			return v
		else:
			print("key is already in the tree!")
			return None

	def deleteByMerging(self, x):
		# 노드들의 height 정보 update 필요
		a, b, pt = x.left, x.right, x.parent
		# c = x 자리를 대체할 노드
		# m = L에서 가장 큰 노드
		if a != None:
			c = a
			m = a
			while m.right:
				m = m.right
			if b:
				b.parent = m
			m.right = b
			
		else: # a == None
			c = b
		if pt != None: # x가 root가 아닌 경우
			if c: c.parent = pt
			if pt.left == x: pt.left = c
			else: pt.right = c
		else: # pt == None // x가 root인 경우
			self.root = c
			if c: c.parent = None

		self.size -= 1
		return 


	def deleteByCopying(self, x):
		# 노드들의 height 정보 update 필요
		a, b, pt = x.left, x.right, x.parent
		if a is None:
			if x is self.root:
				self.root = b
				if b:
					b.parent = None
			else: # x is not self.root
				if x is pt.left: pt.left = b
				else: pt.right = b
				if b: b.parent = pt

		else: # a is not None
			y = a
			while y.right:
				y = y.right
			x.key = y.key
			if y is a:
				x.left = y.left
				if y.left: y.left.parent = x
			else:
				p = y.parent
				p.right = y.left
				if y.left: y.left.parent = p

		self.size -= 1
		return


T = Tree()

while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		v = T.insert(int(cmd[1]))
		print("+ {0} is inserted".format(v.key))
	elif cmd[0] == 'deleteC':
		v = T.search(int(cmd[1]))
		T.deleteByCopying(v)
		print("- {0} is deleted by copying".format(int(cmd[1])))
	elif cmd[0] == 'deleteM':
		v = T.search(int(cmd[1]))
		T.deleteByMerging(v)
		print("- {0} is deleted by merging".format(int(cmd[1])))
	elif cmd[0] == 'search':
		v = T.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print(" * {0} is found!".format(cmd[1]))
	elif cmd[0] == 'preorder':
		T.preorder(T.root)
		print()
	elif cmd[0] == 'postorder':
		T.postorder(T.root)
		print()
	elif cmd[0] == 'inorder':
		T.inorder(T.root)
		print()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")