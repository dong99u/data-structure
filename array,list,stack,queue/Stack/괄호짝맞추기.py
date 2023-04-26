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
			return self.items[-1]
		except IndexError:
			print("Stack is Empty")
	def __len__(self):
		return len(self.items)
	def isEmpty(self):
		if len(self) == 0:
			return True
		return False

def parChecker(parSeq):
	S = Stack()
	for p in parSeq:
		if p in '[{(':
			S.push(p)
		else:
			if len(S) == 0:
				return False
			else:
				q = S.pop()
				if (p == ']' and q != '[') or (p == '}' and q != '{') or (p == ')' and q != '('):
					return False


	if len(S) == 0:
		return True
	else:
		return False

user_input = input()
print(parChecker(user_input))