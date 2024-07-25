lst = []
n = int(input("Enter number of elements : "))
for i in range(n):
    inp = int(input())
    lst.append(inp)

tar = int(input("Target : "))
output = []
for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j] == tar:
            output.append([i,j])
            break

print("Output : ",output)
