from lib.bcolors import bcol

def version_mssg():

    print(bcol.CURSI + "Stock(holm) version 1.0")
    print("July 2022" + bcol.ENDC)

def err_msg(s):
    print(bcol.FAIL + "[ERROR] " + bcol.ENDC + s )

