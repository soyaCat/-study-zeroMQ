import zmq
import time
import zmqnumpy as znp
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9010")

while True:
    print("try recieve from client...")
    received_npArr = znp.recv_array(socket)
    print(np.shape(received_npArr))
    time.sleep(1)
    socket.send(b"received npArr")
