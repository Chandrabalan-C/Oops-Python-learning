"""
def add(a=10):
    print(a)
add(50)

def addition(a,b,c = 0):
    print(a+b+c)
    
addition(1,5)
addition(4,2,6)
"""

"""

Polymorphism - The same function name (but different signature) being used for different types.
The key difference is the data types and number of arguments used in function.

The function will change itself based on the activity that is called polymorphism.
"""

#Method overriding - polymorphism
class Animal():
    def sound(self):
        print("Animal makes sound")
        
class Dog(Animal):
    def sound(self):      # overriding sound()
        print("Dog Barks")

class Bird(Animal):
    def sound(self):
        print("Birds sing")  # overriding sound()

d1 = Dog()
d1.sound()

b1 = Bird()
b1.sound()
