from PIL import Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-Type Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repassword']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ["username", "email"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control "}),
            "email": forms.TextInput(attrs={"class": "form-control "}),

        }

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["image","signature"]













    # def save(self):
    #     profile = super(ProfileUpdateForm, self).save()
    #     x = self.cleaned_data.get('x')
    #     y = self.cleaned_data.get('y')
    #     w = self.cleaned_data.get('width')
    #     h = self.cleaned_data.get('height')

    #     image = Image.open(profile.profile_img)
    #     cropped_image = image.crop((x, y, w+x, h+y))
    #     resized_image = cropped_image.resize((300, 300), Image.ANTIALIAS)
    #     resized_image.save(profile.profile_img.path)
    #     # keep the default pic
    #     default_img_path = settings.MEDIA_ROOT + '/media/profile_pics/covid.jpg'
    #     if profile._current_image.path != default_img_path:
    #         profile._current_image.delete(save=False)

    #     return profile 

