from django.urls import path
from blog.views import PostDetail, HomeView, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('post_detail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('post_update/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
]