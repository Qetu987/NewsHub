from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from blog.models import Post, Tags
from blog.forms import PostForm


class TagsList:
    def get_tags(self):
        return Tags.objects.all()


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