for i in range(1,10,2):
    print(i)

a = []
for i in range(1,11):
    num = int(input("Enter Num{} : ".format(i)))
    a.append(num)
print(a)


sum = 0
for i in a:
    sum = sum+i
print(sum)
