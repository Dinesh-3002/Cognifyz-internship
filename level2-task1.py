# Program to create a simple guessing game

import numpy as np
import warnings

# Suppress DeprecationWarnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
secret_no = int(np.random.randint(1, 100, 1))


def guess_number():
    user_no = 0
    while user_no != secret_no:
        user_no = int(input("Enter the number:"))
        if user_no == secret_no:
            print("CONGRATS,You won!!")
        elif user_no < secret_no:
            print("The number is too low!,try another number")
        elif user_no > secret_no:
            print("The number is too high!,try another number")
        else:
            print("Try again!")
    return user_no


guess_number()
print("the secret_no is:", secret_no)
