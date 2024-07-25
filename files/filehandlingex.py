f = open("fruits.txt","w")
#content = f.read()
#print(content)

f.write("Banana")
f.write("\nMango")

f.close()

f = open("fruits.txt","r+")
print(f.read())
print(f.readline())
f.close()

"""
w - write
a - append
r - read
r+ - read and write
"""
