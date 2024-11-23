class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data)
        current_node = current_node.next

def insert(head, position, value):
    node_to_insert = Node(value)
    # If inserting at the beginning
    if position == 0:
        node_to_insert.next = head
        return node_to_insert  # Updated head

    current_position = 1
    current_node = head

    # Traverse until reaching the position or end of the list
    while current_node and current_position < position:
        current_node = current_node.next
        current_position += 1

    # If position is beyond list length
    if not current_node:
        print("Error: This position does not exist.")
        print("Position to insert is:", position)
        return head

    # Insert node
    node_to_insert.next = current_node.next
    current_node.next = node_to_insert
    return head

# Test code
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = node1
position = 6
value = 4

head = insert(head, position, value)
print_linked_list(head)
