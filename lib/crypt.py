from os import rename
from os.path import split, splitext
from lib.bcolors import bcol
import lib.messages as msg

def encrypt_file(extensions, src, k, silence, folder):
    try:
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
                        print(bcol.FAIL + newname + " encripted" + bcol.ENDC)
                else:
                    if silence == False:
                        print(bcol.FAIL + newfile[1] + " encripted" + bcol.ENDC)
    except Exception as e:
        msg.err_msg("An error ocurred during encription: ")
        print(e)
        return

<<<<<<< HEAD
def encrypt_file(extensions, src, k, silence):

    newfile = split(src)
    ext = splitext(newfile[1])
    if ext[1] != "" and ext[1] != None:
        try:
            if ext[1] in extensions:
                with open(src, 'rb') as o_file:
                    r_file = o_file.read()
                    crypt = k.encrypt(r_file)
                    o_file.close()
                with open(src, 'wb') as crypt_file:
                    crypt_file.write(crypt)
                    crypt_file.close()
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
        except Exception:
            if silence == False:
                print(bcol.FAIL + "A file can't be cripted" + bcol.ENDC)

def decrypt_file(src, k, silence):
        trigger = False
        newfile = split(src)
        if newfile[1].endswith('.ft'):
            try:
                with open(src, 'rb') as o_file:
                    r_file = o_file.read()
                    decrypt = k.decrypt(r_file)
                    o_file.close()
                    with open(src, 'wb') as crypt_file:
                        crypt_file.write(decrypt)
                        crypt_file.close()
                        trigger = True
                if trigger == True:
                    name =  newfile[1]
                    newname = name.replace('.ft', '')
                    dst = folder + '/' + newname
                    rename(src, dst)
                    if silence == False:
                        print(bcol.GREEN + name + " decriped as " + newname + bcol.ENDC)
            except Exception:
                if silence == False:
                    print(bcol.FAIL + "A file can't be decripted" + bcol.ENDC)
            
        
        
=======
def decrypt_file(src, k, silence, folder):
    try:
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
    except Exception as e:
        msg.err_msg("An error ocurred during decription")
        print(e)
        return
>>>>>>> 3e5e839a6b0af94bb7af4abceaac7767686211ab
