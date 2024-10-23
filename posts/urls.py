from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    like,
)


app_name = 'posts'


urlpatterns = [
    path('list/', PostListView.as_view(), name='posts_list'),
    path('create/', PostCreateView.as_view(), name='posts_create'),
    path('detail/<slug>/', PostDetailView.as_view(), name='posts_detail'),
    path('delete/<slug>/', PostDeleteView.as_view(), name='posts_delete'),
    path('update/<slug>/', PostUpdateView.as_view(), name='posts_update'),
    path('like/<slug>/', like, name='post_like'),
    
]
