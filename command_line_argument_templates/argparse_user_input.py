import argparse
from argparse import RawTextHelpFormatter
# pip3 install argparse

examples = '''
	python3 argparse_user_input.py
	python3 argparse_user_input.py -n 1337 -s 8Handles
    '''

options = argparse.ArgumentParser(description='User input with argparse example',formatter_class=RawTextHelpFormatter,epilog=examples)

options.add_argument("-n","--number",required=False,type=int,default=31337,help='Enter a int value')
options.add_argument("-s","--string",required=False,type=str,default="You",help='Enter a string of a person')

args = options.parse_args()

Num = args.number
Str = args.string

print(Str + " is " + str(Num))
