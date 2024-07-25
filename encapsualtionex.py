class company():
    def __init__(self):
        self.__companyName = "Google"    #(__) - Private variable(instance)
        #(_) - protected variable

    def companyName(self):
        print(self.__companyName)  # Function in public but variable in private

c1 = company()
c1.companyName()
#print(c1.__companyName) - Error

# (__)private variable cannot be viewed in out of class
# (_)protected variable it can be viewed in the inheritance classes
