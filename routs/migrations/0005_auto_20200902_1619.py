# Generated by Django 3.1 on 2020-09-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routs', '0004_auto_20200830_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='hotel_Main_Img',
            field=models.ImageField(default='hotelsample.jpg', null=True, upload_to='images/'),
        ),
    ]
