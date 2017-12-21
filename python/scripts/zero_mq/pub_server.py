import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)

# Update
# socket.setsockopt(zmq.ZMQ_IMMEDIATE, 1)
socket.setsockopt(zmq.SNDBUF, 10240)
socket.setsockopt(zmq.SNDHWM, 10000)
# socket.setsockopt(zmq.SWAP, 25000000)

socket.bind("tcp://*:%s" % port)



while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print ("%d %d" % (topic, messagedata))
    socket.send("%d %d" % (topic, messagedata))
    # time.sleep(1)
