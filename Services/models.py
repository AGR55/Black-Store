from django.utils import timezone
from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services')
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['created']

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"
