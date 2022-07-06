from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserImplCreationForm, UserImplChangeForm
from .models import UserImpl


class UserImplAdmin(UserAdmin):
    add_form = UserImplCreationForm
    form = UserImplChangeForm
    model = UserImpl
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'birth_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'birth_date', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(UserImpl, UserImplAdmin)
