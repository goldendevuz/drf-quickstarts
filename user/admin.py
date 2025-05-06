from django.contrib import admin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }