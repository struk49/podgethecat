from django.shortcuts import render

from item.models import Category, Item

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "home/index.html", {
        'categories': categories,
        'items': items,
    })


def contacts(request):
    return render(request, 'home/contacts.html')
