 from typing import List

class Node:
    def __init__(self,value, priority):
        self.value = value
        self.priority = priority

def traverse_pq(pq:List[Node]):
    output = "[ "
    for node in pq:
        output = output + str(node.value)+ " : "+ str(node.priority)+", "
    output = output + " ]"
    print(output)

def enq(pq, value, priority):
    new_node = Node(value, priority)
    N = len(pq)
    # Case 1 when q is empty
    if N is 0:
        pq.append(new_node)
    # Case 2 when the priority is greater than first element priority
    elif priority > pq[0].priority:
        pq = [new_node]+pq
    # Case 3 when the priority is equal to or less than the priority of first element
    else:
        for i in range(N):
            if pq[i].priority < priority:
                pq = pq[0:i]+[new_node]+pq[i:N]
                break
        # If element is not inserted then it has to be inserted at the end
        if len(pq) == N:
            pq = pq+ [new_node]
    return pq

def dq(pq):
    N = len(pq)
    if N == 0:
        return [], None
    elif N == 1:
        return [],pq[0].value
    return pq[1:N], pq[0].value

pq = []
print("Priority Queue initialized")

print(" Insert 4 4")
pq=enq(pq,"4",4)
traverse_pq(pq)


print(" Insert 3 3")
pq=enq(pq,"3",3)
traverse_pq(pq)


print(" Insert 2 2")
pq=enq(pq,"2",2)
traverse_pq(pq)

print(" Insert 6 6")
pq=enq(pq,"6",6)
traverse_pq(pq)


print(" Insert 5 5")
pq=enq(pq,"5",5)
traverse_pq(pq)

print("Pop element.")
pq, poped_element = dq(pq)
print("Poped element: ",poped_element)
traverse_pq(pq)


print("Pop element.")
pq, poped_element = dq(pq)
print("Poped element: ",poped_element)
traverse_pq(pq)

print("Pop element.")
pq, poped_element = dq(pq)
print("Poped element: ",poped_element)
traverse_pq(pq)


print("Pop element.")
pq, poped_element = dq(pq)
print("Poped element: ",poped_element)
traverse_pq(pq)


print("Pop element.")
pq, poped_element = dq(pq)
print("Poped element: ",poped_element)
traverse_pq(pq)



