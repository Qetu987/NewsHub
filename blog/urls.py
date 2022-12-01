from blog.views import PostsList, AddPost, TagPost, HotPost, LikePost
from django.urls import path


urlpatterns = [
    path('', PostsList.as_view(), name='home'),
    path('create_post/', AddPost.as_view(), name='add_post'),
    path("hot_post/", HotPost.as_view(), name='hot_post'),
    path("like/", LikePost.as_view(), name='like'),
    path("tag/<slug:slug>/", TagPost.as_view(), name='tag_post'),
]