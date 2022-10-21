from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

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

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            form.save()
            print("post mmmmmmmmmmmmmmmmm")
            user = form.save(commit=False)
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)
                return redirect("home")
        else:
            print('error')

    else:
        form = CustomUserCreationForm()

    return render(request, "dashregistration/register.html", {"form": form})
