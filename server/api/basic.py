from zlib import DEF_BUF_SIZE
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
import json

json_result = {"docs": [
    {"_id": "bd2d2ba98192df415b097d8b130b7b8c", "_rev": "1-34e7ebd07643af43db578a46ee1d6365", "id": 1, "city": "El Paso", "state": "Texas", "st": "TX", "address": "3 Nova Court", "zip": "88563", "lat": 31.6948, "long": -106.3, "short_name": "Holdlamis", "full_name": "Holdlamis Car Dealership"}, 
    {"_id": "bd2d2ba98192df415b097d8b130b9f9e", "_rev": "1-a79013b42c83451d49e7e3aba4a575e3", "id": 4, "city": "Dallas", "state": "Texas", "st": "TX", "address": "85800 Hazelcrest Circle", "zip": "75241", "lat": 32.6722, "long": -96.7774, "short_name": "Solarbreeze", "full_name": "Solarbreeze Car Dealership"}, 
    {"_id": "bd2d2ba98192df415b097d8b130bcd24", "_rev": "1-63f1a1984f40f1de1eabceaec90f7fb6", "id": 9, "city": "Dallas", "state": "Texas", "st": "TX", "address": "253 Hanson Junction", "zip": "75216", "lat": 32.7086, "long": -96.7955, "short_name": "Job", "full_name": "Job Car Dealership"}, 
    {"_id": "bd2d2ba98192df415b097d8b130c0593", "_rev": "1-018064051a79bae4a38595f6d712f1f4", "id": 15, "city": "San Antonio", "state": "Texas", "st": "TX", "address": "5057 Pankratz Hill", "zip": "78225", "lat": 29.3875, "long": -98.5245, "short_name": "Tempsoft", "full_name": "Tempsoft Car Dealership"}, 
    {"_id": "bd2d2ba98192df415b097d8b130c1347", "_rev": "1-cfc990372e5aead5c1461c5363ab9661", "id": 16, "city": "El Paso", "state": "Texas", "st": "TX", "address": "0 Rieder Trail", "zip": "79994", "lat": 31.6948, "long": -106.3, "short_name": "Treeflex", "full_name": "Treeflex Car Dealership"}, 
    {"_id": "bd2d2ba98192df415b097d8b130c5fb2", "_rev": "1-0d1ad5ed7cfde86fde2b69345e3b8163", "id": 27, "city": "San Antonio", "state": "Texas", "st": "TX", "address": "95321 Superior Hill", "zip": "78245", "lat": 29.4189, "long": -98.6895, "short_name": "Namfix", "full_name": "Namfix Car Dealership"}, 
    {"_id": "bd2d2ba98192df415b097d8b130c7046", "_rev": "1-bc91c48db51d66e73a2e6b759f566014", "id": 30, "city": "Houston", "state": "Texas", "st": "TX", "address": "5423 Spaight Road", "zip": "77218", "lat": 29.834, "long": -95.4342, "short_name": "Opela", "full_name": "Opela Car Dealership"}, 
    {"_id": "bd2d2ba98192df415b097d8b130ca3bb", "_rev": "1-6e07d6d5c6d7a616ba7b7358db413d1a", "id": 38, "city": "Dallas", "state": "Texas", "st": "TX", "address": "821 New Castle Trail", "zip": "75226", "lat": 32.7887, "long": -96.7676, "short_name": "Zamit", "full_name": "Zamit Car Dealership"}], 
    "bookmark": "g1AAAABweJzLYWBgYMpgSmHgKy5JLCrJTq2MT8lPzkzJBYorJKUYpRglJVpaGFoapaSZGJomGViap1gkGRobJCcaJyWB9HHA9BGlIwsAwGsfFw", "warning": "No matching index found, create an index to optimize query time."}


print('*****************************')
print(json_result)
print('*****************************')
print(json_result['docs'][4]['st'])
print('*****************************')

for objects in json_result:
    if isinstance(json_result[objects], list):
        dealers = json_result[objects]
        print(dealers[0])
        print(dealers[0]['state'])

        
        for dealer in dealers:
            print(dealer['state'])

