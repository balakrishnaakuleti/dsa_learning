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
    else:
        x = head.data
        return head.next , x
    
N = 7
head = None

for i in range (N):
    head = push(head,i)

print("display stack")
traverse(head)

while True:
    head, popped_value = pop(head)
    if popped_value == -1:
        print("No elements to pop")
        break
    else:
        print("popped element:",popped_value)
        traverse(head)