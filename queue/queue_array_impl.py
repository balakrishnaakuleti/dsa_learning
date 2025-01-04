
def push(queue,x):
    queue.append(x)
    return queue

def pop(queue):
    n = len(queue)
    if n == 0:
        return queue, -1
    else:
        return queue[1:n], queue[0]
    
queue = []
n = 5

for i in range(0,n):
    queue=push(queue,i)
    

print(queue)

while True:
    queue, element = pop(queue)
    if element == -1:
        print("queue is empty")
        break
    else:
        print(element)
        print(queue)
