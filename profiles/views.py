from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.

def profile(request):
    return render(request, 'profiles/profile.html')


def profileSecurity(request):
    
    return render(request, 'profiles/profile-security.html')

def profileSettings(request):
    
    
    return render(request, 'profiles/profile-settings.html' )



def profileNotification(request):
    return render(request, 'profiles/profile-notification.html')