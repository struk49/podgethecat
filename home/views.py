from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html")


def contacts(request):
    return render(request, 'home/contacts.html')
