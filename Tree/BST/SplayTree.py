class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0

	def __str__(self):
		return str(self.key)


class BST:
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def getHeight(self, root):
		if root is None:
			return -1
		leftHeight = self.getHeight(root.left) + 1
		rightHeight = self.getHeight(root.right) + 1

		return max(leftHeight, rightHeight)

	def updateHeight(self, v):
		if v:
			v.height = self.getHeight(v)
			self.updateHeight(v.left)
			self.updateHeight(v.right)

	def inorderAddList(self, v, list):
		if v:
			self.inorderAddList(v.left, list)
			list.append(v.key)
			self.inorderAddList(v.right, list)

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
			if v.key == key: return v  # key가 일치하면 해당노드 return
			elif v.key < key:
				p = v
				v = v.right
			else:  # v.key > key:
				p = v
				v = v.left
		return p

	def search(self, key):
		p = self.find_loc(key)
		if p and p.key == key: return p
		else: return None  # not found

	def insert(self, key):
		p = self.find_loc(key)
		if p == None or p.key != key:
			v = Node(key)
			if p == None:
				self.root = v
			else:  # p.key != key
				v.parent = p
				if p.key >= key:
					p.left = v
				else:
					p.right = v
			self.size += 1
			#height update
			self.updateHeight(self.root)

			return v
		else:
			print("key is already in the tree!")
			return None

	def deleteByCopying(self, x):
		a, b, pt = x.left, x.right, x.parent
		if a is not None:
			y = a
			while y.right: y = y.right
			x.key = y.key
			if y is a:
				x.left = y.left
				if y.left: y.left.parent = x
				s = x
			else:
				p = y.parent
				p.right = y.left
				if y.left: y.left.parent = p
				s = p
		else: # a is None
			if pt == None: # x is root node
				self.root = b
				if b:
					b.parent = None
				s = pt
			else:
				if x is pt.left: pt.left = b
				else: pt.right = b
				if b: b.parent = pt
				s = pt
		self.size -= 1
		self.updateHeight(self.root)
		return s


	def height(self, x):  # 노드 x의 height 값을 리턴
		if x == None: return -1
		else: return x.height

	def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
		# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
		if x.right is not None:
			current = x.right
			while current is not None:
				if current.left is None:
					break
				current = current.left
			return current
		p = x.parent
		while p is not None:
			if x != p.right:
				break
			x = p
			p = p.parent
		return p

	def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
		# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
		if x.left is not None:
			current = x.left
			while current is not None:
				if current.right is None:
					break
				current = current.right
			return current
		p = x.parent
		while p is not None:
			if x != p.left:
				break
			x = p
			p = p.parent
		return p

	def rotateLeft(self, z):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if not z: return
		x = z.right
		if x == None: return
		b = x.left
		x.parent = z.parent
		if z.parent:
			if z.parent.left == z:
				z.parent.left = x
			else:
				z.parent.right = x
		x.left = z
		z.parent = x
		z.right = b
		if b: b.parent = z
		if z == self.root:
			self.root = x
		#height update
		self.updateHeight(self.root)

	def rotateRight(self, z):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if not z: return
		x = z.left
		if x == None: return
		b = x.right
		x.parent = z.parent
		if z.parent:
			if z.parent.left == z:
				z.parent.left = x
			else:
				z.parent.right = x
		x.right = z
		z.parent = x
		z.left = b
		if b: b.parent = z
		if z == self.root:
			self.root = x
		#height update
		self.updateHeight(self.root)

class SplayTree(BST):
	def __init__(self):
		self.root = None
		self.size = 0

	def zig(self, z):
		super().rotateRight(z)
	def zag(self, z):
		super().rotateLeft(z)
	def splay(self, v):
		if v is self.root:
			return v
		elif v.parent is self.root:
			if v is self.root.left:
				self.zig(self.root)
				self.root = v
			else: # v 가 root node의 right subtree일 경우
				self.zag(self.root)
				self.root = v
			return v
		else: # v의 parent node가 root node 가 아닐 경우
			p = v.parent
			if v is p.left:
				self.zig(p)
			else: # v가 p의 right subtree일 경우
				self.zag(p)
			return self.splay(v)
	
	def search(self, key):
		v = super().search(key)
		if v:
			self.root = self.splay(v)
		return v
	def insert(self, key):
		v = super().insert(key)
		self.root = self.splay(v)
		return v
	def delete(self, x):
		x = self.splay(x)
		L, R = x.left, x.right
		if L:
			m = L
			while m.right:
				m = m.right
			m = self.splay(m)
			m.right = R
			if R:
				R.parent = m
			self.root = m
			m.parent = None
		else: # L is not exist
			if R:
				R.parent = None
			self.root = R
		self.size -= 1
		super().updateHeight(self.root)

		return x


T = SplayTree()
while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		v = T.insert(int(cmd[1]))
		print("+ {0} is inserted".format(v.key))
	elif cmd[0] == 'delete':
		v = T.search(int(cmd[1]))
		T.delete(v)
		print("- {0} is deleted".format(int(cmd[1])))
	elif cmd[0] == 'search':
		v = T.search(int(cmd[1]))
		if v == None:
			print("* {0} is not found!".format(cmd[1]))
		else:
			print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'height':
		h = T.height(T.search(int(cmd[1])))
		if h == -1:
			print("= {0} is not found!".format(cmd[1]))
		else:
			print("= {0} has height of {1}".format(cmd[1], h))
	elif cmd[0] == 'succ':
		v = T.succ(T.search(int(cmd[1])))
		if v == None:
			print("> {0} is not found or has no successor".format(cmd[1]))
		else:
			print("> {0}'s successor is {1}".format(cmd[1], v.key))
	elif cmd[0] == 'pred':
		v = T.pred(T.search(int(cmd[1])))
		if v == None:
			print("< {0} is not found or has no predecssor".format(cmd[1]))
		else:
			print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
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