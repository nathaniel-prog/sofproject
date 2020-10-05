# Generated by Django 3.1 on 2020-10-01 18:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routs', '0013_hotels_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='likes',
            field=models.ManyToManyField(related_name='appart_as_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]