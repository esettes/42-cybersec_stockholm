#!/usr/bin/python3.9
import sys
from lib import messages, utils
from lib.programmode import Stockholm

def main(argv):
    wcry = Stockholm(silence=False, crypt=True)
    args = utils.SetArgs()
    if args.version and args.silent == False and args.reverse == None:
        messages.version_mssg()
        return
    if args.reverse != None:
        wcry.set_silence(False)
        wcry.set_crypt(False)
        wcry.set_key(args.reverse)
    if args.reverse != None and args.silent:
        wcry.set_silence(True)
        wcry.set_crypt(False)
        wcry.set_key(args.reverse)
    if args.silent:
        wcry.set_silence(True)

    utils.files_treat(wcry._lst, wcry.crypt, wcry.silence, wcry.key)
    return

if __name__ == '__main__':
    main(sys.argv)
