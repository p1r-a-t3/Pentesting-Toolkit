```
VAR=$(cat data.txt)
echo "$VAR"
alias rot13="tr A-Za-z N-ZA-Mn-za-m"
echo "$VAR" | rot13
```
----


In Python we can use: ```"YRIRY GJB CNFFJBEQ EBGGRA".decode(encoding="ROT13")```
https://docs.python.org/2/library/codecs.html#codec-base-classes

---

Online: 

http://www.xarg.org/tools/caesar-cipher/
