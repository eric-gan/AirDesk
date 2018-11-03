from pymongo import MongoClient
from flask import Flask
import googlemaps

# setup
gmaps = googlemaps.Client(key='AIzaSyB0mxT2fWkC1tsdGcxD5_rWpLxPsHoKEVQ')
client = MongoClient()
db = client.airdesk
spaces = db.spaces

# converts locations to latitude, longitude
locations = []
for space in spaces:
    geocode_result = gmaps.geocode(space)
    locations.append(geocode_result[0]['geometry']['location'])






# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result[0]['geometry']['location'])
# for i in geocode_result[0]:
#     print(i)
