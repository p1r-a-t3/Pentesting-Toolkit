#!/bin/bash

FILE=~/Desktop/test/ghost
FILE1=~/Desktop/test/cpghost


while [[ true ]]
do 
  if [ -f $FILE ]
    then
       cp $FILE $FILE2 
       echo got it
  fi
  sleep 2
done
