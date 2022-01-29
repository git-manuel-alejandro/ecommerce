from dataclasses import field
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .import models

class AccountAdmin(UserAdmin):
    list_display = ['email','first_name', 'last_name', 'username', 'last_login', 'is_active']
    list_display_link = ('email','first_name', 'last_name')
    readonly_field = ('last_login', 'date_joined')
    ordering = ('date_joined', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()







# Register your models here.


admin.site.register(models.Accounts , AccountAdmin)
