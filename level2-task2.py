# Program to create a  simple Number guesser
import random
import warnings


# Suppress DeprecationWarnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
Name = input("HI USER,WHAT'S YOUR NAME:")
secret_no = random.randint(1, 10)
print(f"HI {Name},Lets begin the game!!")


def guess_number():
    user_no = 0
    while user_no!= secret_no:
        user_no = int(input("Guess a number between 1-100:"))
        if user_no == secret_no:
            print(f"CONGRATS,You won {Name}!!")
        elif user_no < secret_no:
            print(f"The number is too low!,try another number {Name}")
        elif user_no > secret_no:
            print(f"The number is too high!,try another number {Name}")
        else:
            print("Try again with another number!!")
    return user_no

guess_number()
print("the secret_no is:", secret_no)
