#!/bin/bash

if [ $# -lt 1 ]
then
    echo "Debe ingresar como parámetro el nombre de un archivo"
    exit
fi

echo "Elegir alguna de las siguientes opciones."
echo "1- Ingresar palabra y reemplazarla por ****  en el archivo pasado por parámetro"
echo "2- Abrir el archivo"
echo "3- Realizar una copia de seguridad"
echo "4- Ingresar un mail y validarlo mediante RE."
echo "5- Salir"

read a
case $a in 
1) echo "Ingresar palabra y reemplazarla por *** en el archivo"
    read palabra
    sed -i 's/'$palabra'/****/g' $1
    ;;
2) echo "Abrir el archivo"
   cat $1
   ;;
3) echo "Realizar una copia de seguridad"
   cp $1 menu_copia.sh
   ;;
4) echo "Ingresar un mail y validarlo mediante RE."
   read correo
   regex="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
   if [[ $correo =~ $regex ]]; then
	echo "$correo es una dirección de correo válida."
   else
	echo "$correo no es una dirección de correo válida."
   fi
   ;;
5) echo "Salir"
   ;;
esac




