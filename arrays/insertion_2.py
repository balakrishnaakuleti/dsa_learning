arr=[1,2,3,4,5]
elemtent_to_insert=7

n = len(arr)

pos = n

arr_final=[]

for i in range(0,n):
    if i == pos:
        arr_final.append(elemtent_to_insert)
    arr_final.append(arr[i])
    if pos == n  and i == n-1:
        arr_final.append(elemtent_to_insert)
print(arr_final)
