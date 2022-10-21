from django.urls import path
from . import views

urlpatterns = [
    path("pageOrders/",  views.pageOrders, name="pageorders"),
    path("pageTimeline/",  views.pageTimeline, name="pagetimeline"),
    path("pageInvoice/", views.pageInvoice, name="pageinvoice"),
    path("pageBlank/", views.pageBlank, name="pageblank"),
    path("page404/", views.page404, name="page404"),
    path("page500/", views.page500, name="page500"),
]
