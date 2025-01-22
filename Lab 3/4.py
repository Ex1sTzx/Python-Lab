num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2:
    print("Equal numbers:", num1)
elif num1 == num3:
    print("Equal numbers:", num1)
elif num2 == num3:
    print("Equal numbers:", num2)
else:
    print("No two numbers are equal.")