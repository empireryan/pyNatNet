import zmq
from  motive_client import OptitrackProcessor as optitrack
import json
import msgpack

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://204.102.224.3:5000')

processor = optitrack()

# for i in range(10):
#    msg = "msg_{}".format(i)
#    socket.send(msg)
#    print "Sending", msg
#    msg_in = socket.recv()

while (1):
    position, orientation = processor.recv_data(rigid_body_ids=[1])
    socket.send(msgpack.packb(position + orientation))
    msg_in = socket.recv()
