#!/usr/bin/python
#Filename: ioscrack.py

from passlib.utils.pbkdf2 import pbkdf2
import os
import htos
import sys
from time import time
import base64

HOMEDIR = '/Users/yuejiadi/Library/Application Support/MobileSync/Backup/'
PSFILE = '398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b'
ITERATIONS = 1000

backup_dir = os.listdir(HOMEDIR)

for bkup_dir in backup_dir:
    passfile = open(HOMEDIR + bkup_dir + "/" + PSFILE, "r")
    line_list = passfile.readlines()
    secret64 = line_list[6][1:29]
    salt64 = line_list[10][1:9]
    print "secret: ", secret64
    print "salt: ", salt64
    #secret = htos.to_hex(base64.b64decode(secret64))
    secret = base64.b64decode(secret64)
    #print secret
    salt = base64.b64decode(salt64) 
    start_t = time()
    for i in range(10000):
        key = "%04d" % ( i )
        out = pbkdf2(key, salt, ITERATIONS)
        if out == secret:
            print "key: ", key
            duration = time() - start_t
            print "%f seconds" % ( duration )
            sys.exit(0)
    print "no exact key"

