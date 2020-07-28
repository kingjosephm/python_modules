#!/bin/bash

mkdir -p "../data/$(date +%F)"

echo "Creating new Python virtual environment"
python -m venv "../data/$(date +%F)"

# need to make sure call new python
newpip="$PWD/../data/$(date +%F)/Scripts/pip3.exe"
newpython="$PWD/../data/$(date +%F)/Scripts/python.exe"

# install packages to run script
cat requirements.txt | xargs -n 1 $newpip install

echo "Getting a current list of all Anaconda distribution packages"
$newpython get_anaconda_packages.py

# concatenate extra packages to Anaconda list
cat "extra_packages.csv" >> "$PWD/../data/$(date +%F)/anaconda_pkg_list/packages.txt"

# package-by-package install of Anaconda packages
cat "$PWD/../data/$(date +%F)/anaconda_pkg_list/packages.txt" | xargs -n 1 $newpip install

echo "Done."
read -p $'\nPress any key to close session...\n'