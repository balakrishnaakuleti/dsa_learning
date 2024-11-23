myset = {5,1,2,3,4}

print("set original:",myset)

myset.add(6)
print("element added:",myset)

myset.remove(5)
print("element removed",myset)

print("minimum value element",min(myset))

print("maximum value element",max(myset))

print("lenght of set:",len(myset))


a = {1,2}
b = {2,3}
union_set = a|b
intersection_set = a&b
print(union_set)
print(intersection_set)