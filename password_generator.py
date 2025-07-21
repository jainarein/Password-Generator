import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# ---- User Inputs ----
print("=== Password Generator ===")
length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'


generated_password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
print(f"\nGenerated Password: {generated_password}")
