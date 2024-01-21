
import random
import string

#Function to generate a random password between 8 and 16 characters long
def generate_password():
    length = random.randint(16, 32)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#Function to print the generated password
def print_password(password):
    print('Generated Password:', password)

#Start the function and call it
print_password(generate_password())