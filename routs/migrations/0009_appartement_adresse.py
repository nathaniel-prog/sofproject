# Generated by Django 3.1 on 2020-09-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routs', '0008_auto_20200912_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='adresse',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
