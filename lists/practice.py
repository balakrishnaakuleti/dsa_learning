my_list = [1,2,"hello",4,5]

print(my_list)

x = len(my_list)

print(x)

print(my_list[2])

for i in range (0,x):
    print(my_list[i])

for element in my_list:
    print(element)

my_list_2 = [1,2,3,["hello",['a','b',"c"]],4,5,6]

print(my_list_2[3][1][2])

print(my_list[-2])