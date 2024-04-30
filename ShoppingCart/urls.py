from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>', views.add_product, name='add_product'),
    path('substract/<int:product_id>', views.subtract_product, name='subtract_product'),
    path('remove/<int:product_id>', views.remove_product, name='remove_product'),
    path('clear/', views.clear_cart, name='clear_cart'),
]

