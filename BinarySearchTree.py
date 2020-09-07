# Robert Kaufman
# 21 April 2020
# Python program to demonstrate insert operation on binary search trees  

nodes = [30, 10, 45, 38, 20, 50, 25, 33, 8, 12] 
# class that represents an individual node in a BST 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
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
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

def deleteNode(root, key):
    """
    Used https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-4.php
    as a resource to help with deleting nodes
    """
    if not root: 
        return root
    # Find the node in the left subtree if key value is less than root value
    if root.val > key: 
        root.left = deleteNode(root.left, key)
    # Find the node in right subtree if key value is greater than root value, 
    elif root.val < key: 
        root.right= deleteNode(root.right, key)
    # Delete the node if root.value == key
    else: 
    # If there is no right children delete the node and new root would be root.left
        if not root.right:
            return root.left
    # If there is no left children delete the node and new root would be root.right	
        if not root.left:
            return root.right
      # If both left and right children exist in the node replace its value with 
      # the minmimum value in the right subtree. Now delete that minimum node
      # in the right subtree
        temp_val = root.right
        while temp_val.left:
            temp_val = temp_val.left
        # Replace value	
        root.val = temp_val.val
      # Delete the minimum node in right subtree
        root.right = deleteNode(root.right,root.val)
        return root

def search(root, key):
    if root:
        print(root.val)
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)
  
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

def largestValue(root):
    if root.right is None:
        print("The largest key is %d\n" %root.val)
    else:
        largestValue(root.right)

def smallestValue(root):
    if root.left is None:
        print("The smallest key is %d" %root.val)
    else:
        smallestValue(root.left)

# Driver program
r = Node(nodes[0])

for i in range(1,len(nodes)):
    insert(r, Node(nodes[i]))
    
# Print traversals of the BST
print("Inorder traversal:")
inorder(r)
print("Postorder traversal:")
postorder(r)
print("Preorder traversal:")
preorder(r)
print ("The height of the tree is %d" %height(r))
smallestValue(r)
largestValue(r)
print("Searching for 38 path:")
searchedNode = search(r, 38)
print("Searching for 9 path:")
searchedNode2 = search(r,9)
deleteNode(r,10)
print("\nAfter deletion:")
print("Inorder traversal:")
inorder(r)
print("Postorder traversal:")
postorder(r)
print("Preorder traversal:")
preorder(r)
