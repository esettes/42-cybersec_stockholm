#!/usr/bin/python3.9
from cryptography.fernet import Fernet

def write_key():

    key = Fernet.generate_key()
    with open("utils/key.key", "wb") as key_file:
        key_file.write(key)

write_key()