from django.db import models
from users.models import User


class Tags(models.Model):
    text = models.CharField('Текст', max_length=100)
    
    def __str__(self):
        return f'{self.id}_{self.text}'
    

class Post(models.Model):
    title = models.CharField('Название', max_length=300)
    text = models.TextField('Текст поста', blank=True, null=True)
    poster = models.ImageField("Постер", upload_to="blog/", blank=True, null=True)
    draft = models.BooleanField("Черновик", default=False)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания", blank=True)
    tag = models.ManyToManyField(Tags, verbose_name='теги')
    
    def __str__(self):
        return f'{self.title}'

    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_by')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_by_likes')
    created = models.DateTimeField(auto_now_add=True)


class Reviews(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания", blank=True)

    def __str__(self):
        return f"{self.owner} - {self.post}"
