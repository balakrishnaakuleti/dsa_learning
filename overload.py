class Addition:
    def sum(self,a:int,b:int,c=0):
        return a+b+c

    
addition = Addition()
print(addition.sum(2,3))
print(addition.sum(2,3,4))