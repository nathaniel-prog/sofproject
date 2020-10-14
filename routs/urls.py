from django.urls import path
from . views import *
from . import views
from .views import   ListAppart , DetailAppartViews , PostHotel, PostCreateView , LikeViews,Show_number
from media.images import forms
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/', views.home, name='home'),
    path('town/<int:town_id>',  views.town, name='town'),
    path('hotel/<int:hotel_id>', views.hotel, name='hotel'),
    path('search',views.search, name='search'),
    path('hotelowner',views.hotelowner,name='hotelowner'),
    path('like/<int:pk>',LikeViews,name='like_app'),
    path('show/<int:pk>',LikeViews,name='show_num'),


    path('myappart',views.myappart, name='myappart'),
    path('cheap',views.cheap, name='cheap'),

    path('notation',views.notation , name= 'notation'),
    path('appartement',views.appartements, name='appartements'),
    path('post',views.all_post , name= 'post'),
    path('look_app', views.look_app ,name='look_app'),
    path('list_app',ListAppart.as_view()),
    path('list_app/<int:pk>', DetailAppartViews.as_view(), name= 'appart'),
    path('posts', PostHotel.as_view()),
    path('posts/new',PostCreateView.as_view(), name= 'postview')







]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)




