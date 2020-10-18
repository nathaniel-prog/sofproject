from django.db import models
from django.contrib.auth.models import User
from bemember.models import Post
from django.db.models import Q

import datetime

d= datetime.date.today()


class PostquerySet(models.QuerySet):
    def search(self,query=None):
        qs=self
        if query is not None:
            or_lookup= (Q(name__icontains=query)|
                        Q(address__icontains=query)|
                        Q(town__icontains=query))

            qs=qs.filter(or_lookup).distinct()
            return qs

class PostManager(models.Manager):
    def get_queryset(self):
        return PostquerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)









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
























