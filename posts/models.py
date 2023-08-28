from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self. author)