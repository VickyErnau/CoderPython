from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email= forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'first_name', 'last_name',]
    
class UpdateUserForm(UserChangeForm):
    password=None
    email= forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name',]

