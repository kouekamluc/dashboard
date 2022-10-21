from django.shortcuts import render

# Create your views here.

def pageOrders(request):
    return render(request, 'pages/page-orders.html')



def pageInvoice(request):
    return render(request, 'pages/page-invoice.html')



def pageTimeline(request):
    return render(request, 'pages/page-timeline.html')



def pageBlank(request):
    return render(request, 'pages/page-blank.html')



def page404(request):
    return render(request, 'pages/page-404.html')



def page500(request):
    return render(request, 'pages/page-500.html')