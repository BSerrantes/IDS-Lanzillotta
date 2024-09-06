#!/bin/bash

echo -n "Ingrese una extension:"
read x

if [ -z $x ]; then
echo "No se encontró el archivo"d
else 
echo "Se encontraron los archivos"
fi

ls *$x
