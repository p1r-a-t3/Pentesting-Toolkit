#!/usr/bin/env python


from Crypto.PublicKey import RSA
from Crypto import Random


def gen_key(nbits=1024):
    random_generator = Random.new().read
    key = RSA.generate(nbits, random_generator)
    return key

def check_key(key):
    print key.can_encrypt()
    print key.can_sign()
    print key.has_private()


def get_pubk(key):
    return key.publickey()


def encrypt(public_key, text, random):
    return public_key.encrypt(text, random)


def decrypt(data):
    return key.decrypt(enc_data)


if __name__ == '__main__':
    key = gen_key()

    check_key(key)

    public_key = get_pubk(key)

    text = 'abcdefgh'
    enc_data = encrypt(public_key, text, random=32)
    print enc_data

    dec_data = decrypt(enc_data)
    print dec_data

