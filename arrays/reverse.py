arr = [1,2,3,4,5]
rev_arr = []

n = len(arr)

for i in range(n-1,-1,-1):
    rev_arr.append(arr[i])

print(rev_arr)