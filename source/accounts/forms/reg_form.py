from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Обязательно для заполнения')
    username = forms.CharField(max_length=150, required=True,help_text='Не более 150 символов.Только буквы,цифры и @/./+/-/_')
    password2 = forms.CharField(help_text='Введите одинаковый пароль для регистрации')

    class Meta:
        model = User
        fields = ['username','email', 'phone_number', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email уже используется')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Пользователь с этим номером телефона уже зарегистрирован.")
        return phone_number