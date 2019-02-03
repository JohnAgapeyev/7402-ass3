#!/usr/bin/python3

import math
import sys
import os

def encryptMessage (key, message):
    return ''

if len(sys.argv) != 4:
    print('Usage: ./main.py [e/d] <input_file> <output_file>')
    sys.exit(1)

mode = sys.argv[1]
data = open(sys.argv[2]).read()
output_filename = sys.argv[3]

if mode not in ['e', 'd']:
    print('This application must be run with either \'e\' or \'d\' as the first flag to signal mode of operation')
    sys.exit(1)

if len(data) == 0:
    print('Input file must not be empty')
    sys.exit(1)

if os.path.isfile(output_filename):
    print('Output file must not currently exist on the system')
    sys.exit(1)
