#! /bin/bash
env='speil-env'
rm -rf $env
virtualenv -p /usr/bin/python3 $env
source $env/bin/activate
python setup.py

