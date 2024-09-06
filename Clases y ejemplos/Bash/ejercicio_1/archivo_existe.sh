#!/bin/bash

echo "Ingrese el nombre del archivo para ver si existe:"
read nombre_archivo

if [ -f $nombre_archivo ]; then
	echo "El archivo "$nombre_archivo" existe."
	cat $nombre_archivo
	cp $nombre_archivo datos_personales_modif.txt
	echo "Ingrese una palabra a sustituir:"
	read old_text
	echo "Ingrese la palabra sustituta:"
	read new_text
	sed -i "s/"$old_text"/"$new_text"/g" datos_personales_modif.txt
	cat datos_personales_modif.txt
	echo "datos_personales_modif.txt"
else
	echo "El archivo "$nombre_archivo" no existe."
fi


