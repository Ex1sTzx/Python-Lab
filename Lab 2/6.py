def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter a number: "))

print("Factorial of", num, "is", fact(num))