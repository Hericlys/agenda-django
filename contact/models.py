from django.db import models
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    phone = models.CharField(max_length=17)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
