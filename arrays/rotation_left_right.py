arr = [1,2,3,4,5]
x = 8

n = len(arr)

x = x % n

arr_spill=[]
arr_residual=[]

for i in range(0,n-x):
    arr_residual.append(arr[i])
print(arr_residual)

for i in range(n-x,n):
    arr_spill.append(arr[i])
print(arr_spill)

arr_final = arr_spill + arr_residual
print(arr_final)

