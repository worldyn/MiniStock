# MiniStock

A python code test where you run a mini-sized stock with an integer value as the stock amount. The stock object is kept
in memory when application.py is run. You can then create a bunch of clients by running user_interface.py. This is a 
code test which serves as an exercise to create a small but decoupled stock application that can be individually scaled.
The UI can probably be replaced with some kind of web app or something in real life.

# How to run on OS with UNIX terminal

1. Have python3 installed
2. Have pip3 installed
3. Have rabbitmq installed
4. Run rabbitmq on localhost with the command 'rabbitmq-server'on a separate terminal window
5. install virtualenv with pip: 'pip3 install virtualenv' 
6. create the virtual environment in this repository's main directory and name it ministock: 'virtualenv -p python3 ministock'
7. Activate the virtual environment in the main directory: 'source ministock/bin/activate'
8. install Pika, a python implementation of the AMQP (underlying protocol that rabbitmq uses): 'pip install pika'
9. Run application.py
10. open new window and activate the virtual environment and start user_interface.py
11. Open more clients with user_interface.py... and so on

NOTE: if you know what you're doing one can run the repository's shell script 

# Test this application / blow up your computer
1. Run test/test.py while the rabbitmq server is up and application.py is running.
2. Increase the PROCESSES_COUNT and run test/test.py in multiple windows
