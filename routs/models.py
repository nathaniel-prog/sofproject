from django.db import models
from django.contrib.auth.models import User

import datetime

d= datetime.date.today()

class Town(models.Model):
    name= models.CharField(max_length=100,  unique=True )
    image_town = models.FileField(default='hotelsample.jpg', upload_to='images/', null=True)


    def __str__(self):
        return f' {self.name} '


class Hotels(models.Model):
    name= models.CharField(max_length=300)
    rates= models.IntegerField(null= True )
    town= models.ForeignKey(Town,on_delete=models.CASCADE)
    cost = models.IntegerField( null=False,default=150)
    hotel_Main_Img = models.FileField(default='hotelsample.jpg',upload_to='images/', null= True  )


    def __str__(self):
        return f" from {self.town}  we have {self.name} "

   


class Appartement(models.Model):
    town= models.ForeignKey(Town, on_delete=models.CASCADE)
    address=models.CharField(max_length=200,null=True)
    cost = models.IntegerField(null=True, default=150)
    pieces= models.IntegerField(null=False, default=3)
    surface=models.IntegerField(null=False, default= 90)
    mirpeset= models.BooleanField(default=None, null=True)
    parking=models.BooleanField(default=None , null=True)
    air_conditioner= models.BooleanField(default=True, null=True)
    comment= models.TextField(max_length=500)
    app_image = models.ImageField(default='hotelsample.jpg', upload_to='images/', null=True)
    likes= models.ManyToManyField(User, related_name='Appart_like')


    def totalikes(self):
        return self.likes.count()

    def __str__(self):
        return f" {self.address} cost {self.cost}"
























