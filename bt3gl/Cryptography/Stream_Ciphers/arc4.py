#!/usr/bin/env python


from Crypto.Cipher import ARC4

obj1 = ARC4.new('01234567')
obj2 = ARC4.new('01234567')

text = 'abcdefghijklmnop'
cipher_text = obj1.encrypt(text)
print cipher_text
print obj2.decrypt(cipher_text)
