# Generated by Django 4.1.2 on 2022-10-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_poster_alter_post_text_alter_reviews_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(default=0, help_text='указывать кол-во лайков', verbose_name='лайки'),
        ),
    ]