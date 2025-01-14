password = input("PLease enter a password: ")
encryptedpassword=""
key = int(input("Please enter a key: "))

for each in password:
    encryptedpassword += chr(ord(each)+key)

print(encryptedpassword)
