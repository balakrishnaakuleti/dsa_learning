arr = [5,5,6,2,3,4]

n = len(arr)

count_dict={}

for i in range(0,n):
    current_element = arr[i]
    if current_element in count_dict:
        count_dict[current_element] = count_dict[current_element] + 1
    else:
        count_dict[current_element] = 1

print(count_dict)

for key,value in count_dict.items():
    if value > 1:
        print("repeated element:",key)

for i in range(1,n+1):
    if not i in arr:
        print("missing element:",i)
         
