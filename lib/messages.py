from lib.bcolors import bcol
<<<<<<< HEAD

def help_mssg():

    print(bcol.UNDERLINE + "FLAGS")
    print(bcol.ENDC + "\t[ -help ][ -h ] Shows avaible flags for the program.")
    print("\t[ -reverse ][ -r ] Decrypt files using it along with decryption key [ ./stock.py -reverse + [key] ]")
    print("\t[ -silent ][ -s ] Silences the file de/encryption process. [./stock.py -silent] or " +
        "[./stock.py -silent -reverse + [key] ]")
    print("\t[ -version ][ -v ] Shows program version.")
=======
>>>>>>> 3e5e839a6b0af94bb7af4abceaac7767686211ab

def version_mssg():
    print(bcol.CURSI + "Stock(holm) version 1.0")
    print("July 2022" + bcol.ENDC)
<<<<<<< HEAD

def many_args_mssg():
    print(bcol.FAIL + "[ERROR]" + bcol.ENDC + " Too many arguments.")
    print("Try [ ./stock.py -help ]")

def did_you_mean_mssg(v):
    print(bcol.FAIL + "[ERROR]" + bcol.ENDC + " Did you mean [ " + v + " -silent -reverse <key> ] ?")
=======
>>>>>>> 3e5e839a6b0af94bb7af4abceaac7767686211ab

def err_msg(s):
    print(bcol.FAIL + "[ERROR] " + bcol.ENDC + s )

<<<<<<< HEAD
def cmd_not_found_mssg():
    print(bcol.FAIL + "[ERROR]" + bcol.ENDC + " Command not found")
=======
>>>>>>> 3e5e839a6b0af94bb7af4abceaac7767686211ab
