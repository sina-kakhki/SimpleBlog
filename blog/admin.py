from blog.models import Post, Category, Profile, Comment
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
