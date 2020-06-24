## Extract md5 hashes

```
 # egrep -oE '(^|[^a-fA-F0-9])[a-fA-F0-9]{32}(1|$)' *.txt | egrep -o '[a-fA-F0-9]{32}' > md5-hashes.txt
```

## An alternative could be with sed

```
# sed -rn 's/.*[^a-fA-F0-9]([a-fA-F0-9]{32})[^a-fA-F0-9].*/1/p' *.txt > md5-hashes
```

## Extract valid MySQL-Old hashes
```
# cat *.txt | grep -e "[0-7][0-9a-f]{7}[0-7][0-9a-f]{7}" > mysql-old-hashes.txt
```

## Extract blowfish hashes

```
# cat *.txt | grep -e "$2a$8$(.){75}" > blowfish-hashes.txt
```

## Extract Joomla hashes
```
# cat *.txt | egrep -o "([0-9a-zA-Z]{32}):(w{16,32})" > joomla.txt
```

## Extract VBulletin hashes
```
# cat *.txt | egrep -o "([0-9a-zA-Z]{32}):(S{3,32})" > vbulletin.txt
```

## Extract phpBB3-MD5
```
# cat *.txt | egrep -o '$H$S{31}' > phpBB3-md5.txt
```

## Extract Wordpress-MD5
```
# cat *.txt | egrep -o '$P$S{31}' > wordpress-md5.txt
```

## Extract Drupal 7
```
# cat *.txt | egrep -o '$S$S{52}' > drupal-7.txt
```

## Extract old Unix-md5
```
# cat *.txt | egrep -o '$1$w{8}S{22}' > md5-unix-old.txt
```

## Extract md5-apr1
```
# cat *.txt | egrep -o '$apr1$w{8}S{22}' > md5-apr1.txt
```

## Extract sha512crypt, SHA512(Unix)
```
# cat *.txt | egrep -o '$6$w{8}S{86}' > sha512crypt.txt
```

## Extract e-mails from text files
```
# cat *.txt | grep -E -o "[a-zA-Z0-9.#?$*_-]+@[a-zA-Z0-9.#?$*_-]+.[a-zA-Z0-9.-]+" > e-mails.txt
```

## Extract HTTP URLs from text files
```
# cat *.txt | grep http | grep -shoP 'http.*?[" >]' > http-urls.txt
```

## For extracting HTTPS, FTP and other URL format use
```
# cat *.txt | grep -E '(((https|ftp|gopher)|mailto)[.:][^ >"  ]*|www.[-a-z0-9.]+)[^ .,;   >">):]' > urls.txt
```

Note: if grep returns "Binary file (standard input) matches" use the following approaches

```
# cat *.log | tr '[00-1113-37177-377]' '.' | grep -E "Your_Regex"
```
OR

```
# cat -v *.log | egrep -o "Your_Regex"
```

## Extract Floating point numbers
```
# cat *.txt | grep -E -o "^[-+]?[0-9]*.?[0-9]+([eE][-+]?[0-9]+)?$" > floats.txt
```

## Extract credit card data
Visa
```
# cat *.txt | grep -E -o "4[0-9]{3}[ -]?[0-9]{4}[ -]?[0-9]{4}[ -]?[0-9]{4}" > visa.txt
```

MasterCard
```
# cat *.txt | grep -E -o "5[0-9]{3}[ -]?[0-9]{4}[ -]?[0-9]{4}[ -]?[0-9]{4}" > mastercard.txt
```

American Express
```
# cat *.txt | grep -E -o "3[47][0-9]{13}" > americal-express.txt
```

Diners Club
```
# cat *.txt | grep -E -o "3(?:0[0-5]|[68][0-9])[0-9]{11}" > diners.txt
```

Discover
```
# cat *.txt | grep -E -o "6011[ -]?[0-9]{4}[ -]?[0-9]{4}[ -]?[0-9]{4}" > discover.txt
```

JCB
```
# cat *.txt | grep -E -o "(?:2131|1800|35d{3})d{11}" > jcb.txt
```

AMEX
```
# cat *.txt | grep -E -o "3[47][0-9]{2}[ -]?[0-9]{6}[ -]?[0-9]{5}" > amex.txt
```

## Extract Social Security Number (SSN)
```
# cat *.txt | grep -E -o "[0-9]{3}[ -]?[0-9]{2}[ -]?[0-9]{4}" > ssn.txt
```

## Extract Indiana Driver License Number
```
# cat *.txt | grep -E -o "[0-9]{4}[ -]?[0-9]{2}[ -]?[0-9]{4}" > indiana-dln.txt
```

## Extract US Passport Cards
```
# cat *.txt | grep -E -o "C0[0-9]{7}" > us-pass-card.txt
```

## Extract US Passport Number
```
# cat *.txt | grep -E -o "[23][0-9]{8}" > us-pass-num.txt
```

## Extract US Phone Numberss
```
# cat *.txt | grep -Po 'd{3}[s-_]?d{3}[s-_]?d{4}' > us-phones.txt
```

