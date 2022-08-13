#!/usr/bin/python3.9
import sys, argparse
from argparse import RawTextHelpFormatter
from tkinter.messagebox import NO
from xmlrpc.client import boolean
from lib import messages, utils
from lib.bcolors import bcol

def main(argv):

    head = """
  _____ ___ _____ ____        ____            
 |_   _/ _ |_   _|  _ \      / ___| ___ _ __  
   | || | | || | | |_) _____| |  _ / _ | '_ \ 
   | || |_| || | |  __|_____| |_| |  __| | | |
   |_| \___/ |_| |_|         \____|\___|_| |_|

Temporary one time password generator.
------------------------------------------------
Usually steps:
\tCreate a master key:
[ ./ft_otp -rg "My super secret master key 123456 super password" ]

\tGenerate tot-password:
[ ./ft_otp -k ft_otp.key ]
------------------------------------------------
    """
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=head)
    parser.add_argument('-v','--version', action='store_true', help="Show program version.")
    parser.add_argument('-s','--silent', default=None, help="Silence the file de/encryption process.")
    parser.add_argument('-r','--reverse', metavar='<key>', default=None, help="Reverse the files encription.")
    args = parser.parse_args()

    silence = True
    crypt = True
    key = ""
    lst = utils.load_list_ext()
    if args.version and args.silent == None and args.reverse == None: # print prog version
        messages.version_mssg()
        return
    if args.reverse != None and args.silent == None and args.version == None: # reverse cript 
        silence = False
        crypt = False
        key = args.reverse
    if args.reverse != None and args.silent != None and args.version == None: # reverse cript quietly
        silence = True
        crypt = False
        key = args.reverse
    if args.silent != None: # cript files
        silence = True
    utils.files_treat(lst, crypt, silence, key)


    if len(argv) > 4:
        messages.many_args_mssg()
    elif len(argv) > 1:
        if argv[1] == "-help" or argv[1] == "-h":
            if len(argv) > 2:
                messages.many_args_mssg()
            else:
                messages.help_mssg()
        elif argv[1] == "-version" or argv[1] == "-v":
            if len(argv) > 2:
                messages.many_args_mssg()
            else:
                messages.version_mssg()
        elif argv[1] == "-silent" or argv[1] == "-s":
            if len(argv) == 2:
                utils.files_treat(lst, mode, True, key)
            elif len(argv) == 3:
                messages.did_you_mean_mssg(argv[0])
            elif len(argv) == 4:
                utils.call_rev_files(lst, argv[3], True)
        elif argv[1] == "-reverse" or argv[1] == "-r":
            if len(argv) < 3:
                messages.introduce_key_mssg()
            elif len(argv) == 4:
                messages.did_you_mean_mssg(argv[0])
            else:
                utils.call_rev_files(lst, argv[2], False)
        else:
            messages.cmd_not_found_mssg()
    else:
        utils.files_treat(lst, mode, False, key)

if __name__ == '__main__':
    main(sys.argv)
