from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from accounts.views.register import register_view

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