## Extract ISBN Numbers
```
# cat *.txt | egrep -a -o "ISBN(?:-1[03])?:? (?=[0-9X]{10}$|(?=(?:[0-9]+[- ]){3})[- 0-9X]{13}$|97[89][0-9]{10}$|(?=(?:[0-9]+[- ]){4})[- 0-9]{17}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X]" > isbn.txt
```

## WordList Manipulation

Remove the space character with sed

```
# sed -i 's/ //g' file.txt
```

OR
```
# egrep -v "^[[:space:]]*$" file.txt
```

Remove the last space character with sed
```
# sed -i s/.$// file.txt
```

Sorting Wordlists by Length
```
# awk '{print length, $0}' rockyou.txt | sort -n | cut -d " " -f2- > rockyou_length-list.txt
```

Convert uppercase to lowercase and the opposite
```
# cat file.txt | tr [A-Z] [a-z] > lower-case.txt
```
```
# cat file.txt | tr [a-z] [A-Z] > upper-case.txt
```

Remove blank lines with sed
```
# sed -i '/^$/d' List.txt
```

Remove defined character with sed
```
# sed -i "s/'//" file.txt
```

Delete a string with sed
```
# echo 'This is a foo test' | sed -e 's/<foo>//g'
```

Replace characters with tr
```
# cat emails.txt | tr '@' '#'
```
OR
```
# sed 's/@/#' file.txt
```

Print specific columns with awk
```
# awk -F "," '{print $3}' infile.csv > outfile.csv
```
OR

```
# cut -d "," -f 3 infile.csv > outfile.csv
```

Note: if you want to isolate all columns after column 3 use
```
# cut -d "," -f 3- infile.csv > outfile.csv
```

Generate Random Passwords with urandom
```
# cat /dev/urandom | tr -dc 'a-zA-Z0-9._!@#$%^&*()' | fold -w 8 | head -n 500000 > wordlist.txt
```
```
# cat /dev/urandom | tr -dc 'a-zA-Z0-9-_!@#$%^&*()_+{}|:<>?=' | fold -w 12 | head -n 4
```
```
# cat /dev/urandom | base64 | tr -d '[^:alnum:]' | cut -c1-10 | head -2
```
```
# cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 4
```
```
# cat /dev/urandom| tr -dc 'a-zA-Z0-9-_!@#$%^&*()_+{}|:<>?='|fold -w 12| head -n 4| grep -i '[!@#$%^&*()_+{}|:<>?=]'
```
```
# < /dev/urandom tr -dc '[:print:]' |fold -w 10| head -n 10
```
```
# tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n2
```

Remove Parenthesis with tr
```
# cat in_file | tr -d '()' > out_file
```

Generate wordlists from your file-names
```
# ls -A | sed 's/regexp/& /g'
```

Process text files when cat is unable to handle strange characters
```
# sed 's/([[:alnum:]]*)[[:space:]]*(.)(..*)/12/' *.txt
```

Generate length based wordlists with awk
```
# awk 'length == 10' file.txt > 10-length.txt
```

Merge two different txt files
```
# paste -d' ' file1.txt file2.txt > new-file.txt
```

Faster sorting
```
# export alias sort='sort --parallel=<number_of_cpu_cores> -S <amount_of_memory>G ' && export LC_ALL='C' && cat file.txt | sort -u > new-file.txt
```

Mac to unix
```
# tr '15' '12' < in_file > out_file
```

Dos to Unix
```
# dos2unix file.txt
```

Unix to Dos
```
# unix2dos file.txt
```

Remove from one file what is in another file
```
# grep -F -v -f file1.txt -w file2.txt > file3.txt
```

Isolate specific line numbers with sed
```
# sed -n '1,100p' test.file > file.out
```

Create Wordlists from PDF files
```
# pdftotext file.pdf file.txt
```

Find the line number of a string inside a file
```
# awk '{ print NR, $0 }' file.txt | grep "string-to-grep"
```


For faster grepping use all the above grep regular expressions with the command ag. The following is a proof of concept of its speed:

```
# time cat *.txt | ack-grep -o "[a-zA-Z0-9.#?$*_-]+@[a-zA-Z0-9.#?$*_-]+.[a-zA-Z0-9.-]+" > /dev/null
real    1m2.447s
user    1m2.297s
sys 0m0.645s
```

```
# time cat *.txt | egrep -o "[a-zA-Z0-9.#?$*_-]+@[a-zA-Z0-9.#?$*_-]+.[a-zA-Z0-9.-]+" > /dev/null
real    0m30.484s
user    0m30.292s
sys 0m0.310s
```

```
# time cat *.txt | ag -o "[a-zA-Z0-9.#?$*_-]+@[a-zA-Z0-9.#?$*_-]+.[a-zA-Z0-9.-]+" > /dev/null
real    0m4.908s
user    0m4.820s
sys 0m0.277s
```