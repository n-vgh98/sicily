from django.contrib import admin
from .models import *


class AdminUser(admin.ModelAdmin):
    list_display = ('phone_number', 'date_joined', 'is_staff', 'is_owner')
    list_filter = ('is_staff',)
    search_fields = ('phone_number', 'date_joined')


class AdminProfile(admin.ModelAdmin):
    list_display = ('full_name', 'user_phone', 'created_time',)
    search_fields = ('first_name', 'last_name', 'user_phone')

    def user_phone(self, obj):
        return obj.user.phone_number


admin.site.register(User, AdminUser)
admin.site.register(Profile, AdminProfile)
