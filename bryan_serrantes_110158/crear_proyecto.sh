#!/bin/bash

mkdir ParcialIDS
cd ParcialIDS
mkdir .venv
mkdir static
mkdir templates
touch app.py
cd static 
mkdir css
mkdir images
cd ..


pipenv shell
pipenv install flask


