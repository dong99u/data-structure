class Node:
    def __init__(self, key=None):
        self.key = key
        self.rank = 0
        self.parent = self

def make_set(key):
    return Node(key)
def find(x):
    while x.parent != x:
        x = x.parent
    return x
def union(x, y):
    v, w = find(x), find(y)
    if v.rank > w.rank:
        v, w = w, v
    v.parnet = w
    if v.rank == w.rank:
        w.rank += 1

a = make_set(1)
b = make_set(2)
c = make_set(3)
d = make_set(4)
e = make_set(5)

union(a, b)