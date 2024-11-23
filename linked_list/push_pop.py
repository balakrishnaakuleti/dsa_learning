class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data)
        current_node = current_node.next

def push(head, element):
    if head is None:
        return Node(element)  # Create the first node if the list is empty

    current_node = head
    # Traverse to the end of the list
    while current_node.next:
        current_node = current_node.next
    # Add new node at the end
    current_node.next = Node(element)
    return head

def pop(head):
    if head is None:
        print("List is empty, nothing to pop.")
        return None, None  # Return None for both head and popped element

    if head.next is None:
        # Only one element in the list
        popped_element = head.data
        head = None
        return head, popped_element

    # Traverse to the second-to-last node
    current_node = head
    while current_node.next.next:
        current_node = current_node.next
    
    # Pop the last element
    popped_element = current_node.next.data
    current_node.next = None
    return head, popped_element

# Testing the functions
head = None
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)
head = push(head, 4)
head = push(head, 5)


print("Linked List after pushes:")
print_linked_list(head)

head, popped_element = pop(head)
print("\nLinked List after pop:")
print_linked_list(head)
print("\nPopped element:", popped_element)

head, popped_element = pop(head)
print("\nLinked List after pop:")
print_linked_list(head)
print("\nPopped element:", popped_element)

head, popped_element = pop(head)
print("\nLinked List after pop:")
print_linked_list(head)
print("\nPopped element:", popped_element)

head, popped_element = pop(head)
print("\nLinked List after pop:")
print_linked_list(head)
print("\nPopped element:", popped_element)

head, popped_element = pop(head)
print("\nLinked List after pop:")
print_linked_list(head)
print("\nPopped element:", popped_element)

head, popped_element = pop(head)
print("\nLinked List after pop:")
print_linked_list(head)
print("\nPopped element:", popped_element)

head, popped_element = pop(head)
print("\nLinked List after pop:")
print_linked_list(head)
print("\nPopped element:", popped_element)
