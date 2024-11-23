from oop import sum
from error_handling import withdraw_amount, LowBalanceException

y=sum(10,12)
print(y)

my_array=[2,3,9,22,134,4,11,13]
x = 2
index = 0
item_found = False

for item in my_array:
    if x == my_array[index]:
        print("Item found!!!")
        print("@index", index)
        item_found = True
        break
    else:
        index = index + 1
if item_found == False:
    print("item not found")

if x>0:
    print("postive integer")
elif x<0:
    print("negative integer")
else:
    print("number is zero")

while (x>index):
    index=index+1
    print(index)

try:
    a = 1
    b=0
    a=a/b
except ZeroDivisionError:
    print("Zero division found correct it")
    a=0
    a=a/a
except Exception:
    print("exception found")
finally:
    print("code is working")

print("last line of the program")
