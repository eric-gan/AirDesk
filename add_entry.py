from pymongo import MongoClient

client = MongoClient('mongodb://eric:Cheesecaker1@cluster0-shard-00-00-f2g27.gcp.mongodb.net:27017,cluster0-shard-00-01-f2g27.gcp.mongodb.net:27017,cluster0-shard-00-02-f2g27.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')

# read database
db = client.airdesk
collection = db.listings

collection.insert(
    [
        {'_name': "HOUSE", '_location': "2400 Durant", '_desk': "dlkjfadls;jk", '_pictures': "pic",
            '_type': "desk", '_ratings': [], '_amenities': [], '_available': True, '_price': 5},
    ]
)