#! /bin/bash
env='speil-env'
rm -rf $env
virtualenv -p /usr/bin/python $env
source $env/bin/activate
pip install -r requirements.txt

