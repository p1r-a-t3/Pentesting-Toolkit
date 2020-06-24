#!/bin/python

import string
import sys
import operator

def find_frequency(msg):
    dict_freq = dict([(c, 0) for c in string.lowercase])
    total_letters = 0.0
    for c in msg.lower():
        if 'a'<= c <= 'z':
            dict_freq[c] += 1
            total_letters += 1
    list_freq = sorted(dict_freq.items(), key=operator.itemgetter(1))
    return list_freq



def main(filename):
    with open(filename, 'r') as f:
       cipher = f.readlines()
       cipher = cipher[0].strip()
       print(find_frequency(cipher))


if __name__ == "__main__":
	main(str(sys.argv[1]))
