#!/bin/bash


#si la cantidad de param es < 1, le informa al user
# el pesos numeral ($#) te dice la cantidad de param que le estás pasando al script


if [ $# -lt 1 ]
then
	echo "Debe ingresar como parámetro el nombre de un archivo"
	exit
fi

echo "1- Ver el contenido del archivo $1"
echo "2- Editar el archivo $1 con el editor de nano"
echo "3- Ver permisos del archivo $1"
echo "*- Salir"

read a
case $a in

1) echo "Ver el contenido del archivo $1"
	cat $1
	;;
2) echo "Editar el archivo $1 con el editor nano"
	nano $1
	;;
3) echo "Ver permisos del archivo $1"
	ls -l $1
	;;
*) echo "Salir"
	;;
esac
