from django.urls import reverse_lazy

from blog.forms import CreatePostForm
from blog.models import Post, Category, Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'index.html'


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryCreate(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'category_create.html'
    fields = '__all__'
    # fields = ('title', 'body')


class CategoryUpdate(UpdateView):
    model = Category
    # form_class = EditForm
    template_name = 'category_update.html'
    # fields = ['title', 'title_tag', 'body']


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')


class ProfileCreate(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    fields = '__all__'


class ProfileDetail(DetailView):
    model = Post
    template_name = 'profile_detail.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post_create.html'


class PostUpdate(UpdateView):
    model: Post
    template_name = 'post_update.html'
    fields = '__all__'


class PostDelete(DeleteView):
    model: Post
    template_name = 'post_delete.html'
    fields = '__all__'
