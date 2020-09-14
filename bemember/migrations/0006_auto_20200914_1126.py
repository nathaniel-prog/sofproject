# Generated by Django 3.1 on 2020-09-14 08:26

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bemember', '0005_auto_20200909_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='whats in your mind '),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=datetime.date(2020, 9, 14)),
        ),
    ]
