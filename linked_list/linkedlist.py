class Node:
    def __init__(self,data): 
        self.data = data
        self.next = None

def traverse(head):
    while head != None:
        print(head.data)
        head = head.next

def identify_loop(head):
    detected = False
    visited_nodes = set()
    next = head
    while (next != None):
        if next in visited_nodes:
            detected = True
            break
        visited_nodes.add(next)
        next = next.next
    return detected

def delete_loop(head):
    visited_nodes = set()
    next = head
    while (next != None):
        if next.next in visited_nodes:
            #delete the loop by linking it to none
            next.next = None
            break
        visited_nodes.add(next)
        next = next.next



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node2

head = node1

print(identify_loop(head))

delete_loop(head)

traverse(head)