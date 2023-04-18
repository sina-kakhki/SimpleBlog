from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(CreateView):
    model: Post
    template_name = 'post_create.html'
    fields = '__all__'

class PostUpdate(UpdateView):
    model: Post
    template_name = 'post_update.html'
    fields = '__all__'

class PostDelete(DeleteView):
    model: Post
    template_name = 'post_delete.html'
    fields = '__all__'