# Generated by Django 3.1 on 2020-09-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caland', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(),
        ),
    ]
