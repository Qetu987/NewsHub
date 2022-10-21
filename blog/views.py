from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from blog.models import Post, Tags
from blog.forms import PostForm
from users.models import User, Followers
from django.db.models import Count
from django.contrib.auth.models import AnonymousUser


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

class PostsList(TagsList, View):
    template_name = "blog/post_list.html"
    anonimys = AnonymousUser()
    
    def get_data(self):
        queryset = Post.objects.filter(draft=False).order_by('-date')
        
        context = {
            'posts_list': queryset,
            'get_tags': self.get_tags(),
            'get_top_users': self.get_top_users(),
            'get_following': self.get_following() if self.request.user!=self.anonimys else None,
        }

        return context

    def get(self, request):
        context = self.get_data()
        return render(request, self.template_name, context)



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

class TagPost(TagsList, View):
    template_name = "blog/post_list.html"
    
    def get_data(self, slug):
        posts = Post.objects.filter(draft=False, tag__text=slug).order_by("-date")
        
        context = {
            'posts_list': posts,
            'get_tags': self.get_tags(),
            'get_top_users': self.get_top_users(),
            'get_following': self.get_following(),
        }

        return context

    def get(self, request, slug):
        context = self.get_data(slug)
        return render(request, self.template_name, context)

class HotPost(PostsList):
    template_name = "blog/post_list.html"
    
    def get_data(self):
        followers = [follower.follow_by for follower in self.request.user.following.all()]
        followers.append(self.request.user)
        queryset = Post.objects.filter(draft=False, owner__in=followers).order_by("-date")
        
        context = {
            'posts_list': queryset,
            'get_tags': self.get_tags(),
            'get_top_users': self.get_top_users(),
            'get_following': self.get_following(),
        }

        return context

    def get(self, request):
        context = self.get_data()
        return render(request, self.template_name, context)
        