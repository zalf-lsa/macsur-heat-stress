#!/usr/bin/python
# -*- coding: ISO-8859-15-*-

# pragma pylint: disable=mixed-indentation

import zmq
import json
import sys

print "pyzmq version: ", zmq.pyzmq_version()
print "sys.path: ", sys.path
print "sys.version: ", sys.version

def main():
	context = zmq.Context()
	socket = context.socket(zmq.PULL)
	socket.connect("tcp://10.10.26.34:6667")

	#consumerSocket = context.socket(zmq.PUSH)
	#consumerSocket.connect("tcp://localhost:7777");
	
	#workerControlSocket = context.socket(zmq.PUB)
	#consumerSocket.bind("tcp://*:6666");

	#time.sleep(2)

	#for i in range(1):
	i = 0
	while True:
		j = socket.recv_json()
		print "received job ", i 
		i = i + 1

	# Start your result manager and workers before you start your producers
	
	#time.sleep(10)
	#workerControlSocket.send("finish " + json.dumps({"type": "finish"}))
	#consumerSocket.send_json({"type": "finish"})


main()