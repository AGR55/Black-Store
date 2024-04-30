from django.contrib import admin
from Blog.models import Post, CategoryPost

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'modified']


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'modified']


admin.site.register(Post, PostAdmin)
admin.site.register(CategoryPost, CategoryAdmin)
