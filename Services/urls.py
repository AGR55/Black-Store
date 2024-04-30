from django.urls import path
from Services import views

urlpatterns = [
    path('services/', views.services, name='Services'),
]
