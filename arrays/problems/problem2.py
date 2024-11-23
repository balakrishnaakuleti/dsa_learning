arr = [7,5,4,3,2,1,6,5,4,3,2,1,1]

unique_set=set()

for element in arr:
    unique_set.add(element)
print(unique_set)

arr = list(unique_set)


arr=[7,6,5,4,3,2,1]
n=len(arr)
print(arr)
k=1

for i in range(0,k):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
print(arr)

print(k,"th biggest element is :",arr[n-k])


