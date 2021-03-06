# Generated by Django 3.1 on 2020-09-10 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routs', '0005_auto_20200902_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(default=150, null=True)),
                ('mirpeset', models.BooleanField(default=None, null=True)),
                ('parking', models.BooleanField(default=None, null=True)),
                ('air_conditioner', models.BooleanField(default=True, null=True)),
                ('comment', models.TextField(max_length=500)),
                ('app_image', models.ImageField(default='hotelsample.jpg', null=True, upload_to='images/')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routs.town')),
            ],
        ),
    ]
