#!/usr/bin/python

from PIL import Image
import random
import operator

def get_color(x, y, r):
	n = (pow(x, 3) + pow(y, 3)) ^ r
	return (n ^ ((n >> 8) << 8 ))

flag_img = Image.open("flag.png")
im = flag_img.load()
print flag_img.size

enc_img = Image.new(flag_img.mode, flag_img.size)
enpix = enc_img.load()

d = {}
for i in range(0, 256):
	d[i] = 0

for x in range(flag_img.size[0]):
	for y in range(flag_img.size[1]):
		enpix[x,y] = 0
		r = im[x, y] ^ ((pow(x, 3) + pow(y, 3)) % 256)
		d[r] += 1

use = max(d.iteritems(), key=operator.itemgetter(1))[0]

for x in range(flag_img.size[0]):
	for y in range(flag_img.size[1]):
		r = im[x, y] ^ ((pow(x, 3) + pow(y, 3)) % 256)
		if r == use:
			enpix[x, y] = 255

print use

enc_img.save('dec' + '.png')
