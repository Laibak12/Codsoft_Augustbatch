import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character set selected for password generation")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")

    length = int(input("Enter desired password length: "))
    if length <= 0:
        print("Password length must be a positive integer.")
        return

    use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Use digits? (y/n): ").lower() == 'y'
    use_special = input("Use special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    password_generator()
