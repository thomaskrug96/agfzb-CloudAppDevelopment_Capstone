from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

from zlib import DEF_BUF_SIZE
from cloudant.client import Cloudant
from cloudant.error import CloudantException


from .forms import *
from .decorators import *
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_request` view to handle sign in request
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('djangoapp:home')
            else: 
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'djangoapp/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('djangoapp:login')

# Create a `registration_request` view to handle sign up request
def registrationPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)

            return redirect('djangoapp:login')

    context = {'form':form}
    return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


def aboutPage(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)

def contactPage(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

# Create a `registration_request` view to handle sign up request
# Create a `registration_request` view to handle sign up request
def add_review(request):
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
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
            doc['name'] = form['name'].data
            doc['dealership'] = form['dealership'].data
            doc['review'] = form['review'].data
            doc['purchase'] = form['purchase'].data

            print(doc)

            db.create_document(doc, throw_on_exists=False)
            messages.success(request, 'success!')
            return redirect('djangoapp:home')
    else:
        form = CreateReviewForm()

    context = {'form':form}
    return render(request, 'djangoapp/add_review.html', context)

