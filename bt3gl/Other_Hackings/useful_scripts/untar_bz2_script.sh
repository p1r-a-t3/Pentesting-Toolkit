#!/bin/sh
for file in *.tar.bz2;
do mkdir -p "${file}-extracted";
tar --directory "${file}-extracted" -xjf "${file}";
done