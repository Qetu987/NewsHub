from django.urls import path, include
from users.views import Register, Follow, Unfollow

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('follow/', Follow.as_view(), name='follow'),
    path('unfollow/', Unfollow.as_view(), name='unfollow'),
]
