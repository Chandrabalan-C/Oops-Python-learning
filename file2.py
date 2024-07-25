
import sys
file = open("./file2.txt","a")

# for row in file:
#     print(row)
fname = []
def get():
    n = int(input("How many names you want to Enter : "))
    for i in range(n):
        nm = input(f"Name {i} : ")
        file.write(nm)
    sys.exit(0)


get()
file.close()