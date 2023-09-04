from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=128, default="Undefined")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self. author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')