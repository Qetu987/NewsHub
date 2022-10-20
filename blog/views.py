from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from blog.models import Post, Tags
from blog.forms import PostForm
from users.models import User, Followers
from django.db.models import Count


class TagsList:
    def get_tags(self):
        return Tags.objects.all()

    def get_top_users(self):
        return User.objects.annotate(followers_count=Count('followers')).all().order_by('-followers_count')[:5]

    def get_following(self):
        followers = Followers.objects.filter(owner=self.request.user)
        list_follow = list()
        for follower in followers:
            list_follow.append(follower.follow_by)
        return list_follow


class PostsList(TagsList, ListView):
    model = Post
    queryset = Post.objects.filter(draft=False).order_by('-date')
    context_object_name = 'posts_list'
    # template_name = 'blog/posts_list.html'

class AddPost(View):
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            
            tags = request.POST['tag'].split(' ')
            tags.pop()
            for tag in tags:
                form.tag.add(Tags.objects.get_or_create(text=tag)[0])
        return redirect('home')