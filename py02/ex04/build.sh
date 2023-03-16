#!/bin/bash
# Actualiza pip
pip install --upgrade pip
# Construye el paquete en formato wheel
python ./my_minipack/setup.py bdist_wheel
# Construye el paquete en formato tar.gz
python ./my_minipack/setup.py sdist --formats=gztar