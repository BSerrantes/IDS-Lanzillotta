#!/bin/bash

parametro="$1" # El primer parámetro ingresado

if [ -f "$parametro" ]; then  #con -f verifico si un archivo f file
    echo "$parametro es un archivo."
    cat $parametro
elif [ -d "$parametro" ]; then  #con -d verifico si es un directorio d dir
    echo "$parametro es una carpeta."
    ls $parametro
else
    echo "$parametro no existe o no es un archivo ni una carpeta."
fi
