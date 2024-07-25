"""88
def wish():
    print("Hi!")

a = int(input("Number 1 : "))
b = int(input("Number 2 : "))

def add(n1,n2):
    print("Addition of {},{} is {}".format(n1,n2,n1+n2))
add(a,b)


def evenOdd(n):
    if(n%2 == 0):
        print("Even")
    else:
        print("Odd")
num = int(input("Enter the number : "))
evenOdd(num)
"""

a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))

def printRange(a,b):
    for i in range(a,b+1):
        print(i,end = " ")

printRange(a,b)
