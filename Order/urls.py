from django.urls import path
from Order import views

urlpatterns = [
    path('pedidos/', views.process_order, name='ProcessOrder')
]
