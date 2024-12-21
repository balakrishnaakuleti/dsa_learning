class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_queue(head):
    print("")
    while head != None:
        print(head.value, end=" ")
        head = head.next
    print("")

def push(head, value_to_push):
    node_to_push = Node(value_to_push)
    if head is None:
        return node_to_push
    else:
        next = head
        prev = None
        while next is not None:
            prev = next
            next = next.next
        prev.next = node_to_push
    return head

def pop(head):
    if head is None:
        return head, -1
    return head.next, head.value

head= None
N=5
for i in range(N):
    print("Pushing to queue : ", i)
    head = push(head,i)
    print("Queue after pushing: ")
    print_queue(head)

while True:
    head, poped_element = pop(head)
    if poped_element == -1:
        print("Queue is empty !!!")
        break
    print("Poped element: ",poped_element)
    print("Queue after pop operation:")
    print_queue(head)