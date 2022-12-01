from django.contrib import admin
from blog.models import Post, Reviews, Tags, Like
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_image', 'draft', 'owner', 'date']
    list_display_links = ['id','title']
    list_search = ['id', 'title', 'text']
    list_filter = ['draft', 'owner']

    readonly_fields = ('get_image', )
    
    def get_image(self, obj):
        try:
            a = mark_safe(f'<img src={obj.poster.url} width="100" height="110">')
        except:
            a = None
        return a
    get_image.short_description = "Изображение"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'text', 'parent', 'post', 'date']
    list_display_links = ['id','owner']
    list_search = ['id', 'owner', 'text']

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_display_links = ['id','text']
    list_search = ['id', 'text']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user']
    list_display_links = ['id','post']
    list_search = ['id', 'user']