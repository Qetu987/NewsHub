from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Followers(models.Model):
    owner = models.ForeignKey(User, related_name='following', verbose_name="Владелец", on_delete=models.CASCADE)
    follow_by = models.ForeignKey(User, related_name='followers', verbose_name="Подписан на", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата подписки", blank=True)
    draft = models.BooleanField("Черновик", default=False)