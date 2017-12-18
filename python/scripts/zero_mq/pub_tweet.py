import zmq
import random
import sys
import time

port = "5557"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
zmq_socket = context.socket(zmq.PUB)

# Update
# zmq_socket.setsockopt(zmq.ZMQ_IMMEDIATE, 1)
zmq_socket.setsockopt(zmq.SNDBUF, 10240)
zmq_socket.setsockopt(zmq.SNDHWM, 10000)
# zmq_socket.setsockopt(zmq.SWAP, 25000000)

zmq_socket.bind("tcp://*:%s" % port)


#!/usr/bin/python2.7

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------

from twitter import *
import re
import twitter
search_term = "bitcoin, etherium, crypto"
#SELECT text, geohash FROM "tweet" WHERE geohash !~ /[.]/ AND text =~ /eur*/

#search_term = "euro,dollar,yen,gold,oil,Austral,Norw,Swiss,Canad,pound"

#-----------------------------------------------------------------------
# import a load of external features, for text display and date handling
# you will need the termcolor module:
#/home/sdreep/nabla/python/scripts/twitter-stream-search-location.py
# pip install termcolor
#-----------------------------------------------------------------------
from time import strftime
import zmq
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

import simplejson as json

import pygeohash as pgh

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
# config = {}
# execfile("config.py", config)
# Account textolytics@gmail.com
consumer_key = 'YnH734IEAE0gxCa2hupX70KJQ'
consumer_secret = 'ohMDIJO8BwuFLV1d1NdHnWnmKWT8zXzg0QL9BHS07o5D5dtylq'
access_key = '769882262208974848-EEPdY1hzDvNJ5CQbJgwoVhGI5MIJqDF'
access_secret = 'IpYvXUXcNDwkOmhvqGWktn7EtTGTdvMG1dLCWUDdGimbl'

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
stream = TwitterStream(auth = auth, secure = True)

#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
#-----------------------------------------------------------------------
tweet_iter = stream.statuses.filter(track = search_term)

pattern = re.compile("%s" % search_term, re.IGNORECASE)

def twitter():
    try:
        for tweet in tweet_iter:
            tweet_id = tweet["id_str"]
            location_colored = colored(tweet["user"]["location"],"red")
            place = json.dumps(tweet['place'])
            location = tweet["user"]["location"]
            timestamp = parsedate(tweet["created_at"])
            # now format this nicely into HH:MM:SS format
            timetext = strftime("%Y%m%d%H%M%S", timestamp)
            retweet_count =  tweet["retweet_count"]
            # colour our tweet's time, user and text
            time_colored = colored(timetext, color = "white", attrs = ["bold"])
            user_colored = colored(tweet["user"]["screen_name"], "green")
            user = tweet["user"]["screen_name"]
            followers_count = tweet["user"]["followers_count"]
            lang = tweet["user"]["lang"]
            text = tweet["text"]
            # Sentiment analysis
            # positive_score, negative_score = sentiment_analysis_predict(text)
            # symbols = tweet["entities"]["symbols"]
            time_zone = tweet["user"]["time_zone"]
            statuses_count = tweet["user"]["statuses_count"]
            # replace each instance of our search terms with a highlighted version
            text_colored = pattern.sub(colored(search_term.upper(), "yellow"), text)
            # add some indenting to each line and wrap the text nicely
            indent = " " * 0
            text_colored = fill(text_colored, 180, initial_indent = indent, subsequent_indent = indent)
            coordinates = json.dumps(tweet['coordinates'])
            long = 0
            lat = 0
            geohash = ''
            pgeoa = ''
            pgeob = ''
            pgeoc = ''
            pgeod = ''
            if place != 'null':
                place_keys = tweet['place'].keys()
                # print (place_keys)
                place_tag = []

                place_tag = tweet['place']['bounding_box']['coordinates']
                for fields in place_tag:
                    for i, f in enumerate(fields):
                        if i == 0:
                            pgeoalat = f[1]
                            pgeoalong = f[0]
                            print (colored(pgeoalat, "blue"), colored(pgeoalong, "blue"))
                            geohash = pgh.encode(pgeoalat, pgeoalong)
                        if i == 1:
                            pgeob = pgh.encode(f[0], f[1])
                        if i == 2:
                            pgeoc = pgh.encode(f[0], f[1])
                        if i == 3:
                            pgeod = pgh.encode(f[0], f[1])
                    # print (pgeoa, pgeob, pgeoc, pgeod)
                polygon = tweet['place']['bounding_box']
                # print (colored(place_tag, "blue"))
                if coordinates != 'null':
                    coordinates_keys = tweet['coordinates'].keys()
                    coordinates = str(tweet['coordinates']['coordinates'])
                    # print (coordinates_keys)
                    # print (tweet['coordinates']['coordinates'])
                    long = tweet['coordinates']['coordinates'][1]
                    lat = tweet['coordinates']['coordinates'][0]
                    geohash = pgh.encode(long, lat)
                    # print (long, lat, colored(geohash, "green"))

            # positive_score_colored =  colored(positive_score,"green")
            # negative_score_colored = colored(negative_score,"red")
            time_zone_colored = colored(time_zone,"blue")
            print ("%s|  %s %s | %s |%s| @%s |%s| [%s] %s %s" % (
                tweet_id, time_colored, time_zone_colored, location_colored, user_colored,
                statuses_count,
                followers_count, lang, retweet_count, text_colored))
            topic = 'tweet'
            messagedata = (tweet_id, time, time_zone, location, user_colored, statuses_count,followers_count, lang, retweet_count, text)
            zmq_socket.send_string( "%s %s" % (topic , messagedata) )
            # if geohash != '':
            #     myclient.write_points(tweet_json)

    except zmq.ZMQError as e:
        print("ZMQError:", 'Error %s' % e)


def main():
    twitter()

if __name__ == '__main__':

    main()

















