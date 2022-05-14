from .models import Comment
from django import forms




class UserDeleteForm(forms.Form):
   
    delete = forms.BooleanField(required=True)