from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import UserProfile

class UserForm(UserCreationForm):
    class Meta():
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta():
        fields= ('bio', 'personal_site', 'profile_pic')
        model = UserProfile
