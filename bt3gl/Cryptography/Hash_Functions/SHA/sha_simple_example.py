#!/usr/bin/env python

def example_sha():
    from Crypto.Hash import SHA256
    hash = SHA256.new()
    hash.update('message')
    print hash.digest()

if __name__ == '__main__':
    example_sha()