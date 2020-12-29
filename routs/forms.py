from bemember.forms import PersonForm
from media.images.forms import  HotelForm , AppartForm
from django import forms
from bemember.models import Post
from routs.models import Town



class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'size': '40'}))




class PostForm(forms.Form):
    class Meta:
        model=Post
        fields = ['titre','author','body','post_date','likes']




class TownForm(forms.ModelForm):
    class Meta:
        model=Town
        fields = ['name']













