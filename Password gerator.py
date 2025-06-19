import random
import string

# Function to generate password

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

# Characters to choose from

    all_chars = string.ascii_letters + string.digits + string.punctuation

# Ensure at least one from each type

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

# Fill the rest of the password

    password += random.choices(all_chars, k=length - 4)

 # Shuffle to prevent predictable pattern
 
    random.shuffle(password)

    return ''.join(password)

# Take input from user

length = int(input("Enter desired password length: "))
print("Generated password:", generate_password(length))
