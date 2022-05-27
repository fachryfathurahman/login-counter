#!/bin/bash

IPAddress=()

read -p "How many AlphaClient do you have?: " n

for (( c=0; c<n; c++))
do
  echo "Enter IP Address $((c+1)): "
  read io
  IPAddress[$c]=${io}
  #read -p "Enter IP address $c: " IPAddress
done

clear

while true
do
  for i in ${IPAddress[@]}
  do
    test=$(curl -sk "$i/info")
    echo $test
  done
  sleep 2
  clear
done