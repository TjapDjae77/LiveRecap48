from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Account

# Customizing the Admin Interface for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

# Customizing the Admin Interface for Account
class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('user', 'get_favorite_members')
    search_fields = ('user__username', 'user__email')
    ordering = ('user__username',)

    def get_favorite_members(self, obj):
        return ", ".join([member.name for member in obj.favorite_members.all()])
    get_favorite_members.short_description = 'Favorite Members'

# Registering models to the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Account, AccountAdmin)
