from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "home/index.html", {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'home/contacts.html')


def about(request):
    return render(request, 'home/about.html')



def privacy(request):
    return render(request, 'home/privacy.html')


def terms(request):
    return render(request, 'home/terms.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'home/signup.html', {
        'form': form
    })

def logout_user(request):
    logout(request)
    return render(request, 'home/logout.html')