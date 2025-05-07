from django.contrib import admin
from django.contrib.auth import get_user_model
from adminsortable2.admin import SortableAdminMixin

User = get_user_model()

class UserAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
