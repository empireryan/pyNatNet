import zmq

context = zmq.Context()

sock = context.socket(zmq.REP)
PORT = 5000
# sock.connect('tcp://204.102.224.2:{}'.format(PORT))
sock.connect('tcp://127.0.0.1:{}'.format(PORT))

while True:
    # sock.send("wieners")
    message = sock.recv()
    print message
    # response = handle_message(message)
    sock.send(message)
