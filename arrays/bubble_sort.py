arr = [4,2,7,3,1,5]

n = len(arr)

print(arr)
#ascedning
for i in range(0,n,):
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
    print("iteration number:",i+1)
    print(arr)
print(arr)

#desending
for i in range(0,n,):
    for j in range(0, n-i-1):
        if arr[j]<arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
    print("iteration number:",i+1)
    print(arr)
print(arr)
