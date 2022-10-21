from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def loginpage(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "dashregistration/login.html")


def loggoutpage(request):
    logout(request)
    return redirect("login")


def registerView(request):

    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User name already exists') 
                return redirect('register')
            else:
               user = User.objects.create_user(username=username, password=password1, first_name=firstname,last_name=lastname)
               user.save()
       
               login(request, user)
               return redirect("home")
        
    else:
    
        return render(request, "dashregistration/register.html" )
