from django.contrib import admin
from django.contrib.auth import get_user_model
from djangoql.admin import DjangoQLSearchMixin

User = get_user_model()

class UserAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)