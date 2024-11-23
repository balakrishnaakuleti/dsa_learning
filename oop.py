#inheritance
class parent:
    def print_string_parent(self ,x:str):
        print("parent ",x)

class child(parent):
    def print_string_child(x:str):
        print("child ",x)

child = child()
#child.print_string_parent("hello")

class Animal:
    def print_animal_name(self):
        print("animal")

#polymorphism
class Dog(Animal):
    def print_animal_name(self):
        print("dog")

class Cat(Animal):
    def print_animal_name(self):
        print("cat")

dog = Dog()
cat = Cat()

#dog.print_animal_name()
#cat.print_animal_name()


#encapsulation
class BankAccount:
    balance = 2000
    def getbalance(self):
        return self.balance
    
bankaccount = BankAccount()
#print(bankaccount.getbalance())    

def sum(a,b):
    sum = a+b
    return sum

