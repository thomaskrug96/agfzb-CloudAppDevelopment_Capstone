from zlib import DEF_BUF_SIZE
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
import json

myDict = {
    "COUCH_URL": "https://59e8d0a8-4b92-4e5f-b6e9-97065c14665c-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "gmRktU8iPRLIMuP7TU0KxMV0bJZ3VYKw7opsQpCqCGEW",
    "COUCH_USERNAME": "59e8d0a8-4b92-4e5f-b6e9-97065c14665c-bluemix"
}

client = Cloudant.iam(
            account_name=myDict["COUCH_USERNAME"],
            api_key=myDict["IAM_API_KEY"],
            connect=True,
)

dbName = 'reviews'
db = client[dbName]

# Get number of documents in reviews db
i=0
for doc in db:
    i = i+1

# Initialize new document for POST request
doc = {}
doc['id'] = i+1
doc['name'] = 'test'
doc['dealership'] = 15
doc['review'] = 'Good stuff'
doc['purchase'] = False

print(doc)

db.create_document(doc, throw_on_exists=False)

for doc in db:
    print(doc)

'''
dbName = 'reviews'
pk = 'id'
val = 1
print(type(val))

db = client[dbName]

selector = {pk: {'$eq': val}}
docs = db.get_query_result(selector)
for doc in docs:
    print(doc)

'''