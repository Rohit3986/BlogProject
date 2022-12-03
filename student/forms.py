
from dataclasses import field
from urllib import request
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
class Student(AuthenticationForm):
    class Meta:
        model=User
        fields=['first_name','email','last_name']
        label={"first_name":"your_name"}

class EditProfile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','email','last_name']
        label={"last_login":"recent_login"}

class EditAdminProfile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields="__all__"
        label={"last_login":"recent_login"}

class post_blog(forms.Form):
    title=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'enter title...'}))
    category=forms.ChoiceField(choices=(("python","python"),("java","java"),("c++","c++")))
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description here...'}))

