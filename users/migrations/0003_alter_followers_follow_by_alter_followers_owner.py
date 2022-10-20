# Generated by Django 4.1.2 on 2022-10-20 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='follow_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Подписан на'),
        ),
        migrations.AlterField(
            model_name='followers',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
