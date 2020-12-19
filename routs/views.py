from django.shortcuts import render , redirect , get_object_or_404
from django.views import generic
from django.http import Http404 , HttpResponse
from bemember.models import Post
from .models import Town , Hotels ,Appartement , User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from media.images.forms import  HotelForm , AppartForm , RequestForm , PostForm
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView , CreateView










@login_required

def home(request ):
    towns = Town.objects.all().order_by('id')
    appartments = Appartement.objects.all()

    tlv= Town.objects.get(id=1)
    count_htlv= Hotels.objects.filter(town__name='tel-aviv').count()
    best_hotel= Hotels.objects.filter(rates__gt=5)


    context={'towns':towns,'count_htlv':count_htlv, 'tlv':tlv ,  'appartments':appartments, 'besthotels':best_hotel}






    return render(request, 'blog/home.html', context )

def town(request, town_id):
    try:
        town=Town.objects.get(id=town_id)
        hotels = Hotels.objects.filter(town=town).all()
        count = Hotels.objects.filter(town=town).count()
    except Town.DoesNotExist:
      raise Http404(" this town dosn't exist")


    return render(request,'blog/town.html',{'town':town , 'hotels':hotels, 'count': count})



def LikeViews(request,pk):
   hot=get_object_or_404(Appartement,id=request.POST.get('appart_id'))
   hot.likes.add(request.user)

   return HttpResponseRedirect(reverse('appart', args=[str(pk)]))


def Show_number(request,pk):
   hot=get_object_or_404(Appartement,id=request.POST.get('appart_id'))
   hot.address

   return HttpResponseRedirect(reverse('appartement', args=[str(pk)]))






def hotel(request, hotel_id):
    hotel = Hotels.objects.get(id=hotel_id)

    hotel_pic = Hotels.objects.filter(hotel_Main_Img=hotel)


    context = {'hotel': hotel,
               'hotel_pic': hotel_pic,  }
    return render(request, 'blog/hotel.html',context)






def cheap(request):

    moneys= Hotels.objects.filter(cost= 150)
    return render(request,'blog/cheap.html',{'moneys':moneys})









def search(request ):


    if request.method=='POST':
        query=request.POST["q"]

        if query:
            qs=Hotels.objects.filter(Q(name__icontains=query)|
                                     Q(cost__icontains=query)

                               )
            resultas=qs.count()
            if qs:
                return render(request,'blog/search.html',{'results':qs,'count':resultas})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('search')



    return render(request,'blog/search.html')




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
    if request.method=='POST':
        query = request.POST["appart_id"]
        if query:
            qs=Appartement.objects.all()
            if qs:
                return render(request, 'blog/appartements.html', {'results': qs})

            else:
                 return HttpResponseRedirect('appartements')

    app=Appartement.objects.all().order_by('cost')
    return render(request,'blog/appartements.html', {'appartements':app })













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

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)









class ListAppart(ListView):
    queryset = Appartement.objects.all()
    template_name = 'blog/appartement_list.html'


    def search(self,query=None):
        requet= self.request.user
        if query is not None :
            requet=query
            return requet







class DetailAppartViews(DetailView):
    model = Appartement
    template_name = 'blog/appartement_detail.html'

    def get_context_data(self, *args,**kwargs):
        context=super(DetailAppartViews, self).get_context_data()
        stuff = get_object_or_404(Appartement, id=self.kwargs['pk'])
        total_likes = stuff.totalikes()
        context['totalikes']= total_likes


        return context






class PostCreateView(CreateView):
    model=Post
    fields = ['titre', 'body','author', 'post_date']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


































































