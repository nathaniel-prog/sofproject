# Generated by Django 3.0.8 on 2020-08-17 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Tel-Aviv', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('rates', models.IntegerField(null=True)),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routs.Town')),
            ],
        ),
    ]
