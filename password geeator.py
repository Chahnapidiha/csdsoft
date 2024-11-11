# password_generator.py

import random
import string

def generate_password(length):
    # Define the character sets to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the character sets
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Input the desired password length
    length = int(input("Enter the desired length for the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

