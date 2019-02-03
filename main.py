#!/usr/bin/python3

import math
import sys
import os
import secrets

def encryptMessage(key, message):
    return bytes(k ^ m for k, m in zip(key, message))

def get_key(mesg_len):
    return secrets.token_bytes(mesg_len)

if len(sys.argv) != 5:
    print('Usage: ./main.py [e/d] <input_file> <output_file> <key_file>')
    sys.exit(1)

mode = sys.argv[1]
data = open(sys.argv[2], 'rb').read()
output_filename = sys.argv[3]
key_filename = sys.argv[4]

if mode not in ['e', 'd']:
    print('This application must be run with either \'e\' or \'d\' as the first flag to signal mode of operation')
    sys.exit(1)

if len(data) == 0:
    print('Input file must not be empty')
    sys.exit(1)

if os.path.isfile(output_filename):
    print('Output file must not currently exist on the system')
    sys.exit(1)

if mode == 'e':
    if os.path.isfile(key_filename):
        print('Key file must not currently exist on the system')
        sys.exit(1)
    key = get_key(len(data))
    output = open(output_filename, 'wb')
    output.write(encryptMessage(key, data))
    kf = open(key_filename, 'wb')
    kf.write(key)
else:
    key = open(key_filename).read()
    output = open(output_filename, 'wb')
    output.write(encryptMessage(key, data))
