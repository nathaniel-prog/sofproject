from django.shortcuts import render , redirect
from django.http import Http404 , HttpResponse
from bemember.models import *
from .models import Town , Hotels ,Appartement
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login as auth_login
from media.images.forms import  HotelForm , AppartForm
from .forms import CommentForm








@login_required
def towns(request ):
    towns = Town.objects.all()
    return render(request, 'blog/towns.html', {'towns':towns } )

def town(request, town_id):
    try:
        tow=Town.objects.get(id=town_id)
        hotels = Hotels.objects.filter(town=tow).all()
        count = Hotels.objects.filter(town=tow).count()
    except Town.DoesNotExist:
      raise Http404(" this town dosn't exist")


    return render(request,'blog/town.html',{'town':tow , 'hotels':hotels, 'count': count})


def hotel(request, hotel_id):
    hotel = Hotels.objects.get(id=hotel_id)
    hotel_pic = Hotels.objects.filter(hotel_Main_Img=hotel)
    user_comment =Post.objects.filter(comment=User)
    others= Hotels.objects.exclude(id=hotel_id)
    return render(request, 'blog/hotel.html',

    context={'hotel': hotel ,
             'hotel_pic':hotel_pic,
             'comments':user_comment,
             'others':others})





def cheap(request):

    moneys= Hotels.objects.filter(cost= 150)
    return render(request,'blog/cheap.html',{'moneys':moneys})









def search(request):
    query=request.GET.get("q", None)
    towns = Town.objects.all()
    qs= Town.objects.all()
    if query is not None:
        qs.filter(Q(name__icontains=query))

    return render(request,'blog/search.html', {'towns':towns})




def hotelowner(request):
    if request.method == 'POST':
        form = HotelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            hotel_image_view = form.instance

        return render(request, 'blog/hotelowner.htmL', {'form': form,'img_obj':hotel_image_view})

    else:
        form = HotelForm()
    return render(request, 'blog/hotelowner.htmL', {'form' : form})





def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        hotels = Hotels.objects.all()
        return render(request, 'blog/display_hotel_images.html', {'hotel_images': hotels})






def myappart(request):
    if request.method == 'GET':
        form = AppartForm()
        return render(request, 'blog/myappart.htmL', {'form': form})

    if request.method == 'POST':
        form = AppartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('towns')












































