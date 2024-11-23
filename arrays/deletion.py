arr=[1,2,3,4,5]

index_to_delete = 6

n = len(arr)

arr_left=[]
arr_right=[]

for i in range(0,index_to_delete):
    arr_left.append(arr[i])
print(arr_left)

for i in range(index_to_delete+1,n):
    arr_right.append(arr[i])
print(arr_right)

arr_final = arr_left + arr_right
print(arr_final)

print("element deleted at index",index_to_delete,"is",arr[index_to_delete])