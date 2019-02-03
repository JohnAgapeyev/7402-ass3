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

if sys.argv[1] not in ['e', 'd']:
    print('This application must be run with either \'e\' or \'d\' as the first flag to signal mode of operation')
    sys.exit(1)

data = open(sys.argv[2], 'rb').read()

if len(data) == 0:
    print('Input file must not be empty')
    sys.exit(1)

if os.path.isfile(sys.argv[3]):
    print('Output file must not currently exist on the system')
    sys.exit(1)

if sys.argv[1] == 'e':
    if os.path.isfile(sys.argv[4]):
        print('Key file must not currently exist on the system')
        sys.exit(1)
    key = get_key(len(data))
    open(sys.argv[4], 'wb').write(key)
else:
    key = open(sys.argv[4], 'rb').read()
    if len(key) != len(data):
        print('Key is not the same size as the message')
        sys.exit(1)

open(sys.argv[3], 'wb').write(encryptMessage(key, data))
