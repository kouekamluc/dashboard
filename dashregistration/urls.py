from django.urls import path
from . import views



urlpatterns = [
    path('', views.loginpage , name='login'),
    path('loggoutpage/', views.loggoutpage , name='loggout'),
    path('registerView',views.registerView, name='register'),
]
