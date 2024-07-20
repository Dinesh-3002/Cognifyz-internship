# Simple program to reverse a given string

def reversestring(a):
    return a[::-1]


a = str(input("Enter the string:"))
d = reversestring(a)
print(d)
