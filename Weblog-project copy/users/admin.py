from django.contrib import admin

from .models import User, Profile
# Register your models here.

admin.site.register(Profile)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["username", "fname", "last_modify"]
