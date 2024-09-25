from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts.views.login import UserLoginView
from accounts.views.logout import custom_logout_view
from accounts.views.register import register_view

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),
]
