import zmq
import zmqnumpy as znp
import numpy as np

context = zmq.Context()

#Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:9010")

for request in range(10):
    random_npArr = np.random.rand(416,416)
    print("Send message")
    znp.send_array(socket, random_npArr)

    #Get the reply
    message = socket.recv()
    print("receive from server: ", message)