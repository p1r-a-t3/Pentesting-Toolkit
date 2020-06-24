#!/usr/bin/python

import math
import random

def finding_prime(number):
    ''' find whether a number is prime in a simple way'''
    num = abs(number)
    if num < 4 : return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
       

def finding_prime_sqrt(number):
    ''' find whether a number is prime as soon as it rejects all candidates up to sqrt(n) '''
    num = abs(number)
    if num < 4 : return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True


def finding_prime_fermat(number):
    ''' find whether a number is prime with Fermat's theorem, using probabilistic tests '''
    if number <= 102:
        for a in range(2, number):
            if pow(a, number- 1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number - 1, number) != 1:
                return False
        return True



def test_finding_prime():
    number1 = 17
    number2 = 20
    assert(finding_prime(number1) == True)
    assert(finding_prime(number2) == False)
    assert(finding_prime_sqrt(number1) == True)
    assert(finding_prime_sqrt(number2) == False)
    assert(finding_prime_fermat(number1) == True)
    assert(finding_prime_fermat(number2) == False)
    print('Tests passed!')


if __name__ == '__main__':
    test_finding_prime()


