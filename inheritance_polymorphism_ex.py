"""
class Shape():
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 20
        print(l*b)

#s1 = Shape()
#print(s1.area())

r1 = Rectangle()
r1.area()
"""

"""
class Person():
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
        #print(grade)
        
    def display(self):
        print(self.name,self.grade)

s1 = Student("Alwin","A")
s1.display()
"""
"""
class vehicle():
    def start(self):
        print("Vehicle started")

class car(vehicle):
    def start(self):
        print("car started")

c1 = car()
c1.start()
"""

class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
        
    def display(self):
        print("name : ",self.name)
        print("salary : ",self.salary)
        print("Department : ",self.department)

m1 = Manager("chan",1200000,"ECE")
m1.display()
