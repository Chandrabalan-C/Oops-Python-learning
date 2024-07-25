num = int(input("Enter a Number : "))

if num > 1:
    for i in range(2,int(num/2)+1):
        if(i % 2 == 0):
            print("Not a Prime")
            break;
    else:
        print("Prime Number")
else:
    print("Not a Prime")
