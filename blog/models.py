from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from datetime import datetime,date

class Post(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | '+ str(self.auther)

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))
        # return reverse('home')
