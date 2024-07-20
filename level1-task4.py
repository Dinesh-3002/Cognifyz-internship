# Simple Calculator Program

a = int(input("Enter 1st number:"))
b = input("Enter the operator(+,-,*,/):")
c = int(input("Enter 2nd number:"))

if b == "+":
    result = a + c
    print(round(result, 2))
elif b == "-":
    result = a - c
    print(round(result, 2))
elif b == "*":
    result = a * c
    print(round(result, 2))
elif b == "/":
    result = a / c
    print(round(result, 2))
else:
    print("invalid entry")
