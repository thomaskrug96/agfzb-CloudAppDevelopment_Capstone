from django.urls import path
from . import views

urlpatterns = [
    path('dealerships/', views.get_dealerships),
    path('reviews/', views.get_reviews),
]
