# vim: set fileencoding=utf-8 :
from django.contrib import admin
from admin_confirm import AdminConfirmMixin

from user.models import User

class UserAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(User, UserAdmin)