"""
# Inheritance
class dad():
    def phone(self):
        print("Dad's phone")
        
class mom():
    def sweet(self):
        print("Mom's Sweet")
        
class son(dad,mom):                # Multiple Inheritance 
    def laptop(self):
        print("Son's Laptop")

sham = son()
sham.phone()
sham.sweet()

"""
"""
# multi level inheritance
class grandpa():
    def phone(self):
        print("grandpa's phone")

class dad(grandpa):
    def money(self):
        print("dad's money")

class son(dad):
    def laptop(self):
        print("son's laptop")


shan = son()
shan.laptop()
shan.money()
shan.phone()
print()
appa = dad()
appa.phone()
"""

"""
#hierarchical inheritance

class dad():
    def money(self):
        print("Dad's money")

class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

child = son2()
child.money()
"""


#Hybrid Inheritance = mixing of all inheritance
class dad():
    def money(self):
        print("Dad's money")
class land():
    def important(self):
        print("Important land")

class son1(dad,land):            # multiple inheritance
    pass

class son2(dad):
    pass

class son3(dad):
    pass

child = son1()
child.money()
child.important()
