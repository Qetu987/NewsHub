from django.shortcuts import render, redirect
from django.views.generic.base import View
from blog.models import Post, Tags, Like
from blog.forms import PostForm, LikeForm
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

class Posts_list_base(TagsList, View):
    template_name = "blog/post_list.html"
    anonimys = AnonymousUser()

    def get_post_data(self, queryset):
        data = list()
        for post in queryset:
            post_data = {
                'post_data': post,
                'user_likes': [i['user'] for i in Like.objects.values('user').filter(post=post)],
            }
            data.append(post_data)
        return data
    
    def get(self, request):
        context = self.get_data()
        return render(request, self.template_name, context)


class PostsList(Posts_list_base):
    template_name = "blog/post_list.html"
    anonimys = AnonymousUser()
    
    def get_data(self):
        queryset = Post.objects.annotate(post_likes=Count('post_by_likes')).filter(draft=False).order_by('-date')
        data = self.get_post_data(queryset)

        context = {
            'posts_list': data,
            'get_tags': self.get_tags(),
            'get_top_users': self.get_top_users(),
            'get_following': self.get_following() if self.request.user!=self.anonimys else None,
        }

        return context

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

class TagPost(Posts_list_base):
    
    def get_data(self, slug):
        queryset = Post.objects.annotate(post_likes=Count('post_by_likes')).filter(draft=False, tag__text=slug).order_by("-date")
        data = self.get_post_data(queryset)

        context = {
            'posts_list': data,
            'get_tags': self.get_tags(),
            'get_top_users': self.get_top_users(),
            'get_following': self.get_following() if self.request.user!=self.anonimys else None,
        }

        return context

class HotPost(Posts_list_base):
    
    def get_data(self):
        followers = [follower.follow_by for follower in self.request.user.following.all()]
        followers.append(self.request.user)
        queryset = Post.objects.annotate(post_likes=Count('post_by_likes')).filter(draft=False, owner__in=followers).order_by("-date")
        data = self.get_post_data(queryset)

        context = {
            'posts_list': data,
            'get_tags': self.get_tags(),
            'get_top_users': self.get_top_users(),
            'get_following': self.get_following() if self.request.user!=self.anonimys else None,
        }

        return context

class LikePostList(Posts_list_base):
    def get_data(self):
        queryset = Post.objects.annotate(post_likes=Count('post_by_likes')).filter(draft=False, post_by_likes__user=self.request.user).order_by("-date")
        data = self.get_post_data(queryset)

        context = {
            'posts_list': data,
            'get_tags': self.get_tags(),
            'get_top_users': self.get_top_users(),
            'get_following': self.get_following() if self.request.user!=self.anonimys else None,
        }
        return context

class LikePost(View):
    anonimys = AnonymousUser()

    def post(self, request):
        form = LikeForm(request.POST)
        if form.is_valid() and request.user != self.anonimys:
            post = form.cleaned_data.get('post')
            likes = Like.objects.filter(post=post)
            if request.user in [like.user for like in likes]:
                obj = Like.objects.get(post=form.cleaned_data.get('post'), user=request.user)
                obj.delete()
            else:
                form = form.save(commit=False)
                form.user = request.user
                form.save()
        return redirect('home')

class Terms_view(View):
    template_name = "blog/terms_list.html"

    def get(self, request):
        return render(request, self.template_name)
