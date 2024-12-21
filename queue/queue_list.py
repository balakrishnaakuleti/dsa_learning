
def push(queue, element_to_push):
    queue.append(element_to_push)
    return queue
def pop(queue):
    N = len(queue)
    if N is 0:
        return queue, -1
    else:
        return queue[1:N], queue[0]

queue = []
print("Queue initialized")
print(queue)
N=5
for i in range(N):
    print("Pushing element to queue: ",i)
    queue = push(queue,i)
    print("Queue after adding elemenent: ",queue)

while True:
    queue, poped_element = pop(queue)
    if poped_element == -1:
        print("No elements to pop. Reached EOQ.")
        break
    print("Poped element: ",poped_element)
    print("Queue after pop: ", queue)