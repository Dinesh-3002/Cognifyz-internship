# Program to create a password strength checker
# strong password - ex:Dinesh_dk{SABI}2993VARSHU

import string

password = input('Enter the password (must contain uppercase,lowercase,special,digits):')


upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])


characters = [upper_case, lower_case, special, digits]
length = len(password)
strength = 0


with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print('Password was found in common list. strength :0')
    exit()


if length > 5:
    strength += 1
if length > 8:
    strength += 1
if length > 12:
    strength += 1
if length > 17:
    strength += 1
if length > 20:
    strength += 1
print(f"Password length is {str(length)}, adding {str(strength)} points!")

if sum(characters) > 1:
    strength += 1
if sum(characters) > 2:
    strength += 1
if sum(characters) > 3:
    strength += 1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters))} points!")

if strength < 4:
    print(f"the password is too weak! score: {str(strength)} ")
elif strength == 5:
    print(f"the password is ok ! score:{str(strength)}")
elif 5 < strength <= 6:
    print(f"the password is pretty good! score:{str(strength)}")
elif strength > 6:
    print(f"the password is strong! strength:{str(strength)}")
