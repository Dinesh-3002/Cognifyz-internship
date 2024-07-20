# Program to create a Fibonacci sequence

# Defining a function as fibonacci_num()
def fibonacci_num():
    # Creating a variable which holds the input of the user
    num = int(input("Enter a number:"))
    # Creating two variables a and b which holds the initial values of the fibonacci sequence
    a = 0
    b = 1
    # Checks if the given input is equal to 1
    if num == 1:
        # If it is true then print the value of only a
        print(a)
    # Checks if the given input is equal to 2
    elif num == 2:
        # If it is true then print the value of both a and b
        print(a)
        print(b)
    # Checks if the given input is greater than or equal to 0
    elif num <= 0:
        # If it is true the print the below statements
        print("Enter a valid number!")
    else:
        print(a)
        print(b)
        # Iterating through the values between 2 and the given input by the user
        for i in range(2, num):
            c = (a+b)
            print(c)
            a = b
            b = c

fibonacci_num()
