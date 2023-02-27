from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model=models.Contact
        fields=('name','email','subject','message')


class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')

class ProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','username')

class TrainerLogin(forms.ModelForm):
    class Meta:
        model=models.Trainer
        fields=('username','password')

class TrainerProfileForm(forms.Form):
    class Meta:
        model=models.Trainer
        fields={'full_name','mobile','address','detail','image'}