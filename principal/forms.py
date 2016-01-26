# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from principal.models import Post, UserProfile, Dog, Picture, Feedback
from datetime import date
from django.core.validators import RegexValidator
from django.forms.extras.widgets import SelectDateWidget


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='username',
                               min_length=5,
                               widget=forms.TextInput,
                               )

    first_name = forms.CharField(label='Nombre',
                                 min_length=5,
                                 widget=forms.TextInput,
                                 )
    last_name = forms.CharField(label='Apellido',
                                min_length=5,
                                widget=forms.TextInput,
                                )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    address = forms.CharField(label='Dirección',
                              min_length=5,
                              widget=forms.TextInput,
                              )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message="El numero ingresado no es del formato: '+999999999' o no esta entre 9 y 15 digitos.")
    phone = forms.CharField(validators=[phone_regex], label='Telefono')

    class Meta:
        model = UserProfile
        fields = ('address', 'phone')


class PostForm(forms.ModelForm):
    CHOICES = (('Perdido', 'Perdido'), ('Encontrado', 'Encontrado'),)
    title = forms.CharField(label='Titulo',
                            min_length=5,
                            widget=forms.TextInput,
                            )
    detail = forms.CharField(label='Descripción',
                             widget=forms.Textarea,
                             min_length=10, )
    type = forms.ChoiceField(choices=CHOICES, label='Tipo')
    date = forms.DateField(label='Fecha',
                           initial=date.today,
                           widget=SelectDateWidget)

    class Media:
        css = {'all': ('css/geoposition.css',)}

        js = ('js/geoposition.js',)

    class Meta:
        model = Post
        exclude = ('user_post', 'state')


class DogForm(forms.ModelForm):
    CHOICES = (('Macho', 'Macho'), ('Hembra', 'Hembra'),)
    name = forms.CharField(label='Nombre Perro',
                           min_length=5,
                           widget=forms.TextInput,
                           )
    breed = forms.CharField(label='Raza',
                            min_length=5,
                            widget=forms.TextInput,
                            )
    colour = forms.CharField(label='Color',
                             min_length=5,
                             widget=forms.TextInput,
                             )
    sex = forms.ChoiceField(choices=CHOICES, label='Sexo')
    age = forms.CharField(label='Edad',
                          widget=forms.NumberInput,
                          )
    size = forms.CharField(label='Tamaño',
                           widget=forms.NumberInput
                           )

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


class UserInfoForm(forms.ModelForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('email',)

