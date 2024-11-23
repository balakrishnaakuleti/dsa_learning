from array import array 

my_array = array(1, 2, 3, 4, 5,6,7,8,9)

#Searching, 


#Sorting, 
#Inserting, 
insert_place_index=3
element_to_insert=9
my_array2=[]

for i in range(len(my_array)):
    if i== insert_place_index:
        my_array2.append(element_to_insert)    
    my_array2.append(my_array[i])

print(my_array2)


# def reversearray(arr):
#    n = len(arr)
#    temp = [0] * n

#    if i in range(n):
#        temp[i] = arr[n-i-1]

def reversearray2(arr):
    n = len(arr)
    temp = []

    for i in range(n-1,-1,-1):
        print(i)
        print(arr[i])
        temp.append(arr[i])

    return temp

a = reversearray2(my_array)

print(a)

def delete_element(arr,element):
    n = len(arr)
    temp = []

    for i in range(0,n,1):
        if element != arr[i]:
            temp.append(arr[i])
    
    return temp

new_array_after_delete = delete_element(my_array,5)

print(new_array_after_delete)

#reversing and deletion must be done