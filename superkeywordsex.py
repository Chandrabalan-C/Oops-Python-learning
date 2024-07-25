"""
class a():
    def __init__(self):
        print("A")
        
    def display(self):
        print("you are in class a")

class b():
    def __init__(self):
        super().__init__()
        print("B")
        
    def display(self):
        print("You are in class b")

class c(a,b):                # left will be taken hence (a) will be taken here.
    def __init__(self):
        super().__init__()
        print("C")
        
    def display(self):
        print("You are in class c")


obj1 =  c()

"""

class H():
    def __init__(self):
        print("H")
        
    def disp(self):
        print("Ur in H")
class I():
    def __init__(self):
        super().__init__()
        print("I")
        
    def disp(self):
        print("Ur in I")
class J(H,I):
    def __init__(self):
        super().__init__()
        print("J")
        
    def disp(self):
        print()

obj = J()
