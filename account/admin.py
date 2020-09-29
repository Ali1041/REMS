from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserAdminAccount(UserAdmin):
    list_display = ('email','username','purpose','is_staff','is_active')
    search_fields=('email','username')
    readonly_fields = ('last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,UserAdminAccount)