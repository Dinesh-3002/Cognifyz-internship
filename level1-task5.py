# Palindrome Checker

a = input("Enter the value to check palindrome:")
b = a[::-1]
print(b)
if a == b:
    print("yes,it is a palindrome")
else:
    print("No,it is not a palindrome")
