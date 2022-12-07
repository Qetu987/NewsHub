from blog.views import (
    PostsList, 
    AddPost, 
    TagPost, 
    HotPost, 
    LikePost, 
    LikePostList, 
    Terms_view
    )
from django.urls import path


urlpatterns = [
    path('', PostsList.as_view(), name='home'),
    path('terms/', Terms_view.as_view(), name='terms'),
    path('create_post/', AddPost.as_view(), name='add_post'),
    path("hot_post/", HotPost.as_view(), name='hot_post'),
    path("likes_post/", LikePostList.as_view(), name='like_post_list'),
    path("like/", LikePost.as_view(), name='like'),
    path("tag/<slug:slug>/", TagPost.as_view(), name='tag_post'),
]