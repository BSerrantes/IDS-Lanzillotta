#!/bin/bash

i=0
sum=0
while [ $i -lt 10 ]
do
    echo "Ingrese un número:"
    read x
    sum=$(( sum + x))
    ((i++))
done

echo $sum
