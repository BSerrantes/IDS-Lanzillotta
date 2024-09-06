#!/bin/bash

echo "Ingrese el nombre del nuevo proyecto: "
read proyecto

mkdir $proyecto
cd $proyecto
mkdir .venv
touch app.py
mkdir templates
mkdir static
pipenv install flask
pipenv shell

