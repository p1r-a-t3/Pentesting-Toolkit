#!/bin/python

__author__= 'bt3gl'

import string
import sys
import operator


FREQ_ENGLISH = [0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047, 0.0357,0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116, 0.0169, 0.0028, 0.0164, 0.0004]


def find_frequency(msg):
    dict_freq = dict([(c, 0) for c in string.lowercase])
    total_letters = 0.0
    for c in msg.lower():
        if 'a'<= c <= 'z':
            dict_freq[c] += 1
            total_letters += 1
    list_freq = sorted(dict_freq.items(), key=operator.itemgetter(1))
    return [(c, freq/total_letters) for (c, freq) in list_freq]



def main(filename):
    with open(filename, 'r') as f:
       cipher = f.readlines()
       cipher = cipher[0].strip()
       flist = find_frequency(cipher)
       elist = dict((k, value) for (k, value) in  zip(string.lowercase, FREQ_ENGLISH))
       elist = sorted(elist.items(), key=operator.itemgetter(1))
       trans, key = '', ''
       for i, f in enumerate(flist):
          trans += f[0]
          key += elist[i][0]
          print "CIPHER: %s -> %.5f, ENGLISH: %s -> %.5f" %(f[0], f[1], elist[i][0], elist[i][1])
       print "Key is " + key + " for " + trans
       
       # print key sorted to translate to a-z
       res = zip(trans, key)
       res.sort()
       trans, key = '', ''
       for letter in res:
		trans += letter[1].upper()
		key += letter[0].upper()
       print "tr  [" + key + "] [" + trans + "]"


if __name__ == "__main__":
	main(str(sys.argv[1]))

