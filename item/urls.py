from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('add/', views.add, name="add"),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]