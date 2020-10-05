from django.shortcuts import render , redirect , get_object_or_404
from django.views import generic
from django.http import Http404 , HttpResponse
from bemember.models import Post
from .models import Town , Hotels ,Appartement , User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login as auth_login
from media.images.forms import  HotelForm , AppartForm , RequestForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView , CreateView








@login_required

def home(request ):
    towns = Town.objects.all().order_by('id')
    Jerusalem=Town.objects.get(id=2)



    return render(request, 'blog/home.html', {'towns':towns ,'Jerusalem':Jerusalem} )

def town(request, town_id):
    try:
        town=Town.objects.get(id=town_id)
        hotels = Hotels.objects.filter(town=town).all()
        count = Hotels.objects.filter(town=town).count()
    except Town.DoesNotExist:
      raise Http404(" this town dosn't exist")


    return render(request,'blog/town.html',{'town':town , 'hotels':hotels, 'count': count})



def LikeViews(request,pk):
    hot=get_object_or_404(Hotels,id=request.POST.get('hotel_id'))
    hot.likes.add(request.user)
    return HttpResponseRedirect(reverse('hotel', args=[str(pk)]))




def hotel(request, hotel_id):
    hotel = Hotels.objects.get(id=hotel_id)

    hotel_pic = Hotels.objects.filter(hotel_Main_Img=hotel)
    nbroflike= Hotels.objects.filter(likes=hotel_id).count

    context = {'hotel': hotel,
               'hotel_pic': hotel_pic,   'counts': nbroflike }
    return render(request, 'blog/hotel.html',context)






def cheap(request):

    moneys= Hotels.objects.filter(cost= 150)
    return render(request,'blog/cheap.html',{'moneys':moneys})









def search(request ):
    context = {}

    if request.GET:
        kwarg=request.GET["q"]
        context['kwarg']= str(kwarg)
        if kwarg is not None:
            context = {"Jerusalem": ["capital", 'historic town', 'touristic town', 600000],
                       'netanya': 'touristic town',
                       'haifa': 3}



    return render(request,'blog/search.html', {'kwarg': context})




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




def myappart(request):
    budget = Appartement.objects.filter(cost__lt=260)
    if request.method == 'POST':
        form = AppartForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            app_image_view = form.instance

        return render(request, 'blog/myappart.htmL', {'form': form, 'img_obj': app_image_view ,'budgets':budget })
    else:
        form = AppartForm()
    return render(request, 'blog/myappart.htmL', {'form': form})




def notation(request):
    post=Post.objects.all()
    user= request.user
    context={"posts":post,
             "users":user}


    return render(request, 'blog/notation.html', context)



def appartements(request):
    app=Appartement.objects.all().order_by('cost')
    cont={ 'name': 'nathan',
           'age' : 31}


    return render(request,'blog/appartements.html', {'appartements':app, 'fou': cont['age'] })













def all_post(request):
    post=Post.objects.all()
    return render(request,'blog/allpost.html', {'posts':post})


def look_app(request):
    lbudget = Appartement.objects.filter(cost__lt=200)
    hbudget = Appartement.objects.filter(cost__gt=500)
    telaviv= Town.objects.get(id=1)
    el_se=Town.objects.all()

    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            app_image_vieuw = form.instance
            context={'form': form, 'img_obj': app_image_vieuw, 'lbudgets': lbudget ,
                     'hbudgets':hbudget,'tel-aviv':telaviv ,'else': el_se}


        return render(request, 'blog/look_app.htmL', context )
    else:
        form = RequestForm()
    return render(request, 'blog/look_app.htmL', {'form': form})



class PostHotel(ListView):
    model=Post
    template_name = 'blog/hotel.html'
    context_object_name = 'posts'








class ListAppart(ListView):
    queryset = Appartement.objects.all()
    template_name = 'blog/appartement_list.html'


class DetailAppartViews(DetailView):
    queryset = Appartement.objects.all()
    model = Appartement
    template_name = 'blog/appartement_detail.html'


class PostCreateView(CreateView):
    model=Post
    fields = ['titre', 'body']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






























































