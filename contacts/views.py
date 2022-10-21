from django.shortcuts import render

# Create your views here.


def contactGrid(request):
    return render(request, 'contacts/contacts-grid.html')


def contactList(request):
    return render(request, 'contacts/contacts-list.html')

def  contactNew(request):
    return render(request, 'contacts/contacts-new.html')