from django.contrib import admin
from django.contrib.auth import get_user_model
from reversion.admin import VersionAdmin

User = get_user_model()

class UserAdmin(VersionAdmin):
    pass

admin.site.register(User, UserAdmin)