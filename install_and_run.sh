#!/bin/bash

# this scripts assumes that python3 and pip3 is installed
# rabbitmq must also be installed.
# run rabbitmq on a separate window on localhost with
# the command 'rabbitmq-server'

pip3 install virtualenv
virtualenv -p python3 ministock
source ministock/bin/activate
pip install pika
python application.py
