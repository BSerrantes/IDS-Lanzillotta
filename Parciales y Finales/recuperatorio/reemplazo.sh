#!/bin/bash

archivo="$1"

sed -i 's/Pasta frola/Pasta frola de la abuela/g' "$archivo"

echo "Reemplazo realizado en el archivo $archivo."
