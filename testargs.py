#!/Volumes/sgoinfre/students/iostancu/homebrew/bin/python3
import argparse
import getopt
import sys
from os import listdir, rename
from os.path import split

def main(argv):

	parser = argparse.ArgumentParser()
	parser.add_argument('--asd')
	parser.add_argument('bar')
	parser.parse_args('X --asd Y'.split())

	parser.print_help()
	print(parser)

if __name__ == '__main__':
    main(sys.argv)
