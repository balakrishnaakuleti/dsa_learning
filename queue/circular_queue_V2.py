MAX_SIZE = 4
front = -1
rear = -1

circular_queue = [None]*MAX_SIZE

def enqueue(value):
    global front
    global rear
    global MAX_SIZE
    if (front == 0 and rear == MAX_SIZE -1 or rear + 1 == front):
        print("queue is full")
        return
    if(front == -1):
        front = rear = 0
    elif(rear == MAX_SIZE - 1):
        rear = 0
    else:
        rear = rear + 1
    
    circular_queue[rear] = value

def dequeue():
    global front
    global rear
    global MAX_SIZE
    if(front == -1):
        print("underflow")
        return
    value = circular_queue[front]
    circular_queue[front]= None
    if (front == rear):
        front = rear = -1
    elif(front == MAX_SIZE-1):
        front = 0
    else:
        front = front + 1
    return value


print(circular_queue)
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
print(circular_queue)
print(dequeue())
print(circular_queue)
enqueue(5)
print(circular_queue)
print(dequeue())
print(circular_queue)
print(dequeue())
print(circular_queue)
print(dequeue())
print(circular_queue)
print(dequeue())
print(circular_queue)
enqueue(1)
print(circular_queue)