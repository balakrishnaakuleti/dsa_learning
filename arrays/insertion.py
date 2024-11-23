arr=[1,2,3,4,5]
elemtent_to_insert=7
pos=0

n = len(arr)

arr_left=[]
arr_right=[]

for i in range(0, pos):
    arr_left.append(arr[i])
print(arr_left)

for i in range(pos,n):
    arr_right.append(arr[i])
print(arr_right)

arr_final= arr_left + [elemtent_to_insert] + arr_right
print(arr_final)

