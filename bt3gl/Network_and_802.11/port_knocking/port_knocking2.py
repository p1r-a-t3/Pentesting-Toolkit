#!/usr/bin/python


from scapy.all import *

conf.verb = 0
base_URL = "10.13.37.23"

def get_flag_part(port):
    command = ["curl", "-s" ,base_URL+str(port)+"/flag.txt"]
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result.strip()


# ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 199, 443, 995,  587, 1025, 1720, 993, 1723, 3306, 3389, 5900, 8080, 8888]



# METHOD 1

# Knock twice on every port
for dport in range(65535):

    print "[*] Knocking on " +  base_URL + ": " +  str(dport)
    ip = IP(dst=base_URL)
    port = dport + 10
    SYN = ip/TCP(sport=port, dport=dport, flags="S", window=14600, options=[('MSS',1460)], seq=0)
    send(SYN); 
    port = dport + 100
    SYN = ip/TCP(sport=port, dport=dport, flags="S", window=14600, options=[('MSS',1460)], seq=0)
    send(SYN); 

    flag = get_flag_part(port)
    if "404" not in flag:
	print "************************Yaaaayyyyyyyy************************"
	print flag


# METHOD 2

print "[*] Scanning for open ports using nmap"
subprocess.call("nmap -sS -sV -T4 -p 22-2048 " + base_URL, shell=True)
