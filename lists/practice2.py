my_list = [1,2,3,4]

lenght = len(my_list)

print(-lenght)

for i in range(-1,-5,-1):
    print(my_list[i])

for i in range(3,-1,-1):
    print(my_list[i])

print(my_list[1:3])

print(my_list[-2])

my_list.append(5)

print(my_list)

my_list.insert(1,7)

print(my_list)


my_list2 = [6,7]

my_list.extend(my_list2)

print(my_list)

my_list = list(reversed(my_list))

print(my_list)

my_list.remove(7)

print(my_list)