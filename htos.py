#!/usr/bin/python
#Filename: htos.py

#convert string to hex
def to_hex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    return reduce(lambda x,y:x+y, lst)

#convert hex repr to string
def to_str(s):
    return s and chr(int(s[:2], base=16)) + to_str(s[2:]) or ''
