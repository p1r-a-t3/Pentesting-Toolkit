#!/usr/bin/env python

__author__ = "bt3"

import threading
import time
import socket
import os
import struct
import ctypes
from netaddr import IPNetwork, IPAddress
from ICMPHeader import ICMP

# host to listen on
HOST = '192.168.1.114'


# subnet to target (iterates through all IP address in this subnet)
# our local network
SUBNET = '192.168.1.0/24'

# define string signature
MESSAGE = 'hellooooo'

# sprays out the udp datagram
def udp_sender(SUBNET, MESSAGE):
    time.sleep(5)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for ip in IPNetwork(SUBNET):
        try:
            sender.sendto(MESSAGE, ("%s" % ip, 65212))
        except:
            pass


# start sending packets: separated threads  to make sure that we are not interfering
# with our ability to sniff responses
t = threading.Thread(target=udp_sender, args=(SUBNET, MESSAGE))
t.start()


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
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        src_addr = socket.inet_ntoa(iph[8]);

        # create our ICMP structure
        buf = raw_buffer[iph_length:iph_length + ctypes.sizeof(ICMP)]
        icmp_header = ICMP(buf)

        # check for the type 3 and code: first check to make sure that the ICMP
        # response is coming from within our target subenet
        if icmp_header.code == 3 and icmp_header.type == 3:
            # make sure host is in our target subnet
            if IPAddress(src_addr) in IPNetwork(SUBNET):
                # make sure it has magic message
                if raw_buffer[len(raw_buffer) - len(MESSAGE):] == MESSAGE:
                    print("Host up: %s" % src_addr)


if __name__ == '__main__':
    main()