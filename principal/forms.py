# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from principal.models import Post, UserProfile, Dog, Picture, Feedback
from datetime import date
from django.core.validators import RegexValidator


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    address = forms.CharField(label='Dirección')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El numero ingresado no es del formato: '+999999999' o Supera los 15 digitos.")
    phone = forms.CharField(validators=[phone_regex], label='Telefono')
    class Meta:
        model = UserProfile
        fields = ('address', 'phone')


class PostForm(forms.ModelForm):
    CHOICES = (('Perdido', 'Perdido'),('Encontrado', 'Encontrado'),)
    title = forms.CharField(label='Titulo')
    detail = forms.CharField(label='Descripción', widget=forms.Textarea)
    type = forms.ChoiceField(choices=CHOICES, label='Tipo')
    date = forms.DateField(label='Fecha', initial=date.today)

    class Media:

        css = {'all': ('css/geoposition.css',)}

        js = ('js/geoposition.js',)

    class Meta:
        model = Post
        exclude = ('user_post', 'state')


class DogForm(forms.ModelForm):
    CHOICES = (('Macho', 'Macho'),('Hembra', 'Hembra'),)
    name = forms.CharField(label='Nombre Perro')
    breed = forms.CharField(label='Raza')
    colour = forms.CharField(label='Color')
    sex = forms.ChoiceField(choices=CHOICES, label='Sexo')
    age = forms.CharField(label='Edad')
    size = forms.CharField(label='Tamaño')

    class Meta:
        model = Dog
        exclude = ('post_dog',)


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        exclude = ('post_picture',)


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('user_feedback',)
