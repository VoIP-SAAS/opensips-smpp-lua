#!/usr/bin/python3
import binascii
import sys

gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
       "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà")
ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")

def gsm_encode(plaintext):
    res = ""
    for c in plaintext:
        idx = gsm.find(c);
        if idx != -1:
            res += chr(idx)
            continue
        idx = ext.find(c)
        if idx != -1:
            res += chr(27) + chr(idx)
    return binascii.b2a_hex(res.encode("utf-8"))

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
    plaintext = sys.argv[1].strip()
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
    encoded = sys.argv[1].strip()
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

def testing():
    string = sys.argv[1]
    try:
        f = bytes.fromhex(string).decode("utf-16be")
        return 1
    except:
        return 0

if sys.argv[2] == "encode":
    print(encoding())
elif sys.argv[2] == "decode":
    print(decoding())
elif sys.argv[2] == "test":
    print(testing())
