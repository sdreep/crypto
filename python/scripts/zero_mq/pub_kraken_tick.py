import ccs
import simplejson as json
import zmq
import sys

port = "5558"
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

schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getTickerInformation"]
response = ccs.kraken.public.getTradableAssetPairs ()
msg=json.loads(response)
instruments = msg['result']
instrument_list = ','.join ( [str ( instrument ) for instrument in instruments] )

while True:
    response = ccs.kraken.public.getTickerInformation(pair=instrument_list)
    msg = json.loads(response)
    ticks = msg['result']

    for tick in ticks:
        instrument = str ( tick )
        tick = ticks[instrument]
        ask_price, ask_whole_lot_volume, ask_lot_volume = tick['a']
        bid_price, bid_whole_lot_volume, bid_lot_volume = tick['b']
        last_trade_price, last_trade_lot_volume = tick['c']
        volume_today, volume_last_24_hours = tick['v']
        vwap_today, vwap_last_24_hours = tick['p']
        number_of_trades_today,number_of_trades_last_24_hours = tick['t']
        low_today, low_last_24_hours = tick['l']
        high_today, high_last_24_hours = tick['h']
        opening_price = tick['o']




        messagedata = str(instrument ) + "\x01" + str ( volume_today ) + "\x01" + str (  volume_last_24_hours  ) + "\x01" + str ( vwap_today ) + "\x01" + str (  vwap_last_24_hours  ) + "\x01" + str ( number_of_trades_today ) + "\x01" + str ( number_of_trades_last_24_hours  ) + "\x01" + str ( low_today ) + "\x01" + str (  low_last_24_hours  ) + "\x01" + str ( high_today ) + "\x01" + str (  high_last_24_hours  ) + "\x01" + str ( opening_price)

        # topic_instrument = str(instrument)
        # socket.send_string( "%s %s" % (topic_instrument , messagedata) )

        topic = 'kraken_tick'
        socket.send_string( "%s %s" % (topic , messagedata) )

        # print(instrument,volume_today, volume_last_24_hours ,vwap_today, vwap_last_24_hours ,number_of_trades_today,number_of_trades_last_24_hours ,low_today, low_last_24_hours ,high_today, high_last_24_hours ,opening_price)

