import hashlib
import os

def crack(hashed_pass, filepath):
    try:
        with open(filepath, 'r', encoding='latin-1') as file:
            for line in file:
                password = line.strip()
                if hashlib.sha256(password.encode()).hexdigest() == hashed_pass:
                    return f"Password cracked:  {password}"
        return "Password not found!!"
    except FileNotFoundError:
        return f"Error: The File '{filepath}' Not Found"
    except UnicodeDecodeError:
        return f"Encoding error while reading '{filepath}'. Try a different encoding."

hashed_password = input("Enter the Hashed Password!: ")

# password file path
filename = 'rockyou.txt'
# Get the current script's directory
current_directory = os.path.dirname(__file__)

# Construct the full path to the text file
password_file = os.path.join(current_directory, filename)

# Run the cracker
result = crack(hashed_password, password_file)
print(result)

