import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
from django.contrib import admin

def get_request(url, **kwargs):
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def get_dealers_from_cf(url, **kwargs):
    results = {}
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        for objects in json_result:
            if isinstance(json_result[objects], list):
                dealers = json_result[objects]
                for dealer_doc in dealers:
                    # Get its content in `doc` object
                    # Create a CarDealer object with values in `doc` object
                    dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                        dealer_id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                        short_name=dealer_doc["short_name"],
                                        st=dealer_doc["st"], zip=dealer_doc["zip"])
                    results.append(dealer_obj)

    return results

def get_dealers_from_dict(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(
                address=dealer_doc["address"], 
                city=dealer_doc["city"], 
                full_name=dealer_doc["full_name"],
                dealer_id=dealer_doc["id"], 
                lat=dealer_doc["lat"], 
                long=dealer_doc["long"],
                short_name=dealer_doc["short_name"],
                st=dealer_doc["st"], 
                zip=dealer_doc["zip"]
            )

            results.append(dealer_obj)
    return results

def get_all_reviews_from_dict(url):

    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        reviews = json_result["rows"]
        
        results = {}
        # For each dealer object
        for review in reviews:
            # Get content of 'doc' subdict
            # See bottom of this file for sample review JSON object
            review_doc= review["doc"]
            review_id = review_doc["id"]
            results[review_id] = {}

            keys = list(review_doc.keys())
            for n in range(2, len(keys)):
                key = list(review["doc"].keys())[n]
                value = review_doc[key]
                results[review_id][key] = value
        results = list(results.values())
    return results

def get_reviews_from_dict(url, **kwargs):

    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        reviews = json_result["docs"]
        results = {}
        # For each dealer object
        for review in reviews:
            review_id = review["dealership"]
            results[review_id] = {}
            keys = list(review.keys())
            for n in range(2, len(keys)):
                key = list(review.keys())[n]
                value = review[key]
                results[review_id][key] = value
        results = list(results.values())
    return results

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative


#sample review JSON object
#{
# "id": "8c1cb81af0a1d8ab5201c34008e44f68",
# "key": "8c1cb81af0a1d8ab5201c34008e44f68",
# "value": {
#  "rev": "1-6d3a316e140863cdb147048888d26051"
# },
# "doc": {
#  "_id": "8c1cb81af0a1d8ab5201c34008e44f68",
#  "_rev": "1-6d3a316e140863cdb147048888d26051",
#  "id": 1,
#  "name": "Berkly Shepley",
#  "dealership": 15,
#  "review": "Total grid-enabled service-desk",
#  "purchase": true,
#  "purchase_date": "07/11/2020",
#  "car_make": "Audi",
#  "car_model": "A6",
#  "car_year": 2010
# }
#}