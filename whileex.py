"""
cnt = 1
while(cnt<=5):
    print(cnt, end=",")
    cnt = cnt+1

i = 10
while(i>0):
    print(i,end=" ")
    i = i-1
"""

i = int(input("Enter a Number : "))
fact = 1
while(i>0):
    fact = fact * i;
    i = i-1
print(fact)
