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

def calc_distance(user_loc, space):
    """
    Finds the distance between the user location and a given space using Google Maps API

    param user_loc: The user's location in lat/long coordinates
    type user_loc: dict

    param space: The space's location in lat/long coordinates
    type space: dict

    rval: The distance between the locations
    rtype: double
    """
    geocode_result = gmaps.geocode(space['_location'])
    dest_loc = geocode_result[0]['geometry']['location']
    direction = gmaps.distance_matrix(user_loc, dest_loc, mode="walking")
    distance = direction['rows'][0]['elements'][0]['distance']['value']
    # convert to mile
    distance = distance * 0.000621371
    return distance

user_loc = get_user_location('1600 Amphitheatre Parkway, Mountain View, CA') # change me later

# read database
db = client.airdesk
collection = db.listings
listings = collection.find()

# find the closest spaces to user location
distances = []
for space in listings:
    distance = calc_distance(user_loc, space)
    distances.append((space['_id'], distance))

distances = sorted(distances, key=lambda k: k[1])
spaces = [loc[0] for loc in distances]
