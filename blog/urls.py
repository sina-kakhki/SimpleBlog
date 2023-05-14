from django.urls import path
from blog.views import PostDetail, HomeView, PostCreate, PostUpdate, PostDelete, CategoryUpdate, CategoryCreate, \
    CategoryDetail, CategoryDelete, CategoryList, ProfileCreate

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('post_detail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('post_update/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
    path('category_create/', CategoryCreate.as_view(), name='category-create'),
    path('category_update/<int:pk>', CategoryUpdate.as_view(), name='category_update'),
    path('category_delete/<int:pk>', CategoryDelete.as_view(), name='category_delete'),
    path('category_detail/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('category_list/', CategoryList.as_view(), name='category_list'),
    path('profile_create/', ProfileCreate.as_view(), name='profile_create'),
]
