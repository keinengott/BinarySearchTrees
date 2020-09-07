# Robert Kaufman
# 21 April 2020
# Python program that creates t Binary Search Trees by inserting N random keys
# Program will find height of trees.
import random

# class that represents an individual node in a BST 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.count = 1
        self.val = key 
  
# insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node)
        elif root.val == node.val:
            root.count += 1
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)
  
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
        
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
  
def height(node):
    if not node:
        return 0
    else:
        depthL = height(node.left)
        depthR = height(node.right)
        if depthL > depthR:
            return depthL + 1
        else:
            return depthR + 1

N = 500
t = 10
def generateRandomNumbers(N):
    BSTValues = []
    for i in range(N):
        BSTValues.append(random.randint(1,500))
    return BSTValues

a = generateRandomNumbers(N)
b = generateRandomNumbers(N)
c = generateRandomNumbers(N)
d = generateRandomNumbers(N)
e = generateRandomNumbers(N)
f = generateRandomNumbers(N)
g = generateRandomNumbers(N)
h = generateRandomNumbers(N)
j = generateRandomNumbers(N)
k = generateRandomNumbers(N)
v = generateRandomNumbers(N)
w = generateRandomNumbers(N)
x = generateRandomNumbers(N)
y = generateRandomNumbers(N)
z = generateRandomNumbers(N)

# Driver program
n = Node(a[0])
o = Node(b[0])
p = Node(c[0])
q = Node(d[0])
r = Node(e[0])
n1 = Node(f[0])
o1 = Node(g[0])
p1 = Node(h[0])
q1 = Node(j[0])
r1 = Node(k[0])
n2 = Node(v[0])
o2 = Node(w[0])
p2 = Node(x[0])
q2 = Node(y[0])
r2 = Node(z[0])

for i in range(1,N):
    insert(n, Node(a[i]))
    insert(o, Node(b[i]))
    insert(p, Node(c[i]))    
    insert(q, Node(d[i]))    
    insert(r, Node(e[i]))
    insert(n1, Node(f[i]))
    insert(o1, Node(g[i]))
    insert(p1, Node(h[i]))    
    insert(q1, Node(j[i]))    
    insert(r1, Node(k[i]))
    insert(n2, Node(v[i]))
    insert(o2, Node(w[i]))
    insert(p2, Node(x[i]))    
    insert(q2, Node(y[i]))    
    insert(r2, Node(z[i]))
    
print("Binary Search Tree a has a heaight of %d"%height(n))
print("Binary Search Tree b has a heaight of %d"%height(o))
print("Binary Search Tree c has a heaight of %d"%height(p))
print("Binary Search Tree d has a heaight of %d"%height(q))
print("Binary Search Tree e has a heaight of %d"%height(r))
print("Binary Search Tree f has a heaight of %d"%height(n1))
print("Binary Search Tree g has a heaight of %d"%height(o1))
print("Binary Search Tree h has a heaight of %d"%height(p1))
print("Binary Search Tree j has a heaight of %d"%height(q1))
print("Binary Search Tree k has a heaight of %d"%height(r1))
print("Binary Search Tree a has a heaight of %d"%height(n2))
print("Binary Search Tree b has a heaight of %d"%height(o2))
print("Binary Search Tree c has a heaight of %d"%height(p2))
print("Binary Search Tree d has a heaight of %d"%height(q2))
print("Binary Search Tree e has a heaight of %d"%height(r2))
    
