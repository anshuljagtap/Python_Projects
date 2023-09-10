# Author: Anshul Jagtap
# Project Name: Password Generator 
# Description: Generates a secure password using secret module for a user depending on the specifications
# Concepts: string module, secrets module, functions, methods, String formating, For loop, if-else.

import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char in password:
            if char.isupper():
                return True
    
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
                return True
    
    return False

def generate_password(lenght: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase
    
    combination_length = len(combination)
    new_password: str = ''

    for i in range(lenght):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == '__main__':
    for a in range(1,6):
        new_pass: str = generate_password(lenght=13, symbols= True, uppercase= True)
        specifications: str = f'Uppercase:{contains_upper(new_pass)}, Special char: {contains_symbols(new_pass)}'
        print(f'{a} -> {new_pass} ({specifications})')

    