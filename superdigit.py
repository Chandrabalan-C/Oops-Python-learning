n = input("Enter a Number : "))
k = int(input("Enter the Value : "))

def Sum(n):
    if(len(n) == 1):
        return int(n);
    s = 0
    for i in n:
        s += int(i)
    return Sum(str(s))

temp = Sum(n)*k
if(temp > 9):
    temp = Sum(str(temp))
print(temp)
