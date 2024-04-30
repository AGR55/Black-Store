from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CategoryPost(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    category = models.ManyToManyField(CategoryPost)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
