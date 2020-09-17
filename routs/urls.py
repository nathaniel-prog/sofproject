from django.urls import path
from . views import *
from . import views
from .views import LikeViews
from media.images import forms
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/', views.home, name='home'),
    path('town/<int:town_id>', views.town, name='town'),
    path('hotel/<int:hotel_id>', views.hotel, name='hotel'),
    path('search',views.search, name='search'),
    path('hotelowner',views.hotelowner,name='hotelowner'),

    path('myappart',views.myappart, name='myappart'),
    path('cheap',views.cheap, name='cheap'),
    path('display/<int:pk>',views.display_hotel_images, name='display'),
    path('like/<int:pk>', LikeViews , name='like_hotel'),
    path('notation',views.notation , name= 'notation'),
    path('appartement',views.appartements, name='appartements'),
    path('post',views.all_post , name= 'post'),
    path('look_app', views.look_app ,name='look_app')






]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)




