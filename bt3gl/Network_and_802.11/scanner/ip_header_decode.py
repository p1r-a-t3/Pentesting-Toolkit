#!/usr/bin/env python

__author__ = "bt3"


import socket
import os
import struct
import ctypes
from ICMPHeader import ICMP

# host to listen on
HOST = '192.168.1.114'


def main():
    socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind(( HOST, 0 ))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # continually read in packets and parse their information
    while 1:
        # read in a packet and pass the first 20 bytes to initialize the IP structure
        raw_buffer = sniffer.recvfrom(65565)[0]

        #take first 20 characters for the ip header
        ip_header = raw_buffer[0:20]

        #unpack them
        iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)

        # print
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);

        print 'IP -> Version:' + str(version) + ', Header Length:' + str(ihl) + \
        ', TTL:' + str(ttl) + ', Protocol:' + str(protocol) + ', Source:'\
         + str(s_addr) + ', Destination:' + str(d_addr)

        # create our ICMP structure
        buf = raw_buffer[iph_length:iph_length + ctypes.sizeof(ICMP)]
        icmp_header = ICMP(buf)

        print "ICMP -> Type:%d, Code:%d" %(icmp_header.type, icmp_header.code) + '\n'



if __name__ == '__main__':
    main()