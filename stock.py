#!/usr/bin/python3.9
from pathlib import Path
import sys, argparse
from argparse import RawTextHelpFormatter
from lib import messages, utils
from lib.programmode import Stockholm

def main(argv):
#"""default=Path(__file__).relative_to('/home/')""""
    head = """

        █▀ ▀█▀ █▀█ █▀▀ █▄▀ █░█ █▀█ █░░ █▀▄▀█
        ▄█ ░█░ █▄█ █▄▄ █░█ █▀█ █▄█ █▄▄ █░▀░█
                ──▄────▄▄▄▄▄▄▄────▄───
                ─▀▀▄─▄█████████▄─▄▀▀──
                ─────██─▀███▀─██──────
                ───▄─▀████▀████▀─▄────
                ─▀█────██▀█▀██────█▀──              """
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=head)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v','--version', action='store_true', help="Show program version.")
    parser.add_argument('-s','--silent', action='store_true', help="Silence the file de/encryption process.")
    parser.add_argument('-r','--reverse', type=Path, metavar='<key>', default=None, help="Reverse the files encription.")
    args = parser.parse_args()

    stockholm = Stockholm(silence=False, crypt=True)
    if args.version and args.silent == False and args.reverse == None:
        messages.version_mssg()
        return
    if args.reverse != None: #and args.silent == False and args.version == None: # reverse cript 
        stockholm.set_silence(False)
        stockholm.set_crypt(False)
        stockholm.set_key(args.reverse)
    if args.reverse != None and args.silent:# and args.version == None: # reverse cript quietly
        stockholm.set_silence(True)
        stockholm.set_crypt(False)
        stockholm.set_key(args.reverse)
    if args.silent:
        stockholm.set_silence(True)
    #print("silence : " + str(stockholm.silence) + ", crypt: " + str(stockholm.crypt) + ", key: " + str(stockholm.key))
    utils.files_treat(stockholm._lst, stockholm.crypt, stockholm.silence, stockholm.key)

    return

if __name__ == '__main__':
    main(sys.argv)
