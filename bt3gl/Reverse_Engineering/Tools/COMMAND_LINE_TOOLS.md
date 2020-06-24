COMMAND LINE TOOLS
==================


### Tricks:

- Files with spaces in the name + symbolinc links.


### Searching


```
grep word f1

sort | uniq -c

diff f1 f2

find -size f1
```


### Encondings/ Binaries

```
file f1

ltrace bin

strings f1

base64 -d

xxd -r
```



### Compressed Files


```
zcat f1 > f2

gzip -d file

bzip2 -d f1

tar -xvf file
```



### Connecting to a Server/Port

```
echo 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e | nc localhost 30000

openssl s_client -connect localhost:30001 -quiet

nmap -p 31000-32000 localhost

telnet localhost 3000
```



