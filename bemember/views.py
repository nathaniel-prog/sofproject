from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login , authenticate
from .models import Post
from .forms import PersonForm, MyUserCreationForm
from .models import User
from django.http import HttpResponseRedirect



def home(request):
    counts= User.objects.all().count
    return render(request,'profile/welcome.html',{'counts':counts})


def log_in(request):
    return render(request, 'profile/login.html', )





def register(request):
    if request.method == 'GET':
        form = MyUserCreationForm()
        return render(request, 'profile/register.html', {'form': form})

    else:

        if request.method == 'POST':
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
            return HttpResponseRedirect('home')




































