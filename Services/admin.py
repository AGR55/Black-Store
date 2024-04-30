from django.contrib import admin
from Services.models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'modified']
    list_filter = ['modified']
    ordering = ['created']
    list_per_page = 20


admin.site.register(Service, ServiceAdmin)
