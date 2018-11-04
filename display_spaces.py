from pymongo import MongoClient
from flask import Flask
from math import sin, cos, sqrt, atan2, radians
import googlemaps

# setup
gmaps = googlemaps.Client(key='AIzaSyB0mxT2fWkC1tsdGcxD5_rWpLxPsHoKEVQ')
client = MongoClient('mongodb://eric:Cheesecaker1@cluster0-shard-00-00-f2g27.gcp.mongodb.net:27017,cluster0-shard-00-01-f2g27.gcp.mongodb.net:27017,cluster0-shard-00-02-f2g27.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')

def get_user_location(loc):
    """
    Get the user's requested location of a study space
    
    param loc: The user's requested location
    type loc: str

    rval: The user's requested location in latitude, longitude
    rtype: dict
    """
    geocode_result = gmaps.geocode(loc)
    location = geocode_result[0]['geometry']['location']
    return location

def lat_lon_dist(lat1, lat2, lon1, lon2):
    """
    Returns the distance between two longitude and latitude coordinates
    
    param lat1, lat2, lon1, lon2: The two longitude and latitude coordinates.
    type loc: double

    rval: The distance between the locations.
    rtype: double
    """
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

user_loc = get_user_location('1600 Amphitheatre Parkway, Mountain View, CA') # change me later

db = client.airdesk
collection = db.listings
listings = collection.find()

locations = []
for space in listings:
    geocode_result = gmaps.geocode(space['_location'])
    locations.append(geocode_result[0]['geometry']['location'])







# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result[0]['geometry']['location'])
# for i in geocode_result[0]:
#     print(i)
