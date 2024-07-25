def fib(n):
    result = []
    a,b = 0,1

    while b < n:
        result.append(b)
        a,b = b,a+b
    return result

val = int(input("Enter a Number : "))

print(fib(val))
print(sum(fib(val)))