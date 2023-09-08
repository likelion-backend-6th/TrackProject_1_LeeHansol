from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    available = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name='items_joined', blank=True)

    def __str__(self):
        return self.title
