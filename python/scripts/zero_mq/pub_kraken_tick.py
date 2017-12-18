import ccs
import simplejson as json

instruments = ['XZECZEUR','BCHEUR','BCHUSD','XXMRZUSD']
# instruments = "XZECZEUR.BCHEUR.BCHUSD"
# instruments = ['XBTEUR','XXBTZUSD']
instruments = "XXBTZUSD"
schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getTickerInformation"]
print (schema)
while True:
    # print (response)
    response = ccs.kraken.public.getTickerInformation ( instruments )

    msg = json.loads(response)
    # print (msg)
    ticks = msg['result']
    for tick in ticks:
        instrument = str(tick)
        tick = ticks[tick]
        ask_price, ask_whole_lot_volume, ask_lot_volume = tick['a']
        bid_price, bid_whole_lot_volume, bid_lot_volume = tick['b']
        last_trade_price, last_trade_lot_volume = tick['c']
        volume_today, volume_last_24_hours = tick['v']
        vwap_today, vwap_last_24_hours = tick['p']
        number_of_trades_today,number_of_trades_last_24_hours = tick['t']
        low_today, low_last_24_hours = tick['l']
        high_today, high_last_24_hours = tick['h']
        opening_price = tick['o']
    print(instrument,volume_today, volume_last_24_hours ,vwap_today, vwap_last_24_hours ,number_of_trades_today,number_of_trades_last_24_hours ,low_today, low_last_24_hours ,high_today, high_last_24_hours ,opening_price)


# for tick in ticks:
#
#     print (tick['a'])
#
# while True:
#     for item in msg:
#         print (msg[item])
