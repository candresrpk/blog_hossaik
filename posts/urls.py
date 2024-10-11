from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
)


app_name = 'posts'


urlpatterns = [
    path('list/', PostListView.as_view(), name='posts_list'),
    path('detail/<slug>/', PostDetailView.as_view(), name='posts_detail'),
    path('create/', PostCreateView.as_view(), name='posts_create'),
    path('delete/<id>/', PostDeleteView.as_view(), name='posts_delete'),
    path('update/<id>/', PostUpdateView.as_view(), name='posts_update'),
    
]
