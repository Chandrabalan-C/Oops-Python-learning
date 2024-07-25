class laptop:
    chargerType = "C-Type"
    def __init__(self):
        self.brand = ""
        self.price = 100
                                            # Instance method
    def setPrice(self,price):
        self.price = price
        
    def getPrice(self):
        print(self.price)

    @classmethod
    def changeChargerType(cls):             # Class method
        cls.chargerType = "B-Type"
        print("Charger type changed")

    @staticmethod
    def info():                             # Static method
        print("Static method")

hp = laptop()
hp.setPrice(40000)
hp.getPrice()

#laptop.changeChargerType(laptop)
laptop.changeChargerType()  # Due to @classmethod

hp.info()
