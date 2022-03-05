from django import forms
from .models import movie

class Movieforms(forms.ModelForm):
    class Meta :
        model = movie
        fields=['name','desc','year','img']
