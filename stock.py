#!/usr/bin/python3.9
import sys
from lib import messages, utils
from lib.bcolors import bcol

def main(argv):

    key = ""
    mode = "crypt"
    lst = utils.load_list_ext()
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
