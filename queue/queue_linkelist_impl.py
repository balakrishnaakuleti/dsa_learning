class Node:
    def __init__(self,data): 
        self.data = data
        self.next = None

def traverse(head):
    while head != None:
        print(head.data, end = " ")
        head = head.next
    print("")

def push(head,x):
    if head == None:
        node = Node(x)
    else:
        node = Node(x)
        node.next = head
    return node

def pop(head):
    if head is None:
        return head, -1
    next = head
    prev = None
    while True:
        # Check if current element is the last one
        if next.next is None:
            return prev, next.data
        prev = next
        next = next.next


N = 3
head = None

for i in range (N):
    head = push(head,i)

print("display queue")
traverse(head)

while True:
    head , popped_element = pop(head)
    if popped_element == -1:
        print("queue is empty")
        break
    print("popped element:",popped_element)
    print("queue:")
    traverse(head)