from django.contrib.auth.views import LoginView
from django.urls import path
from .views import RegisterView, log_out, log_in

urlpatterns = [
    path('register/', RegisterView.as_view(), name='Auth'),
    path('logout/', log_out, name='Logout'),
    path('login/', log_in, name='Login')
]
