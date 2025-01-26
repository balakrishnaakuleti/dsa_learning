class Node:
    def __init__(self, value):
        self.value = value
        self.children = None
    
def preorder_traverse_tree(root):
    if root is None:
        return
    print(root.value)
    if root.children is None:
         return
    for child in root.children:
            preorder_traverse_tree(child)
def postorder_traverse_tree(root):
    if root is None:
        return
    if root.children is None:
         print(root.value)
         return
    for child in root.children:
            postorder_traverse_tree(child)
    print(root.value)


root = Node(1)
node_with_children = Node(3)
node_with_children.children= [Node(6),Node(7),Node(8)]
children = [Node(2),node_with_children ,Node(4), Node(5)]
root.children = children

print("Pre orer traversal")
preorder_traverse_tree(root)

print("Post order traversal")
postorder_traverse_tree(root)