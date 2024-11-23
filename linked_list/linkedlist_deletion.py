class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data)
        current_node = current_node.next

def deletion(head,value_to_be_deleted):
    #if element to be deleted is the first one
    if head.data == value_to_be_deleted:
        head = head.next
        return head
    current_node = head
    #Traverse the array to the value that has to be deleted
    while value_to_be_deleted != current_node.next.data:
        current_node = current_node.next
        #if next element is the last element and data is not found
        if current_node.next.next is None:
            print("Value not found in the list")
            return head
    current_node.next = current_node.next.next
    return head

    










# Test code
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = node1
value_to_be_deleted = 4

head=deletion(head,value_to_be_deleted)
print_linked_list(head)