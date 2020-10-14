from bemember.forms import PersonForm
from media.images.forms import  HotelForm , AppartForm
from django import forms
from bemember.models import Post



class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'size': '40'}))




class PostForm(forms.Form):
    class Meta:
        Model=Post










