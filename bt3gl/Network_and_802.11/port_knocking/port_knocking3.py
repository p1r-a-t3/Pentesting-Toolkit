#!/usr/bin/python


from scapy.all import *

conf.verb = 0
base_URL = "10.13.37.23"

def get_flag_part(port):
    command = ["curl", "-s" ,base_URL+str(port)+"/flag.txt"]
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result.strip()


ports = [39367, 39368]
save = []

ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 199, 443, 995,  587, 1025, 1720, 993, 1723, 3306, 3389, 5900, 8080, 8888]


# Knock twice on every port
for dport in ports:

    print "[*] Knocking on " +  base_URL + ": " +  str(dport)
    ip = IP(dst=base_URL)
    SYN = ip/TCP(dport=dport, flags="S")
    send(SYN); 
    SYN = ip/TCP(dport=dport, flags="S")
    send(SYN); 

"""
    #flag = get_flag_part(dport)
    #if "404" not in flag:
    #	save.append(flag)
	

if save:
    print "Maybe?"
    print flag


# METHOD 2

#print "[*] Scanning for open ports using nmap"
"""
subprocess.call("nmap -sS -sV -T4 -p 22-2048 " + base_URL, shell=True)

"""
import socket

host = "10.13.37.23"
startport = 0
endport = 32000



def knock(port):
    s = socket.socket(socket.AF_NET, socket.SOCK_TEAM)
    s.send(1024)
    s.settimeout((0,0))
    try:
        s.connect((host, port))
	s.recv(1024)


for port in range (startport, endport):
	knock(host, port)
	time.sleep(3)
"""






