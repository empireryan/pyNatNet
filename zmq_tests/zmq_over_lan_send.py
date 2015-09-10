import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://204.102.224.3:5000')

for i in range(10):
    msg = "msg_{}".format(i)
    socket.send(msg)
    print "Sending", msg
    msg_in = socket.recv()
