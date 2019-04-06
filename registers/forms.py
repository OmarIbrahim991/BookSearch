from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = User
        fields = ("id", "username", "password", "email",)

class CustomChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ("id", "username", "password", "email",)

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", )