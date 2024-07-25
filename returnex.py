uName = "Chan"
uPasswrd = "2024"

userName = input("User name : ")
password = input("Password : ")

def check(userName,password):
    if(userName == uName and uPasswrd == password):
        return True
    else:
        return False

p = check(userName,password)
print(p)

