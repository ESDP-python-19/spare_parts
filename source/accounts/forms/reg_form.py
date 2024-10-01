from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
import re


class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        help_text='Обязательно для заполнения. Укажите номер телефона в формате +7XXXXXXXXXX',
        error_messages={
            'required': 'Введите номер телефона.',
            'max_length': 'Номер телефона слишком длинный.',
        }
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='Не более 150 символов. Только буквы, цифры и @/./+/-/_',
        error_messages={
            'required': 'Введите имя пользователя.',
            'max_length': 'Имя пользователя слишком длинное. Максимум 150 символов.',
        }
    )
    email = forms.EmailField(
        required=True,
        help_text='Введите корректный адрес электронной почты.',
        error_messages={
            'required': 'Введите email.',
            'invalid': 'Введите корректный email адрес.',
        }
    )
    password1 = forms.CharField(
        required=True,
        help_text='Пароль должен содержать как минимум 8 символов.',
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Введите пароль.',
        }
    )
    password2 = forms.CharField(
        required=True,
        help_text='Введите пароль повторно для подтверждения.',
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Подтвердите пароль.',
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует.')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError('Введите корректный email адрес.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует. Выберите другое имя.')
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Пользователь с этим номером телефона уже зарегистрирован.")
        if not phone_number.startswith('+996') or len(phone_number) != 13:
            raise forms.ValidationError("Введите корректный номер телефона в формате +996XXXXXXXXX.")
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают.')

        if len(password1) < 8:
            raise forms.ValidationError('Пароль слишком короткий. Он должен содержать как минимум 8 символов.')

        return password2
