# Generated by Django 3.1 on 2020-09-15 07:18

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bemember', '0006_auto_20200914_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='hotel_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=datetime.date(2020, 9, 15)),
        ),
    ]