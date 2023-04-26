class Stack:
	def __init__(self):
		self.items = []
	def push(self, val):
		self.items.append(val)
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
	def __len__(self):
		return len(self.items)
	def isEmpty(self):
		if len(self) == 0:
			return True
		return False

operator = '+-/*()^'
def get_token_list(expr):
	global operator
	L = []
	expr = expr.replace(' ', '')
	while expr != '':
		if len(expr) == 1:
			L.append(expr)
			expr = expr[i+1:]
		for i in range(len(expr)):
			if expr[i] in operator:
				if expr[:i] != '':
					L.append(expr[:i])
				L.append(expr[i])
				expr = expr[i+1:]
				break
	return L
	

def infix_to_postfix(token_list):
	global operator
	outstack = []
	opstack = Stack()
	
	rank = {
		'^': 3,
		'*': 2,
		'/': 2,
		'+': 1,
		'-': 1,
		'(': 0
	}
	for i in token_list:
		if i not in operator:
			outstack.append(float(i))
		else:
			if i == '(':
				opstack.push(i)
			elif i in '+-*/^':
				while len(opstack) != 0 and rank[i] <= rank[opstack.top()]:
					outstack.append(opstack.pop())
				opstack.push(i)
			elif i == ')':
				while len(opstack) != 0 and opstack.top() != '(':
					outstack.append(opstack.pop())
				opstack.pop()

	while len(opstack) != 0:
		outstack.append(opstack.pop())
	
	return outstack
				
def compute_postfix(token_list):
	global operator
	S = Stack()
	for i in token_list:
		if type(i) == float:
			S.push(i)
		else:
			a = S.pop()
			b = S.pop()
			if i == '+':
				S.push(b+a)
			elif i == '-':
				S.push(b-a)
			elif i == '*':
				S.push(b*a)
			elif i == '/':
				S.push(b/a)
			else:
				S.push(b ** a)
	return S.pop()



expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)