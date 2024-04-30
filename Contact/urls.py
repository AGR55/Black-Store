from django.urls import path
from Contact import views

urlpatterns = [
    path('contact/', views.contact, name='Contact'),
]