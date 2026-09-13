from cryptography.fernet import Fernet

# make a key
key = Fernet.generate_key()

# give the key to the cipher
cipher_suite = Fernet(key)

userinput = input("do to want to decrypt 'd' or encrypt 'e' ")
if userinput == "e":
    text = input("enter the text to encrypt it: ").encode()
    cipher_text = cipher_suite.encrypt(text)
    print("this is the cipher text:>> " + cipher_text.decode())
    keywant = input("do you want the key: y or n: ")
    if keywant == "y":
        print(key.decode())
    else:
        pass
elif userinput == "d":
    cipher_text = input("enter the cipher text:>> ")
    key = input("enter the key: ")
    cipher_suite = Fernet(key.encode())
    text = cipher_suite.decrypt(cipher_text.encode())
    print("the text is :>> ", text.decode())
