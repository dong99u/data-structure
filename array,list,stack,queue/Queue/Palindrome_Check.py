from collections import deque

def check_palindrome(s):
	dq = deque(s)
	result = True
	while len(dq) > 1:
		if dq.popleft() != dq.pop():
			result = False
	return result

# INPUT
s = input()

# OUTPUT
print(check_palindrome(s))

