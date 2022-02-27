from django.urls import path
from . import views

urlpatterns = [
    path('dealerships/', views.get_dealerships),
    path('dealerships/<str:pk>/<str:val>/', views.get_dealerships_filtered),
    path('reviews/', views.get_reviews),
]
