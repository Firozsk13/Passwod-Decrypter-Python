import hashlib

def hash_password(password):
    hashed_pass=hashlib.sha256(password.encode()).hexdigest()
    return hashed_pass

# Example
# password="my_pass"
password=input("Enter the password!")
hashed_pass=hash_password(password)
print("Hashed Password: " ,hashed_pass)