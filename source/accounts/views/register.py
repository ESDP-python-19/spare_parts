from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms.reg_form import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('webapp:parts_list')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте введенные данные.')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
