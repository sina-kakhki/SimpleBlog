from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    # create display label
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 default=None)  # we using category1 because category was used in the previous example.
    # login user, add user to post
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
