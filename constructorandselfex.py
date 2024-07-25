"""
class laptop:
    #constructor
    def __init__(self):
        self.ram = ""
        self.processor = ""
    def display(self):
        print("RAM : ",self.ram)
        print("Processor : ",self.processor)

hp = laptop()
hp.ram = "16GB"
hp.processor = "i5"

#print(hp.ram)
hp.display()
"""

class Amazon:
    def __init__(self):
        self.ram = ""
        self.price = 0
        self.company = ""
    def display(self):
        print("Company : {}".format(self.company))
        print("Price   : {}".format(self.price))
        print("RAM     : {}".format(self.ram))

mobile = Amazon()
laptop = Amazon()

mobile.ram = "4GB"
mobile.price = 15000
mobile.company = "Vivo"

laptop.company = "Asus Vivobook"
laptop.price = 45000
laptop.ram = "16GB"

mobile.display()
print()
laptop.display()
