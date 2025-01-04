class Cqueue:
    def __init__(self,capacity):
        self.cqueue = [None]*capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = 0
    def getFront(self):
        return self.front
    def getRear(self):
        return self.rear
    def enq(self,value):
        # Handle when queue is full
        if self.size == self.capacity:
            print("Queue is full !!!")
            return
        # Handle when queue is empty
        elif self.size == 0:
            self.front=0
            self.rear=0
            self.cqueue[0]=value
        else:
            # If rear is the last element
            if self.rear == self.capacity-1:
                self.cqueue[0] = value
                self.rear=0
            else:
                # Rear is not last element
                self.rear+=1
                self.cqueue[self.rear]=value
        self.size+=1
        return
    def dq(self):
        element=None
        # Handle When is empty
        if self.size == 0:
            print(" Queue is empty boss !!!")
        # Only one element. Dequeue the element and reset front and rear to 0
        elif self.size == 1:
            element = self.cqueue[self.front]
            self.cqueue[self.front]=None
            self.front=0
            self.rear=0
        else:
            element = self.cqueue[self.front]
            self.cqueue[self.front]=None
            # if front is the last element
            if self.front == self.capacity-1:
                self.front=0
            else:
                self.front+=1
                
        self.size-=1
        return element
    def print_queue(self):
        print("")
        for element in self.cqueue:
            print("",element, end="")
        print("")
        self.print_state()
    def print_state(self):
        print("size: ",self.size)
        print("Front: ",self.front)
        print("rear: ",self.rear)


# Queue Init
N=4
my_circular_queue = Cqueue(N)

# Enqueue Operations
my_circular_queue.enq(1)
my_circular_queue.print_queue()

my_circular_queue.enq(2)
my_circular_queue.print_queue()

my_circular_queue.enq(3)
my_circular_queue.print_queue()

my_circular_queue.enq(4)
my_circular_queue.print_queue()

# Dequeue Operations

print("Removed: ",my_circular_queue.dq())
my_circular_queue.print_queue()

# Enqueue Operation
my_circular_queue.enq(5)
my_circular_queue.print_queue()


# Dequeue Operations
print("Removed: ",my_circular_queue.dq())
my_circular_queue.print_queue()

print("Removed: ",my_circular_queue.dq())
my_circular_queue.print_queue()

print("Removed: ",my_circular_queue.dq())
my_circular_queue.print_queue()

my_circular_queue.print_state()
print("Removed: ",my_circular_queue.dq())
my_circular_queue.print_queue()

# Enqueue Operation
my_circular_queue.enq(6)
my_circular_queue.print_queue()
