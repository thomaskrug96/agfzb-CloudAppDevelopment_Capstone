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

dbName = 'dealerships'
pk = 'state'
val = 'Texas'

db = client[dbName]

selector = {pk: {'$eq': val}}
docs = db.get_query_result(selector)
for doc in docs:
    print(doc)

result = {}
for instance in docs.items():
    result[i] = instance 










'''


def main_filtered(dict, dbName, pk, val):
    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )

        print('YOU CALLED MAIN_FILTERED')
        print('YOUR PRIMARY KEY IS = ' + pk)
        print('YOUR VAL IS = ' + val)
        db = client[dbName]

        selector = {pk: {'$eq': val}}
        docs = db.get_query_result(selector)
        for doc in docs:
            print(doc)
        
        result = {}
        for i, instance in docs.items():
            result[i] = instance 

    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}
    return result

result = main_filtered(myDict, dbName, 'state', 'Texas')

print(result)


'''