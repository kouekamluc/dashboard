from django.shortcuts import render
from dashregistration.forms import UserCreationForm

# Create your views here.

def profile(request):
    return render(request, 'profiles/profile.html')


def profileSecurity(request):
    return render(request, 'profiles/profile-security.html')

def profileSettings(request):
    user=request.user
    form = UserCreationForm(instance=user)
    context = {'form':form}
    
    return render(request, 'profiles/profile-settings.html' , context)



def profileNotification(request):
    return render(request, 'profiles/profile-notification.html')