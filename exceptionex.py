
"""
Compile Error - occurs due to syntax
Logical Error - Occurs due to logical(our side)
RunTime Error - Occurs during runTime (Giving wrong data type in the input) (our side)
"""

"""
try:
    a = int(input())
    b = int(input())
    print(a+b)
    
except Exception as e:     #Exception - occured error
    print("Something",e)

finally:
    print("something")
"""

try:
    a = int(input())
    b = input()
    #print(b/a)
    #print(d)
    
except ValueError as e:
    print("Value Error : ",e)

except TypeError as e:
    print("Type Error : ",e)

except Exception:
    print("Something Wrong")

finally:
    print("Done!")

