from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = [f.name for f in User._meta.fields if f.name not in ('password', 'groups', 'user_permissions', 'is_staff', 'is_superuser')]

admin.site.register(User, UserAdmin)
