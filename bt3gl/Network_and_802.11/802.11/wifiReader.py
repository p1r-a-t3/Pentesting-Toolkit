#!/usr/bin/env python
# simple python script to boost txpower and spoof the
# mac address of your wireless interface
# copied from the internet, i lost the reference
import sys
import os
import time


class Colors:
    GREEN = '\033[92m'
    Yellow = '\033[93m'
    ENDC = '\033[0m'


def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])


def show_ifaces():
    cls()
    print('<-------------------Available Interfaces------------------->')
    os.system('airmon-ng > /var/tmp/wifi.txt')
    with open('/var/tmp/wifi.txt', 'r') as f:
        for line in f:
            if line.startswith('wl') or line.startswith('mo'):
                print(line, end=' ')


def change_mac(option2):
    if option2 == '1':
        os.system('ifconfig ' + iface + ' down')
        os.system('macchanger -m 00:11:22:33:44:55 ' + iface)
        os.system('ifconfig ' + iface + ' up')
        time.sleep(2.5)
    elif option2 == '2':
        os.system('ifconfig ' + iface + ' down')
        os.system('macchanger -r ' + iface)
        os.system('ifconfig ' + iface + ' up')
        time.sleep(2.5)
    elif option2 == '3':
        os.system('ifconfig ' + iface + ' down')
        os.system('macchanger -p ' + iface)
        os.system('ifconfig ' + iface + ' up')
        time.sleep(2.5)
    elif option2 == '4':
        print('')
        newmac = input('Address to use: ')
        os.system('ifconfig ' + iface + ' down')
        os.system('macchanger -m ' + newmac + ' ' + iface)
        os.system('ifconfig ' + iface + ' up')
        time.sleep(2.5)
    else:
        print('')
        print('Invalid option')
        time.sleep(0.75)


dbm = ''
iface = ''
while True:
    if len(iface) > 1:
        os.system('iwconfig ' + iface + ' > /var/tmp/wifi2.txt')
        with open('/var/tmp/wifi2.txt') as f:
            for line in f:
                if '=' in line:
                    temp = line.partition('=')
                    temp2 = temp[2]
                    dbm = temp2[0:3]

    show_ifaces()
    print('')
    print('1) select IFACE        ' + Colors.Yellow + 'IFACE:' + iface + '  ' + 'dBm:' + dbm + Colors.ENDC)
    print('2) start monitor mode')
    print('3) boost txpower(30dBm)')
    print('4) spoof mac address')
    print('5) exit')
    option = input('Please choose a menu number: ')

    if option == '1':
        cls()
        show_ifaces()
        print('')
        iface = input('which interface would you like to use? ')

    elif option == '2':
        cls()
        os.system('airmon-ng start ' + iface + ' > /var/tmp/wifi1.txt')
        with open('/var/tmp/wifi1.txt', 'r') as f:
            for line in f:
                if 'monitor' in line:
                    temp = line.partition(' on')
                    temp2 = temp[2]
                    temp3 = temp2[1:5]
                    iface = temp3
                    time.sleep(0.5)

    elif option == '3':
        cls()
        time.sleep(1)
        os.system('iw reg set BO')
        time.sleep(2)
        os.system('iwconfig ' + iface + ' txpower 30')

    elif option == '4':
        cls()
        print('1) use 00:11:22:33:44:55')
        print('2) use random')
        print('3) revert to permanent')
        print('4) pick an address')
        print('')
        option2 = input('Please choose a menu number: ')
        cls()
        change_mac(option2)

    elif option == '5':
        os.system('rm /var/tmp/wifi*.txt')
        sys.exit()

    else:
        cls()
        print('Invalid option')
        time.sleep(1)
