from django.urls import path
from . import views



urlpatterns = [
    path('homepage/', views.homepage, name='home'),
    path('dashboardAnalytics/', views.dashboardAnalytics, name='dashboardanalytics'),
    path('dashboardSaas/', views.dashboardSaas, name='dashboardsaas'),
    path('dashboardSales/', views.dashboardSales, name='dashboardsales'),
    path('dashboardSystem/', views.dashboardSystem, name='dashboardsystem'),
    
]
