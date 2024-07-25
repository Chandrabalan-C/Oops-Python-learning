"""mark = int(input("Enter Your Mark : "))
if(mark > 35):
    print("Pass!")
else:
    print("Fail!")


income = int(input("Income : "))
if(income < 7000):
    print("Eligible for Scholarship")
else:
    print("Not eligible for Scholarship")

a = int(input("Number : "))
if(a%3 == 0 and a%5 == 0):
    print("It is divisible by both 3 and 5")
else:
    print("It is not divisible by 3 and 5")

a = int(input("Num : "))
if(not a%2 == 0):
    print("Odd!")
else:
    print("Even!")

score = int(input("Mark out of 100 : "))
if(score > 70 and score <= 100):
    print("Good Student!")
elif(score > 35 and score < 70):
    print("Average Student!")
elif(score < 35 and score > 0):
    print("Poor Student!")
else:
    print("Invalid!")


a = int(input("Number 1 : "))
b = int(input("Number 2 : "))

com = input("Which operation you want to perform (Add/Sub/Mul/Div) : ")

if(com == 'Add'):
    print("Addition : ",a+b)
elif(com == 'Sub'):
    print("Subtraction : ",a-b)
elif(com == 'Mul'):
    print("Multiplication : ",a*b)
elif(com == 'Div'):
    print("Division : ",a/b)
else:
    print("Invalid!")

percent = int(input("Score Percentage : "))
if(percent >= 70):
    name = input("Name : ")
    depart = input("Department : ")
    location = input("Location : ")
    print("\nYou are eligible!")
else:
    print("You are Not eligible")


salary = int(input("Salary : "))
age = int(input("Age : "))

if(salary >= 20000 or age <= 25):
    loan = int(input("\nHow much loan amount you want : "))
    if(loan <= 50000):
        print("You are eligible for loan!")
    else:
        print("Maximum loan amount is 50000Rs")
else:
    print("You are not eligible for loan!")


a = int(input("Subject 1 mark : "))
b = int(input("Subject 2 mark : "))
c = int(input("Subject 3 mark : "))
d = int(input("Subject 4 mark : "))
e = int(input("Subject 5 mark : "))

avg = (a+b+c+d+e)/5;

if(avg < 35):
    print("Additional class is required!")
else:
    print("You are good to Go!")
"""
