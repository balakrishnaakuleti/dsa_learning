arr=[1,2,3,4,5]

index_to_delete = 2

n = len(arr)

arr_final=[]

for i in range(0,n):
    if not i==index_to_delete:
        arr_final.append(arr[i])

print(arr_final)

print("element deleted at index",index_to_delete,"is",arr[index_to_delete])