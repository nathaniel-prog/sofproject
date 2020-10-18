from django.db import models
import datetime
from django.contrib.auth.models import User



class MyProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    colorofeyes = models.CharField( max_length= 100)



class Post(models.Model):
    titre= models.CharField(max_length=150,default='it was nice', null=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    body= models.TextField(default='whats in your mind ')
    post_date=models.DateField(default=datetime.date.today())
    likes= models.ManyToManyField(User , related_name='hotel_like')


    def __str__(self):
        return f' {self.author} has said {self.titre} '

    def total_like(self):
        return self.likes.count()















# Create your models here.
