from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select
from .models import *

#Для форм не связаннных с БД
# class AddPostForm(forms.Form):
#     name = forms.CharField(max_length=255, label='Название курса', widget=forms.TimeInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255, label='URL')
#     dataStart = forms.DateTimeField(input_formats='%y-%m-%d %H:%M', label='Дата начала', required=False)
#     data_end = forms.DateTimeField(input_formats='%y-%m-%d %H:%M', label='Дата окончания', required=False)
#     price = forms.IntegerField(label='Стоимость')
#     group_min_participants = forms.IntegerField(label='Минимальное числов в группе')
#     group_man_participants = forms.IntegerField(label='Максимальное числов в группе')
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Форма обучения', empty_label='Форма обучения не выбрана')

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cat"].empty_label = "Категория не выбрана"


    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-input'}),

        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 20:
            raise ValidationError("Длина привышает 200 символов")
        return name


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10 }))
    captcha = CaptchaField(label='Защита')


class SetUserForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}), help_text="Как к вам можно обратится")
    content = forms.CharField(label='Дополнения и пожелания', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), help_text="Пожелания по выбранному курсу")


    class Meta:
        model = User
        fields = ('name', 'content')


