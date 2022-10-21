from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile , name='profile'),
    path('profilesecurity/', views.profileSecurity , name='profilesecurity'),
    path('profileSettings/', views.profileSettings, name='profilesettings'),
    path('profileNotification/', views.profileNotification, name='profilenotification'),
]
