from django import forms
from routs.models import Hotels , Appartement




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
        fields=['town', 'cost', 'mirpeset','address', 'pieces','surface', 'app_image' ]


class RequestForm(forms.ModelForm):
    class Meta:
        model= Appartement
        fields=['town', 'cost', 'mirpeset', 'pieces','surface', 'app_image' ]










