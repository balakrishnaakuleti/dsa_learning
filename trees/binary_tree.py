class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traverse(root):
    if root is None:
        return
    print(root.value)
    if root.left is not None:
        preorder_traverse(root.left)
    if root.right is not None:
        preorder_traverse(root.right)

def postorder_traverse(root):
    if root is None:
        return
    if root.left is not None:
        postorder_traverse(root.left)
    if root.right is not None:
        postorder_traverse(root.right)
    print(root.value)

def inorder_traverse(root):
    if root is None:
        return
    if root.left is not None:
        inorder_traverse(root.left)
    print(root.value)
    if root.right is not None:
        inorder_traverse(root.right)

root = Node(10)
root.left = Node(8)
root.right = Node(11)

root.left.left = Node(7)
root.left.right = Node(9)

root.right.left=Node(12)

print("Pre order traversal: ")
preorder_traverse(root)

print("Post order traversal: ")
postorder_traverse(root)

print("In order traversal: ")
inorder_traverse(root)