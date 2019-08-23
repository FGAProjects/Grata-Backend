from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Person,Administrator, Participant

class UserAdmin(BaseUserAdmin):

    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'name', 'ramal',
                       'is_administrator', 'is_participant', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'name', 'is_administrator', 'is_participant', 'ramal', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'name', 'ramal', 'is_administrator', 'is_participant']
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(Participant)
admin.site.register(Administrator)
admin.site.register(Person, UserAdmin)
admin.site.unregister(Group)