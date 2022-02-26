from rest_framework.response import Response
from rest_framework.decorators import api_view
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

cloudant_credentials = {
    "COUCH_URL": "https://59e8d0a8-4b92-4e5f-b6e9-97065c14665c-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "gmRktU8iPRLIMuP7TU0KxMV0bJZ3VYKw7opsQpCqCGEW",
    "COUCH_USERNAME": "59e8d0a8-4b92-4e5f-b6e9-97065c14665c-bluemix"
}


def main(dict, databaseName):
    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )
        print("Databases: {0}".format(client.all_dbs()))

        db = client[databaseName]
        
        for instance in db:
            print(instance)
        
        result = {}
    
        for i, instance in db.items():
            result[i] = instance 

    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}
    return result

@api_view(['GET'])
def get_dealerships(request):
    #person = {'name':'Dennis', 'age':28}
    data = main(cloudant_credentials, 'dealerships')
    return Response(data)


@api_view(['GET'])
def get_reviews(request):
    #person = {'name':'Dennis', 'age':28}
    data = main(cloudant_credentials, 'reviews')
    return Response(data)

