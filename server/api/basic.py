from zlib import DEF_BUF_SIZE
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
import json

mydict = {
    "COUCH_URL": "https://59e8d0a8-4b92-4e5f-b6e9-97065c14665c-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "gmRktU8iPRLIMuP7TU0KxMV0bJZ3VYKw7opsQpCqCGEW",
    "COUCH_USERNAME": "59e8d0a8-4b92-4e5f-b6e9-97065c14665c-bluemix"
}

client = Cloudant.iam(
    account_name=mydict["COUCH_USERNAME"],
    api_key=mydict["IAM_API_KEY"],
    connect=True,
)

databaseName = 'dealerships'
db = client[databaseName]

result = db.all_docs(include_docs=True)
print('*****************************')
print(result)
print('*****************************')
