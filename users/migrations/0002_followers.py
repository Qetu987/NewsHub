# Generated by Django 4.1.2 on 2022-10-20 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата подписки')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('follow_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_by', to=settings.AUTH_USER_MODEL, verbose_name='Подписан на')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
        ),
    ]
