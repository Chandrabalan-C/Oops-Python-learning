class phone:
    chargerType = "C-Type"    # class variable
    def __init__(self,brand,price):
        self.brand = brand     # instance variable
        self.price = price
        #self.chargerType = chargerType
    def display(self):
        print("Brand : ",self.brand)
        print("Price : ",self.price)
        print("ChargerType : ",self.chargerType)

#samsung = phone("Samsung",15000,"C-Type")
#samsung.display()

#phone.chargerType = "B-Type" -> If we want to change the chargertype for whole prgrm we can.
                    
vivo = phone("Vivo",15000)
vivo.display()
print()
redmi = phone("MI",15000)
redmi.display()

"""
Instance variable - It will change for every object
class variable - It will not change for every object
"""
