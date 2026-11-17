from cryptography.fernet import Fernet


def aes(choice):
    # make a key
    key = Fernet.generate_key()
    # give the key to the cipher
    cipher_suite = Fernet(key)
    if choice == "e":
        text = input("enter the text to encrypt it: ").encode()
        cipher_text = cipher_suite.encrypt(text)
        keywant = input("do you want the key: y or n: ")
        if keywant == "y":
            return f"key:>> {key.decode()} cipher text :>> {cipher_text.decode()}"
        else:
            return cipher_text.decode()
    elif choice == "d":
        cipher_text = input("enter the cipher text :>> ")
        key = input("enter the key: ")
        cipher_suite = Fernet(key.encode())
        text = cipher_suite.decrypt(cipher_text.encode())
        return f"text>> {text.decode()}"
    else:
        return 0


userinput = input("do to want to decrypt 'd' or encrypt 'e' ")
if __name__ == "__main__":
    print(aes(userinput))
