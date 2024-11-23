arr = [1,2,3,4,5]
x = 6

n = len(arr)

x = x % n

arr_spill=[]
arr_residual=[]

for i in range(0, x,1):
    arr_spill.append(arr[i])
print(arr_spill)

for i in range(x, n):
    arr_residual.append(arr[i])
print(arr_residual) 

arr_final = arr_residual + arr_spill
print(arr_final)