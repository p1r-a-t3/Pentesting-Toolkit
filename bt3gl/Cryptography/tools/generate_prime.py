#!/usr/bin/python

import math
import random
import sys
from finding_prime import finding_prime_sqrt


def generate_prime(number=3):
    ''' return a n-bit prime '''
    while 1:
        p = random.randint(pow(2, number-2), pow(2, number-1)-1)
        p = 2 * p + 1
        if finding_prime_sqrt(p):
            return p


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Usage: generate_prime.py number")
        sys.exit()
    else:
        number = int(sys.argv[1])
        print(generate_prime(number))









