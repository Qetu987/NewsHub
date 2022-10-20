from blog.views import PostsList, AddPost
from django.urls import path


urlpatterns = [
    path('', PostsList.as_view(), name='home'),
    path('create_post/', AddPost.as_view(), name='add_post'),
]