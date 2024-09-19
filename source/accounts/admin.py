from django.contrib import admin
from accounts.models.user import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(User, UserAdmin)