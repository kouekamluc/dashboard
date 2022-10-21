from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render(request, 'dashadmin/home.html')

@login_required(login_url='login')
def dashboardAnalytics(request):
    return render(request,'dashadmin/dashboard-analytics.html')


@login_required(login_url='login')
def dashboardSystem(request):
    return render(request,'dashadmin/dashboard-system.html')


@login_required(login_url='login')
def dashboardSales(request):
    return render(request,'dashadmin/dashboard-sales.html')


@login_required(login_url='login')
def dashboardSaas(request):
    return render(request,'dashadmin/dashboard-saas.html')