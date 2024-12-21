class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

def push(head:Node, value_to_push):
    node_to_push = Node(value_to_push)
    if head != None:
        node_to_push.next = head
    return node_to_push
    

# def push(head:LL, value_to_push):
#     node_to_push = LL(value_to_push)
#     # If linked list is empty, new node will be the head
#     if head is None:
#         return node_to_push
#     else:
#         next = head
#         while(next is not None):
#             # Identify if the is the last node.
#             if next.next is None:
#                 #Add new element after this node.
#                 next.next = node_to_push
#                 return head
#             else:
#                 next = next.next

def print_stack(head):
    next = head
    if next is None:
        print("Stack is empty")
        return
    while next != None:
        print(next.value, end=" ")
        next = next.next
    print("")

def pop(head):
    # Handle if head is None
    if head is None:
        return head, -1
    poped_element = head.value
    head = head.next
    return head, poped_element
    

# Initialize the head 
head = None
N=5
for i in range(N):
    print("Pushing the element:", i)
    head = push(head,i)
    print('Stack after push:')
    print_stack(head)
head, poped_element = pop(head)
while poped_element != -1:
    print("poped element:", poped_element)
    print("stack after pop")
    print_stack(head)
    head, poped_element = pop(head)

        