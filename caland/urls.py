from django.urls import path
from .  views import *
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index,name='index'),
    path('mydates',views.mydates , name='mydates'),
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    ]