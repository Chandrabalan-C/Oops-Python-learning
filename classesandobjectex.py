"""
class goa:
    name = ""
    snacks = ""
    def party(self):
        print("Let's party!")
    def beach(self):
        print("Enjoy the beach!")

chan = goa()
bala = goa()

#chan.beach()
#bala.party()

chan.name = "Chandrabalan"
bala.name = "Balamurugan"

bala.drink = "No"
chan.drink = "No"

print(chan.name)
print(bala.name)
print("Drink : ",chan.drink)
print("Drink : ",bala.drink)


chan.beach()
bala.party()
"""

class laptop:
    price = 0
    processor = ""
    ram = ""

hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price = 32000
hp.processor = "Intel i3"
hp.ram = "4GB"

dell.price = 40000
dell.processor = "Ryzon 3000"
dell.ram  = "8GB"

lenovo.price = 50000
lenovo.processor = "Intel i9"
lenovo.ram = "16GB"

print(hp.price)
