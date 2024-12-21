

def push(my_stack, element):
    my_stack.append(element)
    return my_stack


def pop(my_stack):
    N = len(my_stack)
    if N == 0:
        return my_stack, -1
    else:
        return my_stack[0:N-1], my_stack[N-1]

# Initialize an empty stack
my_stack = []

# Stack initial size
N = 5
print("Initial size of the stack:", N)

# Push elements to the stack
for i in range(N):
    my_stack = push(my_stack, i)
    print("Stack after adding element ",i," : ", my_stack)

# Pop elements to the stack as long as elements are present

while True:
    my_stack, poped_element = pop(my_stack)
    if poped_element == -1:
        print("Stack is empty.")
        break
    else:
        print("Poped element: ",poped_element)
        print("Stack after pop operation: ", my_stack)
