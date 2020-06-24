'''
from asis 2013: The last crypto (binary numbers) was very puzzling. We couldn’t decipher it. But a few minutes before the CTF ending, we noticed we could brute-force the 6 missing characters offline, because in each task, there was a client-side verification with a sha-256 hash. For this task, the hash of the flag was 6307c5441ebac07051e3b90d53c3106230dd9aa128601dcd5f63efcf824ce1ba. A quick brute-force in Python revealed us the missing chars, and therefore, the final flag to submit!
'''


import hashlib, itertools
hash = '6307c5441ebac07051e3b90d53c3106230dd9aa128601dcd5f63efcf824ce1ba'
ch = 'abcdef0123456789'
for a, b, c, d, e, f in itertools.product(ch, ch, ch, ch, ch, ch):
    if hashlib.sha256('ASIS_a9%s00f497f2eaa4372a7fc21f0d' % (a + b + c + d + e + f)).hexdigest() == hash:
        print 'ASIS_a9%s00f497f2eaa4372a7fc21f0d' % (a + b + c + d + e + f)
