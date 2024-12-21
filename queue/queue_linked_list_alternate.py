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
    if head is not None:
        node_to_push.next=head
    return node_to_push

def pop(head):
    if head is None:
        return None, -1
    current = head
    previous = None
    while True:
        if current.next is None:
            if previous is None:
                return None, current.value
            previous.next = None
            return head, current.value
        previous = current
        current = current.next


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