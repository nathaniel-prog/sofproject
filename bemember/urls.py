from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from . import views

urlpatterns = [
    path('register',views.register, name='register'),
    path('login/', LoginView.as_view(template_name='profile/login.html' ), name='login'),
    path('logout', LogoutView.as_view(template_name= 'profile/logout.html'),name='logout'),
    path('',views.home , name= 'welcome')



    ]



