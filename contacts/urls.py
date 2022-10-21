from django.urls import path
from . import views


urlpatterns = [
    path('contactGrid/', views.contactGrid , name='contactgrid'),
    path('contactList/', views.contactList , name='contactlist'),
    path('contactNew/', views.contactNew, name='contactnew'),
]
