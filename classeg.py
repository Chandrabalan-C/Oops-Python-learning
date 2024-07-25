"""
class student:
    def __init__(self):
        self.name = "name"
        self.regNo = "4211"
    def display(self):
        print("Name : {}".format(self.name))
        print("Reg No : {}".format(self.regNo))

s1 = student()
s2 = student()

s1.name = "Chan"
s1.regNo = "421121104015"

s2.name = "Alwin"
s2.regNo = "421121104004"


# Display details

s1.display()
print()
s2.display()


class Fruit:
    def __init__(self,col):
        self.color = col
        
apple = Fruit("Red")
#apple.color = "Red"
print(apple.color)



class Teachers:
    def __init__(self,n,r):
        self.name = n
        self.regNo = r
    def display(self):
        print("Name : {} \nReg No : {}".format(self.name,self.regNo))

t1 = Teachers("Palani","421121104015")
t2 = Teachers("Matilda","421121104016")

t1.display()
print()
t2.display()
"""

class Calci:
    #def __init__(self,a,b):
        #self.num1 = a
        #self.num2 = b
    def add(self,num1,num2):
        print("Add : ",num1+num2)
    def sub(self,num1,num2):
        print("Sub : ",num1-num2)

a = int(input("Enter a number : "))
b = int(input("Enter a Number : "))

addition = Calci()
addition.add(a,b)

subtraction = Calci()
subtraction.sub(a,b)
























