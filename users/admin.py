from django.contrib import admin

from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["username", "fname", "last_modify"]
