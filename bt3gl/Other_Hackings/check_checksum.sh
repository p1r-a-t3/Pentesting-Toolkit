#!/bin/bash

# usage:
# ./check_checksum.sh <file> <hash>

filehash=`sha1sum $1`

echo "Checking file: $1, calculated as $filehash"
echo "Using SHA1 file: $2"

if [ $filehash != $2 ]
then
  echo "MD5 sums mismatch!!!"
else
  echo "Checksums OK."
fi
