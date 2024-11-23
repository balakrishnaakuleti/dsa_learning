import array

my_arr = array.array('i',[ 1, 3, 3, 2,3,5,6,7,8,7,8,9,6,5,3,4,2,1])

n = len(my_arr)

numdict = {}

for i in range (0,n):
    current_element = my_arr[i]
    if current_element in numdict:
        numdict[current_element] = numdict[current_element] + 1
    else:
        numdict[current_element] = 1
number_of_iterations= 0
is_item_found= False
for k,v in numdict.items():
    number_of_iterations+=1
    if v > n/2:
        print("Majority element:", k)
        is_item_found=True
        break

if(is_item_found is False):
    print("-1")
print(number_of_iterations)


