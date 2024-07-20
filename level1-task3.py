# Program For E-mail Validator

import re


def validemail():
    pattern = r'\b[a-z0-9._%+-]+@[a-z]{5}+\.[a-z]{2,3}\b'
    email_id = input("Enter your email_id:")
    if re.search(pattern, email_id):
        print("email is valid")
    else:
        print("email is invalid")


validemail()
