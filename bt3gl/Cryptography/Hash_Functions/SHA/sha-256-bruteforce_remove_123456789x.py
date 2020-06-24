'''
from asis 2013
'''

from itertools import permutations
from hashlib import sha256

def test(s):
  e = '9f2a579716af14400c9ba1de8682ca52c17b3ed4235ea17ac12ae78ca24876ef'
  return sha256('ASIS_' + s).hexdigest() == e

m = '3c6a1c371b381c943065864b95ae5546'
s = '12456789x'
for p in permutations(s):
    def f(sub, c):
        if c in sub:
            return sub[c]
        else:
            return c
    sub = {c : d for c, d in zip(s, p)}
    z = ''.join(f(sub, c) for c in m)
    if test(z):
        print z
        break
