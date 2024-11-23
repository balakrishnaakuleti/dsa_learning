import array
arr = array.array('i',[2,4,1,3,5])

n = len(arr)

count = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            count+=1
print(count)