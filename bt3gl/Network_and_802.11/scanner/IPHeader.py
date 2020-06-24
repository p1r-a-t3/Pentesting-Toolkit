#!/usr/bin/env python

__author__ = "bt3"

''' A class for the IP header'''

import os
import struct
import socket
import ctypes


class IP(ctypes.Structure):
    _fields_ = [
        ('ihl',         ctypes.c_ubyte, 4),
        ('version',     ctypes.c_ubyte, 4),
        ('tos',         ctypes.c_ubyte),
        ('len',         ctypes.c_ushort),
        ('id',          ctypes.c_ushort),
        ('offset',      ctypes.c_ushort),
        ('ttl',         ctypes.c_ubyte),
        ('protocol_num',ctypes.c_ubyte),
        ('sum',         ctypes.c_ushort),
        ('src',         ctypes.c_ulong),
        ('dst',         ctypes.c_ulong)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        # map protocol constants to their names
        self.protocol_map = {1:'ICMP', 6:'TCP', 17:'UDP'}

        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack('<L', self.src))
        self.dst_address = socket.inet_ntoa(struct.pack('<L', self.dst))

        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

