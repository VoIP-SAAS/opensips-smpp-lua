#!/usr/bin/python3
import random
import six
from smpplib import consts, exceptions
import binascii
import base64
import sys

gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>"
       "?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")


def gsm_encode(plaintext):
    result = []
    for c in plaintext:
        idx = gsm.find(c)
        if idx != -1:
            result.append(chr(idx))
            continue
        idx = ext.find(c)
        if idx != -1:
            result.append(chr(27) + chr(idx))
    return binascii.hexlify(''.join(result).encode('utf-8'))

def gsm_decode(hexstr):
    hexstr = binascii.unhexlify(hexstr)
    res = hexstr
    res = iter(res)
    result = []

    for c in res:        
      if c == chr(27):
          c = next(res)
          result.append(ext[c])
      else:
    
          result.append(gsm[c])
    return ''.join(result)

def encoding():
    plaintext = sys.argv[1]
    if sys.argv[3] == "GSM":
        encoded = gsm_encode(plaintext)
    elif sys.argv[3] == "ISO":    
        encoded = plaintext.encode('iso-8859-1')
    elif sys.argv[3] == "UTF16BE":    
        encoded = plaintext.encode("utf-16-be").hex()
    elif sys.argv[3] == "UTF16LE":    
        encoded = plaintext.encode("utf-16-le").hex()
    elif sys.argv[3] == "UTF16":    
        encoded = plaintext.encode("utf-16").hex()
    elif sys.argv[3] == "UTF8":    
        encoded = plaintext.encode("utf-8").encode('hex')
    return encoded

def decoding():
    encoded = sys.argv[1]
    if sys.argv[3] == "GSM":
        decoded = gsm_decode(encoded)
    elif sys.argv[3] == "ISO":    
        decoded = bytes.fromhex(encoded).decode("iso-8859-1")
    elif sys.argv[3] == "UTF16BE":   
        decoded = bytes.fromhex(encoded).decode("utf-16be")
    elif sys.argv[3] == "UTF16LE":
        decoded = bytes.fromhex(encoded).decode("utf-16-le")
    elif sys.argv[3] == "UTF16":    
        decoded = bytes.fromhex(encoded).decode("utf-16")
    elif sys.argv[3] == "UTF8":    
        decoded = bytes.fromhex(encoded).decode("utf-8")
    return decoded



if sys.argv[2] == "encode":
    print(encoding())
elif sys.argv[2] == "decode":
    print(decoding())
