#!/usr/bin/python

#example of dis

import dis

def foo(a):
    x = 3
    return x + a


print(dis.dis(foo.func_code))
