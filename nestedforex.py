"""
for i in range(1,6):
    for j in range(1,3):
        print(j,"Hi!")



for i in range(1,3):
    print("Week: ",i)
    for j in range(1,4):
        print(" Day: ",j)
    print(".... .. ....")
"""

for i in range(1,5):
    for i in range(1,i+1):
        print("*",end = "")
    print("\n")
