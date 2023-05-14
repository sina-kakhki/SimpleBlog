from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    # create display label
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)  # we using category1 because category was used in the previous example.
    # login user, add user to post
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')
    likes = models.ManyToManyField(User, related_name='user_likes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Profile(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    web_page = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='profile')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Comment(models.Model):
    comment = RichTextField()
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.post.title

