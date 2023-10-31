from django.urls import path

from . import views

app_name = 'home'

urlpatterns= [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('singup/', views.signup, name='signup'),
]