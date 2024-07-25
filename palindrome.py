temp = n = int(input())
if(n < 0):
    print(False)
else:
    s = 0
    while(temp != 0):
        rem = temp % 10
        s = s * 10 + rem
        temp = temp//10
    if(n == s):
        print(True)
    else:
        print(False)
