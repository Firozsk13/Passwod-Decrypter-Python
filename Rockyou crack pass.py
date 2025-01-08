import hashlib
import os

def crack(hashed_pass, password_list):
    for password in password_list:
        if hashlib.sha256(password.encode()).hexdigest()==  hashed_pass:
            return f"Password cracked:  {password}"
    return "Password not found!!"


# Reading the password list file
def read_password_list(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: The File '{filepath}' Not Found")
        return []

hashed_password = input("Enter the Hashed Password!: ")

#password file path
filename = 'rockyou.txt'
# Get the current script's directory
current_directory = os.path.dirname(__file__)

# Construct the full path to the text file
password_file = os.path.join(current_directory, filename)
passwords = read_password_list(password_file)


#Running condition
if passwords:
    result = crack(hashed_password, passwords)
    print(result)
else:
    print("No password check!")

