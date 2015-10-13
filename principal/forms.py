from django import forms
from django.contrib.auth.models import User
from principal.models import Post, UserProfile, Dog, Picture
from geoposition.forms import GeopositionField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address', 'phone')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user_post',)


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ('post_dog',)


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ('post_picture',)
