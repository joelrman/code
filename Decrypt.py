#!/usr/bin/env python3

#txtfile = open('message.txt','r+')
inp = 'wobaoktasbvrqaeqwoergxqazwvrzwvroreezfrtevmsiwjortusjpmtnsacpnfrmdxobosudimjneajneubjhmownqjqpbxqjkohlnlkrbowzxohdcnowrlwnfdwwfqtxjoiyvqteavnniakdpncduuqwfijoircjtpzhwdpdmweegjrplmppfoqimaqompgojosejqrggzitdaaxcpdwmpfcxrqqhmcdpwagrpynmvjzbbgihehdjiuchcqieihefdrereszgswkovndnvohrnqkruqsasdspjrkvmmzbcrzsfborxxdbkznbtznoronuczmaumi'

import hashlib

a = 1#a = ord(input('1?'))-ord('1')+1
key_init = input('Enter key: ')
key_inter = str(hashlib.md5(key_init.encode('utf-8')).hexdigest())
cip = inp.upper()
key = key_inter.upper()

K = len(key)
pt = ''

if a != 100:
    for i in range(len(cip)):
        if (cip[i] == ' '):
            pt += ' '
        elif chr(97+(ord(cip[i])-ord(key[i%K]))%26) == 'z':
            pt += ' '
        else:
            pt += chr(97+(ord(cip[i])-ord(key[i%K]))%26)
else:
    inp = input('Enter ciphertext: ')
    cip = inp.upper()
    for i in range(len(cip)):
        if cip[i] == ' ':
            pt += chr(97+(ord('Z')+ord(key[i%K])-130)%26)
        else:
            pt += chr(97+(ord(cip[i])+ord(key[i%K])-130)%26)
print(pt)