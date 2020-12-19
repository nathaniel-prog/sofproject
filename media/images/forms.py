from django import forms
from routs.models import Hotels , Appartement
from bemember.models import Post




class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotels
        fields=['name', 'rates', 'town', 'cost','hotel_Main_Img' ]

        widget = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                  'rates': forms.NumberInput(attrs={'class': 'form-control'}),
                  'town': forms.Select(attrs={'class': 'form-control'}),
                  'cost': forms.NumberInput(attrs={'class': 'form-control'})}


class AppartForm(forms.ModelForm):
    class Meta:
        model= Appartement
        fields=['town', 'cost', 'address', 'pieces','surface', 'app_image' ]


class RequestForm(forms.ModelForm):
    class Meta:
        model= Appartement
        fields=['town', 'cost',  'pieces','surface', 'app_image' ]


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['titre','author','body']














