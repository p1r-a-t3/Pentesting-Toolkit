#!/usr/bin/env python

__author__ = "bt3"

''' A Basic Sniffer'''

import socket
import os

# DEFINE CONSTANTS
# host to listen
HOST = '192.168.1.114'




def sniffing(host, win, socket_prot):
    while 1:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_prot)
        sniffer.bind((host,0))

        # include the IP headers in the captured packets
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        # if windows, it needs to send an IOCTL to set to promiscuous mode
        # we send IOCTL to the network card driver to enable it
        # promiscuous mode allows us to sniff all packets that the network card sees
        # even those not destined to the host
        if win == 1:
            sniffer.ioctl(socket.SIO_RCVALL, socket_RCVALL_ON)

        # read in a single packet
        print sniffer.recvfrom(65565)



def main(host):

    OS = os.name

    # create a raw socket, binding to the public interface
    # windows allow us to sniff all incoming packets regardless of protocol,
    # whereas Linux forces us to specify we are sniffing ICMP
    if OS == 'nt':
        socket_prot = socket.IPPROTO_IP
        sniffing(host, 1, socket_prot)

    else:
        socket_prot = socket.IPPROTO_ICMP
        sniffing(host, 0, socket_prot)




if __name__ == '__main__':
    main(HOST)