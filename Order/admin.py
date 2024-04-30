from django.contrib import admin
from Order.models import Order, OrderLine

# Register your models here.

admin.site.register([Order, OrderLine])
