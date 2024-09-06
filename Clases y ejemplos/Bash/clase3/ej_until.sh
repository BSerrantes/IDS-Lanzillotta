#!/bin/bash

until (( num > 5 && num <10 ))
do
	#generamos un número random entre 1 y 10
	num=$(( (RANDOM % 10) +1 ))
	echo "El número generado es: $num"
done
echo "Se termina el loop!, último nro generado: $num"
