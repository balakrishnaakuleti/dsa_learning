arr = [5,1,2,3,5]

n=len(arr)

count_dict={}
print(count_dict)
for i in range(0,n):
    current_element= arr[i]
    if current_element in count_dict:
        count_dict[current_element] = count_dict[current_element] + 1
    else:
        count_dict[current_element] = 1
    print("iteration: ",i+1)
    print(count_dict)

print(count_dict)

for k,v in count_dict.items():
    if v > 1:
        print("Duplicate element: ",k)
        break
if  v==1:
    print("no duplicate element")