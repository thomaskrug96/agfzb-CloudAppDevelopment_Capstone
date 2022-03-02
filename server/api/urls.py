from django.urls import path
from . import views

urlpatterns = [
    path('dealerships/', views.get_dealerships),
    path('reviews/<str:pk>/<int:val>/', views.get_reviews_filtered),
    path('dealerships/<str:pk>/<str:val>/', views.get_dealerships_filtered),  
    #path('dealerships/(?P<pk>\w+)', views.get_dealerships_filtered),
    path('reviews/', views.get_reviews),
]

'''
url(r'^emp_detail/(?P<user_name>\w+)/(?P<mobile_number>\d{10,18})/$', 
views.emp_detail, name='emp_detail'),
'''

