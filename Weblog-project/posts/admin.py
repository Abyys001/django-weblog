from django.contrib import admin

from .models import *


# Register your models here.
class CommnetAdminInline(admin.TabularInline):
    model = Comment
    fields = ["text"]
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_enable", "created_time"]
    inlines = [CommnetAdminInline]
