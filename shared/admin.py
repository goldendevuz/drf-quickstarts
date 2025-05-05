from django.contrib import admin
from django.contrib.auth import get_user_model
from simple_history.admin import SimpleHistoryAdmin

User = get_user_model()

admin.site.register(User, SimpleHistoryAdmin)