from django.urls import path
from .  views import *
from . import views
from media.images import forms
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('towns/', views.towns, name='towns'),
    path('towns/<int:town_id>', views.town, name='town'),
    path('hotel/<int:hotel_id>', views.hotel, name='hotel'),
    path('search',views.search, name='search'),
    path('hotelowner',views.hotelowner,name='hotelowner'),

    path('myappart',views.myappart, name='myappart'),
    path('cheap',views.cheap, name='cheap'),
    path('display',views.display_hotel_images, name='display'),




]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)




