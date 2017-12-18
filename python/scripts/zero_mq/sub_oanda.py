import sys
import zmq
import simplejson as json
port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
topicfilter = "GBP_USD"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
socket.setsockopt(zmq.SUBSCRIBE, "1")
print "Collecting updates from weather server..."
socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)

# Subscribe to zipcode, default is NYC, 10001


# Process 5 updates
total_value = 0
for update_nbr in range(5000):
    response = socket.recv_string().decode()
    topic, messagedata = response.split()
    time, bid, ask = messagedata.split('\x01')
    # msg = json.dumps(messagedata)
    # total_value += int(messagedata)
    print topic, time, bid, ask

print "Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr)

