import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9010")

while True:
    # wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    # Do some 'work'
    time.sleep(1)

    #send reply back to client
    socket.send(b"World")
