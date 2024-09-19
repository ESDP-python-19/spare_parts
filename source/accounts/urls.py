from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views.views import register, UserLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]

