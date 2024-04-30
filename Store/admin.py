from django.contrib import admin
from Store.models import Product, CategoryProduct

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'modified']


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'modified']


admin.site.register(CategoryProduct, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
