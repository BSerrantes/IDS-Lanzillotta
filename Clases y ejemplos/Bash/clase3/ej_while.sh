#!/bin/bash

contador=0

while [ $contador -lt 5 ]
do
	let contador++
	echo "Bienvenido por vez número: $contador"
done
